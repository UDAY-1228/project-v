import axios from 'axios';

const api = axios.create({
    baseURL: '/api/super-admin',
    headers: {
        'Content-Type': 'application/json',
    },
});

api.interceptors.request.use((config) => {
    const token = localStorage.getItem('sa_token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export const login = async (credentials: any) => {
    const response = await api.post('/login', credentials);
    if (response.data.access_token) {
        localStorage.setItem('sa_token', response.data.access_token);
    }
    return response.data;
};

export const createInstitution = async (data: any) => {
    const response = await api.post('/institutions', data);
    return response.data;
};

export const getInstitutions = async () => {
    const response = await api.get('/institutions');
    return response.data;
};
