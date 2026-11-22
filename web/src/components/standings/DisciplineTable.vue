<template>
  <div class="space-y-3">
    <div class="bg-slate-900 border border-slate-800 rounded-lg p-2.5 flex items-center justify-between text-xs">
      <span class="font-bold text-white">🇧🇪 比乙联赛 · 纪律榜与停赛监控</span>
      <span v-if="topVirton" class="text-[10px] text-amber-400 font-bold">
        {{ topVirton.player_zh }} {{ topVirton.yellow_cards ?? topVirton.yellow ?? 0 }}黄 ({{ topVirton.status || '正常' }})
      </span>
    </div>

    <div class="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden text-xs">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="bg-slate-850 text-slate-400 border-b border-slate-800 text-[10px]">
            <th class="py-2.5 px-2 text-center w-8">#</th>
            <th class="py-2.5 px-2">球员 / 俱乐部</th>
            <th class="py-2.5 px-1 text-center w-8">🟨 黄</th>
            <th class="py-2.5 px-1 text-center w-8">🟥 红</th>
            <th class="py-2.5 px-2 text-center font-bold w-14">状态</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="d in discipline"
            :key="d.rank"
            :class="[
              'border-b border-slate-800/60 transition hover:bg-slate-850',
              d.is_virton ? 'bg-amber-950/20 font-bold border-l-2 border-amber-500' : 'text-slate-300'
            ]"
          >
            <td class="py-2 px-2 text-center font-bold text-slate-400">{{ d.rank }}</td>
            <td class="py-2 px-2 truncate max-w-[140px]">
              <div class="flex items-center space-x-1.5">
                <span class="font-bold text-slate-200">{{ d.player_zh }}</span>
                <span v-if="d.is_virton" class="text-[9px] bg-amber-600 text-white px-1 rounded font-normal">本队</span>
              </div>
              <div class="text-[10px] text-slate-500 truncate">{{ d.team_short }}</div>
            </td>
            <td class="py-2 px-1 text-center text-amber-400 font-bold">{{ d.yellow_cards ?? d.yellow ?? 0 }}</td>
            <td class="py-2 px-1 text-center text-rose-500 font-bold">{{ d.red_cards ?? d.red ?? 0 }}</td>
            <td class="py-2 px-2 text-center">
              <span :class="[
                'text-[9px] px-1.5 py-0.5 rounded font-bold',
                (d.status || d.suspension_warning || '').includes('停赛') ? 'bg-rose-950 text-rose-400 border border-rose-800' :
                (d.status || d.suspension_warning || '').includes('警告') ? 'bg-amber-950 text-amber-300 border border-amber-800' : 'bg-slate-800 text-slate-400'
              ]">
                {{ d.status || d.suspension_warning || '正常' }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  discipline: {
    type: Array,
    default: () => []
  }
})

const topVirton = computed(() => props.discipline.find(d => d.is_virton))
</script>
