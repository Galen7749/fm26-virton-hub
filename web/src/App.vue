<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 flex flex-col items-center select-none">
    
    <!-- 主口袋容器（限制移动端最大宽度 448px） -->
    <main class="w-full max-w-md bg-slate-950 min-h-screen flex flex-col pb-20 shadow-2xl relative">

      <!-- 1. 全局 Header（含赛季切换器） -->
      <AppHeader
        :clubName="currentClub.name"
        :seasonLabel="activeSeason.label"
        :leagueName="activeSeason.league_short"
        :seasons="seasonsMeta.seasons"
        :activeSeasonId="activeSeasonId"
        @switch-season="onSwitchSeason"
      />

      <!-- 加载过渡态 -->
      <div v-if="isLoading" class="flex-1 flex items-center justify-center">
        <div class="text-center space-y-2">
          <div class="text-2xl animate-spin">⚽</div>
          <div class="text-xs text-slate-400">加载赛季数据中...</div>
        </div>
      </div>

      <!-- 2. 主图内容区（直接展示内容，杜绝双层导航栏） -->
      <div v-else class="flex-1">
        <!-- 模块 A: ⚽ 比赛大盘 (二级导航：列表瀑布流 vs 单场深度详情) -->
        <template v-if="activeTab === 'matches'">
          <!-- 一级：赛程赛果列表 -->
          <MatchList
            v-if="!selectedMatchId"
            :matches="matches"
            :worldNews="worldNews"
            :seasonLabel="activeSeason.label"
            @select-match="onSelectMatch"
          />

          <!-- 二级：比赛专属详情页 (2D战术棒 + 懂球帝战报 + 虎扑热评 + 同轮完整赛果) -->
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

        <!-- 模块 B: 📊 球队战术体系 (哲学架构 + 攻防走今 + 技战术雷达 + 专栏点评) -->
        <TeamTactics
          v-else-if="activeTab === 'tactics'"
          :teamAnalysis="teamAnalysis"
          :squad="squad"
          :clubName="currentClub.name"
        />

        <!-- 模块 C: 🥇 榜单大盘 (七大联赛积分榜 + 比乙射手榜 + 助攻榜 + 纪律榜) -->
        <StandingsBoard
          v-else-if="activeTab === 'standings'"
          :availableLeagues="availableLeagues"
          :leaderboards="leaderboards"
        />

        <!-- 模块 D: 🔥 球迷热情广场 (所有比赛总评 + 场外日常与转会球评) -->
        <FanCommunity
          v-else-if="activeTab === 'community'"
          :communityData="community"
          :newsList="news"
          :matchesList="matches"
          @select-match="onCommunitySelectMatch"
        />

        <!-- 模块 E: 📬 主监信箱 (私域主监工作台页面，非弹窗) -->
        <ManagerMailbox
          v-else-if="activeTab === 'mailbox'"
          :mailbox="mailbox"
        />
      </div>

      <!-- 3. 底部常驻导航条（唯一全局导航：比赛 / 战术 / 榜单 / 信箱） -->
      <BottomNav
        :activeTab="activeTab"
        @update:activeTab="changeTab"
      />

    </main>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

// 模块化子组件导入
import AppHeader from './components/layout/AppHeader.vue'
import BottomNav from './components/layout/BottomNav.vue'
import ManagerMailbox from './components/layout/ManagerMailbox.vue'

import MatchList from './components/matches/MatchList.vue'
import MatchDetail from './components/matches/MatchDetail.vue'

import TeamTactics from './components/tactics/TeamTactics.vue'
import StandingsBoard from './components/standings/StandingsBoard.vue'
import FanCommunity from './components/community/FanCommunity.vue'

// 静态导入：赛季元数据（轻量，始终加载）
import seasonsMetaRaw from './data/seasons_meta.json'

// ── 赛季切换状态 ──────────────────────────────────────────────
const seasonsMeta = ref(seasonsMetaRaw)

// 默认激活最新赛季（current_season 字段）
const activeSeasonId = ref(seasonsMetaRaw.current_season)

const activeSeason = computed(() =>
  seasonsMeta.value.seasons.find(s => s.id === activeSeasonId.value) || seasonsMeta.value.seasons[0]
)

// ── 赛季数据（动态加载）─────────────────────────────────────────
const isLoading = ref(false)

// 所有数据 ref（从当前赛季加载）
const careerData   = ref({})
const matches      = ref([])
const news         = ref([])
const mailbox      = ref({ messages: [] })
const roundMatches = ref({})
const worldNews    = ref([])
const availableLeagues = ref([])
const teamAnalysis = ref({})
const leaderboards = ref({})
const community    = ref({})
const squad        = ref([])

// 动态加载一个赛季的全部数据
async function loadSeasonData(seasonId) {
  isLoading.value = true
  selectedMatchId.value = null   // 重置单场详情

  try {
    const [
      career,
      matchesJson,
      newsJson,
      mailboxJson,
      roundMatchesJson,
      worldNewsJson,
      standingsJson,
      teamAnalysisJson,
      leaderboardsJson,
      communityJson,
      squadJson,
    ] = await Promise.all([
      import(`./data/season_${seasonId}/career.json`),
      import(`./data/season_${seasonId}/matches.json`),
      import(`./data/season_${seasonId}/news.json`),
      import(`./data/season_${seasonId}/mailbox.json`),
      import(`./data/season_${seasonId}/round_matches.json`),
      import(`./data/season_${seasonId}/world_news.json`),
      import(`./data/season_${seasonId}/standings.json`),
      import(`./data/season_${seasonId}/team_analysis.json`),
      import(`./data/season_${seasonId}/leaderboards.json`),
      import(`./data/season_${seasonId}/community.json`),
      import(`./data/season_${seasonId}/squad.json`),
    ])

    careerData.value       = career.default
    matches.value          = matchesJson.default
    news.value             = newsJson.default
    mailbox.value          = mailboxJson.default
    roundMatches.value     = roundMatchesJson.default
    worldNews.value        = Array.isArray(worldNewsJson.default) ? worldNewsJson.default : (worldNewsJson.default?.articles || [])
    availableLeagues.value = standingsJson.default?.leagues || []
    teamAnalysis.value     = teamAnalysisJson.default
    leaderboards.value     = leaderboardsJson.default
    community.value        = communityJson.default
    squad.value            = squadJson.default || []
  } catch (e) {
    console.error(`Failed to load season ${seasonId}:`, e)
  } finally {
    isLoading.value = false
  }
}

// 初始加载
loadSeasonData(activeSeasonId.value)

// 切换赛季
function onSwitchSeason(seasonId) {
  if (seasonId === activeSeasonId.value) return
  activeSeasonId.value = seasonId
  activeTab.value = 'matches'
  loadSeasonData(seasonId)
}

// ── 俱乐部信息（从 careerData 读取）────────────────────────────
const currentClub = computed(() => {
  const clubs = careerData.value?.clubs || []
  const id = careerData.value?.current_club_id
  return clubs.find(c => c.id === id) || clubs[0] || { name: '维尔通精英', seasons: [] }
})

// ── 全局主导航 Tab ────────────────────────────────────────────
const activeTab = ref('matches')

// ── 二级页面状态：选中的比赛 ID ──────────────────────────────
const selectedMatchId = ref(null)

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

// ── 交互操作 ───────────────────────────────────────────────────
const onSelectMatch = (matchId) => {
  selectedMatchId.value = matchId
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const onCommunitySelectMatch = (matchId) => {
  if (matchId) {
    activeTab.value = 'matches'
    selectedMatchId.value = matchId
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
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
