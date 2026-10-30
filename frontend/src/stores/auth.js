import { defineStore } from 'pinia';
import client from '../api/client';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    async login(username, password) {
      const res = await client.post('/auth/login/', { username, password });
      this.token = res.data.access;
      this.user = res.data.user;
      localStorage.setItem('token', this.token);
    },
    async register(username, email, password) {
      const res = await client.post('/auth/register/', { username, email, password });
      this.token = res.data.access;
      this.user = res.data.user;
      localStorage.setItem('token', this.token);
    },
    async fetchMe() {
      if (!this.token) return;
      try {
        const res = await client.get('/auth/me/');
        this.user = res.data;
      } catch (e) {
        this.logout();
      }
    },
    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('token');
    },
  },
});