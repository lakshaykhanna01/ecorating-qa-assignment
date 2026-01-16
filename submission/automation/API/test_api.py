import requests
import time
import pytest

BASE_URL = "http://localhost:3001"

users = [
    {"role": "Analyst", "email": "analyst@test.com", "password": "TestPass123!"},
    {"role": "Admin", "email": "admin@test.com", "password": "AdminPass123!"}
]

@pytest.mark.parametrize("user", users)
def test_login_and_role_access(user):
    
    login_resp = requests.post(f"{BASE_URL}/api/v1/auth/login", json={
        "email": user["email"],
        "password": user["password"]
    })
    assert login_resp.status_code == 200
    token = login_resp.json()["token"]

    headers = {"Authorization": f"Bearer {token}"}
    admin_upload_resp = requests.post(f"{BASE_URL}/api/v1/admin/companies/upload", json={"dummy":"test"}, headers=headers)
    
    if user["role"] == "Admin":
        assert admin_upload_resp.status_code == 200
    else:
        assert admin_upload_resp.status_code in [401, 403]

def test_analyst_submit_question():
    login_resp = requests.post(f"{BASE_URL}/api/v1/auth/login", json={
        "email": "analyst@test.com",
        "password": "TestPass123!"
    })
    token = login_resp.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    qa_resp = requests.post(f"{BASE_URL}/api/v1/qa", json={"question": "What is the ESG score of XYZ?"}, headers=headers)
    assert qa_resp.status_code == 202
    job_id = qa_resp.json()["jobId"]

    status = ""
    for _ in range(10):
        status_resp = requests.get(f"{BASE_URL}/api/v1/qa/{job_id}", headers=headers)
        status = status_resp.json()["status"]
        if status == "done":
            break
        time.sleep(1)
    assert status == "done"

def test_aiml_service_rate_limit():
    pass
