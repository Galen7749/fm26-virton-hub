<template>
  <div
    @click="$emit('select', match.id)"
    class="bg-slate-900 border border-slate-800 hover:border-slate-700 rounded-xl p-3.5 space-y-2.5 cursor-pointer transition shadow-sm hover:shadow-md group active:scale-[0.99]"
  >
    <!-- 顶栏：轮次、赛事、日期、主客场与赛果标签 -->
    <div class="flex items-center justify-between text-xs">
      <div class="flex items-center space-x-2">
        <span
          :class="[
            'text-[10px] font-bold px-1.5 py-0.5 rounded border',
            match.stage_title?.includes('绝杀') ? 'bg-amber-950 text-amber-300 border-amber-600 font-black shadow-sm' :
            match.is_playoff || match.stage_title?.includes('冲甲') ? 'bg-indigo-950 text-indigo-300 border-indigo-700' :
            'bg-slate-800 text-teal-300 border-slate-700'
          ]"
        >
          {{ match.stage_title || ((match.competition || '比乙') + ' · 第 ' + match.round + ' 轮') }}
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
    <div class="flex items-center justify-between py-1.5 px-1">
      <!-- 主队 -->
      <div class="flex-1 text-right pr-2 min-w-0">
        <div :class="[
          'text-xs font-bold truncate',
          match.home_team.includes('维尔通') ? 'text-emerald-400 font-black' : 'text-slate-200'
        ]">
          {{ match.home_team }}
        </div>
        <div class="text-[10px] text-slate-500 mt-0.5">主队</div>
      </div>

      <!-- 比分 (绝对不折行) -->
      <div class="shrink-0 text-center mx-1.5">
        <span class="bg-slate-950 text-white font-mono font-black text-sm px-3 py-1 rounded-lg border border-slate-800 tracking-wider shadow-inner inline-flex items-center justify-center whitespace-nowrap min-w-[54px] select-none">
          {{ match.score_home }} - {{ match.score_away }}
        </span>
      </div>

      <!-- 客队 -->
      <div class="flex-1 text-left pl-2 min-w-0">
        <div :class="[
          'text-xs font-bold truncate',
          match.away_team.includes('维尔通') ? 'text-emerald-400 font-black' : 'text-slate-200'
        ]">
          {{ match.away_team }}
        </div>
        <div class="text-[10px] text-slate-500 mt-0.5">客队</div>
      </div>
    </div>

    <!-- 进球摘要 (主客双栏清晰对阵) -->
    <div v-if="match.scorers && match.scorers.length" class="text-[11px] text-slate-400 pt-1.5 border-t border-slate-800/60">
      <div class="grid grid-cols-2 gap-2 text-[10.5px]">
        <!-- 主队进球 (右对齐贴向比分) -->
        <div class="text-right truncate pr-1">
          <span v-if="homeScorers.length" class="text-slate-300">
            <template v-for="(sc, i) in homeScorers" :key="'h-'+i">
              <span :class="sc.is_virton ? 'text-emerald-400 font-semibold' : 'text-slate-300'">
                {{ sc.player_zh || sc.player }} {{ formatMinute(sc.minute) }}
                <span v-if="sc.is_stoppage || String(sc.minute).includes('+')" class="text-[9px] bg-amber-950 text-amber-300 px-1 py-0.2 rounded border border-amber-800/60 font-bold">绝杀</span>
              </span>
              <span v-if="i < homeScorers.length - 1" class="text-slate-600 mr-1">,</span>
            </template>
            <span class="text-xs ml-1">⚽</span>
          </span>
          <span v-else class="text-slate-600 text-[10px]">-</span>
        </div>

        <!-- 客队进球 (左对齐贴向比分) -->
        <div class="text-left truncate pl-1 border-l border-slate-800/60">
          <span v-if="awayScorers.length" class="text-slate-300">
            <span class="text-xs mr-1">⚽</span>
            <template v-for="(sc, i) in awayScorers" :key="'a-'+i">
              <span :class="sc.is_virton ? 'text-emerald-400 font-semibold' : 'text-slate-300'">
                {{ sc.player_zh || sc.player }} {{ formatMinute(sc.minute) }}
                <span v-if="sc.is_stoppage || String(sc.minute).includes('+')" class="text-[9px] bg-amber-950 text-amber-300 px-1 py-0.2 rounded border border-amber-800/60 font-bold">绝杀</span>
              </span>
              <span v-if="i < awayScorers.length - 1" class="text-slate-600 mr-1">,</span>
            </template>
          </span>
          <span v-else class="text-slate-600 text-[10px]">-</span>
        </div>
      </div>
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
import { computed } from 'vue'

const props = defineProps({
  match: {
    type: Object,
    required: true
  }
})

defineEmits(['select'])

const homeScorers = computed(() => {
  if (!props.match.scorers) return []
  return props.match.scorers.filter(s => s.team === 'home' || (s.team === undefined && props.match.venue === 'home'))
})

const awayScorers = computed(() => {
  if (!props.match.scorers) return []
  return props.match.scorers.filter(s => s.team === 'away' || (s.team === undefined && props.match.venue === 'away'))
})

const formatMinute = (m) => {
  if (!m && m !== 0) return ''
  const s = String(m).trim()
  return s.endsWith("'") ? s : `${s}'`
}
</script>
