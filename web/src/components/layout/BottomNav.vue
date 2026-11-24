<template>
  <footer class="fixed bottom-0 left-0 right-0 max-w-md mx-auto bg-slate-900/98 backdrop-blur-md border-t border-slate-800 px-3 py-1.5 flex items-center justify-around text-xs z-40 shadow-2xl">
    <button
      v-for="tab in navTabs"
      :key="tab.key"
      @click="$emit('update:activeTab', tab.key)"
      :class="[
        'flex flex-col items-center space-y-1 py-1 px-4 rounded-xl transition-all duration-150 relative select-none',
        activeTab === tab.key
          ? 'text-emerald-400 font-bold scale-105'
          : 'text-slate-400 hover:text-slate-200'
      ]"
    >
      <Icon :icon="tab.icon" class="w-5 h-5" />
      <span class="text-[10px] tracking-tight leading-none">{{ tab.name }}</span>
      <!-- 选中指示小圆点 -->
      <span
        v-if="activeTab === tab.key"
        class="w-1 h-1 rounded-full bg-emerald-400 absolute bottom-0"
      ></span>
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

// 全局主导航严格限制为 4 个一级 Tab（接入 Iconify 专业现代线性/填充图标）
const navTabs = [
  { key: 'news', name: '资讯', icon: 'lucide:newspaper' },
  { key: 'matches', name: '比赛', icon: 'mdi:scoreboard-outline' },
  { key: 'community', name: '社区', icon: 'lucide:message-square-more' },
  { key: 'standings', name: '数据', icon: 'lucide:bar-chart-3' }
]
</script>
