<template>
  <div class="space-y-3.5 p-3.5 animate-in fade-in duration-150 pb-6">

    <!-- 1. 顶部控制栏：左侧【联赛下拉选择器】 + 右侧【3个子视图切换】 -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-2.5 flex items-center justify-between gap-2 shadow-sm text-xs">
      <!-- 顶部左侧：联赛下拉选择器 (带矢量国旗徽章，无 Emoji) -->
      <div class="inline-flex items-center gap-1.5 shrink-0">
        <Icon :icon="currentLeague.flag_icon || 'circle-flags:eu'" class="w-4 h-4 rounded-full shrink-0" />
        <select
          v-model="selectedLeagueKey"
          class="bg-slate-950 border border-slate-700 text-slate-200 text-xs font-bold rounded-lg px-2 py-1.5 focus:outline-none focus:border-emerald-500 cursor-pointer shadow-inner pr-6"
        >
          <option
            v-for="lg in leaguesData.leagues"
            :key="lg.key"
            :value="lg.key"
          >
            {{ lg.label }}
          </option>
        </select>
      </div>

      <!-- 顶部右侧：3 个子视图切换 (积分榜 | 射手/助攻榜 | 转会动态) -->
      <div class="bg-slate-950 p-1 rounded-lg border border-slate-800 inline-flex items-center gap-1">
        <button
          @click="subView = 'table'"
          :class="[
            'px-2 py-1 rounded-md text-[11px] font-bold transition inline-flex items-center gap-1',
            subView === 'table' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="lucide:trophy" class="w-3 h-3" />
          <span>积分榜</span>
        </button>

        <button
          @click="subView = 'leaders'"
          :class="[
            'px-2 py-1 rounded-md text-[11px] font-bold transition inline-flex items-center gap-1',
            subView === 'leaders' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="ph:soccer-ball-fill" class="w-3 h-3" />
          <span>射手/助攻</span>
        </button>

        <button
          @click="subView = 'transfers'"
          :class="[
            'px-2 py-1 rounded-md text-[11px] font-bold transition inline-flex items-center gap-1',
            subView === 'transfers' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="tabler:arrows-exchange" class="w-3 h-3" />
          <span>转会动态</span>
        </button>
      </div>
    </div>

    <!-- 2. 当前联赛基本信息条 -->
    <div class="flex items-center justify-between text-[11px] text-slate-400 px-1">
      <div class="inline-flex items-center gap-1.5 font-bold text-slate-200">
        <span>{{ currentLeague.name }}</span>
        <span class="text-slate-500">·</span>
        <span class="text-emerald-400">{{ currentLeague.season }}</span>
      </div>
      <span class="text-slate-500 text-[10px] font-mono">{{ currentLeague.round_info }}</span>
    </div>

    <!-- 3. 子视图 A: 联赛中立积分榜 -->
    <div v-if="subView === 'table'" class="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden shadow-sm">
      <div class="overflow-x-auto">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-950/80 text-[10px] text-slate-400 border-b border-slate-800">
            <tr>
              <th class="py-2.5 px-2 text-center w-8">#</th>
              <th class="py-2.5 px-3">球队</th>
              <th class="py-2.5 px-1.5 text-center">赛</th>
              <th class="py-2.5 px-1.5 text-center">胜</th>
              <th class="py-2.5 px-1.5 text-center">平</th>
              <th class="py-2.5 px-1.5 text-center">负</th>
              <th class="py-2.5 px-2 text-center">得/失</th>
              <th class="py-2.5 px-1.5 text-center">净</th>
              <th class="py-2.5 px-2.5 text-center font-bold text-slate-200">分</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 font-mono text-[11px]">
            <tr
              v-for="row in currentLeague.table"
              :key="row.position"
              class="hover:bg-slate-850/60 transition"
            >
              <!-- 排名 -->
              <td class="py-2 px-2 text-center">
                <span :class="[
                  'w-4 h-4 rounded text-[9px] font-black inline-flex items-center justify-center',
                  row.position === 1 ? 'bg-amber-500 text-slate-950 font-black' :
                  row.position <= 3 ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' :
                  'text-slate-500'
                ]">
                  {{ row.position }}
                </span>
              </td>

              <!-- 球队名称与中立留洋小标签 -->
              <td class="py-2 px-3 font-sans font-bold text-white inline-flex items-center gap-1.5 truncate">
                <span class="truncate">{{ row.team_name }}</span>
                <span
                  v-if="row.is_overseas"
                  class="inline-flex items-center gap-0.5 bg-red-950 text-red-300 border border-red-800 px-1 py-0.1 rounded text-[8px] font-bold shrink-0"
                >
                  <Icon icon="circle-flags:cn" class="w-2.5 h-2.5" />
                  <span>留洋</span>
                </span>
              </td>

              <!-- 赛 胜 平 负 -->
              <td class="py-2 px-1.5 text-center text-slate-400">{{ row.played }}</td>
              <td class="py-2 px-1.5 text-center text-slate-300">{{ row.won }}</td>
              <td class="py-2 px-1.5 text-center text-slate-400">{{ row.drawn }}</td>
              <td class="py-2 px-1.5 text-center text-slate-500">{{ row.lost }}</td>

              <!-- 得失与净胜 -->
              <td class="py-2 px-2 text-center text-slate-400 text-[10px]">{{ row.gf }}-{{ row.ga }}</td>
              <td :class="[
                'py-2 px-1.5 text-center text-[10px] font-bold',
                row.gd > 0 ? 'text-emerald-400' : row.gd < 0 ? 'text-rose-400' : 'text-slate-500'
              ]">
                {{ row.gd > 0 ? '+' + row.gd : row.gd }}
              </td>

              <!-- 积分 -->
              <td class="py-2 px-2.5 text-center font-bold text-amber-400 text-xs">
                {{ row.points }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 4. 子视图 B: 射手/助攻榜 -->
    <div v-else-if="subView === 'leaders'" class="space-y-3">
      <!-- 射手榜卡片 -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-2">
        <div class="flex items-center justify-between text-xs font-bold text-slate-200 border-b border-slate-800 pb-2">
          <span class="inline-flex items-center gap-1.5">
            <Icon icon="ph:soccer-ball-fill" class="w-4 h-4 text-emerald-400" />
            <span>射手榜 (Top Scorers)</span>
          </span>
          <span class="text-[10px] text-slate-500">进球(点球)</span>
        </div>

        <div class="divide-y divide-slate-800/60 font-sans text-xs">
          <div
            v-for="s in currentLeague.scorers"
            :key="s.rank + s.player"
            class="py-2 flex items-center justify-between"
          >
            <div class="inline-flex items-center gap-2.5 min-w-0">
              <span :class="[
                'w-4 h-4 rounded text-[9px] font-black inline-flex items-center justify-center font-mono',
                s.rank === 1 ? 'bg-amber-500 text-slate-950' : 'bg-slate-800 text-slate-400'
              ]">
                {{ s.rank }}
              </span>
              <div class="truncate">
                <span class="font-bold text-white">{{ s.player }}</span>
                <span class="text-[10px] text-slate-500 ml-1.5">({{ s.team }})</span>
              </div>
            </div>
            <div class="text-right font-mono shrink-0">
              <span class="text-sm font-black text-emerald-400">{{ s.goals }}</span>
              <span class="text-[10px] text-slate-500 ml-1">({{ s.penalties }})</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 助攻榜卡片 -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-2">
        <div class="flex items-center justify-between text-xs font-bold text-slate-200 border-b border-slate-800 pb-2">
          <span class="inline-flex items-center gap-1.5">
            <Icon icon="mdi:shoe-cleat" class="w-4 h-4 text-amber-400" />
            <span>助攻榜 (Top Assists)</span>
          </span>
          <span class="text-[10px] text-slate-500">助攻数</span>
        </div>

        <div class="divide-y divide-slate-800/60 font-sans text-xs">
          <div
            v-for="a in currentLeague.assists"
            :key="a.rank + a.player"
            class="py-2 flex items-center justify-between"
          >
            <div class="inline-flex items-center gap-2.5 min-w-0">
              <span :class="[
                'w-4 h-4 rounded text-[9px] font-black inline-flex items-center justify-center font-mono',
                a.rank === 1 ? 'bg-amber-500 text-slate-950' : 'bg-slate-800 text-slate-400'
              ]">
                {{ a.rank }}
              </span>
              <div class="truncate">
                <span class="font-bold text-white">{{ a.player }}</span>
                <span class="text-[10px] text-slate-500 ml-1.5">({{ a.team }})</span>
              </div>
            </div>
            <div class="text-right font-mono shrink-0">
              <span class="text-sm font-black text-amber-400">{{ a.assists }}</span>
              <span class="text-[10px] text-slate-500 ml-1">助</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 5. 子视图 C: 转会动态 -->
    <div v-else-if="subView === 'transfers'" class="space-y-2">
      <div
        v-for="(tr, idx) in currentLeague.transfers"
        :key="idx"
        class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-1.5 text-xs shadow-sm"
      >
        <div class="flex items-center justify-between text-[10px]">
          <span class="bg-slate-950 text-teal-300 px-1.5 py-0.5 rounded border border-teal-900/40 font-bold">
            {{ tr.type }}
          </span>
          <span class="text-slate-500 font-mono inline-flex items-center gap-1">
            <Icon icon="lucide:calendar" class="w-2.5 h-2.5" />
            <span>{{ tr.date }}</span>
          </span>
        </div>

        <div class="flex items-center justify-between">
          <span class="font-bold text-white text-xs sm:text-sm">{{ tr.player }}</span>
          <span class="text-[11px] text-emerald-400 font-mono font-bold">{{ tr.fee }}</span>
        </div>

        <div class="text-[11px] text-slate-400 inline-flex items-center gap-2 pt-0.5">
          <span class="text-slate-300">{{ tr.from }}</span>
          <Icon icon="lucide:arrow-right" class="w-3 h-3 text-slate-500" />
          <span class="text-white font-medium">{{ tr.to }}</span>
        </div>
      </div>

      <div v-if="!currentLeague.transfers || currentLeague.transfers.length === 0" class="text-center py-10 text-slate-500 text-xs bg-slate-900 rounded-xl">
        暂无近期转会记录
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import standingsMultiRaw from '../../data/standings_multi.json'

const leaguesData = ref(standingsMultiRaw)

// 顶部左侧选中的联赛 Key：默认波甲 'pol_d1'
const selectedLeagueKey = ref('pol_d1')

// 顶部右侧子视图模式：'table' (积分榜) | 'leaders' (射手/助攻榜) | 'transfers' (转会动态)
const subView = ref('table')

const currentLeague = computed(() => {
  return leaguesData.value.leagues.find(lg => lg.key === selectedLeagueKey.value) || leaguesData.value.leagues[0]
})
</script>
