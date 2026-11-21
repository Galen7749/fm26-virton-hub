<template>
  <div class="space-y-2 text-xs">
    <div class="flex items-center justify-between text-xs font-bold text-slate-300">
      <span>🇧🇪 比乙第 {{ round }} 轮 · 完整战报栏</span>
      <span class="text-[10px] text-slate-500">官方正式赛果</span>
    </div>

    <div class="bg-slate-900 rounded-xl border border-slate-800 divide-y divide-slate-800/60 text-xs overflow-hidden">
      <div
        v-for="(m, mIdx) in matches"
        :key="mIdx"
        :class="[
          'px-2.5 py-2.5 grid grid-cols-[58px_1fr_46px_1fr] items-center gap-1.5 transition',
          m.is_virton ? 'bg-emerald-950/40 border-l-2 border-emerald-500' : 'hover:bg-slate-850'
        ]"
      >
        <!-- 1. 日期与标记 (固定58px) -->
        <div class="flex items-center space-x-1 text-[10px] text-slate-400 truncate">
          <span class="font-mono">{{ (m.date || '').slice(5) }}</span>
          <span v-if="m.is_virton" class="text-emerald-400 font-bold shrink-0">[本场]</span>
        </div>

        <!-- 2. 主队 (向右对齐贴向比分) -->
        <div class="truncate text-right font-medium text-slate-300">
          <span :class="m.home === '维尔通精英' ? 'text-emerald-400 font-bold' : ''">
            {{ m.home }}
          </span>
        </div>

        <!-- 3. 比分药丸 (固定46px，水平居中) -->
        <div class="flex justify-center">
          <span class="font-mono font-bold bg-slate-950 text-slate-100 px-2 py-0.5 rounded text-[11px] border border-slate-800 text-center w-[46px] block tracking-wider">
            {{ m.score }}
          </span>
        </div>

        <!-- 4. 客队 (向左对齐贴向比分) -->
        <div class="truncate text-left font-medium text-slate-300">
          <span :class="m.away === '维尔通精英' ? 'text-emerald-400 font-bold' : ''">
            {{ m.away }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  matches: {
    type: Array,
    default: () => []
  },
  round: {
    type: [Number, String],
    default: 1
  }
})
</script>
