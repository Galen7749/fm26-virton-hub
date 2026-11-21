<template>
  <header class="bg-slate-900 border-b border-slate-800 px-4 py-3 flex items-center justify-between sticky top-0 z-30 shadow-md">
    <div class="flex items-center space-x-2.5">
      <div class="w-8 h-8 rounded-lg bg-emerald-600 flex items-center justify-center font-black text-white text-base tracking-tighter shadow-sm">
        FH
      </div>
      <div>
        <h1 class="text-sm font-black text-white tracking-wide flex items-center space-x-1.5">
          <span>FootHub · 懂球云</span>
          <span class="text-[9px] bg-slate-800 text-teal-300 font-normal px-1.5 py-0.2 rounded border border-teal-900/40">
            {{ clubName }}
          </span>
        </h1>
        <p class="text-[9px] text-slate-400 font-sans flex items-center space-x-1">
          <span>{{ seasonLabel }}</span>
          <span>·</span>
          <span>{{ leagueName }}</span>
        </p>
      </div>
    </div>

    <!-- 私人入口：主帅信箱按钮 -->
    <button
      @click="$emit('open-mailbox')"
      class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs px-2.5 py-1.5 rounded-lg flex items-center space-x-1 transition shadow-sm relative group"
    >
      <span class="text-xs">💼</span>
      <span class="font-bold text-[11px] text-emerald-400">主帅信箱</span>
      <span class="w-2 h-2 rounded-full bg-amber-400 absolute -top-0.5 -right-0.5 ring-2 ring-slate-900 animate-pulse"></span>
    </button>
  </header>
</template>

<script setup>
defineProps({
  clubName: {
    type: String,
    default: '维尔通精英'
  },
  seasonLabel: {
    type: String,
    default: '2025/26 赛季'
  },
  leagueName: {
    type: String,
    default: '比乙联赛'
  }
})

defineEmits(['open-mailbox'])
</script>
