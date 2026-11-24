<template>
  <header class="bg-slate-900/95 backdrop-blur border-b border-slate-800 px-3.5 py-2.5 sticky top-0 z-30 shadow-md">
    <div class="flex items-center justify-between w-full">
      <!-- 1. 左侧：大众媒体品牌 Logo（组合使用 lucide:cloud + ph:soccer-ball） -->
      <div class="inline-flex items-center gap-2 cursor-pointer select-none" @click="$emit('change-tab', 'news')">
        <div class="w-8 h-8 rounded-lg bg-emerald-600 flex items-center justify-center text-white shadow-sm relative overflow-hidden group">
          <Icon icon="lucide:cloud" class="w-5 h-5 text-emerald-100" />
          <Icon icon="ph:soccer-ball-fill" class="w-2.5 h-2.5 text-white absolute bottom-1 right-1" />
        </div>
        <div class="flex flex-col">
          <span class="text-sm font-black text-white tracking-wider inline-flex items-center gap-1.5">
            <span>懂球云</span>
            <span class="text-[9px] bg-emerald-950 text-emerald-400 font-bold px-1.5 py-0.2 rounded border border-emerald-800/60 uppercase">
              Live
            </span>
          </span>
          <span class="text-[9px] text-slate-400 font-sans tracking-tight">
            全球足球资讯 · 即时比分社区
          </span>
        </div>
      </div>

      <!-- 2. 右侧：搜索输入框与极低调的「lucide:smartphone」主帅私人手机入口 -->
      <div class="inline-flex items-center gap-2 shrink-0">
        <!-- 搜索输入框 -->
        <div class="relative inline-flex items-center">
          <Icon icon="lucide:search" class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 pointer-events-none" />
          <input
            v-model="searchQuery"
            @keyup.enter="handleSearch"
            type="text"
            placeholder="搜索球队/赛事/球星..."
            class="w-32 bg-slate-950 border border-slate-800 focus:border-emerald-500 rounded-full pl-7 pr-2.5 py-1 text-slate-200 text-[11px] placeholder-slate-500 focus:outline-none transition-all"
          />
        </div>

        <!-- 极低调的 smartphone 图标（暗门彩蛋：点击呼出主帅私人手机模拟器） -->
        <button
          @click="$emit('open-phone')"
          class="w-8 h-8 rounded-full bg-slate-950 hover:bg-slate-800 text-slate-400 hover:text-emerald-400 border border-slate-800/80 inline-flex items-center justify-center transition shadow-sm relative group"
          title="主帅私密终端"
        >
          <Icon icon="lucide:smartphone" class="w-4 h-4 text-slate-400 group-hover:text-emerald-400 transition" />
          <!-- 极小绿点提示正常在线 -->
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 absolute top-1.5 right-1.5 animate-pulse"></span>
        </button>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  activeTab: {
    type: String,
    default: 'news'
  }
})

const emit = defineEmits(['change-tab', 'open-phone', 'search'])

const searchQuery = ref('')

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    emit('search', searchQuery.value.trim())
  }
}
</script>
