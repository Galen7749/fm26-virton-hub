<template>
  <div v-if="match" class="p-4 space-y-4 animate-in fade-in duration-200">
    
    <!-- 1. 二级顶栏：返回按钮与轮次快速切换 -->
    <div class="flex items-center justify-between text-xs border-b border-slate-800 pb-2">
      <!-- 返回按钮 -->
      <button
        @click="$emit('back')"
        class="flex items-center space-x-1.5 text-emerald-400 hover:text-emerald-300 font-bold transition px-2 py-1 rounded-lg hover:bg-slate-900 border border-transparent hover:border-slate-800"
      >
        <span class="text-sm">←</span>
        <span>全部比赛大盘</span>
      </button>

      <!-- 轮次指示器与上一场/下一场切换 -->
      <div class="flex items-center space-x-2">
        <button
          :disabled="!hasPrev"
          @click="$emit('switch-match', prevMatchId)"
          class="w-6 h-6 rounded bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-300 disabled:opacity-30 disabled:cursor-not-allowed hover:bg-slate-800 transition"
          title="上一场"
        >
          ‹
        </button>
        <span class="text-[11px] font-bold text-slate-300">
          {{ match.competition || '比乙' }} · {{ match.round_label || ('第 ' + match.round + ' 轮') }}
        </span>
        <button
          :disabled="!hasNext"
          @click="$emit('switch-match', nextMatchId)"
          class="w-6 h-6 rounded bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-300 disabled:opacity-30 disabled:cursor-not-allowed hover:bg-slate-800 transition"
          title="下一场"
        >
          ›
        </button>
      </div>
    </div>

    <!-- 2. 焦点战报卡片 (比分大盘与硬核数据) -->
    <div class="bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 rounded-xl border border-slate-800 p-4 shadow-sm space-y-3">
      <div class="flex justify-between items-center text-[11px] text-slate-400">
        <span class="flex items-center space-x-1 text-emerald-400 font-medium">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>官方战报 · 已完赛</span>
        </span>
        <span class="text-slate-400 truncate max-w-[170px]">{{ match.stadium }}</span>
      </div>

      <!-- 比分栏 -->
      <div class="flex items-center justify-between py-1.5 px-1">
        <div class="flex-1 text-center min-w-0 pr-2">
          <div :class="[
            'text-sm font-bold truncate',
            match.home_team.includes('维尔通') ? 'text-emerald-400 font-black' : 'text-white'
          ]">
            {{ match.home_team }}
          </div>
          <div class="text-[10px] text-slate-500 mt-0.5">主队</div>
        </div>

        <div class="shrink-0 text-center px-2 flex flex-col items-center">
          <div class="text-2xl font-black text-white tracking-wider whitespace-nowrap font-mono">
            {{ match.score_home }} - {{ match.score_away }}
          </div>
          <span :class="[
            'text-[9px] px-1.5 py-0.2 rounded font-bold font-mono inline-block mt-0.5 whitespace-nowrap',
            match.result === 'W' || match.result === '胜' ? 'bg-emerald-950 text-emerald-300 border border-emerald-800' :
            match.result === 'D' || match.result === '平' ? 'bg-amber-950 text-amber-300 border border-amber-800' :
            'bg-rose-950 text-rose-300 border border-rose-800'
          ]">
            {{ match.result === 'W' ? '胜仗' : match.result === 'D' ? '平局' : '失利' }}
          </span>
        </div>

        <div class="flex-1 text-center min-w-0 pl-2">
          <div :class="[
            'text-sm font-bold truncate',
            match.away_team.includes('维尔通') ? 'text-emerald-400 font-black' : 'text-white'
          ]">
            {{ match.away_team }}
          </div>
          <div class="text-[10px] text-slate-500 mt-0.5">客队</div>
        </div>
      </div>

      <!-- 进球列表 -->
      <div v-if="match.scorers && match.scorers.length" class="pt-2 border-t border-slate-800/60 text-center space-y-1">
        <div
          v-for="(sc, sIdx) in match.scorers"
          :key="sIdx"
          class="text-[11px] text-slate-300"
        >
          ⚽ {{ sc.player_zh || sc.player }} ({{ sc.minute }}')
          <span v-if="sc.assist_zh || sc.assist" class="text-slate-500 text-[10px]">
            助攻: {{ sc.assist_zh || sc.assist }}
          </span>
        </div>
      </div>

      <!-- xG与硬数据指标 -->
      <div class="grid grid-cols-3 gap-2 pt-2 text-center border-t border-slate-800/40">
        <div class="bg-slate-950 rounded p-1.5 border border-slate-850">
          <div class="text-[10px] text-slate-400">预期进球(xG)</div>
          <div class="text-xs font-bold text-slate-200 mt-0.5">{{ match.xg }}</div>
        </div>
        <div class="bg-slate-950 rounded p-1.5 border border-slate-850">
          <div class="text-[10px] text-slate-400">射门(射正)</div>
          <div class="text-xs font-bold text-slate-200 mt-0.5">{{ match.shots }} ({{ match.shots_on_target }})</div>
        </div>
        <div class="bg-slate-950 rounded p-1.5 border border-slate-850">
          <div class="text-[10px] text-slate-400">跑动里程</div>
          <div class="text-xs font-bold text-slate-200 mt-0.5">{{ match.distance_km }} km</div>
        </div>
      </div>
    </div>

    <!-- 3. 二级详情专属子导航 Tab -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-1 flex items-center space-x-1 text-xs shadow-inner">
      <button
        @click="subTab = 'lineup'"
        :class="[
          'flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1',
          subTab === 'lineup' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
        ]"
      >
        <span>👥</span>
        <span>赛场阵容</span>
      </button>

      <button
        @click="subTab = 'report'"
        :class="[
          'flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1',
          subTab === 'report' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
        ]"
      >
        <span>📰</span>
        <span>深度战报</span>
      </button>

      <button
        @click="subTab = 'comments'"
        :class="[
          'flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1',
          subTab === 'comments' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
        ]"
      >
        <span>🔥</span>
        <span>虎扑热评</span>
      </button>

      <button
        @click="subTab = 'round'"
        :class="[
          'flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1',
          subTab === 'round' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
        ]"
      >
        <span>🌐</span>
        <span>同轮赛果</span>
      </button>
    </div>

    <!-- 4. 子模块内容视图 -->
    <div class="pt-1">
      <!-- 赛场阵容 (2D战术板与替补) -->
      <MatchLineup v-if="subTab === 'lineup'" :match="match" />

      <!-- 懂球帝战报 -->
      <MatchReport v-else-if="subTab === 'report'" :news="news" :matchDate="match.date" />

      <!-- 虎扑热评 -->
      <MatchComments v-else-if="subTab === 'comments'" :news="news" />

      <!-- 同轮比乙其他场次完整赛果 -->
      <RoundMatches v-else-if="subTab === 'round'" :matches="roundOtherMatches" :round="match.round" />
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import MatchLineup from './MatchLineup.vue'
import MatchReport from './MatchReport.vue'
import MatchComments from './MatchComments.vue'
import RoundMatches from './RoundMatches.vue'

const props = defineProps({
  match: {
    type: Object,
    required: true
  },
  allMatches: {
    type: Array,
    required: true
  },
  news: {
    type: Object,
    default: null
  },
  roundOtherMatches: {
    type: Array,
    default: () => []
  }
})

defineEmits(['back', 'switch-match'])

const subTab = ref('lineup')

// 上一场 / 下一场计算
const currentIndex = computed(() => {
  return props.allMatches.findIndex(m => m.id === props.match.id)
})

const hasPrev = computed(() => currentIndex.value > 0)
const hasNext = computed(() => currentIndex.value < props.allMatches.length - 1)

const prevMatchId = computed(() => {
  return hasPrev.value ? props.allMatches[currentIndex.value - 1].id : null
})

const nextMatchId = computed(() => {
  return hasNext.value ? props.allMatches[currentIndex.value + 1].id : null
})
</script>
