<template>
  <div class="space-y-3.5 p-3.5 animate-in fade-in duration-150 pb-6">

    <!-- 1. 顶部控制栏：空间友好型两段式布局 (第一行：联赛选择器 + 置顶星标；第二行：三大子视图全宽分段切换器) -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-2.5 space-y-2 shadow-sm text-xs">
      
      <!-- 第一行：联赛分组下拉选择器 (带矢量国旗徽章与星标收藏) -->
      <div class="flex items-center justify-between gap-2">
        <div class="inline-flex items-center gap-2 min-w-0 flex-1">
          <Icon :icon="currentLeague.flag_icon || 'circle-flags:eu'" class="w-4 h-4 rounded-full shrink-0 shadow-sm" />
          
          <div class="relative min-w-0 flex-1">
            <select
              v-model="selectedLeagueKey"
              class="w-full bg-slate-950 border border-slate-700 text-slate-200 text-xs font-bold rounded-lg pl-2.5 pr-7 py-1.5 focus:outline-none focus:border-emerald-500 cursor-pointer shadow-inner appearance-none truncate"
            >
              <!-- 分组 1：已置顶赛事 (由 localStorage 动态持久化) -->
              <optgroup v-if="pinnedLeagues.length" label="⭐ 已置顶关注">
                <option
                  v-for="lg in pinnedLeagues"
                  :key="'pinned-' + lg.key"
                  :value="lg.key"
                >
                  ★ {{ lg.name }}
                </option>
              </optgroup>

              <!-- 分组 2：欧战与顶级赛事 (三大欧战 + 五大联赛 + 中超，默认第一顺位) -->
              <optgroup label="🔥 欧战与顶级赛事">
                <option
                  v-for="lg in popularLeagues"
                  :key="lg.key"
                  :value="lg.key"
                >
                  {{ lg.name }}
                </option>
              </optgroup>

              <!-- 分组 3：欧洲主要联赛 (波甲 / 比甲) -->
              <optgroup label="🌍 欧洲主要联赛">
                <option
                  v-for="lg in europeanLeagues"
                  :key="lg.key"
                  :value="lg.key"
                >
                  {{ lg.name }}
                </option>
              </optgroup>
            </select>
            <Icon icon="lucide:chevron-down" class="w-3.5 h-3.5 text-slate-400 absolute right-2 top-2 pointer-events-none" />
          </div>
        </div>

        <!-- 星标置顶切换按钮 (一键将当前联赛置顶在最上方) -->
        <button
          @click="togglePinCurrent"
          class="h-7 px-2.5 rounded-lg border inline-flex items-center justify-center gap-1 transition shadow-sm shrink-0"
          :class="isCurrentPinned ? 'bg-amber-950/80 border-amber-600/80 text-amber-400' : 'bg-slate-950 border-slate-800 text-slate-500 hover:text-slate-300'"
          :title="isCurrentPinned ? '已置顶 · 点击取消置顶' : '点击置顶此联赛'"
        >
          <Icon icon="lucide:star" class="w-3.5 h-3.5" :class="{ 'fill-amber-400': isCurrentPinned }" />
          <span class="text-[11px] font-bold">{{ isCurrentPinned ? '已置顶' : '置顶' }}</span>
        </button>
      </div>

      <!-- 第二行：3 个子视图全宽分段控制切换 (积分榜 | 射手/助攻榜 | 转会动态，杜绝文字溢出与纵向拉伸) -->
      <div class="bg-slate-950 p-1 rounded-lg border border-slate-800 grid grid-cols-3 gap-1 w-full text-center">
        <button
          @click="subView = 'table'"
          :class="[
            'py-1.5 px-1 rounded-md text-[11px] font-bold transition flex items-center justify-center gap-1 min-w-0',
            subView === 'table' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="lucide:trophy" class="w-3.5 h-3.5 shrink-0" />
          <span class="truncate">积分榜</span>
        </button>

        <button
          @click="subView = 'leaders'"
          :class="[
            'py-1.5 px-1 rounded-md text-[11px] font-bold transition flex items-center justify-center gap-1 min-w-0',
            subView === 'leaders' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="ph:soccer-ball-fill" class="w-3.5 h-3.5 shrink-0" />
          <span class="truncate">射手/助攻</span>
        </button>

        <button
          @click="subView = 'transfers'"
          :class="[
            'py-1.5 px-1 rounded-md text-[11px] font-bold transition flex items-center justify-center gap-1 min-w-0',
            subView === 'transfers' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon icon="tabler:arrows-exchange" class="w-3.5 h-3.5 shrink-0" />
          <span class="truncate">转会动态</span>
        </button>
      </div>
    </div>

    <!-- 2. 当前联赛赛季与轮次概况条 (杜绝标签与长文本互相叠盖重合) -->
    <div class="flex items-center justify-between text-[11px] text-slate-400 px-1 gap-2 min-w-0">
      <div class="inline-flex items-center gap-1.5 font-bold text-slate-200 shrink-0">
        <Icon :icon="currentLeague.flag_icon || 'circle-flags:eu'" class="w-3.5 h-3.5 rounded-full shrink-0" />
        <span class="text-emerald-400 font-mono">{{ currentLeague.season }}</span>
        <span v-if="isCurrentPinned" class="bg-amber-950/80 text-amber-300 border border-amber-800/80 text-[9px] px-1.5 py-0.5 rounded font-bold inline-flex items-center gap-0.5 shrink-0">
          <Icon icon="lucide:star" class="w-2.5 h-2.5 fill-amber-300" />
          <span>置顶</span>
        </span>
      </div>
      <span class="text-slate-400 text-[10px] font-mono truncate text-right min-w-0" :title="currentLeague.round_info">
        {{ currentLeague.round_info }}
      </span>
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
                  row.position <= 4 ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' :
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
          <div v-if="!currentLeague.scorers || currentLeague.scorers.length === 0" class="py-4 text-center text-slate-500 text-xs">
            暂无射手榜统计
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
          <div v-if="!currentLeague.assists || currentLeague.assists.length === 0" class="py-4 text-center text-slate-500 text-xs">
            暂无助攻榜统计
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
          <span
            class="text-[11px] font-mono"
            :class="tr.fee && tr.fee.includes('估值') ? 'text-amber-400 font-medium' : tr.fee && tr.fee.includes('租借') ? 'text-sky-400 font-bold' : 'text-emerald-400 font-bold'"
          >
            {{ tr.fee }}
          </span>
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

// ── 用户收藏/置顶赛事 (持久化至 localStorage) ──────────────────────
const PINNED_STORAGE_KEY = 'dqy_pinned_leagues'

function getInitialPinned() {
  try {
    const raw = localStorage.getItem(PINNED_STORAGE_KEY)
    if (raw) {
      const parsed = JSON.parse(raw)
      if (Array.isArray(parsed) && parsed.length) {
        // 优先置顶当前所在联赛 (波甲 pol_d1) 和欧战 (欧冠 ucl) 为第一顺位
        const withoutPol = parsed.filter(k => k !== 'pol_d1')
        return ['pol_d1', ...withoutPol]
      }
    }
  } catch (e) {
    // ignore
  }
  return ['pol_d1', 'ucl'] // 默认置顶：第一位波甲、第二位欧冠
}

const pinnedLeagueKeys = ref(getInitialPinned())

// 默认选中置顶第一项：所在联赛波甲 'pol_d1'
const defaultSelectedKey = pinnedLeagueKeys.value.length ? pinnedLeagueKeys.value[0] : 'pol_d1'
const selectedLeagueKey = ref(defaultSelectedKey)

// 顶部右侧子视图模式：'table' (积分榜) | 'leaders' (射手/助攻榜) | 'transfers' (转会动态)
const subView = ref('table')

// 当前激活联赛对象
const currentLeague = computed(() => {
  return leaguesData.value.leagues.find(lg => lg.key === selectedLeagueKey.value) || leaguesData.value.leagues[0]
})

// 检查当前联赛是否已置顶
const isCurrentPinned = computed(() => {
  return pinnedLeagueKeys.value.includes(selectedLeagueKey.value)
})

// 切换当前联赛置顶状态
const togglePinCurrent = () => {
  const key = selectedLeagueKey.value
  if (pinnedLeagueKeys.value.includes(key)) {
    pinnedLeagueKeys.value = pinnedLeagueKeys.value.filter(k => k !== key)
  } else {
    pinnedLeagueKeys.value = [...pinnedLeagueKeys.value, key]
  }
  try {
    localStorage.setItem(PINNED_STORAGE_KEY, JSON.stringify(pinnedLeagueKeys.value))
  } catch (e) {
    // ignore
  }
}

// 分组计算：置顶赛事
const pinnedLeagues = computed(() => {
  return pinnedLeagueKeys.value
    .map(key => leaguesData.value.leagues.find(lg => lg.key === key))
    .filter(Boolean)
})

// 分组计算：热门顶级赛事 (欧冠、英超、西甲、意甲、德甲、法甲、中超)
const popularLeagues = computed(() => {
  return leaguesData.value.leagues.filter(lg => lg.group === 'popular')
})

// 分组计算：欧洲其他主要联赛 (波甲、比甲、比乙)
const europeanLeagues = computed(() => {
  return leaguesData.value.leagues.filter(lg => lg.group === 'european')
})
</script>
