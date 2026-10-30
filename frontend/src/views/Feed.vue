<template>
  <div class="space-y-8">
    <div v-if="burnout && burnout.needs_break" class="bg-amber-50 border border-amber-200 p-4 rounded-xl flex items-center gap-4">
      <div class="bg-amber-100 p-2 rounded-full">
        <ZapIcon class="w-6 h-6 text-amber-600" />
      </div>
      <div>
        <p class="font-semibold text-amber-900">Burnout Alert!</p>
        <p class="text-amber-700 text-sm">{{ burnout.suggestion }}</p>
      </div>
    </div>

    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div v-for="i in 6" :key="i" class="h-64 bg-slate-200 animate-pulse rounded-2xl"></div>
    </div>

    <div v-else-if="posts.length === 0" class="text-center py-20">
      <p class="text-slate-400">No pieces in your mosaic yet. Start creating!</p>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="post in posts" :key="post.id" class="bg-white rounded-2xl shadow-sm border overflow-hidden hover:shadow-md transition">
        <div v-if="post.media_url" class="aspect-square bg-slate-100">
           <img :src="post.media_url" class="w-full h-full object-cover" />
        </div>
        <div class="p-6">
          <div class="flex items-center gap-2 mb-4">
            <span class="text-xs font-bold uppercase tracking-wider text-indigo-600 bg-indigo-50 px-2 py-1 rounded">{{ post.content_type }}</span>
            <span class="text-xs text-slate-400">{{ post.privacy_level }}</span>
          </div>
          <p class="text-slate-800 line-clamp-4 mb-4">{{ post.content }}</p>
          <div class="flex items-center justify-between text-xs text-slate-500">
            <span>@{{ post.author.username }}</span>
            <span>{{ new Date(post.created_at).toLocaleDateString() }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import client from '../api/client';
import { ZapIcon } from 'lucide-vue-next';

const posts = ref([]);
const burnout = ref(null);
const loading = ref(true);

const fetchData = async () => {
  try {
    const [postsRes, burnoutRes] = await Promise.all([
      client.get('/posts/'),
      client.get('/posts/burnout/')
    ]);
    posts.value = postsRes.data;
    burnout.value = burnoutRes.data;
  } catch (e) {
    console.error(e);
  } finally {
    loading.value = false;
  }
};

onMounted(fetchData);
</script>