Sustaining.ai Lite – QA Assignment
1. How to Run the Tests
1.1 Manual Testing

Navigate to submission/manual
Review the following files:
test-plan.md – overall test approach and scope

testcases_ui.csv – UI test cases

testcases_api.csv – API test cases

bug_report.csv – bugs with steps, severity, and results

Execute test cases manually as per the documented steps

1.2 API Automation (Pytest)

Ensure Python is installed

Start the mock API server on http://localhost:3001

Navigate to:

cd submission/automation/API


Install dependencies:

pip install pytest requests


Run tests:

python -m pytest -v test_api.py


Coverage includes:

Login and authentication

Role-based access (Admin vs Analyst)

Submit ESG questions and poll job status

Fetch recent answers

AIML rate-limit handling

1.3 Performance Testing (k6)

Ensure k6 is installed

Navigate to:

cd submission/performance/perf


Run the test:

k6 run k6-script.js


Test behavior:

Load ramp from 5 to 20 RPS

POST /api/v1/qa

Poll /api/v1/qa/{jobId}

Duration ~10–15 minutes

2. Assumptions Made

Mock API server is running on http://localhost:3001

Test accounts are available:

Analyst: analyst@test.com / TestPass123!

Admin: admin@test.com / AdminPass123!

AIML service may return 429 errors under load

CSV upload size limit is 2MB

3. Limitations Encountered

Python setup issues in some environments

WebSocket/SSE updates not fully automated

Performance tests do not include real network latency

Large file upload scenarios not load-tested

4. What I Would Test Next

End-to-end WebSocket/SSE automation

Admin CSV upload with invalid and large files

Stress testing beyond 20 RPS

Security testing (JWT expiry, invalid tokens)

Cross-browser and responsive UI testing
