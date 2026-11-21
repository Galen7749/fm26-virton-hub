<template>
  <div class="p-4 space-y-4 animate-in fade-in duration-150">
    
    <!-- 顶部二级分段开关 (战术哲学体系 VS 一线队球员阵容) -->
    <div class="flex p-1 bg-slate-900 border border-slate-800 rounded-xl shadow-sm">
      <button
        @click="subTab = 'tactics'"
        :class="[
          'flex-1 py-1.5 text-xs font-bold rounded-lg transition flex items-center justify-center space-x-1.5',
          subTab === 'tactics'
            ? 'bg-emerald-600 text-white shadow-sm'
            : 'text-slate-400 hover:text-white'
        ]"
      >
        <span>📋</span>
        <span>战术哲学体系</span>
      </button>

      <button
        @click="subTab = 'squad'"
        :class="[
          'flex-1 py-1.5 text-xs font-bold rounded-lg transition flex items-center justify-center space-x-1.5',
          subTab === 'squad'
            ? 'bg-emerald-600 text-white shadow-sm'
            : 'text-slate-400 hover:text-white'
        ]"
      >
        <span>👥</span>
        <span>一线队球员阵容</span>
      </button>
    </div>

    <!-- 视图 1: 战术哲学架构 -->
    <div v-if="subTab === 'tactics'" class="space-y-4">
      <!-- 战术身份徽章 -->
      <div class="bg-gradient-to-r from-slate-900 to-slate-950 border border-slate-800 rounded-xl p-3.5 space-y-2.5">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-2">
            <span class="text-base">📋</span>
            <h3 class="font-black text-white text-xs">{{ clubName }} · 战术哲学架构</h3>
          </div>
          <span class="text-[9px] bg-emerald-950 text-emerald-400 border border-emerald-800 px-2 py-0.5 rounded-full font-bold">
            主帅体系档案
          </span>
        </div>

        <div class="grid grid-cols-3 gap-2 text-center text-xs">
          <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
            <div class="text-[10px] text-slate-400">核心阵型</div>
            <div class="font-black text-white mt-0.5">{{ teamAnalysis?.tactical_system?.formation || teamAnalysis?.tactical_overview?.formation || '4-1-1-3-1' }}</div>
          </div>
          <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
            <div class="text-[10px] text-slate-400">战术风格</div>
            <div class="font-bold text-emerald-400 mt-0.5 truncate text-[11px]">{{ teamAnalysis?.tactical_system?.style_name || teamAnalysis?.tactical_overview?.mentality || '密集短传 · Tiki-Taka' }}</div>
          </div>
          <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
            <div class="text-[10px] text-slate-400">比赛心态</div>
            <div class="font-black text-white mt-0.5">{{ teamAnalysis?.tactical_system?.tempo || '积极进取' }}</div>
          </div>
        </div>
      </div>

      <!-- 三路进攻推进走廊分布 -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-2.5">
        <div class="flex items-center justify-between text-xs">
          <span class="font-bold text-white flex items-center space-x-1.5">
            <span>🏹</span>
            <span>三路进攻发起权重 (Attack Channels)</span>
          </span>
          <span class="text-[10px] text-emerald-400 font-bold">右路走廊占优</span>
        </div>

        <!-- 分布走廊三段进度条 -->
        <div class="w-full bg-slate-950 h-3 rounded-full overflow-hidden flex border border-slate-800">
          <div class="bg-teal-600 h-full flex items-center justify-center text-[8px] text-white font-black" :style="{ width: `${leftPct}%` }">
            左 {{ leftPct }}%
          </div>
          <div class="bg-slate-700 h-full flex items-center justify-center text-[8px] text-slate-200 font-black" :style="{ width: `${centerPct}%` }">
            中 {{ centerPct }}%
          </div>
          <div class="bg-emerald-500 h-full flex items-center justify-center text-[8px] text-slate-950 font-black" :style="{ width: `${rightPct}%` }">
            右 {{ rightPct }}%
          </div>
        </div>

        <div class="grid grid-cols-3 gap-2 text-center text-[10px] text-slate-400 pt-1">
          <div>左路发起 ({{ leftPct }}%)</div>
          <div>中路渗透 ({{ centerPct }}%)</div>
          <div class="text-emerald-400 font-bold">右路突击 ({{ rightPct }}% ★)</div>
        </div>
      </div>

      <!-- 技战术能力指标 vs 联赛平均水准对比条 -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-3">
        <div class="flex items-center justify-between text-xs font-bold text-white">
          <span class="flex items-center space-x-1.5">
            <span>📈</span>
            <span>核心战术指标对标 ({{ clubName }} vs 联赛均值)</span>
          </span>
          <span class="text-[10px] text-slate-400 font-normal">官方数据透视</span>
        </div>

        <div class="space-y-2.5">
          <div
            v-for="m in (teamAnalysis?.team_radar || [])"
            :key="m.label"
            class="space-y-1 text-xs"
          >
            <div class="flex justify-between items-center text-[11px]">
              <span class="text-slate-300 font-bold">{{ m.label }}</span>
              <div class="flex items-center space-x-2 font-mono">
                <span class="text-emerald-400 font-black">{{ m.value }}分</span>
                <span class="text-slate-500 text-[10px]">(比乙均值: {{ m.league_avg }})</span>
              </div>
            </div>
            
            <!-- 双层对比条 -->
            <div class="w-full bg-slate-950 h-2 rounded-full overflow-hidden relative border border-slate-800">
              <!-- 联赛基准线 (灰色) -->
              <div class="bg-slate-700/60 h-full absolute top-0 left-0" :style="{ width: `${m.league_avg}%` }"></div>
              <!-- 实力线 (翡翠绿) -->
              <div class="bg-emerald-500 h-full rounded-full transition-all duration-500 relative z-10" :style="{ width: `${m.value}%` }"></div>
            </div>
            <div class="text-[9px] text-slate-500">{{ m.desc }}</div>
          </div>
        </div>
      </div>

      <!-- 战术优劣势透视 -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <!-- 优势 -->
        <div class="bg-slate-900 border border-emerald-900/60 rounded-xl p-3 space-y-1.5">
          <div class="text-xs font-bold text-emerald-400 flex items-center space-x-1">
            <span>✅</span>
            <span>体系核心优势</span>
          </div>
          <ul class="space-y-1 text-[11px] text-slate-300">
            <li v-for="(str, sIdx) in (teamAnalysis?.strengths || [])" :key="sIdx" class="leading-relaxed">
              • {{ str }}
            </li>
          </ul>
        </div>

        <!-- 隐患 -->
        <div class="bg-slate-900 border border-rose-900/60 rounded-xl p-3 space-y-1.5">
          <div class="text-xs font-bold text-rose-400 flex items-center space-x-1">
            <span>⚠️</span>
            <span>潜在阵容与体能隐患</span>
          </div>
          <ul class="space-y-1 text-[11px] text-slate-300">
            <li v-for="(c, cIdx) in (teamAnalysis?.concerns || [])" :key="cIdx" class="leading-relaxed">
              • {{ c }}
            </li>
          </ul>
        </div>
      </div>

      <!-- 欧洲名宿战术点评 -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-1.5">
        <div class="text-xs font-bold text-slate-200 flex items-center space-x-1.5">
          <span>📰</span>
          <span>外媒专栏 · 战术观察哨</span>
        </div>
        <p class="text-xs text-slate-300 leading-relaxed font-sans bg-slate-950 p-2.5 rounded-lg border border-slate-850">
          {{ teamAnalysis?.analyst_quote || teamAnalysis?.media_quote?.content || '暂无外媒点评' }}
        </p>
      </div>
    </div>

    <!-- 视图 2: 一线队球员阵容与六维档案 -->
    <div v-else-if="subTab === 'squad'">
      <TeamSquad />
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import TeamSquad from './TeamSquad.vue'

const props = defineProps({
  teamAnalysis: {
    type: Object,
    default: () => ({})
  },
  clubName: {
    type: String,
    default: '维尔通精英'
  }
})

const subTab = ref('tactics') // 'tactics' | 'squad'

const leftPct = computed(() => props.teamAnalysis?.attack_channels?.left_wing || props.teamAnalysis?.attack_channels?.left || 29)
const centerPct = computed(() => props.teamAnalysis?.attack_channels?.center || 28)
const rightPct = computed(() => props.teamAnalysis?.attack_channels?.right_wing || props.teamAnalysis?.attack_channels?.right || 43)
</script>
