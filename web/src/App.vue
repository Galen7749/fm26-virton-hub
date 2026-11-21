<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 flex flex-col items-center select-none">
    
    <!-- 主视口容器 (限制移动端最大宽度 448px) -->
    <main class="w-full max-w-md bg-slate-950 min-h-screen flex flex-col pb-20 shadow-2xl relative">

      <!-- 1. 公域 Header (支持多俱乐部、多赛季无缝切换展示) -->
      <AppHeader
        :clubName="currentClub.name"
        :seasonLabel="currentSeason.label"
        :leagueName="currentClub.league_short"
        @open-mailbox="showMailbox = true"
      />

      <!-- 2. 全局主导航 Tab (比赛大盘 / 球队战术 / 榜单大盘) -->
      <nav class="flex border-b border-slate-800 bg-slate-900 sticky top-14 z-20 overflow-x-auto no-scrollbar scroll-smooth">
        <button
          v-for="tab in mainTabs"
          :key="tab.key"
          @click="changeTab(tab.key)"
          :class="[
            'flex-1 py-2.5 text-xs font-medium text-center relative transition-colors whitespace-nowrap',
            activeTab === tab.key
              ? 'text-emerald-400 font-bold'
              : 'text-slate-400 hover:text-slate-200'
          ]"
        >
          <span>{{ tab.label }}</span>
          <span
            v-if="activeTab === tab.key"
            class="absolute bottom-0 left-4 right-4 h-0.5 bg-emerald-500 rounded-full"
          ></span>
        </button>
      </nav>

      <!-- 3. 主视图容器 -->
      <div class="flex-1">
        <!-- 模块 A: ⚽ 比赛大盘 (二级导航：列表瀑布流 vs 单场深度详情) -->
        <template v-if="activeTab === 'matches'">
          <!-- 一级：赛程赛果列表 -->
          <MatchList
            v-if="!selectedMatchId"
            :matches="matches"
            :worldNews="worldNews"
            :seasonLabel="currentSeason.label"
            @select-match="onSelectMatch"
          />

          <!-- 二级：比赛专属详情页 (2D战术板 + 懂球帝战报 + 虎扑热评 + 同轮完整赛果) -->
          <MatchDetail
            v-else
            :match="selectedMatch"
            :allMatches="matches"
            :news="selectedNews"
            :roundOtherMatches="selectedRoundOtherMatches"
            @back="selectedMatchId = null"
            @switch-match="onSwitchMatch"
          />
        </template>

        <!-- 模块 B: 📊 球队战术体系 (哲学架构 + 攻防走廊 + 技战术雷达 + 专栏点评) -->
        <TeamTactics
          v-else-if="activeTab === 'tactics'"
          :teamAnalysis="teamAnalysis"
          :clubName="currentClub.name"
        />

        <!-- 模块 C: 🏆 榜单大盘 (七大联赛积分榜 + 比乙射手榜 + 助攻榜 + 纪律榜) -->
        <StandingsBoard
          v-else-if="activeTab === 'standings'"
          :availableLeagues="availableLeagues"
          :leaderboards="leaderboards"
        />
      </div>

      <!-- 4. 底部常驻导航条 -->
      <BottomNav
        :activeTab="activeTab"
        @update:activeTab="changeTab"
        @open-mailbox="showMailbox = true"
      />

      <!-- 5. 私域主帅信箱弹窗 (严格隔离第四面墙) -->
      <ManagerMailbox
        v-if="showMailbox"
        :mailbox="mailbox"
        @close="showMailbox = false"
      />

    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// 模块化子组件导入
import AppHeader from './components/layout/AppHeader.vue'
import BottomNav from './components/layout/BottomNav.vue'
import ManagerMailbox from './components/layout/ManagerMailbox.vue'

import MatchList from './components/matches/MatchList.vue'
import MatchDetail from './components/matches/MatchDetail.vue'

import TeamTactics from './components/tactics/TeamTactics.vue'
import StandingsBoard from './components/standings/StandingsBoard.vue'

// 数据导入
import careerData from './data/career.json'
import matchesData from './data/matches.json'
import newsData from './data/news.json'
import multiLeaguesData from './data/standings.json'
import mailboxData from './data/mailbox.json'
import roundMatchesData from './data/round_matches.json'
import worldNewsData from './data/world_news.json'
import teamAnalysisData from './data/team_analysis.json'
import leaderboardsData from './data/leaderboards.json'

// 响应式数据
const career = ref(careerData)
const matches = ref(matchesData)
const news = ref(newsData)
const mailbox = ref(mailboxData)
const roundMatches = ref(roundMatchesData)
const worldNews = ref(worldNewsData)
const availableLeagues = ref(multiLeaguesData.leagues || [])
const teamAnalysis = ref(teamAnalysisData)
const leaderboards = ref(leaderboardsData)

// 多赛季/多俱乐部上下文支持 (未来扩展只需切换 career.json 对应数据)
const currentClub = computed(() => {
  return career.value.clubs.find(c => c.id === career.value.current_club_id) || career.value.clubs[0]
})

const currentSeason = computed(() => {
  return currentClub.value.seasons.find(s => s.id === career.value.current_season) || currentClub.value.seasons[0]
})

// 全局主导航 Tab
const activeTab = ref('matches')
const mainTabs = [
  { key: 'matches', label: '⚽ 赛程赛果' },
  { key: 'tactics', label: '📊 球队战术' },
  { key: 'standings', label: '🏆 榜单大盘' }
]

// 二级页面状态：选中的比赛 ID (null 表示展示列表瀑布流，有 ID 则进入单场二级详情)
const selectedMatchId = ref(null)

// 选中的单场比赛与新闻数据
const selectedMatch = computed(() => {
  if (!selectedMatchId.value) return null
  return matches.value.find(m => m.id === selectedMatchId.value) || matches.value[0]
})

const selectedNews = computed(() => {
  if (!selectedMatch.value) return null
  return news.value.find(n => n.round === selectedMatch.value.round || n.match_id === selectedMatch.value.id)
})

const selectedRoundOtherMatches = computed(() => {
  if (!selectedMatch.value) return []
  return roundMatches.value[String(selectedMatch.value.round)] || []
})

// 私域主帅信箱显示状态
const showMailbox = ref(false)

// 交互操作
const onSelectMatch = (matchId) => {
  selectedMatchId.value = matchId
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const onSwitchMatch = (matchId) => {
  if (matchId) {
    selectedMatchId.value = matchId
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

const changeTab = (tabKey) => {
  activeTab.value = tabKey
  // 如果切换出 matches，重置二级详情或保留
}
</script>
