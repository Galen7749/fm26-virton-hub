<template>
  <div class="space-y-4 animate-in fade-in duration-150 pb-6">

    <!-- 1. 顶部：焦点赛事横滑区 (Match Ticker) -->
    <section class="space-y-1.5 px-3 pt-3">
      <div class="flex items-center justify-between text-xs text-slate-400 px-1">
        <span class="font-bold inline-flex items-center gap-1.5 text-slate-200">
          <Icon icon="lucide:activity" class="w-3.5 h-3.5 text-emerald-400 animate-pulse" />
          <span>焦点战报 · 即时比分</span>
        </span>
        <span class="text-[10px] text-slate-500 inline-flex items-center gap-0.5">
          <span>左右横滑</span>
          <Icon icon="lucide:chevron-right" class="w-3 h-3" />
        </span>
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
            <span class="font-bold text-slate-300 inline-flex items-center gap-1.5">
              <Icon :icon="ticker.league_flag || 'circle-flags:eu'" class="w-3.5 h-3.5 rounded-full" />
              <span>{{ ticker.league_short }}</span>
              <span v-if="ticker.is_overseas" class="inline-flex items-center gap-0.5 bg-red-950 text-red-300 border border-red-800 px-1.5 py-0.2 rounded font-bold text-[9px]">
                <Icon icon="circle-flags:cn" class="w-2.5 h-2.5" />
                <span>留洋</span>
              </span>
            </span>
            <span class="inline-flex items-center gap-1 bg-slate-950 text-emerald-400 px-2 py-0.5 rounded font-mono font-bold border border-emerald-950 text-[10px]">
              <Icon icon="lucide:check-circle" class="w-2.5 h-2.5" />
              <span>{{ ticker.time }}</span>
            </span>
          </div>

          <!-- 主客对阵比分 -->
          <div class="py-2.5 flex items-center justify-between">
            <!-- 主队 -->
            <div class="flex-1 text-center min-w-0 pr-1 flex flex-col items-center">
              <div
                class="w-7 h-7 rounded-full flex items-center justify-center font-bold text-[10px] text-white border border-slate-700 shadow-sm"
                :style="{ backgroundColor: ticker.home_color || '#334155' }"
              >
                {{ ticker.home_code || ticker.home_team.slice(0, 2) }}
              </div>
              <div class="text-xs font-bold text-white truncate mt-1 w-full">{{ ticker.home_team }}</div>
            </div>

            <!-- 比分 -->
            <div class="shrink-0 px-2.5 text-center">
              <span class="text-lg font-black text-white font-mono tracking-wider">
                {{ ticker.score_home }} - {{ ticker.score_away }}
              </span>
              <div class="text-[9px] text-slate-400 mt-0.5">{{ ticker.status }}</div>
            </div>

            <!-- 客队 -->
            <div class="flex-1 text-center min-w-0 pl-1 flex flex-col items-center">
              <div
                class="w-7 h-7 rounded-full flex items-center justify-center font-bold text-[10px] text-white border border-slate-700 shadow-sm"
                :style="{ backgroundColor: ticker.away_color || '#334155' }"
              >
                {{ ticker.away_code || ticker.away_team.slice(0, 2) }}
              </div>
              <div class="text-xs font-bold text-white truncate mt-1 w-full">{{ ticker.away_team }}</div>
            </div>
          </div>

          <!-- 亮点数据行 -->
          <div class="text-[10px] text-slate-400 bg-slate-950 px-2 py-1 rounded truncate border border-slate-850 inline-flex items-center gap-1.5 w-full">
            <Icon icon="lucide:zap" class="w-3 h-3 text-amber-400 shrink-0" />
            <span class="truncate">{{ ticker.highlights }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. 二级轻量胶囊筛选 (全部头条 | 留洋专区 | 转会动态) -->
    <section class="px-3">
      <div class="bg-slate-900 border border-slate-800 p-1 rounded-xl flex items-center space-x-1 text-xs">
        <button
          @click="activeCategory = 'headline'"
          :class="[
            'flex-1 py-1.5 rounded-lg font-bold text-center transition inline-flex items-center justify-center gap-1.5',
            activeCategory === 'headline'
              ? 'bg-emerald-600 text-white shadow-sm font-black'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="ri:fire-fill" class="w-3.5 h-3.5 text-rose-400" />
          <span>全部头条</span>
        </button>

        <button
          @click="activeCategory = 'overseas'"
          :class="[
            'flex-1 py-1.5 rounded-lg font-bold text-center transition inline-flex items-center justify-center gap-1.5',
            activeCategory === 'overseas'
              ? 'bg-red-700 text-white shadow-sm font-black'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="circle-flags:cn" class="w-3.5 h-3.5" />
          <span>留洋专区</span>
        </button>

        <button
          @click="activeCategory = 'transfer'"
          :class="[
            'flex-1 py-1.5 rounded-lg font-bold text-center transition inline-flex items-center justify-center gap-1.5',
            activeCategory === 'transfer'
              ? 'bg-emerald-600 text-white shadow-sm font-black'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="tabler:arrows-exchange" class="w-3.5 h-3.5 text-emerald-300" />
          <span>转会动态</span>
        </button>
      </div>
    </section>

    <!-- 3. 新闻信息流列表 -->
    <section class="px-3 space-y-2.5">
      <!-- 留洋时间线专栏提示（当在留洋专区时） -->
      <div v-if="activeCategory === 'overseas'" class="bg-slate-900/90 border border-red-900/40 rounded-xl p-2.5 flex items-center justify-between text-xs">
        <div class="inline-flex items-center gap-2">
          <Icon icon="circle-flags:cn" class="w-5 h-5" />
          <div>
            <div class="font-bold text-slate-200">中国籍主帅欧洲执教战报</div>
            <div class="text-[10px] text-slate-400">时间倒序跟踪 · 维尔通冲甲至奥波莱奥德拉</div>
          </div>
        </div>
        <span class="inline-flex items-center gap-1 text-[10px] bg-red-950 text-red-300 border border-red-800 px-2 py-0.5 rounded font-mono font-bold">
          <Icon icon="lucide:archive" class="w-2.5 h-2.5" />
          <span>留洋档案</span>
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
          <div class="inline-flex items-center gap-2">
            <span :class="[
              'inline-flex items-center gap-1 px-1.5 py-0.5 rounded font-bold border',
              item.is_overseas ? 'bg-red-950 text-red-300 border-red-800' : 'bg-slate-800 text-teal-300 border-teal-900/40'
            ]">
              <Icon :icon="item.is_overseas ? 'circle-flags:cn' : 'circle-flags:eu'" class="w-2.5 h-2.5" />
              <span>{{ item.tag || (item.is_overseas ? '留洋报道' : '国际足球') }}</span>
            </span>
            <span class="text-slate-400 font-medium">{{ item.source }}</span>
          </div>
          <span class="text-slate-500 font-mono inline-flex items-center gap-1">
            <Icon icon="lucide:clock" class="w-2.5 h-2.5" />
            <span>{{ item.time }}</span>
          </span>
        </div>

        <!-- 标题 -->
        <h3 class="text-xs sm:text-sm font-bold text-white hover:text-emerald-400 transition leading-snug">
          {{ item.title }}
        </h3>

        <!-- 摘要 -->
        <p class="text-[11px] text-slate-400 leading-relaxed line-clamp-2">
          {{ item.summary }}
        </p>

        <!-- 底部数据栏：阅读数、评论数、作者 -->
        <div class="flex items-center justify-between text-[10px] text-slate-500 pt-1 border-t border-slate-800/60 font-sans">
          <span class="inline-flex items-center gap-1">
            <Icon icon="lucide:user" class="w-2.5 h-2.5" />
            <span>{{ item.author ? '作者: ' + item.author : '懂球云编辑部' }}</span>
          </span>
          <div class="inline-flex items-center gap-3">
            <span class="inline-flex items-center gap-1">
              <Icon icon="lucide:eye" class="w-3 h-3 text-slate-400" />
              <span>{{ item.reads }}</span>
            </span>
            <span class="inline-flex items-center gap-1">
              <Icon icon="lucide:message-circle" class="w-3 h-3 text-slate-400" />
              <span>{{ item.comments_count }} 评</span>
            </span>
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
          <div class="inline-flex items-center gap-2">
            <span class="text-xs bg-emerald-950 text-emerald-400 px-2 py-0.5 rounded font-bold border border-emerald-900">
              {{ selectedArticle.source }}
            </span>
            <span class="text-[11px] text-slate-400 inline-flex items-center gap-1">
              <Icon icon="lucide:clock" class="w-3 h-3" />
              <span>{{ selectedArticle.time }}</span>
            </span>
          </div>
          <button
            @click="selectedArticle = null"
            class="w-6 h-6 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white inline-flex items-center justify-center text-xs transition"
          >
            <Icon icon="lucide:x" class="w-3.5 h-3.5" />
          </button>
        </div>

        <!-- 弹窗内容 -->
        <div class="flex-1 overflow-y-auto p-4 space-y-3.5 text-xs text-slate-200">
          <h2 class="text-sm sm:text-base font-black text-white leading-snug">
            {{ selectedArticle.title }}
          </h2>

          <div class="flex items-center space-x-3 text-[11px] text-slate-400 pb-2 border-b border-slate-800">
            <span class="inline-flex items-center gap-1">
              <Icon icon="lucide:user" class="w-3 h-3" />
              <span>记者: {{ selectedArticle.author || '特派报道' }}</span>
            </span>
            <span>·</span>
            <span>发布时间: {{ selectedArticle.date }}</span>
          </div>

          <div class="text-[11px] sm:text-xs text-slate-300 leading-relaxed whitespace-pre-line space-y-2">
            {{ selectedArticle.content || selectedArticle.summary }}
          </div>

          <!-- 模拟评论互动区 -->
          <div class="pt-4 border-t border-slate-800 space-y-2.5">
            <div class="text-[11px] font-bold text-slate-300 flex items-center justify-between">
              <span class="inline-flex items-center gap-1.5">
                <Icon icon="lucide:message-circle" class="w-3.5 h-3.5 text-emerald-400" />
                <span>热门球迷热议 ({{ currentArticleComments.length }})</span>
              </span>
              <span class="text-emerald-400 text-[10px] cursor-pointer hover:underline">发表评论</span>
            </div>

            <div
              v-for="(cmt, cIdx) in currentArticleComments"
              :key="cIdx"
              class="bg-slate-950 p-2.5 rounded-lg border border-slate-850 space-y-1"
            >
              <div class="flex items-center justify-between text-[10px]">
                <div class="flex items-center space-x-1.5">
                  <div class="w-4 h-4 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-[9px] font-bold text-emerald-400">
                    {{ cmt.user.slice(0, 1) }}
                  </div>
                  <span class="font-bold text-slate-200">{{ cmt.user }}</span>
                  <span v-if="cmt.badge" class="text-[9px] px-1 py-0.2 rounded bg-slate-900 text-amber-300 border border-amber-900/40">
                    {{ cmt.badge }}
                  </span>
                </div>
                <div class="text-slate-500 inline-flex items-center gap-1">
                  <span>{{ cmt.time }} · </span>
                  <Icon icon="lucide:thumbs-up" class="w-2.5 h-2.5 text-amber-400" />
                  <span>{{ cmt.likes }}</span>
                </div>
              </div>
              <p class="text-[10px] text-slate-300 leading-relaxed pl-1">
                {{ cmt.text }}
              </p>
            </div>
          </div>
        </div>

        <!-- 弹窗底栏 -->
        <div class="bg-slate-950 px-4 py-2.5 border-t border-slate-800 flex items-center justify-between text-xs">
          <span class="text-slate-500 text-[10px] inline-flex items-center gap-1">
            <Icon icon="lucide:cloud" class="w-3 h-3 text-emerald-500" />
            <span>懂球云 · 权威足球资讯</span>
          </span>
          <button
            @click="selectedArticle = null"
            class="px-3 py-1 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg font-bold text-xs transition inline-flex items-center gap-1"
          >
            <span>完成阅读</span>
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
import newsCommentsRaw from '../../data/news_comments.json'

defineProps({
  matches: {
    type: Array,
    default: () => []
  }
})

defineEmits(['select-match'])

const tickerMatches = ref(tickerMatchesRaw)
const newsArticles = ref(newsArticlesRaw)

// 3 个轻量胶囊筛选：'headline' (全部头条) | 'overseas' (留洋专区) | 'transfer' (转会动态)
const activeCategory = ref('headline')
const selectedArticle = ref(null)

const currentArticleComments = computed(() => {
  if (!selectedArticle.value) return []
  const specific = newsCommentsRaw[selectedArticle.value.id]
  if (specific && specific.length) return specific
  if (selectedArticle.value.category === 'transfer') {
    return [
      { user: '转会雷达', badge: '转会分析', time: '1小时前', likes: 88, text: '夏窗豪门军备竞赛正处于关键节点，体检和签字很快跟进。' },
      { user: '绿茵球探', badge: '数据控', time: '2小时前', likes: 45, text: '这名球员的战术执行力和身体机能非常契合当前体系，看好能打出来。' }
    ]
  }
  return [
    { user: '球迷老张', badge: '资深球迷', time: '刚刚', likes: 62, text: '欧洲赛场的攻防节奏太快了，战术转换的执行力和对抗让人印象深刻！' },
    { user: '足球战术室', badge: '战术分析', time: '25分钟前', likes: 39, text: '双方在攻防转换阶段的微调很见功底，值得赛后反复复盘。' }
  ]
})

const filteredNews = computed(() => {
  if (activeCategory.value === 'headline') {
    return newsArticles.value
  } else if (activeCategory.value === 'overseas') {
    return newsArticles.value.filter(n => n.category === 'overseas' || n.is_overseas)
  } else if (activeCategory.value === 'transfer') {
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
