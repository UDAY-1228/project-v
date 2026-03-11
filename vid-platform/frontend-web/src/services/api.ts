
const API_BASE_URL = 'http://localhost:8000/api/v1';

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
    const response = await fetch(`${API_BASE_URL}/lms/`);
    return await response.json();
};
