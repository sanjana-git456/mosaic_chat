<template>
  <div class="max-w-2xl mx-auto">
    <h2 class="text-2xl font-bold mb-8">Create a New Piece</h2>
    <form @submit.prevent="handleSubmit" class="bg-white p-8 rounded-2xl shadow-sm border space-y-6">
      <div>
        <label class="block text-sm font-medium text-slate-700 mb-2">Content Type</label>
        <div class="grid grid-cols-4 gap-2">
          <button 
            v-for="type in ['text', 'image', 'voice', 'video']" 
            :key="type"
            type="button"
            @click="form.content_type = type"
            :class="form.content_type === type ? 'bg-indigo-600 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'"
            class="py-2 px-4 rounded-xl capitalize font-medium transition"
          >
            {{ type }}
          </button>
        </div>
      </div>

      <div>
        <label class="block text-sm font-medium text-slate-700 mb-2">Content / Caption</label>
        <textarea v-model="form.content" rows="4" class="w-full p-4 border rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none" placeholder="What's on your mind?"></textarea>
      </div>

      <div v-if="form.content_type !== 'text'">
        <label class="block text-sm font-medium text-slate-700 mb-2">Media URL</label>
        <input v-model="form.media_url" type="url" class="w-full p-4 border rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none" placeholder="https://..." />
      </div>

      <div>
        <label class="block text-sm font-medium text-slate-700 mb-2">Privacy Slider</label>
        <select v-model="form.privacy_level" class="w-full p-4 border rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none">
          <option value="public">Public (Everyone)</option>
          <option value="followers">Followers Only</option>
          <option value="friends">Friends Only</option>
          <option value="private">Private (Only Me)</option>
        </select>
      </div>

      <button :disabled="loading" class="w-full bg-indigo-600 text-white py-4 rounded-xl font-bold hover:bg-indigo-700 transition disabled:opacity-50">
        {{ loading ? 'Publishing...' : 'Publish to Mosaic' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import client from '../api/client';
import { useRouter } from 'vue-router';

const router = useRouter();
const loading = ref(false);
const form = reactive({
  content_type: 'text',
  content: '',
  media_url: '',
  privacy_level: 'public'
});

const handleSubmit = async () => {
  loading.value = true;
  try {
    await client.post('/posts/', form);
    router.push('/dashboard');
  } catch (e) {
    alert('Failed to create post');
  } finally {
    loading.value = false;
  }
};
</script>