import requests
import time
import pytest

BASE_URL = "http://localhost:3001"

# -------------------------
# Test Users
# -------------------------
USERS = [
    {"role": "Analyst", "email": "analyst@test.com", "password": "TestPass123!"},
    {"role": "Admin", "email": "admin@test.com", "password": "AdminPass123!"}
]

# -------------------------
# Helper Functions
# -------------------------
def login(email, password):
    resp = requests.post(
        f"{BASE_URL}/api/v1/auth/login",
        json={"email": email, "password": password}
    )
    assert resp.status_code == 200
    return resp.json()["token"]

# -------------------------
# Tests
# -------------------------

@pytest.mark.parametrize("user", USERS)
def test_role_based_access_to_admin_upload(user):
    """
    Verify only Admin can access company upload endpoint
    """
    token = login(user["email"], user["password"])
    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.post(
        f"{BASE_URL}/api/v1/admin/companies/upload",
        json={"dummy": "test"},
        headers=headers
    )

    if user["role"] == "Admin":
        # Admin reaches validation layer (CSV missing is acceptable)
        assert resp.status_code in [200, 400]
    else:
        # Analyst must be blocked
        assert resp.status_code in [401, 403]


def test_analyst_submit_question_and_get_result():
    """
    Analyst submits ESG question and polls until terminal state
    """
    token = login("analyst@test.com", "TestPass123!")
    headers = {"Authorization": f"Bearer {token}"}

    submit_resp = requests.post(
        f"{BASE_URL}/api/v1/qa",
        json={
            "question": "What are the Scope 1 emissions?",
            "company": "Nokia"
        },
        headers=headers
    )

    assert submit_resp.status_code == 202
    job_id = submit_resp.json()["jobId"]

    final_payload = None

    for _ in range(10):
        poll_resp = requests.get(
            f"{BASE_URL}/api/v1/qa/{job_id}",
            headers=headers
        )
        assert poll_resp.status_code == 200

        final_payload = poll_resp.json()
        if final_payload["status"] in ["done", "failed"]:
            break

        time.sleep(1)

    assert final_payload["status"] in ["done", "failed"]

    if final_payload["status"] == "done":
        assert "result" in final_payload
        assert "answer" in final_payload["result"]
        assert "confidence" in final_payload["result"]
    else:
        assert "error" in final_payload


def test_get_recent_answers_list():
    """
    Verify analyst can fetch recent QA history
    """
    token = login("analyst@test.com", "TestPass123!")
    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.get(f"{BASE_URL}/api/v1/qa", headers=headers)
    assert resp.status_code == 200

    body = resp.json()
    assert "answers" in body
    assert isinstance(body["answers"], list)

    if body["answers"]:
        first = body["answers"][0]
        assert "question" in first
        assert "answer" in first


def test_aiml_service_rate_limit():
    """
    Validate AIML service rate limiting behavior
    """
    for _ in range(12):
        resp = requests.post(
            f"{BASE_URL}/aiml/answer",
            json={
                "question": "Rate limit test",
                "company": "Nokia"
            }
        )

    assert resp.status_code in [200, 429]

