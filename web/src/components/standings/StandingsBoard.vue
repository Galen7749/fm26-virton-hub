<template>
  <div class="p-4 space-y-3 animate-in fade-in duration-150">
    <!-- 榜单类型子切换条 -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-1 flex items-center space-x-1 text-xs shadow-inner">
      <button
        @click="subTab = 'points'"
        :class="['flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1', subTab === 'points' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white']"
      >
        <span>🏆</span>
        <span>积分榜</span>
      </button>
      <button
        @click="subTab = 'scorers'"
        :class="['flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1', subTab === 'scorers' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white']"
      >
        <span>⚽</span>
        <span>射手榜</span>
      </button>
      <button
        @click="subTab = 'assists'"
        :class="['flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1', subTab === 'assists' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white']"
      >
        <span>👟</span>
        <span>助攻榜</span>
      </button>
      <button
        @click="subTab = 'discipline'"
        :class="['flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1', subTab === 'discipline' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white']"
      >
        <span>🟨</span>
        <span>纪律榜</span>
      </button>
    </div>

    <!-- 积分榜 -->
    <LeagueTable
      v-if="subTab === 'points'"
      :availableLeagues="availableLeagues"
    />

    <!-- 射手榜 -->
    <ScorersTable
      v-else-if="subTab === 'scorers'"
      :scorers="leaderboards?.scorers || []"
    />

    <!-- 助攻榜 -->
    <AssistsTable
      v-else-if="subTab === 'assists'"
      :assists="leaderboards?.assists || []"
    />

    <!-- 纪律榜 -->
    <DisciplineTable
      v-else-if="subTab === 'discipline'"
      :discipline="leaderboards?.discipline || []"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LeagueTable from './LeagueTable.vue'
import ScorersTable from './ScorersTable.vue'
import AssistsTable from './AssistsTable.vue'
import DisciplineTable from './DisciplineTable.vue'

defineProps({
  availableLeagues: {
    type: Array,
    default: () => []
  },
  leaderboards: {
    type: Object,
    default: () => ({})
  }
})

const subTab = ref('points')
</script>
