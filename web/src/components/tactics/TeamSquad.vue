<template>
  <div class="space-y-3.5 text-xs animate-in fade-in duration-150">
    
    <!-- 1. 全队总览数据横幅 -->
    <div class="bg-gradient-to-r from-slate-900 via-slate-850 to-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-2.5 shadow-sm">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="text-base">👥</span>
          <div>
            <h3 class="font-black text-white text-xs">维尔通精英 · 2025/26 一线队大名单</h3>
            <p class="text-[9px] text-slate-400 font-sans">FM26 真实存档球员数据 · 共 12 名核心主力</p>
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
          <div class="text-[10px] text-slate-400">全勤门神</div>
          <div class="font-black text-teal-300 text-xs mt-0.5 truncate">德·施瑞沃(GK)</div>
        </div>
      </div>
    </div>

    <!-- 2. 控制条：位置筛选胶囊 + 视图切换 (卡片 / 表格) -->
    <div class="flex items-center justify-between gap-2">
      <!-- 分类位置筛选标签 -->
      <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar text-xs py-0.5 flex-1 min-w-0">
        <button
          v-for="grp in groupFilters"
          :key="grp.key"
          @click="activeGroup = grp.key"
          :class="[
            'px-2.5 py-1 rounded-full text-xs font-semibold shrink-0 transition flex items-center space-x-1',
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

      <!-- 视图模式切换 -->
      <div class="bg-slate-900 border border-slate-800 rounded-lg p-0.5 flex space-x-0.5 shrink-0">
        <button
          @click="displayMode = 'cards'"
          :class="[
            'px-2 py-0.5 rounded text-[10px] font-semibold transition',
            displayMode === 'cards' ? 'bg-emerald-600 text-white font-bold shadow-sm' : 'text-slate-400 hover:text-white'
          ]"
          title="卡片视图"
        >
          📇 卡片
        </button>
        <button
          @click="displayMode = 'table'"
          :class="[
            'px-2 py-0.5 rounded text-[10px] font-semibold transition',
            displayMode === 'table' ? 'bg-emerald-600 text-white font-bold shadow-sm' : 'text-slate-400 hover:text-white'
          ]"
          title="表格视图"
        >
          📑 表格
        </button>
      </div>
    </div>

    <!-- 3A. 球员卡片列表视图 (纯正常数据显示，无冗余主观描述文本) -->
    <div v-if="displayMode === 'cards'" class="space-y-2.5">
      <div
        v-for="p in filteredSquad"
        :key="p.id"
        @click="selectedPlayer = p"
        class="bg-slate-900 border border-slate-800 hover:border-slate-700 rounded-xl p-3 space-y-2.5 cursor-pointer transition shadow-sm group active:scale-[0.99]"
      >
        <!-- 球员顶栏信息 -->
        <div class="flex items-center justify-between text-xs">
          <div class="flex items-center space-x-2.5 min-w-0">
            <!-- 球衣号码徽章 -->
            <div class="w-7 h-7 rounded-lg bg-slate-950 border border-slate-800 text-amber-400 font-mono font-black text-xs flex items-center justify-center shadow-inner shrink-0">
              #{{ p.number }}
            </div>
            <div class="min-w-0">
              <div class="flex items-center space-x-1.5 flex-wrap gap-y-1">
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
                  {{ p.position_desc ? p.position_desc.split(' ')[0] : p.role_type }}
                </span>
              </div>
              <div class="text-[10px] text-slate-500 font-sans mt-0.5 flex items-center space-x-1 truncate">
                <span>{{ p.name_en }}</span>
                <span>·</span>
                <span>{{ p.age }}岁</span>
                <span>·</span>
                <span>{{ p.nation }}</span>
              </div>
            </div>
          </div>

          <!-- 赛季评分徽章 -->
          <div class="text-right shrink-0 ml-2">
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

        <!-- 正常数据指标展示网格 (出场首发、进球/助攻或扑救、身价估值、周薪待遇) -->
        <div class="grid grid-cols-4 gap-1.5 bg-slate-950/70 p-2 rounded-lg border border-slate-850 text-center font-mono">
          <div>
            <div class="text-[9px] text-slate-500">出场 (首发)</div>
            <div class="text-[11px] font-bold text-slate-200 mt-0.5">{{ p.matches }}场 ({{ p.starts }})</div>
          </div>
          <div>
            <div class="text-[9px] text-slate-500">{{ p.position_group === 'goalkeepers' ? '扑救 (零封)' : '进球 / 助攻' }}</div>
            <div class="text-[11px] font-bold text-amber-400 mt-0.5">
              {{ p.position_group === 'goalkeepers' ? '32次 (3场)' : `${p.goals}球 / ${p.assists}助` }}
            </div>
          </div>
          <div>
            <div class="text-[9px] text-slate-500">预估身价</div>
            <div class="text-[11px] font-bold text-slate-200 mt-0.5">{{ p.market_value }}</div>
          </div>
          <div>
            <div class="text-[9px] text-slate-500">周薪待遇</div>
            <div class="text-[11px] font-bold text-emerald-400 mt-0.5">{{ p.wage }}</div>
          </div>
        </div>

        <!-- 底栏：合同年限、球员定位与六维详情入口 -->
        <div class="flex items-center justify-between text-[10px] text-slate-400 pt-0.5 border-t border-slate-800/40">
          <div class="flex items-center space-x-2 font-mono">
            <span>合同至: <strong class="text-slate-300">{{ p.contract_until }}</strong></span>
            <span class="text-slate-700">|</span>
            <span>定位: <strong class="text-slate-300">{{ p.role_type }}</strong></span>
          </div>

          <span class="text-emerald-400 font-bold group-hover:translate-x-0.5 transition-transform flex items-center space-x-0.5 text-[10px]">
            <span>六维能力档案</span>
            <span class="text-xs">→</span>
          </span>
        </div>
      </div>
    </div>

    <!-- 3B. 球员紧凑数据表格视图 (纯数据对齐，一目了然) -->
    <div v-else-if="displayMode === 'table'" class="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden shadow-sm">
      <div class="overflow-x-auto no-scrollbar">
        <table class="w-full text-left text-xs">
          <thead class="bg-slate-950 text-slate-400 text-[10px] uppercase font-mono border-b border-slate-800">
            <tr>
              <th class="py-2.5 px-3">#</th>
              <th class="py-2.5 px-2">球员姓名</th>
              <th class="py-2.5 px-2">位置</th>
              <th class="py-2.5 px-2 text-center">年龄</th>
              <th class="py-2.5 px-2 text-center">出场(首发)</th>
              <th class="py-2.5 px-2 text-center">进球/助攻</th>
              <th class="py-2.5 px-2 text-center">评分</th>
              <th class="py-2.5 px-3 text-right">身价估值</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-850 font-mono text-[11px]">
            <tr
              v-for="p in filteredSquad"
              :key="p.id"
              @click="selectedPlayer = p"
              class="hover:bg-slate-850/60 cursor-pointer transition active:bg-slate-800"
            >
              <td class="py-2.5 px-3 font-bold text-amber-400">#{{ p.number }}</td>
              <td class="py-2.5 px-2 font-sans font-bold text-white truncate max-w-[110px]">
                {{ p.name_zh }}
              </td>
              <td class="py-2.5 px-2">
                <span :class="[
                  'text-[9px] px-1 py-0.2 rounded font-bold',
                  p.position_group === 'forwards' ? 'bg-rose-950 text-rose-300' :
                  p.position_group === 'midfielders' ? 'bg-teal-950 text-teal-300' :
                  p.position_group === 'defenders' ? 'bg-indigo-950 text-indigo-300' :
                  'bg-amber-950 text-amber-300'
                ]">
                  {{ p.position }}
                </span>
              </td>
              <td class="py-2.5 px-2 text-center text-slate-400">{{ p.age }}</td>
              <td class="py-2.5 px-2 text-center text-slate-300">{{ p.matches }}({{ p.starts }})</td>
              <td class="py-2.5 px-2 text-center text-amber-400 font-bold">
                {{ p.position_group === 'goalkeepers' ? '32扑/3零封' : `${p.goals}球/${p.assists}助` }}
              </td>
              <td class="py-2.5 px-2 text-center">
                <span :class="[
                  'font-bold',
                  p.avg_rating >= 7.3 ? 'text-emerald-400' :
                  p.avg_rating >= 7.1 ? 'text-teal-300' : 'text-slate-300'
                ]">
                  {{ p.avg_rating }}
                </span>
              </td>
              <td class="py-2.5 px-3 text-right text-slate-200 font-semibold">{{ p.market_value }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 4. 选中球员六维能力档案弹窗 -->
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

          <!-- 具体核心技战术数据指标 -->
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
const displayMode = ref('cards') // 'cards' | 'table'

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
