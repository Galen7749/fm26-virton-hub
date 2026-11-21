<template>
  <div v-if="news" class="space-y-4 text-xs">
    <!-- 标头与标签 -->
    <div>
      <div class="flex flex-wrap gap-1.5 mb-2">
        <span
          v-for="tag in (news.dongqiudi_article?.tags || [])"
          :key="tag"
          class="text-[10px] bg-slate-800 text-emerald-400 px-2 py-0.5 rounded border border-slate-700"
        >
          #{{ tag }}
        </span>
      </div>
      <h2 class="text-base font-bold text-white leading-snug">
        {{ news.dongqiudi_article?.title }}
      </h2>
      <p class="text-xs text-slate-400 mt-1">
        发布于 {{ matchDate }} · 比利时足球前线 · 懂球云专稿
      </p>
    </div>

    <!-- 摘要金句 -->
    <div class="bg-emerald-950/40 border-l-4 border-emerald-500 p-3 rounded-r-lg text-xs text-emerald-200/90 leading-relaxed">
      {{ news.dongqiudi_article?.summary }}
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

    <!-- 比利时公开媒体声音 -->
    <div class="bg-slate-900 border border-slate-800 rounded-lg p-3">
      <div class="flex items-center space-x-1.5 text-xs font-bold text-slate-200 mb-1.5">
        <span>🇧🇪</span>
        <span>当地媒体《L'Avenir》社论摘要</span>
      </div>
      <p class="text-[11px] text-slate-400 leading-relaxed italic">
        “{{ news.local_media_snippet?.quote || '维尔通在战术执行力上展现出惊人纪律，但能否在紧密的赛程下保持高位逼抢的体能负荷，将是未来数周的最大考验。' }}”
      </p>
      <div class="text-[9px] text-slate-500 text-right mt-1">
        —— 首席随队记者 {{ news.local_media_snippet?.journalist || 'Philippe De Witte' }}
      </div>
    </div>
  </div>

  <div v-else class="text-center py-10 text-slate-500 text-xs">
    暂无该场次的媒体深度战报
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

const articleParagraphs = computed(() => {
  if (!props.news?.dongqiudi_article?.body) return []
  return props.news.dongqiudi_article.body.split('\n\n')
})
</script>
