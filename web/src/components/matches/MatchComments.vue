<template>
  <div v-if="threadData" class="space-y-4 animate-in fade-in duration-150">
    <!-- 主帅评分卡片 -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 flex items-center justify-between shadow-sm">
      <div>
        <div class="text-xs text-slate-400 font-medium">本场主帅综合战术评分</div>
        <div class="text-[11px] text-slate-500 mt-0.5 font-mono">超过 2,481 名球迷参与投票</div>
      </div>
      <div class="text-right">
        <span :class="['text-3xl font-black tracking-tight font-mono', coachScoreColor]">
          {{ threadData.coach_score }}
        </span>
        <span class="text-xs text-slate-400 font-bold ml-0.5">/ 10</span>
      </div>
    </div>

    <!-- 虎扑高亮热评列表 -->
    <div class="space-y-3">
      <div class="flex justify-between items-center text-xs text-slate-400 px-0.5">
        <span class="font-bold text-slate-200 inline-flex items-center gap-1.5">
          <Icon icon="tabler:flame" class="w-4 h-4 text-amber-400" />
          <span>虎扑亮了 · 赛后全网热议</span>
        </span>
        <span class="text-[11px] text-slate-500">按点赞数排序</span>
      </div>

      <div
        v-for="(cmt, cIdx) in threadData.comments"
        :key="cIdx"
        class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3 space-y-2 hover:border-slate-700 transition shadow-sm"
      >
        <div class="flex items-center justify-between text-xs">
          <div class="flex items-center space-x-2">
            <div class="w-6 h-6 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-[10px] font-bold text-emerald-400">
              {{ cmt.username.slice(0, 1) }}
            </div>
            <span class="font-semibold text-slate-200 text-xs">{{ cmt.username }}</span>
            <span class="text-[9px] bg-slate-950 text-amber-300 px-1.5 py-0.2 rounded border border-amber-900/40 font-medium">
              {{ cmt.tag || '球迷热评' }}
            </span>
          </div>
          <span class="text-[10px] text-slate-500 font-mono">#{{ cIdx + 1 }} 楼</span>
        </div>

        <p class="text-xs text-slate-300 leading-relaxed pl-1">
          {{ cmt.content }}
        </p>

        <div class="flex justify-end pt-1">
          <button
            @click="toggleLike(cIdx)"
            :class="[
              'text-[11px] px-2.5 py-1 rounded-full inline-flex items-center gap-1 transition',
              isLiked(cIdx)
                ? 'bg-rose-950/80 text-rose-300 border border-rose-800 shadow-sm'
                : 'bg-slate-950 text-slate-400 hover:text-slate-200 border border-slate-800'
            ]"
          >
            <Icon icon="lucide:thumbs-up" class="w-3 h-3 text-amber-400" />
            <span class="font-bold">亮了</span>
            <span class="font-mono font-bold">{{ getLikesCount(cIdx, cmt.likes) }}</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <div v-else class="text-center py-10 text-slate-500 text-xs bg-slate-900/40 rounded-xl border border-slate-800">
    <Icon icon="lucide:messages-square" class="w-6 h-6 mx-auto mb-2 text-slate-600" />
    <p>暂无该场次的球迷社区热评</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  news: {
    type: Object,
    default: null
  }
})

const threadData = computed(() => {
  return props.news?.hupu_thread || null
})

const coachScoreColor = computed(() => {
  const score = Number(threadData.value?.coach_score) || 0
  if (score >= 8.5) return 'text-emerald-400'
  if (score >= 7.0) return 'text-teal-400'
  return 'text-amber-400'
})

// 点赞互动
const likedComments = ref({})
const toggleLike = (cIdx) => {
  likedComments.value[cIdx] = !likedComments.value[cIdx]
}
const isLiked = (cIdx) => !!likedComments.value[cIdx]
const getLikesCount = (cIdx, baseLikes = 0) => {
  return isLiked(cIdx) ? baseLikes + 1 : baseLikes
}
</script>