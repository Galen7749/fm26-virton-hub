<template>
  <div class="space-y-4 p-3.5 animate-in fade-in duration-150 pb-8">

    <!-- ─────────────────────────────────────────────────────────────
         第一层：顶部【关注球队横向切换器】(含国旗、缩写、联赛简称与 +关注更多)
         ───────────────────────────────────────────────────────────── -->
    <section class="space-y-1.5">
      <div class="flex items-center justify-between text-xs text-slate-400 px-1">
        <span class="font-bold text-slate-200 inline-flex items-center gap-1.5">
          <Icon icon="lucide:star" class="w-3.5 h-3.5 text-amber-400 fill-amber-400/20" />
          <span>我关注的球队 ({{ clubs.length }})</span>
        </span>
        <button
          @click="showAddMoreModal = true"
          class="text-[11px] text-emerald-400 hover:text-emerald-300 font-bold inline-flex items-center gap-1 transition bg-emerald-950/60 hover:bg-emerald-900/60 border border-emerald-800/60 px-2 py-0.5 rounded-lg shadow-sm"
        >
          <Icon icon="lucide:plus" class="w-3 h-3" />
          <span>关注更多</span>
        </button>
      </div>

      <!-- 横向球队选择卡片轨道 -->
      <div class="flex items-center space-x-2 overflow-x-auto no-scrollbar py-1">
        <button
          v-for="c in clubs"
          :key="c.id"
          @click="selectedClubId = c.id"
          :class="[
            'px-3 py-2 rounded-xl text-left shrink-0 transition-all border flex items-center space-x-2.5 shadow-sm min-w-[170px]',
            selectedClubId === c.id
              ? 'bg-slate-900 border-emerald-500/80 ring-1 ring-emerald-500/30'
              : 'bg-slate-900/70 border-slate-800 hover:border-slate-700 hover:bg-slate-850'
          ]"
        >
          <!-- 球队标志缩写块 -->
          <div
            class="w-8 h-8 rounded-lg flex items-center justify-center font-black text-xs text-white shadow-inner shrink-0"
            :style="{ backgroundColor: c.badge_bg }"
          >
            {{ c.badge_code }}
          </div>

          <div class="min-w-0 flex-1">
            <div class="flex items-center space-x-1.5">
              <span class="text-xs font-bold text-white truncate">{{ c.name }}</span>
              <Icon :icon="c.country_flag" class="w-3 h-3 rounded-full shrink-0" />
            </div>
            <div class="flex items-center justify-between text-[10px] text-slate-400 mt-0.5">
              <span class="font-mono text-slate-300">{{ c.league_short }}</span>
              <span class="text-emerald-400 font-mono font-bold">{{ c.rank_desc.split(' ')[0] }}</span>
            </div>
          </div>
        </button>
      </div>
    </section>

    <!-- ─────────────────────────────────────────────────────────────
         第二层：中部【俱乐部实时概览名片】(积分排名、现任主帅、身价、近5场战绩走势)
         ───────────────────────────────────────────────────────────── -->
    <section v-if="activeClub" class="bg-gradient-to-br from-slate-900 via-slate-900 to-slate-950 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-3 relative overflow-hidden">
      <!-- 背景光晕装饰 -->
      <div
        class="absolute -top-10 -right-10 w-36 h-36 rounded-full blur-3xl opacity-15 pointer-events-none"
        :style="{ backgroundColor: activeClub.badge_bg }"
      ></div>

      <!-- 俱乐部名称与联赛排名信息行 -->
      <div class="flex items-start justify-between relative z-10">
        <div class="flex items-center space-x-3">
          <div
            class="w-12 h-12 rounded-xl flex items-center justify-center text-base font-black text-white shadow-lg border border-slate-700 shrink-0"
            :style="{ backgroundColor: activeClub.badge_bg }"
          >
            {{ activeClub.badge_code }}
          </div>
          <div>
            <div class="flex items-center space-x-2">
              <h2 class="text-base sm:text-lg font-black text-white tracking-wide">{{ activeClub.name }}</h2>
              <Icon :icon="activeClub.country_flag" class="w-4 h-4 rounded-full" />
            </div>
            <div class="text-[11px] text-slate-400 font-mono">{{ activeClub.name_en }}</div>
            <div class="text-[11px] text-emerald-400 font-bold mt-0.5 inline-flex items-center gap-1">
              <span>{{ activeClub.league_name }}</span>
              <span class="text-slate-500">·</span>
              <span>{{ activeClub.rank_desc }}</span>
            </div>
          </div>
        </div>

        <!-- 关注状态胶囊 -->
        <div class="inline-flex items-center gap-1 bg-amber-950/60 border border-amber-800/60 text-amber-300 text-[10px] font-bold px-2 py-0.5 rounded-full shadow-sm">
          <Icon icon="lucide:star" class="w-3 h-3 fill-amber-400 text-amber-400" />
          <span>已关注</span>
        </div>
      </div>

      <!-- 核心指标网格：主教练、总身价、主场球场、赛季积分概况 -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 border-t border-slate-800/80 text-[11px] relative z-10">
        <!-- 现任主帅 -->
        <div class="bg-slate-950/70 p-2 rounded-xl border border-slate-850">
          <div class="text-[10px] text-slate-500">现任主帅</div>
          <div class="font-bold text-white truncate inline-flex items-center gap-1 mt-0.5">
            <Icon :icon="activeClub.manager_flag" class="w-3 h-3 rounded-full shrink-0" />
            <span class="truncate">{{ activeClub.manager }}</span>
          </div>
        </div>

        <!-- 阵容总身价 -->
        <div class="bg-slate-950/70 p-2 rounded-xl border border-slate-850">
          <div class="text-[10px] text-slate-500">阵容总身价</div>
          <div class="font-bold font-mono text-emerald-400 mt-0.5">{{ activeClub.market_value }}</div>
        </div>

        <!-- 战绩与积分 -->
        <div class="bg-slate-950/70 p-2 rounded-xl border border-slate-850">
          <div class="text-[10px] text-slate-500">联赛积分走势</div>
          <div class="font-bold font-mono text-slate-200 mt-0.5">
            {{ activeClub.stats.won }}胜 {{ activeClub.stats.drawn }}平 {{ activeClub.stats.lost }}负 ({{ activeClub.stats.points }}分)
          </div>
        </div>

        <!-- 主场球场 -->
        <div class="bg-slate-950/70 p-2 rounded-xl border border-slate-850">
          <div class="text-[10px] text-slate-500">主场球场</div>
          <div class="font-bold text-slate-300 truncate mt-0.5" :title="activeClub.stadium">
            {{ activeClub.stadium.split('(')[0] }}
          </div>
        </div>
      </div>

      <!-- 近 5 场走势 (胜/平/负 经典色块) -->
      <div class="flex items-center justify-between text-xs pt-2 border-t border-slate-800/80 relative z-10">
        <span class="text-[11px] text-slate-400 font-medium inline-flex items-center gap-1.5">
          <Icon icon="lucide:trending-up" class="w-3 h-3 text-slate-400" />
          <span>近 5 场战绩走势</span>
        </span>
        <div class="flex items-center space-x-1.5">
          <span
            v-for="(res, ridx) in activeClub.form"
            :key="ridx"
            :class="[
              'w-5 h-5 rounded-md flex items-center justify-center font-bold text-[10px] text-white shadow-sm font-mono',
              res === 'W' ? 'bg-emerald-600' : res === 'D' ? 'bg-slate-600' : 'bg-rose-600'
            ]"
            :title="res === 'W' ? '胜' : res === 'D' ? '平' : '负'"
          >
            {{ res === 'W' ? '胜' : res === 'D' ? '平' : '负' }}
          </span>
        </div>
      </div>
    </section>

    <!-- ─────────────────────────────────────────────────────────────
         第三层：下部【四大核心数据子 Tab】(动态 | 比赛 | 阵容 | 转会)
         ───────────────────────────────────────────────────────────── -->
    <section v-if="activeClub" class="space-y-3">
      <!-- 子 Tab 导航胶囊 -->
      <div class="bg-slate-900 border border-slate-800 p-1 rounded-xl flex items-center space-x-1 text-xs">
        <button
          v-for="sub in subTabs"
          :key="sub.key"
          @click="activeSubTab = sub.key"
          :class="[
            'flex-1 py-1.5 rounded-lg font-bold text-center transition inline-flex items-center justify-center gap-1 text-[11px]',
            activeSubTab === sub.key
              ? 'bg-emerald-600 text-white shadow-sm font-black'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon :icon="sub.icon" class="w-3.5 h-3.5" />
          <span>{{ sub.name }}</span>
        </button>
      </div>

      <!-- ── 子 Tab 1: 【动态】(新闻、公告与社区热帖) ───────────── -->
      <div v-if="activeSubTab === 'dynamics'" class="space-y-2.5">
        <article
          v-for="dyn in activeClub.dynamics"
          :key="dyn.id"
          class="bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-slate-700 rounded-xl p-3.5 space-y-2 transition shadow-sm"
        >
          <div class="flex items-center justify-between text-[10px]">
            <span
              :class="[
                'px-1.5 py-0.2 rounded font-bold border text-[9px]',
                dyn.type === 'notice'
                  ? 'bg-amber-950 text-amber-300 border-amber-800'
                  : dyn.type === 'community'
                  ? 'bg-sky-950 text-sky-300 border-sky-800'
                  : 'bg-emerald-950 text-emerald-300 border-emerald-800'
              ]"
            >
              {{ dyn.tag }}
            </span>
            <span class="text-slate-500 font-mono">{{ dyn.date }}</span>
          </div>

          <h3 class="text-xs sm:text-sm font-bold text-slate-100 leading-snug">
            {{ dyn.title }}
          </h3>

          <p class="text-[11px] text-slate-400 leading-relaxed">
            {{ dyn.summary }}
          </p>

          <div class="flex items-center justify-between text-[10px] text-slate-500 pt-1 border-t border-slate-800/60">
            <span class="inline-flex items-center gap-1">
              <Icon icon="lucide:newspaper" class="w-3 h-3 text-slate-400" />
              <span>来源: {{ dyn.source }}</span>
            </span>
            <span class="text-emerald-400 font-medium">查看详情 →</span>
          </div>
        </article>
      </div>

      <!-- ── 子 Tab 2: 【比赛】(已完赛记录 + 接下来 3 场赛程预告) ──── -->
      <div v-else-if="activeSubTab === 'matches'" class="space-y-3.5">
        <!-- 1. 已完赛赛果 -->
        <div class="space-y-2">
          <div class="text-xs font-bold text-slate-300 px-1 inline-flex items-center gap-1.5">
            <Icon icon="lucide:check-circle" class="w-3.5 h-3.5 text-emerald-400" />
            <span>已完赛记录 ({{ activeClub.matches.completed.length }} 场)</span>
          </div>

          <div
            v-for="m in activeClub.matches.completed"
            :key="'comp-' + m.id"
            class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-2 shadow-sm"
          >
            <div class="flex items-center justify-between text-[10px] text-slate-400 pb-1.5 border-b border-slate-800/80">
              <span class="font-bold text-slate-300">{{ m.round_label }}</span>
              <span class="font-mono">{{ m.date }}</span>
            </div>

            <div class="flex items-center justify-between py-1">
              <div class="flex-1 text-right font-bold text-xs text-white truncate pr-2">
                {{ m.home_team }}
              </div>
              <div class="px-3 py-1 bg-slate-950 rounded-lg border border-slate-800 text-center font-mono font-black text-sm tracking-wider text-white">
                {{ m.score_home }} - {{ m.score_away }}
              </div>
              <div class="flex-1 text-left font-bold text-xs text-white truncate pl-2">
                {{ m.away_team }}
              </div>
            </div>

            <!-- 进球速递 -->
            <div v-if="m.scorers" class="text-[10px] text-slate-400 bg-slate-950/80 p-1.5 rounded border border-slate-850 inline-flex items-center gap-1.5 w-full truncate">
              <Icon icon="ph:soccer-ball-fill" class="w-3 h-3 text-emerald-400 shrink-0" />
              <span class="truncate">{{ m.scorers }}</span>
            </div>
          </div>
        </div>

        <!-- 2. 接下来 3 场赛程预告 -->
        <div class="space-y-2 pt-2">
          <div class="text-xs font-bold text-slate-300 px-1 inline-flex items-center gap-1.5">
            <Icon icon="lucide:calendar-clock" class="w-3.5 h-3.5 text-amber-400" />
            <span>未来赛程预告 (接下来 3 场)</span>
          </div>

          <div
            v-for="up in activeClub.matches.upcoming"
            :key="'up-' + up.id"
            class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-2 shadow-sm"
          >
            <div class="flex items-center justify-between text-[10px]">
              <span class="font-bold text-slate-300">{{ up.round_label }}</span>
              <span class="text-amber-400 font-mono font-bold">{{ up.date }}</span>
            </div>

            <div class="flex items-center justify-between py-1.5">
              <div class="flex-1 text-right font-bold text-xs text-white truncate pr-2">
                {{ up.home_team }}
              </div>
              <div class="px-2.5 py-0.5 bg-slate-950 rounded border border-slate-800 text-[10px] text-slate-400 font-bold">
                VS
              </div>
              <div class="flex-1 text-left font-bold text-xs text-white truncate pl-2">
                {{ up.away_team }}
              </div>
            </div>

            <div class="flex items-center justify-between text-[10px] text-slate-400 bg-slate-950/60 px-2 py-1 rounded border border-slate-850">
              <span class="inline-flex items-center gap-1 truncate">
                <Icon icon="lucide:map-pin" class="w-2.5 h-2.5 text-slate-500" />
                <span class="truncate">{{ up.stadium }}</span>
              </span>
              <span class="text-emerald-400 font-bold shrink-0">{{ up.note }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ── 子 Tab 3: 【阵容】(按位置分组、国籍、出场、进球助攻、评分与合同状态) ── -->
      <div v-else-if="activeSubTab === 'squad'" class="space-y-2.5">
        <!-- 位置筛选胶囊 -->
        <div class="flex items-center space-x-1 overflow-x-auto no-scrollbar py-0.5 text-xs">
          <button
            v-for="pos in positionFilters"
            :key="pos.key"
            @click="selectedPositionFilter = pos.key"
            :class="[
              'px-2.5 py-1 rounded-lg text-[11px] font-bold shrink-0 transition',
              selectedPositionFilter === pos.key
                ? 'bg-slate-800 text-emerald-400 border border-emerald-500/50'
                : 'text-slate-400 hover:text-white bg-slate-900 border border-slate-850'
            ]"
          >
            {{ pos.label }}
          </button>
        </div>

        <!-- 球员详细列表 (表格卡片视觉) -->
        <div class="space-y-1.5">
          <div
            v-for="player in filteredSquad"
            :key="player.number + player.name"
            class="bg-slate-900 hover:bg-slate-850 border border-slate-800 rounded-xl p-2.5 flex items-center justify-between gap-2 shadow-sm transition"
          >
            <!-- 左侧：号码、姓名、年龄、国籍、位置 -->
            <div class="flex items-center space-x-2.5 min-w-0 flex-1">
              <!-- 号码 -->
              <span class="w-6 h-6 rounded-md bg-slate-950 border border-slate-800 flex items-center justify-center font-mono font-black text-xs text-slate-300 shrink-0">
                {{ player.number }}
              </span>

              <!-- 姓名与基础信息 -->
              <div class="min-w-0 flex-1">
                <div class="flex items-center space-x-1.5">
                  <span class="text-xs font-bold text-white truncate">{{ player.name_zh || player.name }}</span>
                  <Icon :icon="player.flag" class="w-3 h-3 rounded-full shrink-0" />
                </div>
                <div class="flex items-center space-x-2 text-[10px] text-slate-400 mt-0.5 font-mono">
                  <span class="text-slate-300 font-bold px-1 py-0.2 bg-slate-950 rounded text-[9px]">
                    {{ player.position }}
                  </span>
                  <span>{{ player.age }}岁</span>
                  <span>到期: {{ player.contract_until }}</span>
                </div>
              </div>
            </div>

            <!-- 右侧：出场/数据、场均评分、身价 -->
            <div class="flex items-center space-x-3 shrink-0 text-right">
              <!-- 进球与助攻 -->
              <div class="text-[10px] text-slate-400 font-mono">
                <div>{{ player.apps }} 场</div>
                <div class="font-bold text-slate-300">{{ player.goals }}球 {{ player.assists }}助</div>
              </div>

              <!-- 场均评分 (>= 7.0 亮绿高亮) -->
              <div class="w-10 text-center">
                <div class="text-[9px] text-slate-500">评分</div>
                <div
                  :class="[
                    'text-xs font-mono font-black',
                    parseFloat(player.rating) >= 7.0
                      ? 'text-emerald-400 bg-emerald-950/80 px-1 rounded border border-emerald-800/80'
                      : 'text-slate-300'
                  ]"
                >
                  {{ player.rating }}
                </div>
              </div>

              <!-- 身价 -->
              <div class="w-14 text-right">
                <div class="text-[9px] text-slate-500">身价</div>
                <div class="text-xs font-mono font-bold text-slate-300">{{ player.market_value }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ── 子 Tab 4: 【转会】(转入 In 与 转出 Out 列表) ───────── -->
      <div v-else-if="activeSubTab === 'transfers'" class="space-y-3.5">
        <!-- 转入 In -->
        <div class="space-y-2">
          <div class="text-xs font-bold text-emerald-400 px-1 inline-flex items-center gap-1.5">
            <Icon icon="lucide:arrow-down-left" class="w-3.5 h-3.5" />
            <span>新赛季转入球员 (In · {{ activeClub.transfers.in.length }})</span>
          </div>

          <div
            v-for="(t, tidx) in activeClub.transfers.in"
            :key="'in-' + tidx"
            class="bg-slate-900 border border-slate-800 rounded-xl p-3 flex items-center justify-between text-xs shadow-sm"
          >
            <div>
              <div class="font-bold text-white text-xs flex items-center space-x-1.5">
                <span>{{ t.player }}</span>
                <span class="text-[9px] font-mono bg-slate-950 text-slate-400 px-1 py-0.2 rounded border border-slate-850">
                  {{ t.pos }} · {{ t.age }}岁
                </span>
              </div>
              <div class="text-[10px] text-slate-400 mt-0.5">
                原俱乐部: <span class="text-slate-300 font-bold">{{ t.from }}</span>
              </div>
            </div>

            <div class="text-right">
              <span class="text-xs font-mono font-bold text-emerald-400 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-900">
                {{ t.fee }}
              </span>
              <div class="text-[9px] text-slate-500 font-mono mt-0.5">{{ t.date }}</div>
            </div>
          </div>
        </div>

        <!-- 转出 Out -->
        <div class="space-y-2 pt-2">
          <div class="text-xs font-bold text-rose-400 px-1 inline-flex items-center gap-1.5">
            <Icon icon="lucide:arrow-up-right" class="w-3.5 h-3.5" />
            <span>离队 / 转出球员 (Out · {{ activeClub.transfers.out.length }})</span>
          </div>

          <div
            v-for="(t, tidx) in activeClub.transfers.out"
            :key="'out-' + tidx"
            class="bg-slate-900 border border-slate-800 rounded-xl p-3 flex items-center justify-between text-xs shadow-sm"
          >
            <div>
              <div class="font-bold text-white text-xs flex items-center space-x-1.5">
                <span>{{ t.player }}</span>
                <span class="text-[9px] font-mono bg-slate-950 text-slate-400 px-1 py-0.2 rounded border border-slate-850">
                  {{ t.pos }} · {{ t.age }}岁
                </span>
              </div>
              <div class="text-[10px] text-slate-400 mt-0.5">
                新去向: <span class="text-slate-300 font-bold">{{ t.to }}</span>
              </div>
            </div>

            <div class="text-right">
              <span class="text-xs font-mono font-bold text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-900">
                {{ t.fee }}
              </span>
              <div class="text-[9px] text-slate-500 font-mono mt-0.5">{{ t.date }}</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ─────────────────────────────────────────────────────────────
         关注更多弹窗 (轻量交互，维持真实大众 App 体验)
         ───────────────────────────────────────────────────────────── -->
    <div
      v-if="showAddMoreModal"
      class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 animate-in fade-in"
      @click.self="showAddMoreModal = false"
    >
      <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-sm w-full p-4 space-y-3.5 shadow-2xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div class="font-bold text-white text-sm inline-flex items-center gap-1.5">
            <Icon icon="lucide:plus-circle" class="w-4 h-4 text-emerald-400" />
            <span>添加关注球队</span>
          </div>
          <button @click="showAddMoreModal = false" class="text-slate-400 hover:text-white">
            <Icon icon="lucide:x" class="w-4 h-4" />
          </button>
        </div>

        <p class="text-xs text-slate-300 leading-relaxed">
          您当前已关注核心追踪主队：<strong class="text-white">奥波莱奥德拉</strong> 与 <strong class="text-white">维尔通精英</strong>。
        </p>
        <p class="text-[11px] text-slate-400 leading-relaxed bg-slate-950 p-2.5 rounded-xl border border-slate-850">
          欧洲五大联赛及其他主要联赛的球队关注与个性化订阅推送功能将在后续版本全面开放，敬请期待！
        </p>

        <div class="flex justify-end pt-2">
          <button
            @click="showAddMoreModal = false"
            class="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-bold transition"
          >
            知道了
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import followedClubsRaw from '../../data/followed_clubs.json'

const clubs = ref(followedClubsRaw)
const selectedClubId = ref(clubs.value[0]?.id || 'odra')
const showAddMoreModal = ref(false)

const activeClub = computed(() => {
  return clubs.value.find(c => c.id === selectedClubId.value) || clubs.value[0]
})

// 4 大核心数据子 Tab
const subTabs = [
  { key: 'dynamics', name: '动态', icon: 'lucide:rss' },
  { key: 'matches', name: '比赛', icon: 'mdi:scoreboard-outline' },
  { key: 'squad', name: '阵容', icon: 'lucide:users' },
  { key: 'transfers', name: '转会', icon: 'tabler:arrows-exchange' }
]

const activeSubTab = ref('dynamics')

// 阵容位置筛选
const positionFilters = [
  { key: 'all', label: '全队名单' },
  { key: 'GK', label: '门将' },
  { key: 'DF', label: '后卫' },
  { key: 'MF', label: '中场' },
  { key: 'FW', label: '前锋' }
]

const selectedPositionFilter = ref('all')

const filteredSquad = computed(() => {
  if (!activeClub.value || !activeClub.value.squad) return []
  if (selectedPositionFilter.value === 'all') {
    return activeClub.value.squad
  }
  return activeClub.value.squad.filter(p => p.position === selectedPositionFilter.value)
})
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
