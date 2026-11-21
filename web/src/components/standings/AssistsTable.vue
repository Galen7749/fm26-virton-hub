<template>
  <div class="space-y-3">
    <div class="bg-slate-900 border border-slate-800 rounded-lg p-2.5 flex items-center justify-between text-xs">
      <span class="font-bold text-white">🇧🇪 比乙联赛 · 官方助攻榜</span>
      <span class="text-[10px] text-emerald-400 font-bold">泰伦·托明 4次领跑第1</span>
    </div>

    <div class="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden text-xs">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="bg-slate-850 text-slate-400 border-b border-slate-800 text-[10px]">
            <th class="py-2.5 px-2 text-center w-8">#</th>
            <th class="py-2.5 px-2">球员 / 俱乐部</th>
            <th class="py-2.5 px-1 text-center w-8">场次</th>
            <th class="py-2.5 px-1 text-center w-12">关键传球</th>
            <th class="py-2.5 px-2 text-center font-bold w-10">助攻</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="a in assists"
            :key="a.rank"
            :class="[
              'border-b border-slate-800/60 transition hover:bg-slate-850',
              a.is_virton ? 'bg-emerald-950/60 font-bold text-emerald-300 border-l-2 border-emerald-500' : 'text-slate-300'
            ]"
          >
            <td class="py-2 px-2 text-center font-bold">
              <span :class="[
                'w-5 h-5 rounded flex items-center justify-center text-[10px] mx-auto',
                a.rank === 1 ? 'bg-amber-400 text-slate-950 font-black' :
                a.rank <= 3 ? 'bg-amber-400/20 text-amber-300 font-bold' : 'text-slate-400'
              ]">
                {{ a.rank }}
              </span>
            </td>
            <td class="py-2 px-2 truncate max-w-[140px]">
              <div class="flex items-center space-x-1.5">
                <span class="font-bold text-slate-200">{{ a.player_zh }}</span>
                <span v-if="a.is_virton" class="text-[9px] bg-emerald-600 text-white px-1 rounded font-normal">本队</span>
              </div>
              <div class="text-[10px] text-slate-500 truncate">{{ a.team_short }}</div>
            </td>
            <td class="py-2 px-1 text-center text-slate-400">{{ a.matches }}</td>
            <td class="py-2 px-1 text-center text-slate-400">{{ a.key_passes }}</td>
            <td class="py-2 px-2 text-center font-black text-teal-400 text-sm">{{ a.assists }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
defineProps({
  assists: {
    type: Array,
    default: () => []
  }
})
</script>
