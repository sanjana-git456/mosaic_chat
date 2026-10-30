<template>
  <div class="min-h-screen flex bg-slate-50">
    <!-- Sidebar -->
    <aside class="w-64 bg-white border-r flex flex-col">
      <div class="p-6">
        <h1 class="text-2xl font-bold text-indigo-600">MosaicChat</h1>
      </div>
      <nav class="flex-1 px-4 space-y-2">
        <router-link to="/dashboard" class="flex items-center gap-3 p-3 rounded-xl hover:bg-slate-100 transition">
          <LayoutGridIcon class="w-5 h-5" /> Feed
        </router-link>
        <router-link to="/dashboard/create" class="flex items-center gap-3 p-3 rounded-xl hover:bg-slate-100 transition">
          <PlusSquareIcon class="w-5 h-5" /> Create Piece
        </router-link>
      </nav>
      <div class="p-4 border-t">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 font-bold">
            {{ auth.user?.username?.charAt(0).toUpperCase() }}
          </div>
          <div class="overflow-hidden">
            <p class="font-semibold truncate">{{ auth.user?.username }}</p>
            <p class="text-xs text-slate-500">Creator Tier: Free</p>
          </div>
        </div>
        <button @click="handleLogout" class="w-full flex items-center gap-3 p-3 text-red-600 hover:bg-red-50 rounded-xl transition">
          <LogOutIcon class="w-5 h-5" /> Logout
        </button>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 overflow-y-auto">
      <div class="max-w-5xl mx-auto p-8">
        <router-view />
      </div>
    </main>
  </div>
</template>

<script setup>
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';
import { LayoutGridIcon, PlusSquareIcon, LogOutIcon } from 'lucide-vue-next';

const auth = useAuthStore();
const router = useRouter();

const handleLogout = () => {
  auth.logout();
  router.push('/');
};
</script>