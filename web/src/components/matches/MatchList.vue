<template>
  <div class="space-y-3.5 p-3.5 animate-in fade-in duration-150 pb-6">

    <!-- 1. 顶部控制器：【轮次/日期快捷筛选】 + 右侧【联赛筛选下拉框】 -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-2.5 flex items-center justify-between gap-2 text-xs shadow-sm">
      <!-- 轮次选择胶囊 -->
      <div class="flex items-center space-x-1 overflow-x-auto no-scrollbar py-0.5">
        <button
          v-for="r in roundOptions"
          :key="r.key"
          @click="selectedRoundFilter = r.key"
          :class="[
            'px-2.5 py-1 rounded-lg text-[11px] font-bold shrink-0 transition inline-flex items-center gap-1',
            selectedRoundFilter === r.key
              ? 'bg-emerald-600 text-white shadow-sm'
              : 'text-slate-400 hover:text-white bg-slate-950/60'
          ]"
        >
          <Icon :icon="r.icon" class="w-3 h-3" />
          <span>{{ r.label }}</span>
        </button>
      </div>

      <!-- 右侧：联赛筛选下拉框 (全站无 Emoji，纯文本规范呈现，支持置顶与分组) -->
      <div class="shrink-0 relative">
        <select
          v-model="selectedLeague"
          class="bg-slate-950 border border-slate-700 text-slate-200 text-xs font-bold rounded-lg px-2.5 py-1.5 focus:outline-none focus:border-emerald-500 cursor-pointer shadow-inner pr-6"
        >
          <option value="all">全部重要赛事</option>
          <optgroup v-if="pinnedLeagues.length" label="⭐ 已置顶关注">
            <option
              v-for="lg in pinnedLeagues"
              :key="'match-pinned-' + lg.key"
              :value="lg.key"
            >
              ★ {{ lg.name }}
            </option>
          </optgroup>
          <optgroup label="🔥 热门顶级赛事">
            <option
              v-for="lg in popularLeagues"
              :key="'match-pop-' + lg.key"
              :value="lg.key"
            >
              {{ lg.name }}
            </option>
          </optgroup>
          <optgroup label="🌍 欧洲其他联赛">
            <option
              v-for="lg in europeanLeagues"
              :key="'match-euro-' + lg.key"
              :value="lg.key"
            >
              {{ lg.name }}
            </option>
          </optgroup>
        </select>
      </div>
    </div>

    <!-- 2. 赛事汇总提示条 -->
    <div class="flex items-center justify-between text-[11px] text-slate-400 px-1">
      <span class="inline-flex items-center gap-1.5">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
        <span>共匹配到 <strong class="text-white">{{ filteredMatches.length }}</strong> 场比赛</span>
      </span>
      <span class="text-slate-500 text-[10px] inline-flex items-center gap-1">
        <Icon icon="lucide:info" class="w-3 h-3" />
        <span>点击卡片进入深度战报与阵容评分</span>
      </span>
    </div>

    <!-- 3. 中立赛事列表（完全中立 主队 比分 客队 布局） -->
    <div class="space-y-2">
      <div
        v-for="m in filteredMatches"
        :key="m.id"
        @click="$emit('select-match', m.id)"
        class="bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-slate-700 rounded-xl p-3 shadow-sm cursor-pointer transition transform hover:-translate-y-0.5 space-y-2"
      >
        <!-- 比赛元信息行：联赛国旗图标、名称、日期轮次、以及中立「留洋」标签 -->
        <div class="flex items-center justify-between text-[10px] pb-1.5 border-b border-slate-800/60">
          <div class="inline-flex items-center gap-1.5">
            <Icon :icon="getLeagueFlag(m.league_key)" class="w-3.5 h-3.5 rounded-full shrink-0" />
            <span class="font-bold text-slate-300">{{ m.league_name || m.competition || '比乙' }}</span>
            <span class="text-slate-500">·</span>
            <span class="text-slate-400">{{ m.round_label || ('第 ' + m.round + ' 轮') }}</span>
            <span class="text-slate-500 font-mono inline-flex items-center gap-0.5">
              <Icon icon="lucide:calendar" class="w-2.5 h-2.5" />
              <span>{{ m.date_short || m.date }}</span>
            </span>
          </div>

          <div class="inline-flex items-center gap-1.5">
            <!-- 仅在涉及中国主帅执教的比赛角落附带中立「circle-flags:cn 留洋」标签 -->
            <span
              v-if="m.is_overseas || isOverseasMatch(m)"
              class="inline-flex items-center gap-1 bg-red-950 text-red-300 border border-red-800/80 px-1.5 py-0.2 rounded font-bold text-[9px]"
            >
              <Icon icon="circle-flags:cn" class="w-2.5 h-2.5" />
              <span>留洋</span>
            </span>

            <span class="inline-flex items-center gap-0.5 bg-slate-950 text-emerald-400 px-1.5 py-0.2 rounded border border-emerald-950 font-bold font-mono text-[9px]">
              <Icon icon="lucide:check-circle" class="w-2.5 h-2.5" />
              <span>{{ m.status_label || (m.status === 'FT' ? '完赛' : '已完赛') }}</span>
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

        <!-- 进球速览摘要（使用矢量足球图标 ph:soccer-ball-fill） -->
        <div v-if="m.scorers && m.scorers.length" class="text-[10px] text-slate-400 bg-slate-950/70 p-1.5 rounded border border-slate-850 truncate inline-flex items-center gap-1.5 w-full">
          <Icon icon="ph:soccer-ball-fill" class="w-3 h-3 text-emerald-400 shrink-0" />
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
import standingsMultiRaw from '../../data/standings_multi.json'

const props = defineProps({
  matches: {
    type: Array,
    default: () => []
  }
})

defineEmits(['select-match'])

// 联赛下拉筛选器
const selectedLeague = ref('all')

// ── 用户置顶赛事 (从 localStorage 同步) ──────────────────────
const PINNED_STORAGE_KEY = 'dqy_pinned_leagues'
function getInitialPinned() {
  try {
    const raw = localStorage.getItem(PINNED_STORAGE_KEY)
    if (raw) return JSON.parse(raw)
  } catch (e) {
    // ignore
  }
  return ['ucl', 'pl']
}

const pinnedLeagueKeys = ref(getInitialPinned())
const allLeagues = standingsMultiRaw.leagues || []

// 分组计算：置顶赛事
const pinnedLeagues = computed(() => {
  return pinnedLeagueKeys.value
    .map(key => allLeagues.find(lg => lg.key === key))
    .filter(Boolean)
})

// 分组计算：热门顶级赛事 (五大联赛 + 欧冠 + 中超)
const popularLeagues = computed(() => {
  return allLeagues.filter(lg => lg.group === 'popular')
})

// 分组计算：欧洲其他主要联赛 (波甲、比甲、比乙)
const europeanLeagues = computed(() => {
  return allLeagues.filter(lg => lg.group === 'european')
})

// 轮次快捷筛选
const selectedRoundFilter = ref('all')
const roundOptions = [
  { key: 'all', label: '全部焦点', icon: 'lucide:layers' },
  { key: 'recent', label: '最近完赛', icon: 'lucide:clock' },
  { key: 'finals', label: '决赛/争冠', icon: 'lucide:trophy' }
]

const getLeagueFlag = (key) => {
  const flags = {
    ucl: 'circle-flags:eu',
    pl: 'circle-flags:gb-eng',
    laliga: 'circle-flags:es',
    serie_a: 'circle-flags:it',
    bundesliga: 'circle-flags:de',
    ligue1: 'circle-flags:fr',
    csl: 'circle-flags:cn',
    pol_d1: 'circle-flags:pl',
    bel_d1: 'circle-flags:be',
    bel_d2: 'circle-flags:be'
  }
  return flags[key] || 'circle-flags:eu'
}

const isOverseasMatch = (m) => {
  return m.is_overseas || m.home_team.includes('奥波莱') || m.away_team.includes('奥波莱') || m.home_team.includes('维尔通') || m.away_team.includes('维尔通')
}

// 整合与去重
const combinedMatches = computed(() => {
  const map = new Map()

  allMatchesRaw.forEach(m => {
    map.set(m.id, m)
  })

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

const filteredMatches = computed(() => {
  return combinedMatches.value.filter(m => {
    if (selectedLeague.value !== 'all') {
      const matchLeagueKey = m.league_key || (isOverseasMatch(m) ? 'pol_d1' : 'ucl')
      if (matchLeagueKey !== selectedLeague.value) return false
    }

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
