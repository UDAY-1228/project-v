const API_BASE_URL = 'http://localhost:8000/api/v1';

export const login = async (username: string, password: string) => {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        body: formData,
    });
    
    if (!response.ok) {
        throw new Error('Login failed');
    }
    
    return await response.json();
};

export const getSummary = async () => {
    const response = await fetch(`${API_BASE_URL}/analytics/summary`);
    return await response.json();
};

export const fetchConfig = async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/system/config`);
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch platform config:', error);
        return null;
    }
};

export const getAttendanceSummary = async () => {
    const response = await fetch(`${API_BASE_URL}/attendance/`);
    return await response.json();
};

export const getCourses = async () => {
    const response = await fetch(`${API_BASE_URL}/lms/courses`);
    return await response.json();
};
