<template>
  <footer class="fixed bottom-0 w-full max-w-md bg-slate-900/95 backdrop-blur border-t border-slate-800 px-2 py-1.5 flex items-center justify-around text-xs z-30 shadow-lg">
    <button
      @click="$emit('update:activeTab', 'matches')"
      :class="[
        'flex flex-col items-center space-y-0.5 py-1 px-2.5 rounded-lg transition',
        activeTab === 'matches' ? 'text-emerald-400 font-bold' : 'text-slate-400 hover:text-slate-200'
      ]"
    >
      <span class="text-base">⚽</span>
      <span class="text-[10px]">比赛大盘</span>
    </button>

    <button
      @click="$emit('update:activeTab', 'tactics')"
      :class="[
        'flex flex-col items-center space-y-0.5 py-1 px-2.5 rounded-lg transition',
        activeTab === 'tactics' ? 'text-emerald-400 font-bold' : 'text-slate-400 hover:text-slate-200'
      ]"
    >
      <span class="text-base">📊</span>
      <span class="text-[10px]">战术阵容</span>
    </button>

    <button
      @click="$emit('update:activeTab', 'standings')"
      :class="[
        'flex flex-col items-center space-y-0.5 py-1 px-2.5 rounded-lg transition',
        activeTab === 'standings' ? 'text-emerald-400 font-bold' : 'text-slate-400 hover:text-slate-200'
      ]"
    >
      <span class="text-base">🏆</span>
      <span class="text-[10px]">榜单大盘</span>
    </button>

    <!-- 新增：🔥 球迷广场 (包含所有比赛综合评价与场外八卦日常) -->
    <button
      @click="$emit('update:activeTab', 'community')"
      :class="[
        'flex flex-col items-center space-y-0.5 py-1 px-2.5 rounded-lg transition relative',
        activeTab === 'community' ? 'text-rose-400 font-bold' : 'text-slate-400 hover:text-slate-200'
      ]"
    >
      <span class="text-base">🔥</span>
      <span class="text-[10px]">球迷热议</span>
      <span class="w-1.5 h-1.5 rounded-full bg-rose-500 absolute top-1 right-2 animate-pulse"></span>
    </button>

    <button
      @click="$emit('update:activeTab', 'mailbox')"
      :class="[
        'flex flex-col items-center space-y-0.5 py-1 px-2.5 rounded-lg transition relative',
        activeTab === 'mailbox' ? 'text-amber-400 font-bold' : 'text-slate-400 hover:text-slate-200'
      ]"
    >
      <span class="text-base">💼</span>
      <span class="text-[10px]">主帅信箱</span>
      <span class="w-1.5 h-1.5 rounded-full bg-amber-400 absolute top-1 right-2"></span>
    </button>
  </footer>
</template>

<script setup>
defineProps({
  activeTab: {
    type: String,
    required: true
  }
})

defineEmits(['update:activeTab'])
</script>
