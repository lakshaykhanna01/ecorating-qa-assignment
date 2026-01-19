Sustaining.ai Lite – QA Assignment
How to Run the Tests
Manual Testing

Go to submission/manual

Files included:

test-plan.md – test approach, scope, risks

testcases_ui.csv – UI test cases

testcases_api.csv – API test cases

bug_report.csv – bugs found with steps and severity

Follow the steps mentioned in each test case to execute manually.

API Automation (Pytest)

Pre-requisite: Python installed and mock API server running on http://localhost:3001

Steps:

cd submission/automation/API
pip install pytest requests
python -m pytest -v test_api.py


Covers:

Login and authentication

Role-based access (Analyst vs Admin)

Submit ESG question and poll job status

Recent answers API

AIML rate-limit behavior

Performance Testing (k6)

Pre-requisite: k6 installed

Steps:

cd submission/performance/perf
k6 run k6-script.js


This test:

Sends POST requests to /api/v1/qa

Ramps load from 5 to 20 RPS

Polls /api/v1/qa/{jobId}

Runs for ~10–15 minutes

Assumptions

Mock API server is running locally on port 3001

Test users are available:

Analyst: analyst@test.com / TestPass123!

Admin: admin@test.com / AdminPass123!

AIML service may return rate-limit errors when overloaded

CSV upload size limit is 2MB

Limitations

Some environments had Python setup issues initially

WebSocket/SSE streaming was tested functionally but not fully automated

Performance testing does not include large file uploads or real network latency

What I Would Test Next

Full WebSocket/SSE automation for live job updates

Larger and malformed CSV uploads for Admin users

Higher load and stress testing beyond 20 RPS

Security scenarios (JWT expiry, invalid tokens, input validation)

Cross-browser UI testing
