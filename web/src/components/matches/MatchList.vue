<template>
  <div class="p-4 space-y-4 animate-in fade-in duration-150">
    
    <!-- 赛季战绩大盘概览卡片 -->
    <div class="bg-gradient-to-r from-slate-900 via-slate-900 to-slate-950 border border-slate-800 rounded-xl p-3.5 space-y-2.5 shadow-sm">
      <div class="flex items-center justify-between text-xs">
        <div class="flex items-center space-x-2">
          <span class="text-sm">{{ matches.length > 0 ? '🇧🇪' : '🌍' }}</span>
          <span class="font-bold text-white">{{ seasonLabel }} · {{ matches.length > 0 ? '战绩看板' : '求职雷达' }}</span>
        </div>
        <span :class="[
          'text-[10px] font-bold px-2 py-0.5 rounded border',
          matches.length === 0 ? 'bg-amber-950/80 text-amber-300 border-amber-600/60 font-bold' :
          isPromoted ? 'bg-amber-950 text-amber-300 border-amber-600 shadow-sm font-black' : 'bg-emerald-950 text-emerald-400 border-emerald-900/50'
        ]">
          {{ matches.length === 0 ? '💼 自由身待业 · 寻找欧洲第2站' : isPromoted ? '🏆 冲甲附加赛总冠军 · 成功升入比甲！' : '比乙冲甲附加区' }}
        </span>
      </div>

      <!-- 战绩统计网格 (常规已赛) -->
      <div v-if="matches.length > 0" class="grid grid-cols-4 gap-2 text-center text-xs">
        <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
          <div class="text-[10px] text-slate-400">已赛场次</div>
          <div class="font-black text-white text-sm mt-0.5">{{ matches.length }} 场</div>
        </div>
        <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
          <div class="text-[10px] text-slate-400">胜/平/负</div>
          <div class="font-black text-emerald-400 text-sm mt-0.5">{{ winCount }}胜 {{ drawCount }}平 {{ lossCount }}负</div>
        </div>
        <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
          <div class="text-[10px] text-slate-400">得失球/净胜</div>
          <div class="font-black text-white text-sm mt-0.5">{{ totalGoalsFor }}-{{ totalGoalsAgainst }} (+{{ totalGoalsFor - totalGoalsAgainst }})</div>
        </div>
        <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
          <div class="text-[10px] text-slate-400">联赛积分</div>
          <div class="font-black text-amber-400 text-sm mt-0.5">{{ totalPoints }} 分</div>
        </div>
      </div>

      <!-- 待业求职看板 (0场比赛待业时) -->
      <div v-else class="bg-slate-950 p-3 rounded-xl border border-slate-850 space-y-2 text-xs">
        <div class="flex items-center justify-between">
          <span class="text-amber-400 font-bold flex items-center space-x-1.5">
            <span>🔥</span>
            <span>突发掀桌辞职！徐指导夏窗开启自由身求职</span>
          </span>
          <span class="text-[9px] bg-slate-800 text-amber-300 px-2 py-0.5 rounded border border-amber-900/40 font-mono">
            奇迹声望加持
          </span>
        </div>
        <p class="text-[11px] text-slate-300 leading-relaxed">
          刚带维尔通绝杀冲甲，因不满管理层清洗功勋老将、且拒绝报销教练班学费，徐指导已当场辞职走人！凭借带保级队逆天升甲的硬核声望，已有多家欧洲俱乐部接洽。唯一刚性底线：<strong>【新东家必须全额报销欧足联教练班学费】</strong>！
        </p>
        <div class="flex items-center space-x-1.5 pt-0.5 text-[9px] text-slate-400 overflow-x-auto no-scrollbar">
          <span class="bg-slate-900 px-2 py-0.5 rounded border border-slate-800 shrink-0">🎯 意向：荷乙中上游</span>
          <span class="bg-slate-900 px-2 py-0.5 rounded border border-slate-800 shrink-0">🇫🇷 法丙冲乙劲旅</span>
          <span class="bg-slate-900 px-2 py-0.5 rounded border border-slate-800 shrink-0">🇨🇭 瑞士联赛</span>
        </div>
      </div>
    </div>

    <!-- 筛选过滤与排序控制条 -->
    <div class="flex items-center justify-between text-xs">
      <!-- 过滤标签 -->
      <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar">
        <button
          v-for="filter in filters"
          :key="filter.key"
          @click="activeFilter = filter.key"
          :class="[
            'px-2.5 py-1 rounded-full text-xs font-semibold shrink-0 transition',
            activeFilter === filter.key
              ? 'bg-emerald-600 text-white font-bold shadow-sm'
              : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
          ]"
        >
          {{ filter.label }}
        </button>
      </div>

      <!-- 排序切换 -->
      <button
        @click="orderDesc = !orderDesc"
        class="text-[11px] text-slate-400 hover:text-emerald-400 flex items-center space-x-1 shrink-0 ml-2"
        title="切换排序"
      >
        <span>{{ orderDesc ? '最新赛果' : '开赛顺序' }}</span>
        <span class="text-xs">{{ orderDesc ? '↓' : '↑' }}</span>
      </button>
    </div>

    <!-- 比赛列表瀑布流 -->
    <div class="space-y-3">
      <MatchCard
        v-for="m in displayedMatches"
        :key="m.id"
        :match="m"
        @select="$emit('select-match', m.id)"
      />

      <div v-if="!displayedMatches.length" class="text-center py-10 px-4 space-y-2 text-slate-500 text-xs">
        <div class="text-2xl animate-bounce">✈️</div>
        <div class="font-bold text-slate-300">
          {{ matches.length === 0 ? '正在欧洲自由市场物色下家' : '暂无符合筛选条件的比赛' }}
        </div>
        <p v-if="matches.length === 0" class="text-[11px] text-slate-500 max-w-xs mx-auto leading-relaxed">
          手握比乙冲甲奇迹声望，静候愿全额资助欧足联教练班进修资格的良心东家递上橄榄枝！
        </p>
      </div>
    </div>

    <!-- 国际背景板：同期欧洲快讯 -->
    <div class="pt-4 border-t border-slate-800/80 space-y-2.5">
      <div class="flex items-center justify-between text-xs font-bold text-slate-300">
        <span class="flex items-center space-x-1.5">
          <span>🌍</span>
          <span>同期欧洲足坛要闻 (比甲 / 五大联赛)</span>
        </span>
        <span class="text-[10px] text-slate-500">国际版面</span>
      </div>

      <div class="space-y-2">
        <div
          v-for="wn in worldNews"
          :key="wn.id"
          class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-1 hover:border-slate-700 transition text-xs"
        >
          <div class="flex items-center justify-between text-[10px]">
            <span class="bg-slate-800 text-teal-400 px-1.5 py-0.5 rounded font-medium">
              {{ wn.league }}
            </span>
            <span class="text-slate-500">{{ wn.time }}</span>
          </div>
          <h4 class="font-bold text-slate-200 leading-snug">
            {{ wn.title }}
          </h4>
          <p class="text-[11px] text-slate-400 leading-relaxed">
            {{ wn.summary }}
          </p>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import MatchCard from './MatchCard.vue'

const props = defineProps({
  matches: {
    type: Array,
    required: true
  },
  worldNews: {
    type: Array,
    default: () => []
  },
  seasonLabel: {
    type: String,
    default: '2025/26 赛季'
  }
})

defineEmits(['select-match'])

const activeFilter = ref('all')
const orderDesc = ref(true) // 默认最新赛果排在前面

const isPromoted = computed(() => props.matches.some(m => m.stage_title?.includes('绝杀') || m.round >= 32))

const filters = [
  { key: 'all', label: '全部比赛' },
  { key: 'playoff', label: '🏆 冲甲决战' },
  { key: 'regular', label: '常规赛' },
  { key: 'win', label: '胜仗' },
  { key: 'home', label: '主场' },
  { key: 'away', label: '客场' }
]

// 统计计算
const winCount = computed(() => props.matches.filter(m => m.result === 'W' || m.result === '胜').length)
const drawCount = computed(() => props.matches.filter(m => m.result === 'D' || m.result === '平').length)
const lossCount = computed(() => props.matches.filter(m => m.result === 'L' || m.result === '负').length)

const totalPoints = computed(() => (winCount.value * 3) + drawCount.value)

const totalGoalsFor = computed(() => {
  return props.matches.reduce((sum, m) => {
    return sum + (m.home_team.includes('维尔通') ? m.score_home : m.score_away)
  }, 0)
})

const totalGoalsAgainst = computed(() => {
  return props.matches.reduce((sum, m) => {
    return sum + (m.home_team.includes('维尔通') ? m.score_away : m.score_home)
  }, 0)
})

// 筛选与排序
const displayedMatches = computed(() => {
  let list = [...props.matches]
  
  if (activeFilter.value === 'playoff') {
    list = list.filter(m => m.is_playoff || m.stage_title?.includes('冲甲') || m.round >= 29)
  } else if (activeFilter.value === 'regular') {
    list = list.filter(m => !m.is_playoff && !m.stage_title?.includes('冲甲') && m.round < 29)
  } else if (activeFilter.value === 'win') {
    list = list.filter(m => m.result === 'W' || m.result === '胜')
  } else if (activeFilter.value === 'home') {
    list = list.filter(m => m.venue === 'home' || m.home_team.includes('维尔通'))
  } else if (activeFilter.value === 'away') {
    list = list.filter(m => m.venue === 'away' || m.away_team.includes('维尔通'))
  }

  // 排序
  list.sort((a, b) => {
    return orderDesc.value ? (b.id - a.id) : (a.id - b.id)
  })

  return list
})
</script>
