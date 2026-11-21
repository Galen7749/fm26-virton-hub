<template>
  <div class="w-full bg-slate-950 rounded-xl p-3 border border-slate-850 space-y-2 relative">
    <!-- 图表顶栏说明 -->
    <div class="flex items-center justify-between text-xs">
      <div class="flex items-center space-x-1.5">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span class="font-bold text-slate-200 text-[11px]">8轮战术执教评分趋势跟踪</span>
      </div>
      <div class="flex items-center space-x-2 text-[10px] text-slate-400 font-mono">
        <span class="flex items-center space-x-1">
          <span class="w-2 h-0.5 bg-emerald-400 inline-block"></span>
          <span>评分曲线</span>
        </span>
        <span class="text-amber-400">最高 9.9</span>
      </div>
    </div>

    <!-- Canvas 视口 -->
    <div class="w-full h-44 relative">
      <canvas ref="canvasRef"></canvas>
    </div>

    <!-- 底部辅助说明 -->
    <div class="flex items-center justify-between text-[9px] text-slate-500 font-sans pt-1 border-t border-slate-900">
      <span>轻触数据点可查看该场对阵详情与虎扑评分</span>
      <span class="text-emerald-400 font-bold">第8轮创赛季新高 ★</span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import {
  Chart,
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Tooltip,
  Filler
} from 'chart.js'

Chart.register(
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Tooltip,
  Filler
)

const props = defineProps({
  scores: {
    type: Array,
    required: true
  }
})

const canvasRef = ref(null)
let chartInstance = null

const initChart = () => {
  if (!canvasRef.value) return
  if (chartInstance) {
    chartInstance.destroy()
  }

  const ctx = canvasRef.value.getContext('2d')

  // 创建渐变填充背景 (Emerald Green Gradient)
  const gradient = ctx.createLinearGradient(0, 0, 0, 160)
  gradient.addColorStop(0, 'rgba(16, 185, 129, 0.45)')
  gradient.addColorStop(0.7, 'rgba(16, 185, 129, 0.08)')
  gradient.addColorStop(1, 'rgba(16, 185, 129, 0.0)')

  const labels = props.scores.map(s => `第${s.round}轮`)
  const data = props.scores.map(s => s.score)

  // 区分特定高亮点
  const pointBgColors = props.scores.map(s => {
    if (s.score >= 9.8) return '#fbbf24' // 琥珀金 (最高分)
    if (s.score < 7.0) return '#f43f5e'  // 玫瑰红 (失利场次)
    return '#34d399'                     // 翡翠绿
  })

  const pointBorderColors = props.scores.map(s => {
    if (s.score >= 9.8) return '#fff'
    if (s.score < 7.0) return '#fff'
    return '#064e3b'
  })

  chartInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: '主帅评分',
          data: data,
          borderColor: '#10b981',
          borderWidth: 2.5,
          backgroundColor: gradient,
          fill: true,
          tension: 0.35, // 优雅的贝塞尔平滑曲线
          pointBackgroundColor: pointBgColors,
          pointBorderColor: pointBorderColors,
          pointBorderWidth: 1.5,
          pointRadius: 4.5,
          pointHoverRadius: 7,
          pointHoverBackgroundColor: '#10b981',
          pointHoverBorderColor: '#fff',
          pointHoverBorderWidth: 2
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          backgroundColor: 'rgba(15, 23, 42, 0.95)',
          titleColor: '#e2e8f0',
          titleFont: { size: 11, weight: 'bold' },
          bodyColor: '#34d399',
          bodyFont: { size: 12, weight: 'bold', family: 'monospace' },
          borderColor: 'rgba(51, 65, 85, 0.8)',
          borderWidth: 1,
          padding: 8,
          displayColors: false,
          callbacks: {
            title: (items) => {
              const idx = items[0].dataIndex
              const s = props.scores[idx]
              return `第 ${s.round} 轮 · ${s.fixture} (${s.badge})`
            },
            label: (item) => {
              return `★ 主帅执教评分: ${item.raw} 分 / 10`
            }
          }
        }
      },
      scales: {
        x: {
          grid: {
            display: false,
            drawBorder: false
          },
          ticks: {
            color: '#94a3b8',
            font: {
              size: 10
            }
          }
        },
        y: {
          min: 6.0,
          max: 10.0,
          grid: {
            color: 'rgba(255, 255, 255, 0.05)',
            drawBorder: false
          },
          ticks: {
            stepSize: 1.0,
            color: '#64748b',
            font: {
              size: 9,
              family: 'monospace'
            },
            callback: (val) => `${val}分`
          }
        }
      }
    }
  })
}

onMounted(() => {
  initChart()
})

onBeforeUnmount(() => {
  if (chartInstance) {
    chartInstance.destroy()
  }
})

watch(() => props.scores, () => {
  initChart()
}, { deep: true })
</script>
