# Test Plan – Sustaining.ai Lite (Mock API)

## 1. Scope
The scope of testing includes validation of the mock backend API for Sustaining.ai Lite.  
The following functionalities will be tested:

- User Authentication (Login & Logout)
- ESG Question Submission API
- Job Status Tracking
- Fetching Recent Answers
- Admin-only CSV Upload functionality
- Role-based access control (Analyst vs Admin)
- Error handling and validation
- WebSocket connectivity for real-time updates
- API response structure, status codes, and performance basics

---

## 2. Risks
High-risk areas that require focused testing:

- Authentication and authorization failures
- Role-based access violations (Admin vs Analyst)
- Incorrect or inconsistent API responses
- Asynchronous job processing and job status polling
- File upload handling (CSV upload)
- WebSocket connection stability
- Input validation and security-related issues (invalid tokens, malformed payloads)

---

## 3. Out of Scope
The following items are not covered in this testing cycle:

- Frontend UI testing (no UI provided)
- Production-level security testing
- Load testing beyond basic performance checks
- AI/ML answer correctness and model validation
- Database persistence validation
- Cross-browser or mobile testing

---

## 4. Test Strategy
A combination of **manual and automated testing** will be used:

### Manual Testing
- Exploratory API testing using Postman / curl
- Validation of API behavior against documentation
- Negative testing and boundary testing
- Role-based access validation

### Automation Testing
- API automation using Postman collections or pytest
- UI automation (if applicable) using Playwright (basic setup)
- Performance testing using k6 for critical endpoints

---

## 5. Test Environment
- OS: Windows
- API Server: Mock API Server (Node.js)
- Server URL: http://localhost:3001
- WebSocket URL: ws://localhost:3001
- Environment: Local development setup

---

## 6. Test Data
The following test data will be used:

### User Accounts
- Analyst User  
  - Email: analyst@test.com  
  - Password: TestPass123!

- Admin User  
  - Email: admin@test.com  
  - Password: AdminPass123!

### Other Data
- Valid and invalid ESG questions
- Sample CSV files for admin upload
- Invalid payloads and unauthorized requests

---

## 7. Tools
The following tools will be used during testing:

- Postman – Manual and automated API testing
- curl – Quick API validation
- Playwright – UI automation (if applicable)
- k6 – Performance testing
- Visual Studio Code – Test development
- Git – Version control

---
