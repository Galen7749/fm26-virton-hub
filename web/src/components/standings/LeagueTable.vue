<template>
  <div class="space-y-3">
    <!-- 七大联赛横向切换选择器 -->
    <div class="relative flex items-center bg-slate-900 rounded-xl p-1 border border-slate-800">
      <button
        @click="scrollLeagues(-100)"
        class="w-6 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs shrink-0 transition"
        title="向左滚动"
      >
        ‹
      </button>

      <div
        ref="leagueScrollRef"
        @wheel.prevent="onLeagueWheel"
        class="flex-1 flex items-center space-x-1.5 overflow-x-auto py-1 px-1.5 scroll-smooth no-scrollbar select-none"
        style="-webkit-overflow-scrolling: touch; touch-action: pan-x;"
      >
        <button
          v-for="lg in availableLeagues"
          :key="lg.id"
          @click="selectedLeagueId = lg.id"
          :class="[
            'px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 transition flex items-center space-x-1.5 whitespace-nowrap',
            selectedLeagueId === lg.id
              ? 'bg-emerald-600 text-white font-bold shadow-sm'
              : 'bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-slate-200'
          ]"
        >
          <svg v-if="getLeagueIcon(lg.id)" class="icon text-sm">
            <use :xlink:href="'#' + getLeagueIcon(lg.id)"></use>
          </svg>
          <span v-else>{{ lg.flag }}</span>
          <span>{{ lg.short_name }}</span>
        </button>
      </div>

      <button
        @click="scrollLeagues(100)"
        class="w-6 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs shrink-0 transition"
        title="向右滚动"
      >
        ›
      </button>
    </div>

    <!-- 当前选中联赛的提示信息 -->
    <div class="bg-slate-900 border border-slate-800 rounded-lg p-2.5 flex items-center justify-between text-xs">
      <div class="flex items-center space-x-2.5">
        <div class="w-8 h-8 rounded-lg bg-slate-800/80 border border-slate-700 flex items-center justify-center shrink-0">
          <svg v-if="getLeagueIcon(currentDisplayLeague.id)" class="icon text-xl text-emerald-400">
            <use :xlink:href="'#' + getLeagueIcon(currentDisplayLeague.id)"></use>
          </svg>
          <span v-else class="text-base">{{ currentDisplayLeague.flag }}</span>
        </div>
        <div>
          <div class="font-bold text-white">{{ currentDisplayLeague.name }}</div>
          <div class="text-[10px] text-slate-400 mt-0.5">
            已战至第 {{ currentDisplayLeague.round }} 轮 · 官方即时积分
          </div>
        </div>
      </div>
      <span class="text-[10px] bg-slate-800 text-emerald-400 px-2 py-0.5 rounded border border-slate-700 shrink-0">
        {{ currentDisplayLeague.tag || '欧洲职业联赛' }}
      </span>
    </div>

    <!-- 完整积分表 -->
    <div class="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden text-xs shadow-inner">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="bg-slate-850 text-slate-400 border-b border-slate-800 text-[10px]">
            <th class="py-2.5 px-2 text-center w-8">#</th>
            <th class="py-2.5 px-2">球队</th>
            <th class="py-2.5 px-1 text-center w-7">赛</th>
            <th class="py-2.5 px-1 text-center w-12">胜/平/负</th>
            <th class="py-2.5 px-1 text-center w-8">净胜</th>
            <th class="py-2.5 px-2 text-center font-bold w-9">积分</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="row in currentDisplayLeague.table"
            :key="row.position"
            :class="[
              'border-b border-slate-800/60 transition hover:bg-slate-850/80',
              row.is_my_team || row.team_name.includes('维尔通')
                ? 'bg-emerald-950/60 font-bold text-emerald-300 border-l-2 border-emerald-500'
                : 'text-slate-300'
            ]"
          >
            <td class="py-2 px-2 text-center font-bold">
              <span
                :class="[
                  'w-5 h-5 rounded flex items-center justify-center text-[10px] mx-auto',
                  row.position <= 4 ? 'bg-amber-400/20 text-amber-300 font-black' :
                  row.position > currentDisplayLeague.total_teams - 3 ? 'bg-rose-950 text-rose-400 font-bold' :
                  'text-slate-400'
                ]"
              >
                {{ row.position }}
              </span>
            </td>
            <td class="py-2 px-2 truncate max-w-[130px]">
              <div class="flex items-center space-x-1">
                <span class="truncate">{{ row.team_name }}</span>
                <span
                  v-if="row.is_my_team || row.team_name.includes('维尔通')"
                  class="text-[9px] bg-emerald-600 text-white px-1 py-0.2 rounded shrink-0 font-normal"
                >
                  执教中
                </span>
              </div>
            </td>
            <td class="py-2 px-1 text-center text-slate-400">{{ row.played }}</td>
            <td class="py-2 px-1 text-center text-slate-400 text-[11px]">{{ row.won }}/{{ row.drawn }}/{{ row.lost }}</td>
            <td
              class="py-2 px-1 text-center text-[11px]"
              :class="row.gd > 0 ? 'text-emerald-400 font-semibold' : row.gd < 0 ? 'text-rose-400' : 'text-slate-400'"
            >
              {{ row.gd > 0 ? '+' + row.gd : row.gd }}
            </td>
            <td class="py-2 px-2 text-center font-black text-white text-xs">{{ row.points }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  availableLeagues: {
    type: Array,
    default: () => []
  }
})

const selectedLeagueId = ref('bel_d2')
const currentDisplayLeague = computed(() => {
  return props.availableLeagues.find(l => l.id === selectedLeagueId.value) || props.availableLeagues[0] || {}
})

const leagueScrollRef = ref(null)
const onLeagueWheel = (e) => {
  if (leagueScrollRef.value) {
    leagueScrollRef.value.scrollLeft += (e.deltaY || e.deltaX) * 0.9
  }
}
const scrollLeagues = (offset) => {
  if (leagueScrollRef.value) {
    leagueScrollRef.value.scrollBy({ left: offset, behavior: 'smooth' })
  }
}

const getLeagueIcon = (id) => {
  const iconMap = {
    pl: 'icon-yingchao',
    laliga: 'icon-xijia',
    serie_a: 'icon-yijia',
    bundesliga: 'icon-dejia',
    ligue1: 'icon-a-zu10290'
  }
  return iconMap[id] || null
}
</script>
