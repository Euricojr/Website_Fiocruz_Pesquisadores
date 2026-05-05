
/**
 * api.js - Centralized API communication with Bearer Token handling.
 */

const API = {
    getToken() {
        return localStorage.getItem('access_token');
    },

    async request(endpoint, options = {}) {
        const token = this.getToken();
        if (!token) {
            window.location.href = 'index.html';
            return;
        }

        const headers = {
            'Authorization': `Bearer ${token}`,
            ...options.headers
        };

        if (options.body && !(options.body instanceof FormData)) {
            headers['Content-Type'] = 'application/json';
            options.body = JSON.stringify(options.body);
        }

        try {
            const response = await fetch(`/api${endpoint}`, { ...options, headers });
            
            if (response.status === 401) {
                localStorage.removeItem('access_token');
                window.location.href = 'index.html';
                return;
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error(`API Error on ${endpoint}:`, error);
            throw error;
        }
    },

    get(endpoint) { return this.request(endpoint, { method: 'GET' }); },
    post(endpoint, data) { return this.request(endpoint, { method: 'POST', body: data }); },
    delete(endpoint) { return this.request(endpoint, { method: 'DELETE' }); }
};
