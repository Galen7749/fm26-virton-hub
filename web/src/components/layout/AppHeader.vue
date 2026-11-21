<template>
  <header class="bg-slate-900 border-b border-slate-800 px-4 py-3 flex items-center justify-between sticky top-0 z-30 shadow-md">
    <!-- 左侧：媒体品牌与执教俱乐部 -->
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
          <span>{{ leagueName }}</span>
          <span>·</span>
          <span>即时比分与数据中心</span>
        </p>
      </div>
    </div>

    <!-- 右侧：当前赛季标识徽章 (纯净公域展示，去除重复的信箱按钮) -->
    <div class="flex items-center space-x-1.5 bg-slate-800/80 border border-slate-700/80 px-2.5 py-1 rounded-full text-xs shadow-sm">
      <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
      <span class="text-[11px] font-bold text-slate-200">{{ seasonLabel }}</span>
    </div>
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
</script>
