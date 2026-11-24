<template>
  <div class="space-y-3.5 p-3.5 animate-in fade-in duration-150 pb-6">

    <!-- 1. 顶部控制器：【轮次/日期选择器】 + 右侧【联赛筛选下拉框】 -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-2.5 flex items-center justify-between gap-2 text-xs shadow-sm">
      <!-- 轮次/日期选择胶囊 -->
      <div class="flex items-center space-x-1 overflow-x-auto no-scrollbar py-0.5">
        <button
          v-for="r in roundOptions"
          :key="r.key"
          @click="selectedRoundFilter = r.key"
          :class="[
            'px-2.5 py-1 rounded-lg text-[11px] font-bold shrink-0 transition',
            selectedRoundFilter === r.key
              ? 'bg-emerald-600 text-white shadow-sm'
              : 'text-slate-400 hover:text-white bg-slate-950/60'
          ]"
        >
          {{ r.label }}
        </button>
      </div>

      <!-- 右侧：联赛筛选下拉框 (全部重要赛事 / 波甲 / 比甲 / 比乙 / 英超 / 欧冠) -->
      <div class="shrink-0">
        <select
          v-model="selectedLeague"
          class="bg-slate-950 border border-slate-700 text-slate-200 text-xs font-bold rounded-lg px-2.5 py-1 focus:outline-none focus:border-emerald-500 cursor-pointer shadow-inner"
        >
          <option value="all">🌐 全部重要赛事</option>
          <option value="pol_d1">🇵🇱 波甲 (奥波莱)</option>
          <option value="bel_d1">🇧🇪 比甲 (顶级联赛)</option>
          <option value="bel_d2">🇧🇪 比乙 (维尔通冲甲)</option>
          <option value="pl">🏴󠁧󠁢󠁥󠁮󠁧󠁿 英超</option>
          <option value="ucl">🇪🇺 欧冠</option>
        </select>
      </div>
    </div>

    <!-- 2. 赛事汇总提示条 -->
    <div class="flex items-center justify-between text-[11px] text-slate-400 px-1">
      <span class="flex items-center space-x-1.5">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
        <span>共匹配到 <strong class="text-white">{{ filteredMatches.length }}</strong> 场比赛</span>
      </span>
      <span class="text-slate-500 text-[10px]">点击比赛卡片进入深度战报与阵容评分</span>
    </div>

    <!-- 3. 中立赛事列表（完全中立 主队 比分 客队 布局） -->
    <div class="space-y-2">
      <div
        v-for="m in filteredMatches"
        :key="m.id"
        @click="$emit('select-match', m.id)"
        class="bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-slate-700 rounded-xl p-3 shadow-sm cursor-pointer transition transform hover:-translate-y-0.5 space-y-2"
      >
        <!-- 比赛元信息行：联赛名称、日期轮次、以及中立「🇨🇳 留洋」标签 -->
        <div class="flex items-center justify-between text-[10px] pb-1.5 border-b border-slate-800/60">
          <div class="flex items-center space-x-2">
            <span class="font-bold text-slate-300">{{ m.league_name || m.competition || '比乙' }}</span>
            <span class="text-slate-500">·</span>
            <span class="text-slate-400">{{ m.round_label || ('第 ' + m.round + ' 轮') }}</span>
            <span class="text-slate-500 font-mono">{{ m.date_short || m.date }}</span>
          </div>

          <div class="flex items-center space-x-1.5">
            <!-- 仅在有中国主教练执教的比赛右侧附带一个低调中立的「🇨🇳 留洋」标签 -->
            <span
              v-if="m.is_overseas || m.home_team.includes('维尔通') || m.away_team.includes('维尔通') || m.home_team.includes('奥波莱') || m.away_team.includes('奥波莱')"
              class="bg-red-950 text-red-300 border border-red-800/80 px-1.5 py-0.2 rounded font-bold text-[9px] flex items-center space-x-0.5"
            >
              <span>🇨🇳</span>
              <span>留洋</span>
            </span>

            <span class="bg-slate-950 text-emerald-400 px-1.5 py-0.2 rounded border border-emerald-950 font-bold font-mono">
              {{ m.status_label || (m.status === 'FT' ? '完赛' : '已完赛') }}
            </span>
          </div>
        </div>

        <!-- 比赛双方与比分主体（中立居中对齐） -->
        <div class="flex items-center justify-between py-1">
          <!-- 主队 -->
          <div class="flex-1 text-right min-w-0 pr-3">
            <div class="text-xs sm:text-sm font-bold text-white truncate">
              {{ m.home_team }}
            </div>
            <div class="text-[9px] text-slate-500 mt-0.5 font-mono">
              {{ m.stadium ? m.stadium.split(' ')[0] : '主场' }}
            </div>
          </div>

          <!-- 比分中缝 -->
          <div class="shrink-0 px-3 py-1 bg-slate-950 rounded-lg border border-slate-800 text-center flex flex-col items-center min-w-[72px]">
            <span class="text-base sm:text-lg font-black text-white font-mono tracking-wider">
              {{ m.score_home }} - {{ m.score_away }}
            </span>
            <span class="text-[9px] text-slate-500 font-mono">xG {{ m.xg || '1.4 - 0.9' }}</span>
          </div>

          <!-- 客队 -->
          <div class="flex-1 text-left min-w-0 pl-3">
            <div class="text-xs sm:text-sm font-bold text-white truncate">
              {{ m.away_team }}
            </div>
            <div class="text-[9px] text-slate-500 mt-0.5">客场</div>
          </div>
        </div>

        <!-- 进球速览摘要（有进球球员时紧凑展示） -->
        <div v-if="m.scorers && m.scorers.length" class="text-[10px] text-slate-400 bg-slate-950/70 p-1.5 rounded border border-slate-850 truncate flex items-center space-x-1.5">
          <span class="text-xs shrink-0">⚽</span>
          <span class="truncate">
            <template v-for="(sc, sidx) in m.scorers" :key="sidx">
              <span :class="sc.is_header ? 'text-amber-300 font-bold' : 'text-slate-300'">
                {{ sc.player_zh || sc.player }} {{ sc.minute }}'{{ sc.is_header ? '(头球)' : '' }}
              </span>
              <span v-if="sidx < m.scorers.length - 1" class="text-slate-600 mx-1">,</span>
            </template>
          </span>
        </div>
      </div>

      <!-- 无数据兜底 -->
      <div v-if="filteredMatches.length === 0" class="text-center py-12 text-slate-500 text-xs bg-slate-900/50 rounded-xl border border-slate-800">
        暂无该联赛筛选条件下的比赛记录
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import allMatchesRaw from '../../data/all_matches.json'

const props = defineProps({
  matches: {
    type: Array,
    default: () => []
  }
})

defineEmits(['select-match'])

// 联赛下拉筛选器：'all' | 'pol_d1' | 'bel_d1' | 'bel_d2' | 'pl' | 'ucl'
const selectedLeague = ref('all')

// 轮次/日期快捷筛选
const selectedRoundFilter = ref('all')
const roundOptions = [
  { key: 'all', label: '全部焦点' },
  { key: 'recent', label: '最近完赛' },
  { key: 'finals', label: '决赛/争冠' }
]

// 将 allMatchesRaw 与 props.matches 整合去重
const combinedMatches = computed(() => {
  const map = new Map()

  // 首先载入内置多联赛比赛 (波甲、欧冠、英超、比甲焦点战)
  allMatchesRaw.forEach(m => {
    map.set(m.id, m)
  })

  // 载入当前赛季比赛 (例如 Virton 32 场)
  props.matches.forEach(m => {
    if (!map.has(m.id)) {
      map.set(m.id, {
        ...m,
        league_key: 'bel_d2',
        league_name: '比乙',
        is_overseas: true,
        date_short: m.date
      })
    }
  })

  return Array.from(map.values())
})

// 根据联赛与轮次进行中立过滤
const filteredMatches = computed(() => {
  return combinedMatches.value.filter(m => {
    // 联赛筛选
    if (selectedLeague.value !== 'all') {
      const matchLeagueKey = m.league_key || (m.home_team.includes('维尔通') || m.away_team.includes('维尔通') ? 'bel_d2' : 'pol_d1')
      if (matchLeagueKey !== selectedLeague.value) return false
    }

    // 轮次/状态筛选
    if (selectedRoundFilter.value === 'finals') {
      const isFinal = String(m.round_label || '').includes('决赛') || String(m.round_label || '').includes('附加赛')
      if (!isFinal) return false
    }

    return true
  })
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
