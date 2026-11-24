<template>
  <div class="space-y-3.5 p-3.5 animate-in fade-in duration-150 pb-6">

    <!-- 1. 顶部控制栏：社区版块标头 + 【热门 | 最新】排序切换 -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 flex items-center justify-between shadow-sm">
      <div class="inline-flex items-center gap-2">
        <div class="w-7 h-7 rounded-lg bg-rose-950/80 border border-rose-800/60 flex items-center justify-center text-rose-400">
          <Icon icon="ri:fire-fill" class="w-4 h-4" />
        </div>
        <div>
          <h2 class="text-xs font-black text-white tracking-wide">虎扑足球论坛 · 球迷热议大盘</h2>
          <p class="text-[9px] text-slate-400 font-sans">真实球迷热帖 · 技战术复盘与欧战风云</p>
        </div>
      </div>

      <!-- 排序切换胶囊：严格保留 热门 | 最新 -->
      <div class="bg-slate-950 p-1 rounded-lg border border-slate-800 inline-flex items-center gap-1 text-xs">
        <button
          @click="activeSort = 'hot'"
          :class="[
            'px-2.5 py-1 rounded-md text-[11px] font-bold transition inline-flex items-center gap-1',
            activeSort === 'hot'
              ? 'bg-rose-600 text-white shadow-sm'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="ri:fire-fill" class="w-3 h-3 text-amber-200" />
          <span>热门</span>
        </button>
        <button
          @click="activeSort = 'latest'"
          :class="[
            'px-2.5 py-1 rounded-md text-[11px] font-bold transition inline-flex items-center gap-1',
            activeSort === 'latest'
              ? 'bg-emerald-600 text-white shadow-sm'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="lucide:sparkles" class="w-3 h-3 text-emerald-200" />
          <span>最新</span>
        </button>
      </div>
    </div>

    <!-- 2. 二级版块微筛选（全部 / 国际足球 / 留洋专区 / 英超专区 / 转会专区） -->
    <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar py-0.5 text-xs">
      <button
        v-for="cat in categoryFilters"
        :key="cat.key"
        @click="selectedCategory = cat.key"
        :class="[
          'px-2.5 py-1 rounded-full text-[11px] font-semibold shrink-0 transition inline-flex items-center gap-1.5',
          selectedCategory === cat.key
            ? 'bg-slate-800 text-emerald-400 border border-emerald-500/50 font-bold'
            : 'bg-slate-900 text-slate-400 border border-slate-800 hover:text-slate-200'
        ]"
      >
        <Icon :icon="cat.icon" class="w-3 h-3" />
        <span>{{ cat.label }}</span>
      </button>
    </div>

    <!-- 3. 仿虎扑论坛帖子列表流 -->
    <div class="space-y-2.5">
      <article
        v-for="post in sortedPosts"
        :key="post.id"
        class="bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-slate-700 rounded-xl p-3.5 space-y-2.5 transition shadow-sm"
      >
        <!-- 头部作者信息与版块小标签 -->
        <div class="flex items-center justify-between text-[11px]">
          <div class="inline-flex items-center gap-2">
            <span class="w-5 h-5 rounded-full bg-slate-800 border border-slate-700 inline-flex items-center justify-center font-bold text-[9px] text-slate-300">
              {{ post.author.slice(0, 1) }}
            </span>
            <span class="font-bold text-slate-200 truncate max-w-[120px]">{{ post.author }}</span>
            <span v-if="post.tag" class="bg-slate-950 text-slate-400 px-1.5 py-0.2 rounded text-[9px] border border-slate-800">
              {{ post.tag }}
            </span>
          </div>

          <div class="inline-flex items-center gap-2">
            <!-- 所属版块小标签（使用矢量国旗或专用图标） -->
            <span :class="[
              'inline-flex items-center gap-1 px-2 py-0.5 rounded font-bold text-[9px] border',
              post.category === '留洋专区'
                ? 'bg-red-950 text-red-300 border-red-800'
                : 'bg-slate-800 text-teal-300 border-teal-900/40'
            ]">
              <Icon :icon="post.category === '留洋专区' ? 'circle-flags:cn' : post.category === '英超专区' ? 'circle-flags:gb-eng' : 'circle-flags:eu'" class="w-2.5 h-2.5" />
              <span>{{ post.category }}</span>
            </span>
            <span class="text-slate-500 font-mono text-[10px] inline-flex items-center gap-0.5">
              <Icon icon="lucide:clock" class="w-2.5 h-2.5" />
              <span>{{ post.time }}</span>
            </span>
          </div>
        </div>

        <!-- 帖子标题（点击展开阅读） -->
        <h3
          @click="toggleExpand(post.id)"
          class="text-xs sm:text-sm font-bold text-white hover:text-emerald-400 cursor-pointer leading-snug transition"
        >
          {{ post.title }}
        </h3>

        <!-- 帖子内容摘要或展开正文 -->
        <div
          v-if="expandedPostId === post.id"
          class="space-y-3 pt-1 text-xs text-slate-300 border-t border-slate-850 animate-in fade-in duration-150"
        >
          <p class="whitespace-pre-line leading-relaxed bg-slate-950/60 p-3 rounded-lg border border-slate-850">
            {{ post.content }}
          </p>

          <!-- 亮评展示区 (虎扑经典亮评) -->
          <div v-if="post.replies && post.replies.length" class="space-y-2 pt-1">
            <div class="text-[11px] font-bold text-amber-400 inline-flex items-center gap-1.5">
              <Icon icon="lucide:lightbulb" class="w-3.5 h-3.5" />
              <span>虎扑亮评 ({{ post.replies.length }})</span>
            </div>

            <div
              v-for="rep in post.replies"
              :key="rep.id"
              class="bg-slate-950 p-2.5 rounded-lg border border-slate-850 space-y-1.5 text-xs"
            >
              <div class="flex items-center justify-between text-[10px]">
                <div class="inline-flex items-center gap-1.5">
                  <span class="font-bold text-slate-200">{{ rep.username }}</span>
                  <span class="text-slate-500 bg-slate-900 px-1 rounded text-[9px]">{{ rep.tag }}</span>
                </div>
                <button
                  @click="rep.likes++"
                  class="inline-flex items-center gap-1 text-amber-400 hover:text-amber-300 font-mono font-bold transition"
                >
                  <Icon icon="lucide:thumbs-up" class="w-2.5 h-2.5" />
                  <span>亮了</span>
                  <span>({{ rep.likes }})</span>
                </button>
              </div>
              <p class="text-[11px] text-slate-300 leading-relaxed">
                {{ rep.content }}
              </p>
            </div>
          </div>
        </div>

        <!-- 底部数据栏：亮评数与回复数 -->
        <div class="flex items-center justify-between text-[10px] text-slate-500 pt-1 border-t border-slate-800/60 font-mono">
          <div class="inline-flex items-center gap-3">
            <button
              @click="post.likes++"
              class="inline-flex items-center gap-1 hover:text-rose-400 transition"
            >
              <Icon icon="lucide:thumbs-up" class="w-3 h-3 text-rose-500/80" />
              <span>亮评</span>
              <span class="font-bold text-slate-400">{{ post.likes }}</span>
            </button>
            <span class="inline-flex items-center gap-1">
              <Icon icon="lucide:message-circle" class="w-3 h-3 text-slate-400" />
              <span>回复</span>
              <span class="font-bold text-slate-400">{{ post.reply_count }}</span>
            </span>
          </div>

          <button
            @click="toggleExpand(post.id)"
            class="text-emerald-400 hover:underline font-sans text-[11px] inline-flex items-center gap-0.5"
          >
            <span>{{ expandedPostId === post.id ? '收起详情' : '查看讨论与亮评' }}</span>
            <Icon :icon="expandedPostId === post.id ? 'lucide:chevron-up' : 'lucide:chevron-down'" class="w-3 h-3" />
          </button>
        </div>
      </article>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import communityPostsRaw from '../../data/community_posts.json'

const posts = ref(communityPostsRaw)

// 排序模式：'hot' (热门) | 'latest' (最新)
const activeSort = ref('hot')

// 版块微筛选（带专属矢量国旗/图样）
const selectedCategory = ref('all')
const categoryFilters = [
  { key: 'all', label: '全部热帖', icon: 'lucide:layout-grid' },
  { key: '国际足球', label: '国际足球', icon: 'circle-flags:eu' },
  { key: '留洋专区', label: '留洋专区', icon: 'circle-flags:cn' },
  { key: '英超专区', label: '英超专区', icon: 'circle-flags:gb-eng' },
  { key: '转会专区', label: '转会专区', icon: 'tabler:arrows-exchange' }
]

const expandedPostId = ref('post_ucl_final')

const toggleExpand = (id) => {
  expandedPostId.value = expandedPostId.value === id ? null : id
}

// 过滤与排序
const sortedPosts = computed(() => {
  let list = posts.value

  if (selectedCategory.value !== 'all') {
    list = list.filter(p => p.category === selectedCategory.value)
  }

  if (activeSort.value === 'hot') {
    return [...list].sort((a, b) => (b.likes + b.reply_count * 5) - (a.likes + a.reply_count * 5))
  } else {
    return [...list].sort((a, b) => (b.created_at || 0) - (a.created_at || 0))
  }
})
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
