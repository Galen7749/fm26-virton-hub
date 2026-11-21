<template>
  <div v-if="news && news.hupu_thread" class="space-y-4">
    <!-- 主帅评分卡片 -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 flex items-center justify-between shadow-sm">
      <div>
        <div class="text-xs text-slate-400">本场主帅综合战术评分</div>
        <div class="text-xs text-slate-500 mt-0.5">超过 2,481 名球迷参与投票</div>
      </div>
      <div class="text-right">
        <span :class="['text-3xl font-black tracking-tight', coachScoreColor]">
          {{ news.hupu_thread.coach_score }}
        </span>
        <span class="text-xs text-slate-400 font-bold ml-0.5">/ 10</span>
      </div>
    </div>

    <!-- 虎扑高亮热评列表 -->
    <div class="space-y-3">
      <div class="flex justify-between items-center text-xs text-slate-400">
        <span class="font-bold text-slate-200">🔥 虎扑亮了·全网热议</span>
        <span>按赞同排序</span>
      </div>

      <div
        v-for="(cmt, cIdx) in news.hupu_thread.comments"
        :key="cIdx"
        class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3 space-y-2 hover:border-slate-700 transition"
      >
        <div class="flex items-center justify-between text-xs">
          <div class="flex items-center space-x-2">
            <div class="w-6 h-6 rounded-full bg-slate-700 flex items-center justify-center text-[10px] font-bold text-slate-200">
              {{ cmt.username.slice(0, 1) }}
            </div>
            <span class="font-semibold text-slate-200 text-xs">{{ cmt.username }}</span>
            <span class="text-[10px] bg-slate-800 text-amber-300/90 px-1.5 py-0.2 rounded border border-amber-900/40">
              {{ cmt.tag }}
            </span>
          </div>
          <span class="text-[10px] text-slate-500">#{{ cIdx + 1 }} 楼</span>
        </div>

        <p class="text-xs text-slate-300 leading-relaxed">
          {{ cmt.content }}
        </p>

        <div class="flex justify-end pt-1">
          <button
            @click="toggleLike(news.match_id, cIdx)"
            :class="[
              'text-[11px] px-2.5 py-1 rounded-full flex items-center space-x-1 transition',
              isLiked(news.match_id, cIdx)
                ? 'bg-rose-950 text-rose-400 border border-rose-800'
                : 'bg-slate-800/70 text-slate-400 hover:text-slate-200'
            ]"
          >
            <span>{{ isLiked(news.match_id, cIdx) ? '❤️ 亮了' : '👍 亮了' }}</span>
            <span class="font-semibold">{{ getLikesCount(news.match_id, cIdx, cmt.likes) }}</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <div v-else class="text-center py-10 text-slate-500 text-xs">
    暂无该场次的球迷社区热评
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

const coachScoreColor = computed(() => {
  const score = props.news?.hupu_thread?.coach_score || 0
  if (score >= 8.5) return 'text-emerald-400'
  if (score >= 7.0) return 'text-teal-400'
  return 'text-amber-400'
})

// 点赞互动
const likedComments = ref({})
const toggleLike = (matchId, cIdx) => {
  const key = `${matchId}_${cIdx}`
  likedComments.value[key] = !likedComments.value[key]
}
const isLiked = (matchId, cIdx) => !!likedComments.value[`${matchId}_${cIdx}`]
const getLikesCount = (matchId, cIdx, baseLikes) => {
  return isLiked(matchId, cIdx) ? baseLikes + 1 : baseLikes
}
</script>
