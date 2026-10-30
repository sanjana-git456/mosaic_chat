<template>
  <div class="min-h-screen bg-slate-50 flex items-center justify-center p-4">
    <div class="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md">
      <h2 class="text-3xl font-bold text-center mb-8">Join Mosaic</h2>
      <form @submit.prevent="handleRegister" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Username</label>
          <input v-model="form.username" type="text" class="w-full p-3 border rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none" required />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Email</label>
          <input v-model="form.email" type="email" class="w-full p-3 border rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none" required />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Password</label>
          <input v-model="form.password" type="password" class="w-full p-3 border rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none" required />
        </div>
        <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
        <button :disabled="loading" class="w-full bg-indigo-600 text-white py-3 rounded-xl font-bold hover:bg-indigo-700 disabled:opacity-50">
          {{ loading ? 'Creating Account...' : 'Sign Up' }}
        </button>
      </form>
      <p class="mt-6 text-center text-slate-600">
        Already have an account? <router-link to="/login" class="text-indigo-600 font-semibold">Log in</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();
const form = reactive({ username: '', email: '', password: '' });
const error = ref('');
const loading = ref(false);

const handleRegister = async () => {
  loading.value = true;
  error.value = '';
  try {
    await auth.register(form.username, form.email, form.password);
    router.push('/dashboard');
  } catch (e) {
    error.value = e.response?.data?.detail || 'Registration failed';
  } finally {
    loading.value = false;
  }
};
</script>