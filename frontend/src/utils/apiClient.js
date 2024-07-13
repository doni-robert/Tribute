import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/'
});

apiClient.interceptors.response.use(
  response => response,
  error => {
    // Handle global errors here, e.g., authentication errors, network errors
    console.error('Global error:', error);
    return Promise.reject(error);
  }
);

export default apiClient;