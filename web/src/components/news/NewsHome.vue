<template>
  <div class="space-y-4 animate-in fade-in duration-150 pb-6">

    <!-- 1. 顶部：焦点赛事横滑区 (Match Ticker) -->
    <section class="space-y-1.5 px-3 pt-3">
      <div class="flex items-center justify-between text-xs text-slate-400 px-1">
        <span class="font-bold flex items-center space-x-1.5 text-slate-200">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>焦点战报 · 即时比分</span>
        </span>
        <span class="text-[10px] text-slate-500">左右横滑查看 ›</span>
      </div>

      <!-- 横滑卡片轨道 -->
      <div class="flex space-x-2.5 overflow-x-auto no-scrollbar py-1 px-0.5 select-none scroll-smooth">
        <div
          v-for="ticker in tickerMatches"
          :key="ticker.id"
          @click="$emit('select-match', ticker.match_id)"
          class="shrink-0 w-64 bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-slate-700 rounded-xl p-3 shadow-md cursor-pointer transition transform hover:-translate-y-0.5 flex flex-col justify-between"
        >
          <!-- 联赛与状态标签 -->
          <div class="flex items-center justify-between text-[10px] pb-2 border-b border-slate-800/80">
            <span class="font-bold text-slate-300 flex items-center space-x-1">
              <span>{{ ticker.league_short }}</span>
              <span v-if="ticker.is_overseas" class="bg-red-950 text-red-300 border border-red-800 px-1.5 py-0.2 rounded font-bold text-[9px]">
                🇨🇳 留洋
              </span>
            </span>
            <span class="bg-slate-950 text-emerald-400 px-2 py-0.5 rounded font-mono font-bold border border-emerald-950">
              {{ ticker.time }}
            </span>
          </div>

          <!-- 主客对阵比分 -->
          <div class="py-2.5 flex items-center justify-between">
            <!-- 主队 -->
            <div class="flex-1 text-center min-w-0 pr-1">
              <div class="text-base">{{ ticker.home_logo }}</div>
              <div class="text-xs font-bold text-white truncate mt-1">{{ ticker.home_team }}</div>
            </div>

            <!-- 比分 -->
            <div class="shrink-0 px-2.5 text-center">
              <span class="text-lg font-black text-white font-mono tracking-wider">
                {{ ticker.score_home }} - {{ ticker.score_away }}
              </span>
              <div class="text-[9px] text-slate-400 mt-0.5">{{ ticker.status }}</div>
            </div>

            <!-- 客队 -->
            <div class="flex-1 text-center min-w-0 pl-1">
              <div class="text-base">{{ ticker.away_logo }}</div>
              <div class="text-xs font-bold text-white truncate mt-1">{{ ticker.away_team }}</div>
            </div>
          </div>

          <!-- 亮点一句话 -->
          <div class="text-[10px] text-slate-400 bg-slate-950 px-2 py-1 rounded truncate border border-slate-850">
            ⚡ {{ ticker.highlights }}
          </div>
        </div>
      </div>
    </section>

    <!-- 2. 二级轻量胶囊筛选 (严格 3 个：全部头条 | 🇨🇳 留洋 | 转会) -->
    <section class="px-3">
      <div class="bg-slate-900 border border-slate-800 p-1 rounded-xl flex items-center space-x-1 text-xs">
        <button
          @click="activeCategory = 'headline'"
          :class="[
            'flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1',
            activeCategory === 'headline'
              ? 'bg-emerald-600 text-white shadow-sm font-black'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <span>🔥</span>
          <span>全部头条</span>
        </button>

        <button
          @click="activeCategory = 'overseas'"
          :class="[
            'flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1',
            activeCategory === 'overseas'
              ? 'bg-red-700 text-white shadow-sm font-black'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <span>🇨🇳</span>
          <span>留洋专区</span>
        </button>

        <button
          @click="activeCategory = 'transfer'"
          :class="[
            'flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1',
            activeCategory === 'transfer'
              ? 'bg-emerald-600 text-white shadow-sm font-black'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <span>🚨</span>
          <span>转会动态</span>
        </button>
      </div>
    </section>

    <!-- 3. 新闻信息流列表 -->
    <section class="px-3 space-y-2.5">
      <!-- 留洋时间线专栏提示（当在留洋专区时） -->
      <div v-if="activeCategory === 'overseas'" class="bg-slate-900/90 border border-red-900/40 rounded-xl p-2.5 flex items-center justify-between text-xs">
        <div class="flex items-center space-x-2">
          <span class="text-base">🇨🇳</span>
          <div>
            <div class="font-bold text-slate-200">中国籍主教练欧洲执教动态</div>
            <div class="text-[10px] text-slate-400">时间倒序跟踪 · 维尔通奇迹冲甲至奥波莱奥德拉</div>
          </div>
        </div>
        <span class="text-[10px] bg-red-950 text-red-300 border border-red-800 px-2 py-0.5 rounded font-mono font-bold">
          全记录
        </span>
      </div>

      <!-- 新闻条目卡片 -->
      <article
        v-for="item in filteredNews"
        :key="item.id"
        @click="openNews(item)"
        class="bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-slate-700 rounded-xl p-3.5 space-y-2.5 cursor-pointer transition shadow-sm"
      >
        <!-- 标签与来源 -->
        <div class="flex items-center justify-between text-[10px]">
          <div class="flex items-center space-x-2">
            <span :class="[
              'px-1.5 py-0.5 rounded font-bold border',
              item.is_overseas ? 'bg-red-950 text-red-300 border-red-800' : 'bg-slate-800 text-teal-300 border-teal-900/40'
            ]">
              {{ item.tag || (item.is_overseas ? '留洋报道' : '国际足球') }}
            </span>
            <span class="text-slate-400 font-medium">{{ item.source }}</span>
          </div>
          <span class="text-slate-500 font-mono">{{ item.time }}</span>
        </div>

        <!-- 标题 -->
        <h3 class="text-xs sm:text-sm font-bold text-white hover:text-emerald-400 transition leading-snug">
          {{ item.title }}
        </h3>

        <!-- 摘要摘要 -->
        <p class="text-[11px] text-slate-400 leading-relaxed line-clamp-2">
          {{ item.summary }}
        </p>

        <!-- 底部数据栏：阅读数、评论数、作者 -->
        <div class="flex items-center justify-between text-[10px] text-slate-500 pt-1 border-t border-slate-800/60 font-sans">
          <span>{{ item.author ? '作者: ' + item.author : '懂球云编辑部' }}</span>
          <div class="flex items-center space-x-3">
            <span>👁️ {{ item.reads }}</span>
            <span>💬 {{ item.comments_count }} 评</span>
          </div>
        </div>
      </article>
    </section>

    <!-- 新闻阅读 Modal 弹窗 -->
    <div
      v-if="selectedArticle"
      class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in duration-150"
    >
      <div class="absolute inset-0" @click="selectedArticle = null"></div>
      <div class="relative w-full max-w-lg bg-slate-900 border border-slate-700 rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[85vh] z-10">
        <!-- 弹窗顶栏 -->
        <div class="bg-slate-950 px-4 py-3 border-b border-slate-800 flex items-center justify-between">
          <div class="flex items-center space-x-2">
            <span class="text-xs bg-emerald-950 text-emerald-400 px-2 py-0.5 rounded font-bold border border-emerald-900">
              {{ selectedArticle.source }}
            </span>
            <span class="text-[11px] text-slate-400">{{ selectedArticle.time }}</span>
          </div>
          <button
            @click="selectedArticle = null"
            class="w-6 h-6 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs transition"
          >
            ✕
          </button>
        </div>

        <!-- 弹窗内容 -->
        <div class="flex-1 overflow-y-auto p-4 space-y-3.5 text-xs text-slate-200">
          <h2 class="text-sm sm:text-base font-black text-white leading-snug">
            {{ selectedArticle.title }}
          </h2>

          <div class="flex items-center space-x-3 text-[11px] text-slate-400 pb-2 border-b border-slate-800">
            <span>记者: {{ selectedArticle.author || '特派报道' }}</span>
            <span>·</span>
            <span>发布时间: {{ selectedArticle.date }}</span>
          </div>

          <div class="text-[11px] sm:text-xs text-slate-300 leading-relaxed whitespace-pre-line space-y-2">
            {{ selectedArticle.content || selectedArticle.summary }}
          </div>

          <!-- 模拟评论互动区 -->
          <div class="pt-4 border-t border-slate-800 space-y-2.5">
            <div class="text-[11px] font-bold text-slate-300 flex items-center justify-between">
              <span>热门评论 ({{ selectedArticle.comments_count }})</span>
              <span class="text-emerald-400 text-[10px]">发表评论</span>
            </div>
            <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-850 space-y-1">
              <div class="flex items-center justify-between text-[10px]">
                <span class="font-bold text-slate-200">Galen</span>
                <span class="text-slate-500">刚刚 · 👍 89</span>
              </div>
              <p class="text-[10px] text-slate-400">
                这场比赛看得真过瘾！中国教练在欧洲联赛带队拼下开门红，战术思路非常清晰。
              </p>
            </div>
          </div>
        </div>

        <!-- 弹窗底栏 -->
        <div class="bg-slate-950 px-4 py-2.5 border-t border-slate-800 flex items-center justify-between text-xs">
          <span class="text-slate-500 text-[10px]">☁️ 懂球云 · 权威足球资讯</span>
          <button
            @click="selectedArticle = null"
            class="px-3 py-1 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg font-bold text-xs transition"
          >
            完成阅读
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

import tickerMatchesRaw from '../../data/ticker_matches.json'
import newsArticlesRaw from '../../data/news_articles.json'

defineProps({
  matches: {
    type: Array,
    default: () => []
  }
})

defineEmits(['select-match'])

const tickerMatches = ref(tickerMatchesRaw)
const newsArticles = ref(newsArticlesRaw)

// 3 个轻量胶囊筛选：'headline' (全部头条) | 'overseas' (🇨🇳 留洋) | 'transfer' (转会)
const activeCategory = ref('headline')
const selectedArticle = ref(null)

const filteredNews = computed(() => {
  if (activeCategory.value === 'headline') {
    // 全部头条：混排世界足坛新闻与留洋新闻
    return newsArticles.value
  } else if (activeCategory.value === 'overseas') {
    // 🇨🇳 留洋：按时间倒序展示从维尔通时期到奥波莱时期的所有中国主帅相关新闻
    return newsArticles.value.filter(n => n.category === 'overseas' || n.is_overseas)
  } else if (activeCategory.value === 'transfer') {
    // 转会：转会流言与官方动态
    return newsArticles.value.filter(n => n.category === 'transfer')
  }
  return newsArticles.value
})

const openNews = (article) => {
  selectedArticle.value = article
}
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
