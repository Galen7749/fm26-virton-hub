<template>
  <div class="space-y-4 text-xs animate-in fade-in duration-150">
    
    <!-- 1. 全队总览数据横幅 -->
    <div class="bg-gradient-to-r from-slate-900 via-slate-850 to-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-2.5 shadow-sm">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="text-base">👥</span>
          <div>
            <h3 class="font-black text-white text-xs">维尔通精英 · 2025/26 一线队大名单</h3>
            <p class="text-[9px] text-slate-400 font-sans">FM26 真实存档球员数据档案 · 共 12 名核心主力</p>
          </div>
        </div>
        <span class="text-[9px] bg-emerald-950 text-emerald-400 border border-emerald-800 px-2 py-0.5 rounded-full font-bold">
          平均年龄 23.4 岁
        </span>
      </div>

      <!-- 概览网格 -->
      <div class="grid grid-cols-4 gap-2 text-center text-xs">
        <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
          <div class="text-[10px] text-slate-400">一线队人数</div>
          <div class="font-black text-white text-sm mt-0.5">{{ squadList.length }} 人</div>
        </div>
        <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
          <div class="text-[10px] text-slate-400">射手榜首</div>
          <div class="font-black text-amber-400 text-xs mt-0.5 truncate">哈切姆(5球)</div>
        </div>
        <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
          <div class="text-[10px] text-slate-400">助攻王</div>
          <div class="font-black text-emerald-400 text-xs mt-0.5 truncate">托明(4助)</div>
        </div>
        <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
          <div class="text-[10px] text-slate-400">全勤战神</div>
          <div class="font-black text-teal-300 text-xs mt-0.5 truncate">德·施瑞沃(GK)</div>
        </div>
      </div>
    </div>

    <!-- 2. 分类位置筛选标签 -->
    <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar text-xs py-0.5">
      <button
        v-for="grp in groupFilters"
        :key="grp.key"
        @click="activeGroup = grp.key"
        :class="[
          'px-3 py-1.5 rounded-full text-xs font-semibold shrink-0 transition flex items-center space-x-1',
          activeGroup === grp.key
            ? 'bg-emerald-600 text-white font-bold shadow-sm'
            : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
        ]"
      >
        <span>{{ grp.icon }}</span>
        <span>{{ grp.label }}</span>
        <span class="text-[10px] opacity-75 font-mono">({{ getGroupCount(grp.key) }})</span>
      </button>
    </div>

    <!-- 3. 球员卡片网格列表 -->
    <div class="space-y-2.5">
      <div
        v-for="p in filteredSquad"
        :key="p.id"
        @click="selectedPlayer = p"
        class="bg-slate-900 border border-slate-800 hover:border-slate-700 rounded-xl p-3 space-y-2 cursor-pointer transition shadow-sm group active:scale-[0.99]"
      >
        <!-- 球员顶栏信息 -->
        <div class="flex items-center justify-between text-xs">
          <div class="flex items-center space-x-2.5">
            <!-- 球衣号码徽章 -->
            <div class="w-7 h-7 rounded-lg bg-slate-950 border border-slate-800 text-amber-400 font-mono font-black text-xs flex items-center justify-center shadow-inner shrink-0">
              #{{ p.number }}
            </div>
            <div>
              <div class="flex items-center space-x-1.5">
                <span class="font-black text-white text-xs">{{ p.name_zh }}</span>
                <span :class="[
                  'text-[9px] px-1.5 py-0.2 rounded font-bold font-mono',
                  p.position_group === 'forwards' ? 'bg-rose-950 text-rose-300 border border-rose-900' :
                  p.position_group === 'midfielders' ? 'bg-teal-950 text-teal-300 border border-teal-900' :
                  p.position_group === 'defenders' ? 'bg-indigo-950 text-indigo-300 border border-indigo-900' :
                  'bg-amber-950 text-amber-300 border border-amber-900'
                ]">
                  {{ p.position }}
                </span>
                <span class="text-[9px] bg-slate-800 text-slate-400 px-1.5 py-0.2 rounded">
                  {{ p.role_type }}
                </span>
              </div>
              <div class="text-[10px] text-slate-500 font-sans mt-0.5 flex items-center space-x-1">
                <span>{{ p.name_en }}</span>
                <span>·</span>
                <span>{{ p.age }}岁</span>
                <span>·</span>
                <span>{{ p.nation }}</span>
              </div>
            </div>
          </div>

          <!-- 赛季评分徽章 -->
          <div class="text-right shrink-0">
            <span :class="[
              'text-xs font-black font-mono px-2 py-0.5 rounded-lg border inline-block',
              p.avg_rating >= 7.3 ? 'bg-emerald-950 text-emerald-400 border-emerald-800' :
              p.avg_rating >= 7.1 ? 'bg-teal-950 text-teal-300 border-teal-800' :
              'bg-slate-850 text-slate-300 border-slate-700'
            ]">
              {{ p.avg_rating }}分
            </span>
            <div class="text-[9px] text-slate-500 mt-0.5">场均评分</div>
          </div>
        </div>

        <!-- 球员技战术简述 -->
        <p class="text-[11px] text-slate-300 leading-relaxed font-sans bg-slate-950/60 p-2 rounded-lg border border-slate-850">
          {{ p.tactical_role }}
        </p>

        <!-- 数据与身价底栏 -->
        <div class="flex items-center justify-between text-[10px] text-slate-400 pt-1 border-t border-slate-800/50">
          <div class="flex items-center space-x-3 font-mono">
            <span>出场: <strong class="text-slate-200">{{ p.matches }}场</strong></span>
            <span v-if="p.goals">进球: <strong class="text-amber-400">{{ p.goals }}球</strong></span>
            <span v-if="p.assists">助攻: <strong class="text-emerald-400">{{ p.assists }}次</strong></span>
            <span>身价: <strong class="text-slate-200">{{ p.market_value }}</strong></span>
          </div>

          <span class="text-emerald-400 font-bold group-hover:translate-x-0.5 transition-transform flex items-center space-x-0.5">
            <span>六维档案</span>
            <span>→</span>
          </span>
        </div>
      </div>
    </div>

    <!-- 4. 选中球员六维能力弹窗详情 -->
    <div
      v-if="selectedPlayer"
      class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-in fade-in duration-150"
      @click.self="selectedPlayer = null"
    >
      <div class="bg-slate-900 border border-slate-700 w-full max-w-sm rounded-2xl overflow-hidden shadow-2xl flex flex-col max-h-[85vh]">
        <!-- 弹窗顶栏 -->
        <div class="bg-gradient-to-r from-slate-850 to-slate-900 p-3.5 border-b border-slate-800 flex items-center justify-between">
          <div class="flex items-center space-x-2.5">
            <span class="w-8 h-8 rounded-lg bg-slate-950 text-amber-400 border border-slate-800 flex items-center justify-center font-mono font-black text-sm">
              #{{ selectedPlayer.number }}
            </span>
            <div>
              <div class="font-black text-sm text-white flex items-center space-x-1.5">
                <span>{{ selectedPlayer.name_zh }}</span>
                <span class="text-[9px] bg-emerald-950 text-emerald-400 border border-emerald-800 px-1.5 py-0.2 rounded font-mono">
                  {{ selectedPlayer.position }}
                </span>
              </div>
              <div class="text-[10px] text-slate-400 mt-0.5">
                {{ selectedPlayer.name_en }} · {{ selectedPlayer.age }}岁 · {{ selectedPlayer.nation }}
              </div>
            </div>
          </div>
          <button
            @click="selectedPlayer = null"
            class="text-slate-400 hover:text-white text-lg w-7 h-7 flex items-center justify-center rounded-full hover:bg-slate-800 transition"
          >
            ✕
          </button>
        </div>

        <!-- 弹窗内容区 (支持滚动) -->
        <div class="p-4 overflow-y-auto space-y-3.5 text-xs">
          <!-- 六维雷达图 -->
          <PlayerRadar :radar="selectedPlayer.radar" :title="selectedPlayer.name_zh + ' · 六维赛场综合能力'" />

          <!-- 具体核心技战术指标 -->
          <div class="space-y-1.5">
            <div class="text-[11px] font-bold text-slate-300">📊 赛季核心技战术数据指标</div>
            <div class="grid grid-cols-2 gap-2 text-xs">
              <div
                v-for="(val, key) in (selectedPlayer.stats || {})"
                :key="key"
                class="bg-slate-950 p-2.5 rounded-lg border border-slate-850"
              >
                <div class="text-[10px] text-slate-400 truncate">{{ key }}</div>
                <div class="font-black text-xs text-white mt-0.5 tracking-tight">{{ val }}</div>
              </div>
            </div>
          </div>

          <!-- 合同与身价信息 -->
          <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-850 space-y-1.5">
            <div class="text-[11px] font-bold text-slate-300">💼 球员合同与身价估值</div>
            <div class="grid grid-cols-3 gap-2 text-center text-xs pt-0.5">
              <div>
                <div class="text-[9px] text-slate-500">预估身价</div>
                <div class="font-black text-amber-400 text-xs mt-0.5">{{ selectedPlayer.market_value }}</div>
              </div>
              <div>
                <div class="text-[9px] text-slate-500">周薪待遇</div>
                <div class="font-black text-slate-200 text-xs mt-0.5">{{ selectedPlayer.wage }}</div>
              </div>
              <div>
                <div class="text-[9px] text-slate-500">合同期至</div>
                <div class="font-black text-slate-200 text-xs mt-0.5">{{ selectedPlayer.contract_until }}</div>
              </div>
            </div>
          </div>

          <!-- 战术定位说明 -->
          <div class="space-y-1 bg-slate-850/60 p-2.5 rounded-xl border border-slate-800">
            <div class="text-[10px] font-bold text-emerald-400">📋 4-1-1-3-1 战术体系角色重构</div>
            <p class="text-[11px] text-slate-300 leading-relaxed font-sans">
              {{ selectedPlayer.tactical_role }}
            </p>
          </div>
        </div>

        <!-- 弹窗底栏 -->
        <div class="p-3 bg-slate-950 border-t border-slate-800 text-center">
          <button
            @click="selectedPlayer = null"
            class="w-full bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs py-2 rounded-xl transition"
          >
            关闭档案
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import PlayerRadar from '../common/PlayerRadar.vue'
import squadData from '../../data/squad.json'

const squadList = ref(squadData)
const selectedPlayer = ref(null)

const activeGroup = ref('all')
const groupFilters = [
  { key: 'all', label: '全部球员', icon: '👥' },
  { key: 'forwards', label: '前锋锋线', icon: '⚽' },
  { key: 'midfielders', label: '中场中枢', icon: '🎯' },
  { key: 'defenders', label: '后防防线', icon: '🛡️' },
  { key: 'goalkeepers', label: '门将门神', icon: '🧤' }
]

const getGroupCount = (groupKey) => {
  if (groupKey === 'all') return squadList.value.length
  return squadList.value.filter(p => p.position_group === groupKey).length
}

const filteredSquad = computed(() => {
  if (activeGroup.value === 'all') return squadList.value
  return squadList.value.filter(p => p.position_group === activeGroup.value)
})
</script>
