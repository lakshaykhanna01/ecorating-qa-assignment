import http from 'k6/http';
import { sleep, check } from 'k6';
import { Rate } from 'k6/metrics';

export let errorRate = new Rate('errors');

export let options = {
    stages: [
        { duration: '2m', target: 5 },   
        { duration: '3m', target: 10 },  
        { duration: '3m', target: 20 },  
        { duration: '2m', target: 0 },   
    ],
    thresholds: {
        'errors': ['rate<0.05'],          
        'http_req_duration': ['p(95)<2000'] 
    }
};

const BASE_URL = 'http://localhost:3001';

const analyst = { email: 'analyst@test.com', password: 'TestPass123!' };

export default function () {
    let loginRes = http.post(`${BASE_URL}/api/v1/auth/login`, JSON.stringify(analyst), {
        headers: { 'Content-Type': 'application/json' }
    });

    check(loginRes, {
        'login status 200': (r) => r.status === 200,
        'received token': (r) => r.json('token') !== undefined
    }) || errorRate.add(1);

    let token = loginRes.json('token');

    let qaPayload = {
        question: 'What are the Scope 1 emissions for Nokia?',
        company: 'Nokia'
    };

    let qaRes = http.post(`${BASE_URL}/api/v1/qa`, JSON.stringify(qaPayload), {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });

    check(qaRes, {
        'QA submission accepted': (r) => r.status === 202,
        'jobId returned': (r) => r.json('jobId') !== undefined
    }) || errorRate.add(1);

    let jobId = qaRes.json('jobId');

    let jobRes = http.get(`${BASE_URL}/api/v1/qa/${jobId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
    });

    check(jobRes, {
        'job status returned': (r) => r.status === 200,
        'result object present': (r) => r.json('result') !== undefined
    }) || errorRate.add(1);

    sleep(1); 
}
