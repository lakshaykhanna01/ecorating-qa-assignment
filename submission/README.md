
# Sustaining.ai Lite - QA Assignment Test Suite

## How to Run the Tests

### 1. Manual Test Cases
- Open the `/submission/manual` folder.
- Review:
  - `test-plan.md` – overall strategy, risks, test data.
  - `test-cases-ui.csv` – UI test cases.
  - `test-cases-api.csv` – API test cases.
  - `bug-reports.csv` – documented bugs.
- Execute manually as described in test steps.

### 2. UI Automation (Playwright)
1. Ensure **Node.js** is installed and mock API server is running:  
   ```bash
   cd mock-api
   npm install
   npm start
Install Playwright dependencies (from project root):

bash
Copy code
npm install -D @playwright/test
npx playwright install
Run tests:

bash
Copy code
npx playwright test submission/automation/UI/ui.spec.ts
Test coverage: login, submit question, stream status → result, role-based access.

3. API Automation (Pytest + Requests)
Python must be installed.

Navigate to /submission/automation/api.

Install required packages:

bash
Copy code
pip install pytest requests
Run tests:

bash
Copy code
pytest -v test_api.py
Coverage includes authentication, QA flows, AIML service, and file upload with positive & negative scenarios.

4. Performance & Resilience (k6)
Navigate to /submission/perf.

Run test:

bash
Copy code
k6 run k6-script.js
The test simulates 5→20 RPS load on /qa endpoints for 10–15 minutes, polls job status, and checks results.

Assumptions Made
Mock API server (http://localhost:3001) is running for all tests.

Analyst and Admin accounts exist:

Analyst: analyst@test.com / TestPass123!

Admin: admin@test.com / AdminPass123!

AIML service may return HTTP 429 if rate limit exceeded; scripts include retry handling.

File uploads are limited to 2MB and CSV format.

Limitations Encountered
API Automation could not be fully validated without Python installed in some environments.

Some Playwright UI tests failed initially due to timing issues and element locators; fixed with data-testid selectors.

Performance tests do not simulate full network latency or large file uploads.

WebSocket/SSE real-time streaming not fully visualized in automated tests.

What Would Be Tested Next with More Time
Full end-to-end integration of WebSocket/SSE real-time updates in UI automation.

File upload validation with malformed or large datasets for Admin users.

Advanced load and stress testing beyond 20 RPS for concurrency limits.

Security & compliance tests for JWT expiry, XSS, CSRF, and input validation.

Cross-browser UI testing and mobile responsiveness.

