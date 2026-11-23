<template>
  <div class="p-4 space-y-4 animate-in fade-in duration-150">
    
    <!-- 1. 顶栏：球迷广场与主帅全季评价总览 -->
    <div class="bg-gradient-to-r from-slate-900 via-slate-850 to-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-3 shadow-sm">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="text-base">🔥</span>
          <div>
            <h2 class="text-xs font-black text-white tracking-wide">维尔通球迷广场 · 全赛程热评大盘</h2>
            <p class="text-[9px] text-slate-400 font-sans">汇聚 21 轮全部比赛赛后热评、主帅评分走势与社区吃瓜</p>
          </div>
        </div>
        <span class="text-[9px] bg-rose-950 text-rose-300 border border-rose-800 px-2 py-0.5 rounded-full font-bold">
          21轮全记录
        </span>
      </div>

      <!-- 主帅赛季总评分大盘卡 -->
      <div class="bg-slate-950 p-3 rounded-xl border border-slate-850 space-y-2.5">
        <div class="flex items-center justify-between">
          <div>
            <div class="text-[10px] text-slate-400 font-bold">徐指导 · 全季21轮执教综合评分</div>
            <div class="text-[10px] text-emerald-400 mt-0.5">
              {{ communityData?.season_coach_summary?.trend_label || '豪取三连胜稳坐冲甲附加区' }}
            </div>
          </div>
          <div class="text-right">
            <span class="text-3xl font-black text-emerald-400 font-mono tracking-tight">
              {{ communityData?.season_coach_summary?.average_score || 9.0 }}
            </span>
            <span class="text-xs text-slate-400 font-bold ml-0.5">/ 10</span>
          </div>
        </div>

        <div class="flex items-center justify-between text-[10px] text-slate-400 border-t border-slate-850 pt-1.5">
          <span>球迷好评率: <strong class="text-amber-400">{{ communityData?.season_coach_summary?.support_rate || '95.8%' }}</strong></span>
          <span>参与评选人次: <strong class="text-slate-200">{{ communityData?.season_coach_summary?.total_votes || '21,850' }}</strong></span>
        </div>

        <!-- 走势视图切换条 (动态折线走势图 vs 轮次药丸) -->
        <div class="flex items-center justify-between pt-1">
          <div class="text-[9px] text-slate-500 font-bold">
            全季主帅执教战术评分走势：
          </div>
          <div class="bg-slate-900 border border-slate-800 rounded-lg p-0.5 flex space-x-1">
            <button
              @click="chartViewMode = 'chart'"
              :class="['px-2 py-0.5 rounded text-[10px] font-semibold transition', chartViewMode === 'chart' ? 'bg-emerald-600 text-white font-bold' : 'text-slate-400 hover:text-white']"
            >
              📈 趋势图表
            </button>
            <button
              @click="chartViewMode = 'pills'"
              :class="['px-2 py-0.5 rounded text-[10px] font-semibold transition', chartViewMode === 'pills' ? 'bg-emerald-600 text-white font-bold' : 'text-slate-400 hover:text-white']"
            >
              📋 轮次卡片
            </button>
          </div>
        </div>

        <!-- 模式 A: 平滑折线走势图 -->
        <div v-show="chartViewMode === 'chart'" class="pt-0.5">
          <ScoreTrendChart :scores="communityData?.season_coach_summary?.round_scores || []" />
        </div>

        <!-- 模式 B: 历轮评分滑动卡片 (覆盖全部21轮) -->
        <div v-show="chartViewMode === 'pills'" class="space-y-1 pt-1">
          <div class="text-[9px] text-slate-500 font-bold flex justify-between">
            <span>横向轻扫查看历场执教评分：</span>
            <span>滑动浏览 ›</span>
          </div>
          <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar py-0.5 select-none">
            <div
              v-for="r in (communityData?.season_coach_summary?.round_scores || [])"
              :key="r.round"
              class="bg-slate-900 border border-slate-800 rounded-lg p-1.5 shrink-0 text-center w-[78px] transition hover:border-slate-700 cursor-pointer"
              @click="filterByRound(r.round)"
            >
              <div class="text-[9px] text-slate-400 truncate">{{ r.round >= 29 ? (r.round === 32 ? '🏆冲甲决胜' : '附加赛') : ('第' + r.round + '轮') }}</div>
              <div :class="[
                'text-xs font-black font-mono my-0.5',
                r.score >= 9.0 ? 'text-emerald-400' :
                r.score >= 8.0 ? 'text-teal-300' :
                r.score >= 7.0 ? 'text-amber-300' : 'text-rose-400'
              ]">
                {{ r.score }}分
              </div>
              <div class="text-[8px] bg-slate-950 px-1 py-0.2 rounded text-slate-400 truncate">
                {{ r.opponent || r.badge || '联赛' }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. 核心大板块切换 (💬 历轮比赛总评 vs 🔥 社区热帖广场) -->
    <div class="flex p-1 bg-slate-900 border border-slate-800 rounded-xl shadow-sm">
      <button
        @click="activeMainTab = 'match_reviews'"
        :class="[
          'flex-1 py-1.5 text-xs font-bold rounded-lg transition flex items-center justify-center space-x-1.5',
          activeMainTab === 'match_reviews'
            ? 'bg-emerald-600 text-white shadow-sm'
            : 'text-slate-400 hover:text-white'
        ]"
      >
        <span>💬</span>
        <span>历轮比赛总评 (21轮历史热评)</span>
      </button>

      <button
        @click="activeMainTab = 'forum_threads'"
        :class="[
          'flex-1 py-1.5 text-xs font-bold rounded-lg transition flex items-center justify-center space-x-1.5',
          activeMainTab === 'forum_threads'
            ? 'bg-emerald-600 text-white shadow-sm'
            : 'text-slate-400 hover:text-white'
        ]"
      >
        <span>🔥</span>
        <span>社区热帖广场 (转会与日常)</span>
      </button>
    </div>

    <!-- 板块 A: 💬 历轮比赛总评 (包含全赛季从第 1 轮到第 21 轮的所有历史评论) -->
    <div v-if="activeMainTab === 'match_reviews'" class="space-y-3">
      <!-- 轮次快速过滤胶囊 -->
      <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar text-xs py-0.5">
        <button
          @click="selectedRoundFilter = null"
          :class="[
            'px-2.5 py-1 rounded-full text-xs font-semibold shrink-0 transition flex items-center space-x-1',
            selectedRoundFilter === null
              ? 'bg-emerald-600 text-white font-bold shadow-sm'
              : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
          ]"
        >
          <span>📋</span>
          <span>全季全部战报 ({{ availableRounds.length }}场)</span>
        </button>

        <button
          v-for="rNum in availableRounds"
          :key="rNum"
          @click="selectedRoundFilter = rNum"
          :class="[
            'px-2 py-0.8 rounded-full text-[11px] font-mono shrink-0 transition',
            selectedRoundFilter === rNum
              ? 'bg-emerald-600 text-white font-bold shadow-sm'
              : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
          ]"
        >
          {{ rNum >= 29 ? (rNum === 32 ? '🏆 决胜战' : ('附加赛 R' + rNum)) : ('第' + rNum + '轮') }}
        </button>
      </div>

      <!-- 历史比赛热评瀑布流 -->
      <div class="space-y-3.5">
        <div
          v-for="item in displayedMatchReviews"
          :key="item.round"
          class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-3 shadow-sm hover:border-slate-700 transition"
        >
          <!-- 比赛概况顶栏 -->
          <div class="flex items-center justify-between text-xs border-b border-slate-800/60 pb-2">
            <div class="flex items-center space-x-2">
              <span class="text-[10px] bg-slate-800 text-teal-300 font-bold px-1.5 py-0.5 rounded border border-slate-700">
                第 {{ item.round }} 轮
              </span>
              <span class="text-slate-400 text-[10px] font-mono">{{ item.match?.date }}</span>
              <span class="font-bold text-white text-xs">
                {{ item.match?.home_team }} {{ item.match?.score_home }} - {{ item.match?.score_away }} {{ item.match?.away_team }}
              </span>
            </div>

            <!-- 胜负与单场主帅评分 -->
            <div class="flex items-center space-x-2 shrink-0">
              <span :class="[
                'text-[9px] px-1.5 py-0.2 rounded font-bold font-mono',
                item.match?.result === 'W' ? 'bg-emerald-950 text-emerald-300 border border-emerald-800' :
                item.match?.result === 'D' ? 'bg-amber-950 text-amber-300 border border-amber-800' :
                'bg-rose-950 text-rose-300 border border-rose-800'
              ]">
                {{ item.match?.result === 'W' ? '胜仗' : item.match?.result === 'D' ? '平局' : '失利' }}
              </span>
              <span v-if="item.hupu_thread?.coach_score" class="text-xs font-black font-mono text-emerald-400 bg-slate-950 px-2 py-0.5 rounded border border-slate-800">
                ⭐ {{ item.hupu_thread.coach_score }}分
              </span>
            </div>
          </div>

          <!-- 该场比赛的虎扑亮帖热评 -->
          <div v-if="item.hupu_thread && item.hupu_thread.comments && item.hupu_thread.comments.length" class="space-y-2">
            <div class="text-[10px] text-slate-400 font-bold flex items-center space-x-1">
              <span>🔥</span>
              <span>虎扑亮了 · 球迷实时讨论 ({{ item.hupu_thread.comments.length }}条精选)</span>
            </div>

            <div
              v-for="(cmt, cIdx) in item.hupu_thread.comments"
              :key="cIdx"
              class="bg-slate-950/70 p-2.5 rounded-lg border border-slate-850/80 space-y-1.5 text-xs"
            >
              <div class="flex items-center justify-between text-[11px]">
                <div class="flex items-center space-x-2">
                  <div class="w-5 h-5 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-[10px] font-bold text-slate-300">
                    {{ cmt.username.slice(0, 1) }}
                  </div>
                  <span class="font-bold text-slate-200">{{ cmt.username }}</span>
                  <span class="text-[9px] bg-slate-900 text-amber-300/90 px-1.5 py-0.2 rounded border border-amber-900/40">
                    {{ cmt.tag }}
                  </span>
                </div>
                <span class="text-[9px] text-slate-500 font-mono">#{{ cIdx + 1 }}楼</span>
              </div>

              <p class="text-slate-300 leading-relaxed font-sans text-xs">
                {{ cmt.content }}
              </p>

              <div class="flex justify-end pt-0.5">
                <button
                  @click="toggleCommentLike(item.round, cIdx)"
                  :class="[
                    'text-[10px] px-2 py-0.5 rounded-full flex items-center space-x-1 transition',
                    isCommentLiked(item.round, cIdx)
                      ? 'bg-rose-950 text-rose-400 border border-rose-800 font-bold'
                      : 'bg-slate-900 text-slate-400 hover:text-slate-200'
                  ]"
                >
                  <span>{{ isCommentLiked(item.round, cIdx) ? '❤️ 已亮' : '👍 点亮' }}</span>
                  <span class="font-mono font-bold">{{ getCommentLikes(item.round, cIdx, cmt.likes) }}</span>
                </button>
              </div>
            </div>
          </div>

          <div v-else class="text-slate-500 text-[11px] py-2 text-center bg-slate-950/40 rounded-lg">
            暂无本场特别记录
          </div>

          <!-- 查看单场详情入口 -->
          <div class="flex justify-end pt-1 border-t border-slate-800/40">
            <button
              @click="$emit('select-match', item.match?.id)"
              class="text-[11px] text-emerald-400 hover:text-emerald-300 font-bold flex items-center space-x-1 transition"
            >
              <span>查看本场完整战报与首发阵容</span>
              <span>→</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- 板块 B: 🔥 社区热帖广场 (转会传闻、名场面、战术研讨与周边) -->
    <div v-else-if="activeMainTab === 'forum_threads'" class="space-y-3">
      <!-- 分类筛选 Tabs -->
      <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar text-xs py-0.5">
        <button
          v-for="tab in filterTabs"
          :key="tab.key"
          @click="activeCategory = tab.key"
          :class="[
            'px-3 py-1.5 rounded-full text-xs font-semibold shrink-0 transition flex items-center space-x-1 whitespace-nowrap',
            activeCategory === tab.key
              ? 'bg-emerald-600 text-white font-bold shadow-sm'
              : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
          ]"
        >
          <span>{{ tab.icon }}</span>
          <span>{{ tab.label }}</span>
        </button>
      </div>

      <!-- 帖子列表瀑布流 -->
      <div class="space-y-3">
        <div
          v-for="thread in filteredThreads"
          :key="thread.id"
          class="bg-slate-900 border border-slate-800 hover:border-slate-700 rounded-xl p-3.5 space-y-2.5 transition shadow-sm"
        >
          <!-- 发帖人与分类标头 -->
          <div class="flex items-center justify-between text-xs">
            <div class="flex items-center space-x-2">
              <div class="w-7 h-7 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-sm">
                {{ thread.avatar || '⚽' }}
              </div>
              <div>
                <div class="flex items-center space-x-1.5">
                  <span class="font-bold text-slate-200 text-xs">{{ thread.author }}</span>
                  <span class="text-[9px] bg-slate-800 text-amber-300 px-1.5 py-0.2 rounded border border-amber-900/30">
                    {{ thread.tag }}
                  </span>
                </div>
                <div class="text-[9px] text-slate-500 font-mono mt-0.5">{{ thread.time }}</div>
              </div>
            </div>

            <div class="flex items-center space-x-1.5">
              <span v-if="thread.is_hot" class="text-[9px] bg-rose-950 text-rose-400 px-1.5 py-0.2 rounded font-bold border border-rose-900">
                🔥 热门
              </span>
              <span class="text-[9px] bg-slate-800 text-teal-300 px-2 py-0.5 rounded border border-slate-700">
                {{ thread.category_label }}
              </span>
            </div>
          </div>

          <!-- 帖子标题 -->
          <h3 class="text-xs font-bold text-white leading-snug hover:text-emerald-400 transition cursor-pointer">
            {{ thread.title }}
          </h3>

          <!-- 帖子正文 -->
          <p class="text-xs text-slate-300 leading-relaxed font-sans bg-slate-950/70 p-2.5 rounded-lg border border-slate-850 whitespace-pre-line">
            {{ thread.content }}
          </p>

          <!-- 精选热评折叠区 -->
          <div v-if="thread.top_replies && thread.top_replies.length" class="space-y-1.5 pt-1 border-t border-slate-800/60">
            <div class="text-[10px] text-slate-400 font-bold flex items-center space-x-1">
              <span>💬</span>
              <span>高赞热评精选</span>
            </div>

            <div
              v-for="(reply, rIdx) in thread.top_replies"
              :key="rIdx"
              class="bg-slate-950/60 p-2 rounded-lg border border-slate-850/80 text-[11px] space-y-1"
            >
              <div class="flex items-center justify-between text-slate-400">
                <div class="flex items-center space-x-1.5">
                  <span class="font-semibold text-slate-300">{{ reply.username }}</span>
                  <span v-if="reply.tag" class="text-[9px] bg-slate-900 text-amber-300/80 px-1 py-0.2 rounded">
                    {{ reply.tag }}
                  </span>
                </div>
                <span class="text-[10px] text-rose-400">❤️ {{ reply.likes || 120 }} 亮</span>
              </div>
              <p class="text-slate-300 leading-relaxed">{{ reply.content }}</p>
            </div>
          </div>

          <!-- 底部互动栏 (亮了 / 评论 / 浏览) -->
          <div class="flex items-center justify-between pt-1 border-t border-slate-800/40 text-[11px] text-slate-400">
            <div class="flex items-center space-x-3 text-[10px] text-slate-500 font-mono">
              <span>👁️ {{ thread.views || 1000 }} 阅读</span>
              <span>💬 {{ thread.reply_count || 10 }} 讨论</span>
            </div>

            <button
              @click="toggleThreadLike(thread.id)"
              :class="[
                'px-2.5 py-1 rounded-full flex items-center space-x-1 text-xs transition',
                isThreadLiked(thread.id)
                  ? 'bg-rose-950 text-rose-400 border border-rose-800 font-bold'
                  : 'bg-slate-800 hover:bg-slate-700 text-slate-300'
              ]"
            >
              <span>{{ isThreadLiked(thread.id) ? '❤️ 已亮' : '👍 点亮' }}</span>
              <span class="font-mono font-bold">{{ getThreadLikes(thread.id, thread.likes || 100) }}</span>
            </button>
          </div>
        </div>

        <div v-if="!filteredThreads.length" class="text-center py-12 text-slate-500 text-xs">
          暂无该分类下的讨论帖
        </div>
      </div>
    </div>

    <!-- 3. 底部发表新球迷热评互动卡 -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-2">
      <div class="text-[11px] font-bold text-slate-300 flex items-center justify-between">
        <span>✍️ 发表你的球迷热评</span>
        <span class="text-[9px] text-slate-500">文明发言 · 传递纯粹足球</span>
      </div>
      <div class="flex items-center space-x-2">
        <input
          v-model="newCommentText"
          type="text"
          placeholder="聊聊徐指导的战术，或者点评本轮球员表现..."
          @keyup.enter="submitNewComment"
          class="flex-1 bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-xs text-slate-200 placeholder-slate-600 focus:outline-none focus:border-emerald-500 transition"
        />
        <button
          @click="submitNewComment"
          class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs px-3.5 py-2 rounded-lg transition shrink-0 shadow-sm"
        >
          发布
        </button>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ScoreTrendChart from '../common/ScoreTrendChart.vue'

const props = defineProps({
  communityData: {
    type: Object,
    required: true
  },
  newsList: {
    type: Array,
    default: () => []
  },
  matchesList: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['select-match'])

// 走势图模式：'chart' (折线图) vs 'pills' (药丸列表)
const chartViewMode = ref('chart')

// 核心两大版块切换：'match_reviews' (历轮比赛总评) vs 'forum_threads' (社区热帖广场)
const activeMainTab = ref('match_reviews')

// 轮次筛选器 (null 表示全部轮次)
const selectedRoundFilter = ref(null)

const filterByRound = (rNum) => {
  activeMainTab.value = 'match_reviews'
  selectedRoundFilter.value = rNum
}

// 可选轮次列表
const availableRounds = computed(() => {
  const rSet = new Set(props.matchesList.map(m => m.round))
  return Array.from(rSet).sort((a, b) => b - a)
})

// 历轮比赛总评数据聚合 (包含从第21轮倒序至第1轮的全部历史评论)
const allMatchReviews = computed(() => {
  const sortedMatches = [...props.matchesList].sort((a, b) => b.round - a.round)
  return sortedMatches.map(m => {
    const newsItem = props.newsList.find(n => n.round === m.round)
    return {
      round: m.round,
      match: m,
      hupu_thread: newsItem?.hupu_thread || null
    }
  })
})

const displayedMatchReviews = computed(() => {
  if (selectedRoundFilter.value === null) {
    return allMatchReviews.value
  }
  return allMatchReviews.value.filter(item => item.round === selectedRoundFilter.value)
})

// 分类筛选 Tabs (社区热帖广场)
const activeCategory = ref('all')
const filterTabs = [
  { key: 'all', label: '全部热议', icon: '🔥' },
  { key: 'matches', label: '比赛复盘', icon: '⚽' },
  { key: 'coach', label: '主帅专区', icon: '💼' },
  { key: 'transfer', label: '转会传闻', icon: '💰' },
  { key: 'tactics', label: '战术研讨', icon: '🔬' },
  { key: 'offpitch', label: '场外日常', icon: '🍺' }
]

// 论坛动态帖子列表
const localThreads = ref([...(props.communityData?.threads || [])])

const filteredThreads = computed(() => {
  if (activeCategory.value === 'all') return localThreads.value
  return localThreads.value.filter(t => t.category === activeCategory.value)
})

// 评论点赞互动
const likedCommentMap = ref({})
const toggleCommentLike = (rNum, cIdx) => {
  const key = `${rNum}_${cIdx}`
  likedCommentMap.value[key] = !likedCommentMap.value[key]
}
const isCommentLiked = (rNum, cIdx) => !!likedCommentMap.value[`${rNum}_${cIdx}`]
const getCommentLikes = (rNum, cIdx, baseLikes = 100) => {
  return isCommentLiked(rNum, cIdx) ? baseLikes + 1 : baseLikes
}

// 帖子点赞互动
const likedThreadMap = ref({})
const toggleThreadLike = (id) => {
  likedThreadMap.value[id] = !likedThreadMap.value[id]
}
const isThreadLiked = (id) => !!likedThreadMap.value[id]
const getThreadLikes = (id, baseLikes = 100) => {
  return isThreadLiked(id) ? baseLikes + 1 : baseLikes
}

// 用户发表新评论互动
const newCommentText = ref('')
const submitNewComment = () => {
  if (!newCommentText.value.trim()) return
  const newThread = {
    id: 'user_' + Date.now(),
    category: activeCategory.value === 'all' ? 'matches' : activeCategory.value,
    category_label: filterTabs.find(t => t.key === activeCategory.value)?.label || '球迷热评',
    title: '【球迷实时发言】' + newCommentText.value.trim().slice(0, 24) + (newCommentText.value.length > 24 ? '...' : ''),
    author: '现场热心老哥',
    avatar: '🤠',
    tag: '忠实球迷',
    time: '刚刚',
    is_hot: true,
    views: 1,
    likes: 1,
    content: newCommentText.value.trim(),
    reply_count: 0,
    top_replies: []
  }
  localThreads.value.unshift(newThread)
  activeMainTab.value = 'forum_threads'
  newCommentText.value = ''
}
</script>
