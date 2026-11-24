<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 flex flex-col items-center select-none font-sans">
    
    <!-- 主手机/应用容器（对标 FotMob / 懂球帝，最大宽度 448px 居中渲染） -->
    <main class="w-full max-w-md bg-slate-950 min-h-screen flex flex-col pb-20 shadow-2xl relative">

      <!-- 1. 全局 Header（品牌「懂球云」、搜索栏、低调主帅手机入口） -->
      <AppHeader
        :activeTab="activeTab"
        @change-tab="changeTab"
        @open-phone="isPhoneOpen = true"
      />

      <!-- 2. 四大一级页面内容区 (资讯 | 比赛 | 社区 | 数据) -->
      <div class="flex-1">
        <!-- Tab 1: 【资讯】页（默认首页：焦点横滑比分 + 头条/留洋/转会胶囊 + 详情阅读Modal） -->
        <NewsHome
          v-if="activeTab === 'news'"
          :matches="matches"
          @select-match="onSelectMatch"
        />

        <!-- Tab 2: 【比赛】页 (顶部中立轮次/联赛下拉 + 中立比分列表 + 详情页子Tab) -->
        <template v-else-if="activeTab === 'matches'">
          <!-- 比赛列表瀑布流 (使用 v-show 确保进入比赛详情后再返回时，保留用户先前的联赛与轮次筛选选项) -->
          <MatchList
            v-show="!selectedMatchId"
            :matches="matches"
            @select-match="onSelectMatch"
          />

          <!-- 比赛详情页 (战报 | 赛况/阵容评分 | 热评 | 同轮赛果) -->
          <MatchDetail
            v-if="selectedMatchId"
            :match="selectedMatch"
            :allMatches="matches"
            :news="selectedNews"
            :roundOtherMatches="selectedRoundOtherMatches"
            :backText="backButtonText"
            @back="handleBackFromMatch"
            @switch-match="onSwitchMatch"
          />
        </template>

        <!-- Tab 3: 【关注】页 (追踪当前与历史主队全维度数据：动态 | 比赛 | 阵容 | 转会) -->
        <FollowedClubs
          v-else-if="activeTab === 'followed'"
          @select-match="onSelectMatch"
        />

        <!-- Tab 4: 【社区】页 (虎扑经典热帖流：热门/最新切换 + 亮评互动) -->
        <FanCommunity
          v-else-if="activeTab === 'community'"
          @select-match="onSelectMatch"
        />

        <!-- Tab 5: 【数据】页 (顶部左侧联赛下拉选择器 + 顶部右侧：积分榜 / 射手/助攻榜 / 转会动态) -->
        <StandingsBoard
          v-else-if="activeTab === 'standings'"
        />
      </div>

      <!-- 3. 底部固定 Tab Bar（严格限制为 4 个一级 Tab，移动端与桌面端统一体验） -->
      <BottomNav
        :activeTab="activeTab"
        @update:activeTab="changeTab"
      />

      <!-- 4. 隐藏式「主帅私人手机模拟器」Drawer/Modal (点击顶栏手机图标呼出，完全脱离公开媒体流) -->
      <PhoneDrawer
        :isOpen="isPhoneOpen"
        @close="isPhoneOpen = false"
      />

    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// 模块化子组件导入
import AppHeader from './components/layout/AppHeader.vue'
import BottomNav from './components/layout/BottomNav.vue'
import PhoneDrawer from './components/layout/PhoneDrawer.vue'

import NewsHome from './components/news/NewsHome.vue'
import MatchList from './components/matches/MatchList.vue'
import MatchDetail from './components/matches/MatchDetail.vue'
import FollowedClubs from './components/followed/FollowedClubs.vue'
import FanCommunity from './components/community/FanCommunity.vue'
import StandingsBoard from './components/standings/StandingsBoard.vue'

// 数据文件
import allMatchesRaw from './data/all_matches.json'
import seasonsMetaRaw from './data/seasons_meta.json'

// ── 全局一级导航状态：标准 5 栏结构 (资讯 | 比赛 | 关注 | 社区 | 数据)，默认首页为 'news' ──────
const activeTab = ref('news') // 'news' | 'matches' | 'followed' | 'community' | 'standings'
const isPhoneOpen = ref(false)
const selectedMatchId = ref(null)

// ── 赛季底层数据同步加载（用于比乙维尔通历史比赛与战报匹配）──────
const allSeasonFiles = import.meta.glob('./data/season_*/*.json', { eager: true })

function getSeasonData(seasonId, fileName) {
  const key = `./data/season_${seasonId}/${fileName}.json`
  const mod = allSeasonFiles[key]
  return mod ? (mod.default ?? mod) : null
}

const matches      = ref([])
const news         = ref([])
const roundMatches = ref({})

function loadBaseData() {
  // 载入历史完整比赛数据以支持详情页点击展开
  matches.value      = getSeasonData(1, 'matches') || []
  news.value         = getSeasonData(1, 'news') || []
  roundMatches.value = getSeasonData(1, 'round_matches') || {}
}

loadBaseData()

// ── 单场详情匹配计算属性 ────────────────────────────────────
const selectedMatch = computed(() => {
  if (!selectedMatchId.value) return null
  const fromAll = allMatchesRaw.find(m => m.id === selectedMatchId.value)
  if (fromAll) return fromAll
  return matches.value.find(m => m.id === selectedMatchId.value) || allMatchesRaw[0]
})

const selectedNews = computed(() => {
  if (!selectedMatch.value) return null
  if (selectedMatch.value.news) return selectedMatch.value.news
  const isVirtonMatch = selectedMatch.value.league_key === 'bel_d2' ||
                        selectedMatch.value.home_team?.includes('维尔通') ||
                        selectedMatch.value.away_team?.includes('维尔通')
  if (isVirtonMatch) {
    return news.value.find(n => n.match_id === selectedMatch.value.id || n.round === selectedMatch.value.round)
  }
  return null
})

const selectedRoundOtherMatches = computed(() => {
  if (!selectedMatch.value) return []
  if (roundMatches.value[String(selectedMatch.value.round)]) {
    return roundMatches.value[String(selectedMatch.value.round)]
  }
  return allMatchesRaw.filter(m => m.league_key === selectedMatch.value.league_key && m.id !== selectedMatch.value.id)
})

// ── 导航历史与返回上一级支持 ────────────────────────────────
const previousTab = ref(null)

const backButtonText = computed(() => {
  if (previousTab.value === 'news') return '返回资讯'
  if (previousTab.value === 'followed') return '返回关注'
  if (previousTab.value === 'community') return '返回社区'
  return '返回比赛列表'
})

// ── 交互导航 ────────────────────────────────────────────────
const changeTab = (tabKey) => {
  activeTab.value = tabKey
  selectedMatchId.value = null
  previousTab.value = null // 用户指示：“tab之间跳可以不保存”
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const onSelectMatch = (matchId) => {
  // 记录来源上一级 Tab，以便详情页点击返回时能准确回到上一级
  previousTab.value = activeTab.value
  activeTab.value = 'matches'
  selectedMatchId.value = matchId
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const handleBackFromMatch = () => {
  selectedMatchId.value = null
  if (previousTab.value && previousTab.value !== 'matches') {
    activeTab.value = previousTab.value
    previousTab.value = null
  }
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const onSwitchMatch = (matchId) => {
  if (matchId) {
    selectedMatchId.value = matchId
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}
</script>
