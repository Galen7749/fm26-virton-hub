<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 flex flex-col items-center select-none">
    
    <!-- 主视口容器 (限制移动端最大宽度 448px) -->
    <main class="w-full max-w-md bg-slate-950 min-h-screen flex flex-col pb-20 shadow-2xl relative">

      <!-- 1. 公域 Header (去重复入口，只保留媒体身份与赛季状态) -->
      <AppHeader
        :clubName="currentClub.name"
        :seasonLabel="currentSeason.label"
        :leagueName="currentClub.league_short"
      />

      <!-- 2. 主视图容器 (直接展示内容，杜绝双层导航栏) -->
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

        <!-- 模块 D: 🔥 球迷热议广场 (所有比赛总评 + 场外日常与转会吃瓜) -->
        <FanCommunity
          v-else-if="activeTab === 'community'"
          :communityData="community"
        />

        <!-- 模块 E: 💼 主帅信箱 (私域主帅工作台页面，非弹窗) -->
        <ManagerMailbox
          v-else-if="activeTab === 'mailbox'"
          :mailbox="mailbox"
        />
      </div>

      <!-- 3. 底部常驻导航条 (唯一全局导航：比赛 / 战术 / 榜单 / 信箱) -->
      <BottomNav
        :activeTab="activeTab"
        @update:activeTab="changeTab"
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
import FanCommunity from './components/community/FanCommunity.vue'

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
import communityData from './data/community.json'

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
const community = ref(communityData)

// 多赛季/多俱乐部上下文支持
const currentClub = computed(() => {
  return career.value.clubs.find(c => c.id === career.value.current_club_id) || career.value.clubs[0]
})

const currentSeason = computed(() => {
  return currentClub.value.seasons.find(s => s.id === career.value.current_season) || currentClub.value.seasons[0]
})

// 全局主导航 Tab (当前选中：'matches' | 'tactics' | 'standings')
const activeTab = ref('matches')

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
}
</script>
