// api.js

import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
        'Content-Type': 'application/json'
    }
});

// 添加JWT令牌到请求头
api.interceptors.request.use(config => {
    const token = localStorage.getItem('jwtToken');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    } else {
        localStorage.removeItem('jwtToken');
        delete config.headers.Authorization;
    }
    return config;
}, error => {
    localStorage.removeItem('jwtToken');
    delete error.config.headers.Authorization;
    return Promise.reject(error);
});

export default api;
