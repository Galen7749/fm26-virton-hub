<template>
  <div v-if="news && (news.dongqiudi_article || news.title)" class="space-y-4 text-xs animate-in fade-in duration-150">
    <!-- 标头与标签 -->
    <div>
      <div class="flex flex-wrap gap-1.5 mb-2">
        <span
          v-for="tag in articleTags"
          :key="tag"
          class="text-[10px] bg-slate-800 text-emerald-400 px-2 py-0.5 rounded border border-slate-700"
        >
          #{{ tag }}
        </span>
      </div>
      <h2 class="text-base font-bold text-white leading-snug">
        {{ articleTitle }}
      </h2>
      <p class="text-xs text-slate-400 mt-1 inline-flex items-center gap-1.5">
        <Icon icon="lucide:clock" class="w-3 h-3 text-slate-500" />
        <span>发布于 {{ matchDate }} · {{ reporterLabel }}</span>
      </p>
    </div>

    <!-- 摘要金句 -->
    <div v-if="articleSummary" class="bg-emerald-950/40 border-l-4 border-emerald-500 p-3 rounded-r-lg text-xs text-emerald-200/90 leading-relaxed shadow-sm">
      {{ articleSummary }}
    </div>

    <!-- 正文段落 -->
    <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
      <p
        v-for="(para, pIdx) in articleParagraphs"
        :key="pIdx"
        :class="para.startsWith('【') ? 'font-bold text-slate-100 text-sm pt-2 text-emerald-400' : ''"
      >
        {{ para }}
      </p>
    </div>

    <!-- 当地主流体育媒体声音 -->
    <div v-if="news.local_media_snippet" class="bg-slate-900 border border-slate-800 rounded-lg p-3 space-y-1.5 shadow-sm">
      <div class="flex items-center space-x-1.5 text-xs font-bold text-slate-200">
        <Icon :icon="news.local_media_snippet.country_flag || (isPoland ? 'circle-flags:pl' : 'circle-flags:be')" class="w-3.5 h-3.5 rounded-full shrink-0" />
        <span>当地媒体《{{ news.local_media_snippet.outlet || (isPoland ? '波兰体育周刊' : 'L\'Avenir') }}》社论摘要</span>
      </div>
      <p class="text-[11px] text-slate-400 leading-relaxed italic">
        “{{ news.local_media_snippet.quote }}”
      </p>
      <div v-if="news.local_media_snippet.journalist" class="text-[9px] text-slate-500 text-right">
        —— 首席随队记者 {{ news.local_media_snippet.journalist }}
      </div>
    </div>
  </div>

  <div v-else class="text-center py-10 text-slate-500 text-xs bg-slate-900/40 rounded-xl border border-slate-800">
    <Icon icon="lucide:file-question" class="w-6 h-6 mx-auto mb-2 text-slate-600" />
    <p>暂无该场次的媒体深度战报</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  news: {
    type: Object,
    default: null
  },
  matchDate: {
    type: String,
    default: ''
  }
})

const isPoland = computed(() => {
  return props.news?.league === '波甲' || props.matchDate?.startsWith('2026')
})

const articleTitle = computed(() => {
  return props.news?.dongqiudi_article?.title || props.news?.title || ''
})

const articleSummary = computed(() => {
  return props.news?.dongqiudi_article?.summary || props.news?.summary || ''
})

const articleTags = computed(() => {
  return props.news?.dongqiudi_article?.tags || props.news?.tags || ['波甲', '奥波莱奥德拉', '留洋战报']
})

const reporterLabel = computed(() => {
  if (props.news?.reporter) return `${props.news.reporter} · 懂球云专稿`
  return isPoland.value ? '波兰足球前线 · 懂球云特派' : '比利时足球前线 · 懂球云特派'
})

const articleParagraphs = computed(() => {
  const body = props.news?.dongqiudi_article?.body || props.news?.body || props.news?.content || ''
  if (!body) return []
  return body.split('\n\n')
})
</script>