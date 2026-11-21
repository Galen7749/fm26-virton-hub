<template>
  <div
    @click="$emit('select', match.id)"
    class="bg-slate-900 border border-slate-800 hover:border-slate-700 rounded-xl p-3.5 space-y-2.5 cursor-pointer transition shadow-sm hover:shadow-md group active:scale-[0.99]"
  >
    <!-- 顶栏：轮次、赛事、日期、主客场与赛果标签 -->
    <div class="flex items-center justify-between text-xs">
      <div class="flex items-center space-x-2">
        <span class="text-[10px] bg-slate-800 text-teal-300 font-bold px-1.5 py-0.5 rounded border border-slate-700">
          {{ match.competition || '比乙' }} · {{ match.round_label || ('第 ' + match.round + ' 轮') }}
        </span>
        <span class="text-slate-400 text-[11px] font-mono">{{ match.date }}</span>
        <span class="text-[10px] text-slate-500">({{ match.venue === 'home' ? '主场' : '客场' }})</span>
      </div>

      <!-- 胜平负彩标 -->
      <span
        :class="[
          'text-[10px] font-bold px-2 py-0.5 rounded-full border',
          match.result === 'W' || match.result === '胜' ? 'bg-emerald-950 text-emerald-400 border-emerald-800' :
          match.result === 'D' || match.result === '平' ? 'bg-amber-950 text-amber-300 border-amber-800' :
          'bg-rose-950 text-rose-400 border-rose-800'
        ]"
      >
        {{ match.result === 'W' ? '胜仗' : match.result === 'D' ? '平局' : '失利' }}
      </span>
    </div>

    <!-- 中间对阵与比分 -->
    <div class="flex items-center justify-between py-1 px-1">
      <!-- 主队 -->
      <div class="w-5/12 text-right pr-2">
        <div :class="[
          'text-xs font-bold truncate',
          match.home_team.includes('维尔通') ? 'text-emerald-400 font-black' : 'text-slate-200'
        ]">
          {{ match.home_team }}
        </div>
        <div class="text-[10px] text-slate-500 mt-0.5">主队</div>
      </div>

      <!-- 比分 -->
      <div class="w-2/12 text-center shrink-0">
        <span class="bg-slate-950 text-white font-mono font-black text-base px-2.5 py-1 rounded-lg border border-slate-800 tracking-wider shadow-inner inline-block">
          {{ match.score_home }} - {{ match.score_away }}
        </span>
      </div>

      <!-- 客队 -->
      <div class="w-5/12 text-left pl-2">
        <div :class="[
          'text-xs font-bold truncate',
          match.away_team.includes('维尔通') ? 'text-emerald-400 font-black' : 'text-slate-200'
        ]">
          {{ match.away_team }}
        </div>
        <div class="text-[10px] text-slate-500 mt-0.5">客队</div>
      </div>
    </div>

    <!-- 进球摘要 -->
    <div v-if="match.scorers && match.scorers.length" class="text-[11px] text-slate-400 flex items-center flex-wrap gap-1.5 pt-1 border-t border-slate-800/60">
      <span class="text-xs">⚽</span>
      <span v-for="(sc, sIdx) in match.scorers" :key="sIdx" class="text-slate-300">
        {{ sc.player_zh || sc.player }} ({{ sc.minute }}')<span v-if="sIdx < match.scorers.length - 1">,</span>
      </span>
    </div>

    <!-- 底栏数据指示与进入详情入口 -->
    <div class="flex items-center justify-between pt-1 border-t border-slate-800/40 text-[10px] text-slate-400">
      <div class="flex items-center space-x-3 font-mono">
        <span>xG <strong class="text-slate-200 font-semibold">{{ match.xg }}</strong></span>
        <span>射门 <strong class="text-slate-200 font-semibold">{{ match.shots }}({{ match.shots_on_target }})</strong></span>
        <span v-if="match.distance_km">跑动 <strong class="text-slate-200 font-semibold">{{ match.distance_km }}km</strong></span>
      </div>
      <div class="text-emerald-400 font-bold flex items-center space-x-1 group-hover:translate-x-0.5 transition-transform">
        <span>战报与阵容</span>
        <span class="text-xs">→</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  match: {
    type: Object,
    required: true
  }
})

defineEmits(['select'])
</script>
