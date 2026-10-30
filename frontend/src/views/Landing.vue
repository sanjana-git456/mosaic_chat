<template>
  <div class="min-h-screen bg-gradient-to-br from-indigo-600 to-purple-700 text-white flex flex-col items-center justify-center p-6">
    <div class="max-w-4xl text-center">
      <h1 class="text-6xl font-bold mb-6">MosaicChat</h1>
      <p class="text-xl mb-12 opacity-90">Stitch together your life's snippets into a beautiful, private mosaic.</p>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
        <div class="bg-white/10 p-6 rounded-2xl backdrop-blur-sm">
          <h3 class="text-xl font-semibold mb-2">Unified Inbox</h3>
          <p class="text-sm opacity-80">Text, image, video, and voice snippets in one seamless flow.</p>
        </div>
        <div class="bg-white/10 p-6 rounded-2xl backdrop-blur-sm">
          <h3 class="text-xl font-semibold mb-2">Granular Privacy</h3>
          <p class="text-sm opacity-80">Control who sees every piece with simple sliders.</p>
        </div>
        <div class="bg-white/10 p-6 rounded-2xl backdrop-blur-sm">
          <h3 class="text-xl font-semibold mb-2">Creator First</h3>
          <p class="text-sm opacity-80">Earn directly from your followers with zero ad-revenue split.</p>
        </div>
      </div>

      <div class="flex gap-4 justify-center">
        <router-link to="/register" class="bg-white text-indigo-600 px-8 py-3 rounded-full font-bold hover:bg-indigo-50 transition">Get Started</router-link>
        <router-link to="/login" class="border border-white/30 px-8 py-3 rounded-full font-bold hover:bg-white/10 transition">Log In</router-link>
      </div>
    </div>
  </div>
</template>