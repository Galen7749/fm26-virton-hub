<template>
  <div class="p-4 space-y-4 animate-in fade-in duration-150">
    
    <!-- 1. 顶栏：球迷广场与主帅全季评价总览 -->
    <div class="bg-gradient-to-r from-slate-900 via-slate-850 to-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-3 shadow-sm">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="text-base">🔥</span>
          <div>
            <h2 class="text-xs font-black text-white tracking-wide">维尔通球迷广场 · 虎扑热议区</h2>
            <p class="text-[9px] text-slate-400 font-sans">汇聚全网战报复盘、主帅总评、转会吃瓜与场外花絮</p>
          </div>
        </div>
        <span class="text-[9px] bg-rose-950 text-rose-300 border border-rose-800 px-2 py-0.5 rounded-full font-bold">
          全网热议中
        </span>
      </div>

      <!-- 主帅赛季总评分大盘卡 -->
      <div class="bg-slate-950 p-3 rounded-xl border border-slate-850 space-y-2.5">
        <div class="flex items-center justify-between">
          <div>
            <div class="text-[10px] text-slate-400 font-bold">徐指导 · 前8轮执教综合评分</div>
            <div class="text-[10px] text-emerald-400 mt-0.5">
              {{ communityData?.season_coach_summary?.trend_label || '两连胜杀入冲甲附加区' }}
            </div>
          </div>
          <div class="text-right">
            <span class="text-3xl font-black text-emerald-400 font-mono tracking-tight">
              {{ communityData?.season_coach_summary?.average_score || 8.9 }}
            </span>
            <span class="text-xs text-slate-400 font-bold ml-0.5">/ 10</span>
          </div>
        </div>

        <div class="flex items-center justify-between text-[10px] text-slate-400 border-t border-slate-850 pt-1.5">
          <span>球迷好评率: <strong class="text-amber-400">{{ communityData?.season_coach_summary?.support_rate || '94.6%' }}</strong></span>
          <span>参与评选人数: <strong class="text-slate-200">{{ communityData?.season_coach_summary?.total_votes || '19,850' }}</strong></span>
        </div>

        <!-- 历轮评分走势小滑块条 -->
        <div class="space-y-1 pt-1">
          <div class="text-[9px] text-slate-500 font-bold flex justify-between">
            <span>各轮次单场主帅评分走势：</span>
            <span>滑动查看全部轮次 ›</span>
          </div>
          <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar py-0.5 select-none">
            <div
              v-for="r in (communityData?.season_coach_summary?.round_scores || [])"
              :key="r.round"
              class="bg-slate-900 border border-slate-800 rounded-lg p-1.5 shrink-0 text-center w-[76px] transition hover:border-slate-700"
            >
              <div class="text-[9px] text-slate-400 truncate">第{{ r.round }}轮</div>
              <div :class="[
                'text-xs font-black font-mono my-0.5',
                r.score >= 9.0 ? 'text-emerald-400' :
                r.score >= 8.0 ? 'text-teal-300' :
                r.score >= 7.0 ? 'text-amber-300' : 'text-rose-400'
              ]">
                {{ r.score }}分
              </div>
              <div class="text-[8px] bg-slate-950 px-1 py-0.2 rounded text-slate-400 truncate">
                {{ r.badge }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. 分类标签筛选栏 -->
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

    <!-- 3. 帖子列表瀑布流 -->
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
              {{ thread.avatar }}
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
              <span class="font-semibold text-slate-300">{{ reply.username }}</span>
              <span class="text-[10px] text-rose-400">❤️ {{ reply.likes }} 亮</span>
            </div>
            <p class="text-slate-300 leading-relaxed">{{ reply.content }}</p>
          </div>
        </div>

        <!-- 底部互动栏 (亮了 / 评论 / 浏览) -->
        <div class="flex items-center justify-between pt-1 border-t border-slate-800/40 text-[11px] text-slate-400">
          <div class="flex items-center space-x-3 text-[10px] text-slate-500 font-mono">
            <span>👁️ {{ thread.views }} 阅读</span>
            <span>💬 {{ thread.reply_count }} 讨论</span>
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
            <span class="font-mono font-bold">{{ getThreadLikes(thread.id, thread.likes) }}</span>
          </button>
        </div>
      </div>

      <div v-if="!filteredThreads.length" class="text-center py-12 text-slate-500 text-xs">
        暂无该分类下的讨论帖
      </div>
    </div>

    <!-- 4. 底部发帖互动入口 -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-2">
      <div class="text-[11px] font-bold text-slate-300 flex items-center justify-between">
        <span>✍️ 发表你的球迷热评</span>
        <span class="text-[9px] text-slate-500">文明发言 · 传递纯粹足球</span>
      </div>
      <div class="flex items-center space-x-2">
        <input
          v-model="newCommentText"
          type="text"
          placeholder="聊聊徐指导的战术，或者爆料场外八卦..."
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

const props = defineProps({
  communityData: {
    type: Object,
    required: true
  }
})

// 分类筛选 Tabs
const activeCategory = ref('all')
const filterTabs = [
  { key: 'all', label: '全部热议', icon: '🔥' },
  { key: 'matches', label: '比赛复盘', icon: '⚽' },
  { key: 'coach', label: '主帅专区', icon: '💼' },
  { key: 'transfer', label: '转会传闻', icon: '💰' },
  { key: 'tactics', label: '战术研讨', icon: '🔬' },
  { key: 'offpitch', label: '场外日常', icon: '🍺' }
]

// 动态帖子列表
const localThreads = ref([...(props.communityData?.threads || [])])

const filteredThreads = computed(() => {
  if (activeCategory.value === 'all') return localThreads.value
  return localThreads.value.filter(t => t.category === activeCategory.value)
})

// 点亮点赞互动
const likedThreadMap = ref({})
const toggleThreadLike = (id) => {
  likedThreadMap.value[id] = !likedThreadMap.value[id]
}
const isThreadLiked = (id) => !!likedThreadMap.value[id]
const getThreadLikes = (id, baseLikes) => {
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
    author: '热心维尔通老哥',
    avatar: '🤠',
    tag: '现场球迷',
    time: '刚刚',
    is_hot: true,
    views: 1,
    likes: 1,
    content: newCommentText.value.trim(),
    reply_count: 0,
    top_replies: []
  }
  localThreads.value.unshift(newThread)
  newCommentText.value = ''
}
</script>
