<template>
  <div class="flex flex-col items-center justify-center bg-slate-950 rounded-lg p-2 border border-slate-850 relative">
    <div v-if="title" class="text-[10px] font-bold text-slate-400 mb-1">{{ title }}</div>
    <svg class="w-44 h-44 overflow-visible" viewBox="0 0 180 180">
      <!-- 同心网格 (25%, 50%, 75%, 100%) -->
      <polygon
        v-for="lvl in [0.25, 0.5, 0.75, 1.0]"
        :key="lvl"
        :points="getPolygonPoints(radar, 90, 90, 60 * lvl, true)"
        class="stroke-slate-800/80 fill-none"
        stroke-width="1"
      />
      <!-- 轴线 -->
      <line
        v-for="(axis, aIdx) in (radar || [])"
        :key="aIdx"
        :x1="90"
        :y1="90"
        :x2="getVertexCoord(aIdx, radar.length, 90, 90, 60).x"
        :y2="getVertexCoord(aIdx, radar.length, 90, 90, 60).y"
        class="stroke-slate-800"
        stroke-width="1"
      />
      <!-- 真实数据多边形 -->
      <polygon
        :points="getPolygonPoints(radar, 90, 90, 60)"
        class="fill-emerald-500/30 stroke-emerald-400 transition-all duration-300"
        stroke-width="2"
      />
      <!-- 各顶点小圆点 -->
      <circle
        v-for="(pt, pIdx) in getPointCoords(radar, 90, 90, 60)"
        :key="pIdx"
        :cx="pt.x"
        :cy="pt.y"
        r="3"
        class="fill-emerald-400 stroke-slate-950"
        stroke-width="1"
      />
      <!-- 维度标签文字 -->
      <text
        v-for="(item, tIdx) in (radar || [])"
        :key="'t_' + tIdx"
        :x="getVertexCoord(tIdx, radar.length, 90, 90, 75).x"
        :y="getVertexCoord(tIdx, radar.length, 90, 90, 75).y + 3"
        class="fill-slate-400 text-[9px] font-sans font-medium text-center"
        text-anchor="middle"
      >
        {{ item.subject }}
      </text>
    </svg>
  </div>
</template>

<script setup>
const props = defineProps({
  radar: {
    type: Array,
    default: () => []
  },
  title: {
    type: String,
    default: '六维赛场发挥雷达'
  }
})

const getPolygonPoints = (radar, cx = 90, cy = 90, r = 60, isBackground = false) => {
  if (!radar || !radar.length) return ''
  const n = radar.length
  return radar.map((item, i) => {
    const angle = (i * 2 * Math.PI / n) - (Math.PI / 2)
    const valRadius = isBackground ? r : (Math.max(25, Math.min(100, item.value)) / 100) * r
    const x = cx + valRadius * Math.cos(angle)
    const y = cy + valRadius * Math.sin(angle)
    return `${x.toFixed(1)},${y.toFixed(1)}`
  }).join(' ')
}

const getVertexCoord = (i, n = 6, cx = 90, cy = 90, r = 60) => {
  const angle = (i * 2 * Math.PI / n) - (Math.PI / 2)
  return {
    x: Number((cx + r * Math.cos(angle)).toFixed(1)),
    y: Number((cy + r * Math.sin(angle)).toFixed(1))
  }
}

const getPointCoords = (radar, cx = 90, cy = 90, r = 60) => {
  if (!radar || !radar.length) return []
  const n = radar.length
  return radar.map((item, i) => {
    const angle = (i * 2 * Math.PI / n) - (Math.PI / 2)
    const valRadius = (Math.max(25, Math.min(100, item.value)) / 100) * r
    return {
      x: Number((cx + valRadius * Math.cos(angle)).toFixed(1)),
      y: Number((cy + valRadius * Math.sin(angle)).toFixed(1))
    }
  })
}
</script>
