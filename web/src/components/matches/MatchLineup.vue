<template>
  <div class="space-y-4">
    <!-- 顶栏切换模式 (2D绿茵战术板 vs 详细列表) -->
    <div class="flex items-center justify-between text-xs">
      <div>
        <div class="font-bold text-white flex items-center space-x-1.5">
          <span>首发阵型：{{ match.formation || '4-1-1-4 (双前锋)' }}</span>
          <span class="text-[9px] bg-emerald-950 text-emerald-400 border border-emerald-800 px-1.5 rounded">
            {{ match.tactical_style || '密集短传 · Tiki-Taka' }}
          </span>
        </div>
        <div class="text-[10px] text-slate-400 mt-0.5">点击场上球员圆点，查看单场硬核数据与雷达图</div>
      </div>
      <div class="bg-slate-900 border border-slate-800 rounded-lg p-0.5 flex space-x-1">
        <button
          @click="lineupViewMode = 'pitch'"
          :class="['px-2.5 py-1 rounded text-[11px] font-semibold transition', lineupViewMode === 'pitch' ? 'bg-emerald-600 text-white font-bold' : 'text-slate-400 hover:text-white']"
        >
          2D球场
        </button>
        <button
          @click="lineupViewMode = 'list'"
          :class="['px-2.5 py-1 rounded text-[11px] font-semibold transition', lineupViewMode === 'list' ? 'bg-emerald-600 text-white font-bold' : 'text-slate-400 hover:text-white']"
        >
          列表对比
        </button>
      </div>
    </div>

    <!-- 1. 绿茵场 2D 俯视战术板 (4-1-1-3-1 阵型草坪布阵) -->
    <div v-show="lineupViewMode === 'pitch'" class="relative w-full aspect-[4/4.8] max-w-sm mx-auto rounded-2xl overflow-hidden border border-emerald-600/40 shadow-2xl bg-gradient-to-b from-emerald-950 via-emerald-900 to-emerald-950 p-2 select-none">
      <!-- 球场草皮条纹交替背景 -->
      <div class="absolute inset-0 flex flex-col pointer-events-none opacity-20">
        <div v-for="i in 8" :key="i" class="flex-1 odd:bg-black/25 even:bg-white/10"></div>
      </div>

      <!-- 球场白线标识 (SVG) -->
      <svg class="absolute inset-2 w-[calc(100%-16px)] h-[calc(100%-16px)] pointer-events-none stroke-emerald-300/40 fill-none" viewBox="0 0 100 120" preserveAspectRatio="none">
        <!-- 边线与中线 -->
        <rect x="2" y="2" width="96" height="116" stroke-width="0.8" rx="2" />
        <line x1="2" y1="60" x2="98" y2="60" stroke-width="0.8" />
        <circle cx="50" cy="60" r="14" stroke-width="0.8" />
        <circle cx="50" cy="60" r="1" fill="#34d399" />
        <!-- 上方禁区 (客队半场侧) -->
        <rect x="22" y="2" width="56" height="20" stroke-width="0.8" />
        <rect x="36" y="2" width="28" height="7" stroke-width="0.8" />
        <path d="M 38 22 A 12 12 0 0 0 62 22" stroke-width="0.8" />
        <!-- 下方禁区 (主队半场门将侧) -->
        <rect x="22" y="98" width="56" height="20" stroke-width="0.8" />
        <rect x="36" y="111" width="28" height="7" stroke-width="0.8" />
        <path d="M 38 98 A 12 12 0 0 1 62 98" stroke-width="0.8" />
      </svg>

      <!-- 11位球员战术棋子 -->
      <div
        v-for="p in formationPlayers"
        :key="p.name_en || p.name"
        @click="selectedPlayer = p"
        :style="{ top: p.pitch_top, left: p.pitch_left }"
        :class="[
          'absolute -translate-x-1/2 -translate-y-1/2 cursor-pointer flex flex-col items-center group transition-all duration-200 z-10',
          selectedPlayer?.name_en === p.name_en ? 'scale-110 z-20' : 'hover:scale-105'
        ]"
      >
        <!-- 棋子圆点 -->
        <div :class="[
          'w-8 h-8 rounded-full border-2 flex items-center justify-center shadow-lg text-[10px] font-black transition relative',
          selectedPlayer?.name_en === p.name_en
            ? 'bg-amber-400 text-slate-950 border-white ring-4 ring-amber-400/50 shadow-amber-500/50'
            : p.is_mvp
              ? 'bg-emerald-500 text-slate-950 border-amber-300 ring-2 ring-emerald-400/40 shadow-emerald-500/50'
              : 'bg-slate-900/95 text-white border-emerald-400/80 hover:border-emerald-300'
        ]">
          <span>{{ p.pos }}</span>
          <!-- MVP 标记 -->
          <span v-if="p.is_mvp" class="absolute -top-2 -right-1 text-[8px] bg-amber-400 text-slate-950 rounded-full px-1 font-black shadow inline-flex items-center">
            <Icon icon="lucide:star" class="w-2 h-2" />
          </span>
          <!-- 评分小角标 -->
          <span :class="[
            'absolute -bottom-1 -right-2 text-[8px] font-bold px-1 rounded-full shadow border border-slate-900',
            p.rating >= 7.5 ? 'bg-emerald-500 text-slate-950 font-black' :
            p.rating >= 7.0 ? 'bg-teal-500 text-slate-950' : 'bg-slate-800 text-slate-200'
          ]">
            {{ p.rating }}
          </span>
        </div>
        <!-- 中文姓名气泡 -->
        <div :class="[
          'mt-1 px-1.5 py-0.2 rounded text-[9px] font-bold tracking-tight whitespace-nowrap shadow backdrop-blur transition border',
          selectedPlayer?.name_en === p.name_en
            ? 'bg-amber-400 text-slate-950 font-black border-amber-300'
            : 'bg-slate-950/85 text-slate-200 border-slate-800'
        ]">
          {{ p.name_zh || p.name }}
        </div>
      </div>
    </div>

    <!-- 2. 选中球员详情卡片 (硬核数据 + 六维雷达图) -->
    <div v-if="activePlayer" class="bg-slate-900 rounded-xl border border-slate-800 p-3.5 space-y-3 shadow-lg animate-in fade-in duration-200">
      <!-- 球员名片顶栏 -->
      <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
        <div class="flex items-center space-x-2.5">
          <span class="w-8 h-8 rounded-lg bg-emerald-950 text-emerald-400 border border-emerald-800 flex items-center justify-center font-black text-xs">
            {{ activePlayer.pos }}
          </span>
          <div>
            <div class="font-black text-sm text-white flex items-center space-x-1.5">
              <span>{{ activePlayer.name_zh || activePlayer.name }}</span>
              <span v-if="activePlayer.is_mvp" class="text-[9px] bg-amber-400 text-slate-950 font-black px-1.5 py-0.2 rounded">全场最佳</span>
            </div>
            <div class="text-[10px] text-slate-400 mt-0.5">
              {{ activePlayer.name_en || activePlayer.name }} · 出场 {{ activePlayer.min || 90 }} 分钟
            </div>
          </div>
        </div>

        <!-- 赛后评分徽章 -->
        <div class="text-right">
          <div :class="[
            'text-lg font-black px-2.5 py-0.5 rounded-lg border inline-block',
            activePlayer.rating >= 7.5 ? 'bg-emerald-950 text-emerald-400 border-emerald-800' :
            activePlayer.rating >= 7.0 ? 'bg-teal-950 text-teal-300 border-teal-800' :
            'bg-slate-850 text-slate-300 border-slate-700'
          ]">
            {{ activePlayer.rating }}
          </div>
          <div class="text-[9px] text-slate-500 mt-0.5">FM 赛后评分</div>
        </div>
      </div>

      <!-- 六维雷达图与指标透视 -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center">
        <!-- SVG 雷达图组件 -->
        <PlayerRadar :radar="activePlayer.radar" title="六维赛场发挥雷达" />

        <!-- 6项硬核单场技战术统计 -->
        <div class="grid grid-cols-2 gap-2 text-xs">
          <div
            v-for="(val, key) in (activePlayer.stats || {})"
            :key="key"
            class="bg-slate-950 p-2 rounded-lg border border-slate-850"
          >
            <div class="text-[10px] text-slate-400 truncate">{{ key }}</div>
            <div class="font-black text-sm text-white mt-0.5 tracking-tight">{{ val }}</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. 全队首发清单与替补登场记录 -->
    <div class="space-y-2 pt-1">
      <div class="text-[11px] font-bold text-slate-400 mb-1 flex items-center justify-between">
        <span>全队首发清单 · 点击任一球员即可定位</span>
        <span class="text-[10px] text-slate-500">共 11 人首发</span>
      </div>

      <div
        v-for="p in match.lineup"
        :key="p.name_en || p.name"
        @click="selectedPlayer = p"
        :class="[
          'flex items-center justify-between p-2.5 rounded-lg border text-xs cursor-pointer transition',
          selectedPlayer?.name_en === p.name_en
            ? 'bg-slate-850 border-emerald-500 shadow-sm'
            : 'bg-slate-900 border-slate-800 hover:border-slate-700'
        ]"
      >
        <div class="flex items-center space-x-2.5">
          <span class="w-7 text-[10px] font-bold text-slate-400 text-center bg-slate-800 px-1 py-0.5 rounded shrink-0">
            {{ p.pos }}
          </span>
          <div>
            <div class="font-bold text-slate-200 flex items-center space-x-1.5">
              <span>{{ p.name_zh || p.name }}</span>
              <span v-if="p.is_mvp" class="text-[9px] bg-amber-500 text-slate-950 font-black px-1 rounded">MVP</span>
              <span v-if="p.goal" class="text-[10px] inline-flex items-center gap-0.5 text-emerald-400">
                <Icon icon="ph:soccer-ball-fill" class="w-2.5 h-2.5" />
                <span>x{{ p.goal }}</span>
              </span>
              <span v-if="p.assist" class="text-[10px] inline-flex items-center gap-0.5 text-teal-400">
                <Icon icon="mdi:shoe-cleat" class="w-2.5 h-2.5" />
                <span>x{{ p.assist }}</span>
              </span>
            </div>
            <div class="text-[10px] text-slate-500 flex items-center space-x-1">
              <span>{{ p.name_en || p.name }}</span>
              <span>·</span>
              <span>出场 {{ p.min }} 分钟</span>
            </div>
          </div>
        </div>

        <div class="flex items-center space-x-2">
          <span
            :class="[
              'font-black text-sm px-2 py-0.5 rounded',
              p.rating >= 7.5 ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' :
              p.rating >= 7.0 ? 'bg-teal-950 text-teal-300 border border-teal-800' :
              p.rating >= 6.5 ? 'bg-slate-800 text-slate-200' :
              'bg-rose-950 text-rose-300 border border-rose-900'
            ]"
          >
            {{ p.rating }}
          </span>
        </div>
      </div>

      <!-- 替补换人记录 -->
      <div v-if="match.bench_subs && match.bench_subs.length" class="space-y-1.5 pt-2">
        <div class="text-[11px] font-bold text-slate-400 mb-1 flex items-center justify-between">
          <span class="inline-flex items-center gap-1.5">
            <Icon icon="tabler:arrows-exchange" class="w-3.5 h-3.5 text-emerald-400" />
            <span>真实赛场替补换人记录</span>
          </span>
          <span class="text-[10px] text-slate-500">共 {{ match.bench_subs.length }} 人替补登场</span>
        </div>
        <div
          v-for="(sub, subIdx) in match.bench_subs"
          :key="subIdx"
          class="flex items-center justify-between p-2 rounded-lg bg-slate-950/70 border border-slate-800 text-xs"
        >
          <div class="flex items-center space-x-2">
            <span class="text-[10px] bg-slate-800 text-amber-400 px-1.5 py-0.5 rounded font-mono font-bold inline-flex items-center gap-1">
              <Icon icon="lucide:arrow-up-right" class="w-2.5 h-2.5 text-emerald-400" />
              <span>{{ sub.entered_minute }}' 换上</span>
            </span>
            <span class="font-bold text-slate-200">{{ sub.name_zh }}</span>
            <span class="text-[10px] text-slate-500 font-mono">({{ sub.pos }})</span>
            <span v-if="sub.goals" class="text-[10px] text-emerald-400 font-bold inline-flex items-center gap-0.5">
              <Icon icon="ph:soccer-ball-fill" class="w-2.5 h-2.5" />
              <span>x{{ sub.goals }}</span>
            </span>
            <span v-if="sub.assists" class="text-[10px] text-teal-400 font-bold inline-flex items-center gap-0.5">
              <Icon icon="mdi:shoe-cleat" class="w-2.5 h-2.5" />
              <span>x{{ sub.assists }}</span>
            </span>
          </div>
          <span class="text-[11px] font-mono text-emerald-400 font-bold">{{ sub.rating ? sub.rating + '分' : '登场' }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import PlayerRadar from '../common/PlayerRadar.vue'

const props = defineProps({
  match: {
    type: Object,
    required: true
  }
})

const lineupViewMode = ref('pitch')
const selectedPlayer = ref(null)

// 动态多阵型坐标映射 (支持 4-1-1-4 双前锋 / 4-1-1-3-1 单前锋 等无缝适配)
const formationPlayers = computed(() => {
  if (!props.match?.lineup) return []
  const lineup = props.match.lineup
  const coords = {
    'GK': { top: '89%', left: '50%' },
    'DL': { top: '70%', left: '16%' },
    'DC1': { top: '74%', left: '38%' },
    'DC2': { top: '74%', left: '62%' },
    'DR': { top: '70%', left: '84%' },
    'DM': { top: '56%', left: '38%' },
    'MC': { top: '48%', left: '64%' },
    'AML': { top: '30%', left: '18%' },
    'AMC': { top: '30%', left: '50%' },
    'AMR': { top: '30%', left: '82%' },
    'ST': { top: '12%', left: '50%' },
    'ST1': { top: '13%', left: '36%' },
    'ST2': { top: '13%', left: '64%' }
  }

  const stTotal = lineup.filter(p => p.pos && p.pos.includes('ST')).length
  let dcCount = 0
  let stCount = 0

  return lineup.map((p) => {
    let posKey = p.pos || 'MC'
    if (posKey.includes('DC')) {
      dcCount++
      posKey = dcCount === 1 ? 'DC1' : 'DC2'
    } else if (posKey.includes('ST')) {
      if (stTotal >= 2) {
        stCount++
        posKey = stCount === 1 ? 'ST1' : 'ST2'
      } else {
        posKey = 'ST'
      }
    }
    const coord = coords[posKey] || { top: '50%', left: '50%' }
    return {
      ...p,
      pitch_top: coord.top,
      pitch_left: coord.left
    }
  })
})

const activePlayer = computed(() => {
  if (selectedPlayer.value) {
    const matchInCur = formationPlayers.value.find(p => p.name_en === selectedPlayer.value.name_en || p.name === selectedPlayer.value.name)
    if (matchInCur) return matchInCur
  }
  return formationPlayers.value.find(p => p.is_mvp) || formationPlayers.value[formationPlayers.value.length - 1] || formationPlayers.value[0]
})
</script>
