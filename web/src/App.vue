<template>
  <div class="min-h-screen bg-slate-900 text-slate-100 flex justify-center font-sans">
    <!-- 移动端视口外壳 (在桌面端居中如手机 App) -->
    <main class="w-full max-w-md bg-slate-950 min-h-screen flex flex-col shadow-2xl relative border-x border-slate-800 pb-16">
      
      <!-- 1. 顶部公域门户 Header (严格去主角化，第四面墙) -->
      <header class="bg-emerald-700 text-white px-4 py-3 sticky top-0 z-30 shadow-md flex items-center justify-between">
        <div class="flex items-center space-x-2.5">
          <div class="w-8 h-8 rounded-lg bg-emerald-900 flex items-center justify-center font-black text-white text-xs tracking-tighter border border-emerald-500/40">
            FH
          </div>
          <div>
            <div class="flex items-center space-x-1.5">
              <h1 class="text-sm font-black tracking-tight">FootHub · 懂球云</h1>
              <span class="text-[9px] bg-emerald-900/90 text-emerald-200 border border-emerald-500/30 px-1 py-0.2 rounded">
                比利时专区
              </span>
            </div>
            <p class="text-[10px] text-emerald-100/80">
              欧洲职业足球即时比分与数据门户
            </p>
          </div>
        </div>

        <!-- 右上角：私域入口【📩 主帅信箱】 -->
        <button
          @click="showMailbox = true"
          class="relative bg-emerald-800 hover:bg-emerald-900 text-emerald-100 text-[11px] px-2.5 py-1.5 rounded-lg border border-emerald-600/60 flex items-center space-x-1 shadow-sm transition active:scale-95"
        >
          <span>📩</span>
          <span class="font-bold">主帅信箱</span>
          <span class="absolute -top-1 -right-1 w-2.5 h-2.5 bg-amber-400 rounded-full animate-pulse border-2 border-emerald-800"></span>
        </button>
      </header>

      <!-- 轮次切换条 -->
      <div class="bg-slate-900 border-b border-slate-800 px-3 py-2 flex items-center justify-between">
        <div class="flex items-center space-x-2 overflow-x-auto no-scrollbar">
          <button
            v-for="r in [1, 2, 3]"
            :key="r"
            @click="currentRound = r"
            :class="[
              'px-3 py-1 rounded-lg text-xs font-semibold shrink-0 transition flex items-center space-x-1.5',
              currentRound === r
                ? 'bg-emerald-600 text-white shadow-sm'
                : 'bg-slate-800 text-slate-400 hover:text-slate-200'
            ]"
          >
            <span>比乙 第 {{ r }} 轮</span>
          </button>
        </div>
        <span class="text-[10px] text-slate-400 shrink-0 ml-2">2025/26 赛季</span>
      </div>

      <!-- 公域主导航 Tab -->
      <nav class="flex border-b border-slate-800 bg-slate-900 sticky top-14 z-20">
        <button
          v-for="tab in tabs"
          :key="tab.key"
          @click="activeTab = tab.key"
          :class="[
            'flex-1 py-2.5 text-xs font-medium text-center relative transition-colors',
            activeTab === tab.key
              ? 'text-emerald-400 font-bold'
              : 'text-slate-400 hover:text-slate-200'
          ]"
        >
          <span>{{ tab.label }}</span>
          <span
            v-if="activeTab === tab.key"
            class="absolute bottom-0 left-1/4 right-1/4 h-0.5 bg-emerald-500 rounded-full"
          ></span>
        </button>
      </nav>

      <!-- ==================== TAB 1: ⚽ 赛事大盘 (世界背景板) ==================== -->
      <section v-if="activeTab === 'matches'" class="p-4 space-y-4">
        
        <!-- 焦点战报卡片 (维尔通本场) -->
        <div v-if="currentMatch" class="bg-gradient-to-b from-slate-900 to-slate-950 rounded-xl border border-slate-800 p-4 shadow-sm">
          <div class="flex justify-between items-center text-[11px] text-slate-400 mb-2">
            <span class="flex items-center space-x-1 text-emerald-400 font-medium">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              <span>比乙焦点 · 已完赛</span>
            </span>
            <span class="text-slate-400 truncate max-w-[170px]">{{ currentMatch.stadium }}</span>
          </div>

          <!-- 比分栏 -->
          <div class="flex items-center justify-between py-2">
            <div class="w-5/12 text-center">
              <div class="text-sm font-bold text-white truncate">{{ currentMatch.home_team }}</div>
              <div class="text-[10px] text-slate-500 mt-0.5">主队</div>
            </div>
            <div class="w-2/12 text-center">
              <div class="text-2xl font-black text-white tracking-wider">
                {{ currentMatch.score_home }} - {{ currentMatch.score_away }}
              </div>
            </div>
            <div class="w-5/12 text-center">
              <div class="text-sm font-bold text-white truncate">{{ currentMatch.away_team }}</div>
              <div class="text-[10px] text-slate-500 mt-0.5">客队</div>
            </div>
          </div>

          <!-- 进球列表 -->
          <div v-if="currentMatch.scorers && currentMatch.scorers.length" class="mt-2 pt-2 border-t border-slate-800/60 text-center">
            <div
              v-for="(sc, sIdx) in currentMatch.scorers"
              :key="sIdx"
              class="text-[11px] text-slate-300"
            >
              ⚽ {{ sc.player_zh || sc.player }} ({{ sc.minute }}')
              <span v-if="sc.assist_zh || sc.assist" class="text-slate-500 text-[10px]">
                助攻: {{ sc.assist_zh || sc.assist }}
              </span>
            </div>
          </div>

          <!-- xG与硬数据指标 -->
          <div class="grid grid-cols-3 gap-2 mt-3 pt-2 text-center border-t border-slate-800/40">
            <div class="bg-slate-850 rounded p-1.5">
              <div class="text-[10px] text-slate-400">预期进球(xG)</div>
              <div class="text-xs font-bold text-slate-200">{{ currentMatch.xg }}</div>
            </div>
            <div class="bg-slate-850 rounded p-1.5">
              <div class="text-[10px] text-slate-400">射门(射正)</div>
              <div class="text-xs font-bold text-slate-200">{{ currentMatch.shots }} ({{ currentMatch.shots_on_target }})</div>
            </div>
            <div class="bg-slate-850 rounded p-1.5">
              <div class="text-[10px] text-slate-400">跑动里程</div>
              <div class="text-xs font-bold text-slate-200">{{ currentMatch.distance_km }} km</div>
            </div>
          </div>
        </div>

        <!-- 世界背景板 1：同轮次比乙其他场次完整赛果 (精确对齐网格布局) -->
        <div class="space-y-2">
          <div class="flex items-center justify-between text-xs font-bold text-slate-300">
            <span>🇧🇪 比乙第 {{ currentRound }} 轮 · 完整战报栏</span>
            <span class="text-[10px] text-slate-500">官方正式赛果</span>
          </div>

          <div class="bg-slate-900 rounded-xl border border-slate-800 divide-y divide-slate-800/60 text-xs overflow-hidden">
            <div
              v-for="(m, mIdx) in currentRoundOtherMatches"
              :key="mIdx"
              :class="[
                'px-2.5 py-2.5 grid grid-cols-[58px_1fr_46px_1fr] items-center gap-1.5 transition',
                m.is_virton ? 'bg-emerald-950/40 border-l-2 border-emerald-500' : 'hover:bg-slate-850'
              ]"
            >
              <!-- 1. 日期与标记 (固定58px) -->
              <div class="flex items-center space-x-1 text-[10px] text-slate-400 truncate">
                <span class="font-mono">{{ m.date.slice(5) }}</span>
                <span v-if="m.is_virton" class="text-emerald-400 font-bold shrink-0">[本场]</span>
              </div>

              <!-- 2. 主队 (1fr 弹性宽度，向右对齐贴向比分) -->
              <div class="text-right truncate pr-1">
                <span
                  :class="[
                    'truncate',
                    m.home === '维尔通精英' || m.home.includes('维尔通') ? 'font-bold text-emerald-300' : 'text-slate-300'
                  ]"
                >
                  {{ m.home }}
                </span>
              </div>

              <!-- 3. 比分 (固定46px，正中心等宽字体，尺子般垂绝对齐) -->
              <div class="text-center font-mono font-black text-white text-xs bg-slate-950/70 py-0.5 rounded border border-slate-800 tracking-wider">
                {{ m.score }}
              </div>

              <!-- 4. 客队 (1fr 弹性宽度，向左对齐贴向比分) -->
              <div class="text-left truncate pl-1">
                <span
                  :class="[
                    'truncate',
                    m.away === '维尔通精英' || m.away.includes('维尔通') ? 'font-bold text-emerald-300' : 'text-slate-300'
                  ]"
                >
                  {{ m.away }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- 世界背景板 2：欧洲五大联赛与比甲快讯 -->
        <div class="space-y-2">
          <div class="flex items-center justify-between text-xs font-bold text-slate-300">
            <span>🌍 同期欧洲足坛快讯 (比甲 / 五大联赛)</span>
            <span class="text-[10px] text-slate-500">国际版面</span>
          </div>

          <div class="space-y-2">
            <div
              v-for="wn in worldNews"
              :key="wn.id"
              class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-1 hover:border-slate-700 transition"
            >
              <div class="flex items-center justify-between text-[10px]">
                <span class="bg-slate-800 text-teal-400 px-1.5 py-0.5 rounded font-medium flex items-center space-x-1">
                  <svg v-if="getLeagueIconByName(wn.league)" class="icon text-xs">
                    <use :xlink:href="'#' + getLeagueIconByName(wn.league)"></use>
                  </svg>
                  <span>{{ wn.league }}</span>
                </span>
                <span class="text-slate-500">{{ wn.time }}</span>
              </div>
              <h4 class="text-xs font-bold text-slate-200 leading-snug">
                {{ wn.title }}
              </h4>
              <p class="text-[11px] text-slate-400 leading-relaxed">
                {{ wn.summary }}
              </p>
            </div>
          </div>
        </div>

      </section>

      <!-- ==================== TAB 2: 📰 战报资讯 (客观公域战报) ==================== -->
      <section v-if="activeTab === 'report' && currentNews" class="p-4 space-y-4">
        <div>
          <div class="flex flex-wrap gap-1.5 mb-2">
            <span
              v-for="tag in currentNews.dongqiudi_article.tags"
              :key="tag"
              class="text-[10px] bg-slate-800 text-emerald-400 px-2 py-0.5 rounded border border-slate-700"
            >
              #{{ tag }}
            </span>
          </div>
          <h2 class="text-base font-bold text-white leading-snug">
            {{ currentNews.dongqiudi_article.title }}
          </h2>
          <p class="text-xs text-slate-400 mt-1">
            发布于 {{ currentMatch?.date }} · 比利时足球前线
          </p>
        </div>

        <div class="bg-emerald-950/40 border-l-4 border-emerald-500 p-3 rounded-r-lg text-xs text-emerald-200/90 leading-relaxed">
          {{ currentNews.dongqiudi_article.summary }}
        </div>

        <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
          <p
            v-for="(para, pIdx) in articleParagraphs"
            :key="pIdx"
            :class="para.startsWith('【') ? 'font-bold text-slate-100 text-sm pt-2 text-emerald-400' : ''"
          >
            {{ para }}
          </p>
        </div>

        <!-- 比利时公开媒体声音 -->
        <div class="bg-slate-900 border border-slate-800 rounded-lg p-3">
          <div class="flex items-center space-x-1.5 text-xs font-bold text-slate-200 mb-1.5">
            <span>🇧🇪</span>
            <span>比利时当地媒体简评 (公开报道)</span>
          </div>
          <p class="text-xs text-slate-400 italic">
            {{ currentNews.belgian_media_snippet }}
          </p>
        </div>
      </section>

      <!-- ==================== TAB 3: 🔥 社区热评 (公域社媒) ==================== -->
      <section v-if="activeTab === 'comments' && currentNews" class="p-4 space-y-4">
        <!-- 主帅评分卡片 -->
        <div class="bg-gradient-to-r from-slate-900 to-slate-850 p-4 rounded-xl border border-slate-800 flex items-center justify-between">
          <div>
            <div class="text-[11px] text-slate-400">本场主帅综合评分</div>
            <div class="text-sm font-bold text-white mt-0.5">主教练：耶稣 徐</div>
            <div class="text-[10px] text-slate-500 mt-1">共有 2,419 名球迷参与打分</div>
          </div>
          <div class="text-right">
            <div class="text-3xl font-black tracking-tight" :class="coachScoreColor">
              {{ currentNews.hupu_thread.coach_score }}
            </div>
            <div class="text-[10px] text-slate-400">/ 10 分</div>
          </div>
        </div>

        <div class="border-b border-slate-800 pb-2">
          <h3 class="text-xs font-bold text-slate-300">
            {{ currentNews.hupu_thread.title }}
          </h3>
        </div>

        <!-- 评论列表 -->
        <div class="space-y-3">
          <div
            v-for="(cmt, cIdx) in currentNews.hupu_thread.comments"
            :key="cIdx"
            class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-3 space-y-2 hover:border-slate-700 transition"
          >
            <div class="flex items-center justify-between text-xs">
              <div class="flex items-center space-x-2">
                <div class="w-6 h-6 rounded-full bg-slate-700 flex items-center justify-center text-[10px] font-bold text-slate-200">
                  {{ cmt.username.slice(0, 1) }}
                </div>
                <span class="font-semibold text-slate-200 text-xs">{{ cmt.username }}</span>
                <span class="text-[10px] bg-slate-800 text-amber-300/90 px-1.5 py-0.2 rounded border border-amber-900/40">
                  {{ cmt.tag }}
                </span>
              </div>
              <span class="text-[10px] text-slate-500">#{{ cIdx + 1 }} 楼</span>
            </div>

            <p class="text-xs text-slate-300 leading-relaxed">
              {{ cmt.content }}
            </p>

            <div class="flex justify-end pt-1">
              <button
                @click="toggleLike(currentNews.match_id, cIdx)"
                :class="[
                  'text-[11px] px-2.5 py-1 rounded-full flex items-center space-x-1 transition',
                  isLiked(currentNews.match_id, cIdx)
                    ? 'bg-rose-950 text-rose-400 border border-rose-800'
                    : 'bg-slate-800/70 text-slate-400 hover:text-slate-200'
                ]"
              >
                <span>{{ isLiked(currentNews.match_id, cIdx) ? '❤️ 亮了' : '👍 亮了' }}</span>
                <span class="font-semibold">{{ getLikesCount(currentNews.match_id, cIdx, cmt.likes) }}</span>
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- ==================== TAB 4: 👥 首发阵容 ==================== -->
      <section v-if="activeTab === 'lineup' && currentMatch" class="p-4 space-y-3">
        <div class="flex justify-between items-center text-xs text-slate-400 mb-1">
          <span class="font-bold text-slate-200">首发阵容 (4-2-3-1)</span>
          <span>FM 真实中文数据</span>
        </div>

        <div class="space-y-1.5">
          <div
            v-for="p in currentMatch.lineup"
            :key="p.name_en || p.name"
            class="flex items-center justify-between p-2.5 bg-slate-900 rounded-lg border border-slate-800 text-xs"
          >
            <div class="flex items-center space-x-2.5">
              <span class="w-7 text-[10px] font-bold text-slate-400 text-center bg-slate-800 px-1 py-0.5 rounded shrink-0">
                {{ p.pos }}
              </span>
              <div>
                <div class="font-bold text-slate-200 flex items-center space-x-1.5">
                  <span>{{ p.name_zh || p.name }}</span>
                  <span v-if="p.is_motm" class="text-[9px] bg-amber-500 text-slate-950 font-black px-1 rounded">MVP</span>
                  <span v-if="p.goal" class="text-[10px]">⚽ x{{ p.goal }}</span>
                  <span v-if="p.assist" class="text-[10px]">🅰️ x{{ p.assist }}</span>
                </div>
                <div class="text-[10px] text-slate-500 flex items-center space-x-1">
                  <span>{{ p.name_en || p.name }}</span>
                  <span>·</span>
                  <span>出场 {{ p.min }} 分钟</span>
                </div>
              </div>
            </div>

            <div class="flex items-center space-x-2">
              <span
                :class="[
                  'font-black text-sm px-2 py-0.5 rounded',
                  p.rating >= 7.5 ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' :
                  p.rating >= 7.0 ? 'bg-teal-950 text-teal-300 border border-teal-800' :
                  p.rating >= 6.5 ? 'bg-slate-800 text-slate-200' :
                  'bg-rose-950 text-rose-300 border border-rose-900'
                ]"
              >
                {{ p.rating }}
              </span>
            </div>
          </div>
        </div>
      </section>

      <!-- ==================== TAB 5: 🏆 联赛大盘 (七大联赛完整大盘) ==================== -->
      <section v-if="activeTab === 'standings'" class="p-4 space-y-3">
        <div>
          <div class="text-xs font-bold text-slate-300 mb-2 flex items-center justify-between">
            <span>🌍 欧洲各大联赛完整积分大盘</span>
            <span class="text-[10px] text-slate-500">七大联赛完整收录</span>
          </div>

          <!-- 七大联赛横向切换选择器 (比乙、比甲、英超、西甲、意甲、德甲、法甲) -->
          <div class="relative flex items-center bg-slate-900 rounded-xl p-1 border border-slate-800">
            <!-- 左滑箭头 (桌面端友好) -->
            <button
              @click="scrollLeagues(-100)"
              class="w-6 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs shrink-0 transition"
              title="向左滚动"
            >
              ‹
            </button>

            <!-- 滚动按钮区 (支持鼠标滚轮 + 触屏手势) -->
            <div
              ref="leagueScrollRef"
              @wheel.prevent="onLeagueWheel"
              class="flex-1 flex items-center space-x-1.5 overflow-x-auto py-1 px-1.5 scroll-smooth no-scrollbar select-none"
              style="-webkit-overflow-scrolling: touch; touch-action: pan-x;"
            >
              <button
                v-for="lg in availableLeagues"
                :key="lg.id"
                @click="selectedLeagueId = lg.id"
                :class="[
                  'px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 transition flex items-center space-x-1.5 whitespace-nowrap',
                  selectedLeagueId === lg.id
                    ? 'bg-emerald-600 text-white font-bold shadow-sm'
                    : 'bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-slate-200'
                ]"
              >
                <svg v-if="getLeagueIcon(lg.id)" class="icon text-sm">
                  <use :xlink:href="'#' + getLeagueIcon(lg.id)"></use>
                </svg>
                <span v-else>{{ lg.flag }}</span>
                <span>{{ lg.short_name }}</span>
              </button>
            </div>

            <!-- 右滑箭头 (桌面端友好) -->
            <button
              @click="scrollLeagues(100)"
              class="w-6 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs shrink-0 transition"
              title="向右滚动"
            >
              ›
            </button>
          </div>
        </div>

        <!-- 当前选中联赛的提示信息 (不显示队伍总数，带联赛官方Icon) -->
        <div class="bg-slate-900 border border-slate-800 rounded-lg p-2.5 flex items-center justify-between text-xs">
          <div class="flex items-center space-x-2.5">
            <div class="w-8 h-8 rounded-lg bg-slate-800/80 border border-slate-700 flex items-center justify-center shrink-0">
              <svg v-if="getLeagueIcon(currentDisplayLeague.id)" class="icon text-xl text-emerald-400">
                <use :xlink:href="'#' + getLeagueIcon(currentDisplayLeague.id)"></use>
              </svg>
              <span v-else class="text-base">{{ currentDisplayLeague.flag }}</span>
            </div>
            <div>
              <div class="font-bold text-white">{{ currentDisplayLeague.name }}</div>
              <div class="text-[10px] text-slate-400 mt-0.5">
                已战至第 {{ currentDisplayLeague.round }} 轮 · 官方即时积分
              </div>
            </div>
          </div>
          <span class="text-[10px] bg-slate-800 text-emerald-400 px-2 py-0.5 rounded border border-slate-700 shrink-0">
            {{ currentDisplayLeague.tag || '欧洲职业联赛' }}
          </span>
        </div>

        <!-- 完整积分表 -->
        <div class="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden text-xs shadow-inner">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="bg-slate-850 text-slate-400 border-b border-slate-800 text-[10px]">
                <th class="py-2.5 px-2 text-center w-8">#</th>
                <th class="py-2.5 px-2">球队</th>
                <th class="py-2.5 px-1 text-center w-7">赛</th>
                <th class="py-2.5 px-1 text-center w-12">胜/平/负</th>
                <th class="py-2.5 px-1 text-center w-8">净胜</th>
                <th class="py-2.5 px-2 text-center font-bold w-9">积分</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="row in currentDisplayLeague.table"
                :key="row.position"
                :class="[
                  'border-b border-slate-800/60 transition hover:bg-slate-850/80',
                  row.is_my_team || row.team_name.includes('维尔通')
                    ? 'bg-emerald-950/60 font-bold text-emerald-300 border-l-2 border-emerald-500'
                    : 'text-slate-300'
                ]"
              >
                <!-- 排名高亮标识 -->
                <td class="py-2 px-2 text-center font-bold">
                  <span
                    :class="[
                      'w-5 h-5 rounded flex items-center justify-center text-[10px] mx-auto',
                      row.position <= 4 ? 'bg-amber-400/20 text-amber-300 font-black' :
                      row.position > currentDisplayLeague.total_teams - 3 ? 'bg-rose-950 text-rose-400 font-bold' :
                      'text-slate-400'
                    ]"
                  >
                    {{ row.position }}
                  </span>
                </td>
                <td class="py-2 px-2 truncate max-w-[130px]">
                  <div class="flex items-center space-x-1">
                    <span class="truncate">{{ row.team_name }}</span>
                    <span
                      v-if="row.is_my_team || row.team_name.includes('维尔通')"
                      class="text-[9px] bg-emerald-600 text-white px-1 py-0.2 rounded shrink-0 font-normal"
                    >
                      执教中
                    </span>
                  </div>
                </td>
                <td class="py-2 px-1 text-center text-slate-400">{{ row.played }}</td>
                <td class="py-2 px-1 text-center text-slate-400 text-[11px]">{{ row.won }}/{{ row.drawn }}/{{ row.lost }}</td>
                <td
                  class="py-2 px-1 text-center text-[11px]"
                  :class="row.gd > 0 ? 'text-emerald-400 font-semibold' : row.gd < 0 ? 'text-rose-400' : 'text-slate-400'"
                >
                  {{ row.gd > 0 ? '+' + row.gd : row.gd }}
                </td>
                <td class="py-2 px-2 text-center font-black text-white text-xs">{{ row.points }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- 榜单底部分区说明 -->
        <div class="flex items-center justify-between text-[10px] text-slate-500 px-1">
          <div class="flex items-center space-x-3">
            <span class="flex items-center space-x-1">
              <span class="w-2 h-2 rounded bg-amber-400/30"></span>
              <span>欧冠/升级区 (前4)</span>
            </span>
            <span class="flex items-center space-x-1">
              <span class="w-2 h-2 rounded bg-rose-950"></span>
              <span>降级区 (末2~3名)</span>
            </span>
          </div>
          <span>FM 真实同步数据</span>
        </div>
      </section>

      <!-- 底部常驻栏 (中立综合门户风格) -->
      <footer class="fixed bottom-0 w-full max-w-md bg-slate-900/95 backdrop-blur border-t border-slate-800 px-4 py-2.5 flex items-center justify-between text-xs z-30">
        <div class="flex items-center space-x-1.5 text-slate-400 text-[11px]">
          <span>⚽ FootHub 数据中心已连线</span>
        </div>
        <div class="flex items-center space-x-2">
          <button
            @click="activeTab = 'comments'"
            class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs px-3 py-1.5 rounded-full shadow-sm flex items-center space-x-1"
          >
            <span>球迷社区</span>
          </button>
        </div>
      </footer>

      <!-- ==================== 2. 私域弹窗：📩 主帅信箱 (严格隔离第四面墙) ==================== -->
      <div
        v-if="showMailbox"
        class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
        @click.self="showMailbox = false"
      >
        <div class="bg-slate-900 border border-slate-700 w-full max-w-sm rounded-2xl overflow-hidden shadow-2xl flex flex-col max-h-[85vh] animate-in fade-in zoom-in-95 duration-200">
          
          <!-- 弹窗顶栏 -->
          <div class="bg-gradient-to-r from-slate-800 to-slate-900 p-3.5 border-b border-slate-700 flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="text-base">💼</span>
              <div>
                <h3 class="text-xs font-bold text-white tracking-wide">主帅私人工作台 · 信箱</h3>
                <p class="text-[9px] text-slate-400 font-mono">CONFIDENTIAL // MANAGER ONLY</p>
              </div>
            </div>
            <button
              @click="showMailbox = false"
              class="text-slate-400 hover:text-white text-lg w-7 h-7 flex items-center justify-center rounded-full hover:bg-slate-800 transition"
            >
              ✕
            </button>
          </div>

          <!-- 弹窗内容滚动区 -->
          <div class="p-4 overflow-y-auto space-y-4 text-xs">
            
            <!-- 档案状态卡 -->
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
              <div class="flex items-center justify-between">
                <div>
                  <div class="font-black text-sm text-white">{{ mailbox.manager_profile.name }}</div>
                  <div class="text-[10px] text-emerald-400 mt-0.5">{{ mailbox.manager_profile.club_name }}</div>
                </div>
                <span class="text-[10px] bg-emerald-950 text-emerald-300 border border-emerald-800 px-2 py-0.5 rounded-full">
                  {{ mailbox.manager_profile.role }}
                </span>
              </div>
              <div class="text-[10px] text-slate-400 pt-1 border-t border-slate-800/80 flex justify-between">
                <span>助理教练: {{ mailbox.manager_profile.assistant_name }}</span>
                <span>合同期至: 2026-06</span>
              </div>
            </div>

            <!-- 足协合规倒计时 (60天豁免期) -->
            <div class="bg-amber-950/30 border border-amber-900/60 rounded-xl p-3 space-y-2">
              <div class="flex items-center justify-between text-xs">
                <span class="font-bold text-amber-300 flex items-center space-x-1">
                  <span>⚠️</span>
                  <span>比利时足协(KBVB)临时豁免期</span>
                </span>
                <span class="font-mono text-amber-400 font-bold">
                  第 {{ mailbox.manager_profile.waiver_days_used }} / {{ mailbox.manager_profile.waiver_days_total }} 天
                </span>
              </div>

              <!-- 进度条 -->
              <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                <div
                  class="bg-amber-400 h-full rounded-full transition-all duration-500"
                  :style="{ width: `${(mailbox.manager_profile.waiver_days_used / mailbox.manager_profile.waiver_days_total) * 100}%` }"
                ></div>
              </div>

              <p class="text-[10px] text-amber-200/80 leading-relaxed">
                依据比利时足协条款，无职业级执照主帅享有最多 60 天代理执教豁免期。请在期满前完成资格注册或由持证助教大卫·齐特利签署相关掩护文件。
              </p>
            </div>

            <!-- 董事会与坎特私信列表 -->
            <div class="space-y-2">
              <div class="font-bold text-slate-300 text-[11px] flex items-center justify-between">
                <span>📩 董事会 & 坎特直达信件</span>
                <span class="text-[10px] text-slate-500 font-normal">共 3 封通讯</span>
              </div>

              <div class="space-y-2.5">
                <div
                  v-for="msg in mailbox.messages"
                  :key="msg.id"
                  class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1.5 hover:border-slate-700 transition"
                >
                  <div class="flex items-center justify-between text-[11px]">
                    <div class="flex items-center space-x-1.5">
                      <span>{{ msg.avatar }}</span>
                      <span class="font-bold text-slate-200">{{ msg.from }}</span>
                    </div>
                    <span class="text-[9px] bg-slate-800 text-slate-400 px-1.5 py-0.2 rounded font-mono">
                      {{ msg.type }}
                    </span>
                  </div>

                  <div class="text-[10px] text-emerald-400/90 font-medium">
                    {{ msg.subject }}
                  </div>

                  <p class="text-[11px] text-slate-300 leading-relaxed font-sans bg-slate-900/60 p-2 rounded border border-slate-800/40">
                    {{ msg.content }}
                  </p>

                  <div class="text-[9px] text-slate-500 text-right font-mono">
                    {{ msg.date }}
                  </div>
                </div>
              </div>
            </div>

          </div>

          <!-- 弹窗底栏 -->
          <div class="p-3 bg-slate-950 border-t border-slate-800 text-center">
            <button
              @click="showMailbox = false"
              class="w-full bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs py-2 rounded-xl transition"
            >
              关闭并返回公域门户
            </button>
          </div>

        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

import matchesData from './data/matches.json'
import newsData from './data/news.json'
import multiLeaguesData from './data/standings.json'
import mailboxData from './data/mailbox.json'
import roundMatchesData from './data/round_matches.json'
import worldNewsData from './data/world_news.json'

const matches = ref(matchesData)
const news = ref(newsData)
const mailbox = ref(mailboxData)
const roundMatches = ref(roundMatchesData)
const worldNews = ref(worldNewsData)
const availableLeagues = ref(multiLeaguesData.leagues || [])

// 选中的轮次 (默认最新第 3 轮)
const currentRound = ref(3)

// 联赛滚动控制 (支持鼠标滚轮 + 左右微调按钮)
const leagueScrollRef = ref(null)
const onLeagueWheel = (e) => {
  if (leagueScrollRef.value) {
    leagueScrollRef.value.scrollLeft += (e.deltaY || e.deltaX) * 0.9
  }
}
const scrollLeagues = (offset) => {
  if (leagueScrollRef.value) {
    leagueScrollRef.value.scrollBy({ left: offset, behavior: 'smooth' })
  }
}

// 选中的公域 Tab
const activeTab = ref('matches')

const tabs = [
  { key: 'matches', label: '⚽ 赛事大盘' },
  { key: 'report', label: '📰 战报资讯' },
  { key: 'comments', label: '🔥 球迷热评' },
  { key: 'lineup', label: '👥 首发阵容' },
  { key: 'standings', label: '🏆 积分榜' }
]

// 控制私域主帅信箱弹窗显示/隐藏
const showMailbox = ref(false)

// 联赛大盘中选中的联赛 (默认比乙)
const selectedLeagueId = ref('bel_d2')
const currentDisplayLeague = computed(() => {
  return availableLeagues.value.find(l => l.id === selectedLeagueId.value) || availableLeagues.value[0]
})

// 五大联赛官方矢量 Icon 映射 (基于用户提供的阿里 Iconfont Symbol JS)
const getLeagueIcon = (id) => {
  const iconMap = {
    pl: 'icon-yingchao',       // 英超
    laliga: 'icon-xijia',      // 西甲
    serie_a: 'icon-yijia',     // 意甲
    bundesliga: 'icon-dejia',  // 德甲
    ligue1: 'icon-a-zu10290'   // 法甲
  }
  return iconMap[id] || null
}

const getLeagueIconByName = (name) => {
  if (!name) return null
  if (name.includes('英超')) return 'icon-yingchao'
  if (name.includes('西甲')) return 'icon-xijia'
  if (name.includes('意甲')) return 'icon-yijia'
  if (name.includes('德甲')) return 'icon-dejia'
  if (name.includes('法甲')) return 'icon-a-zu10290'
  return null
}

// 当前维尔通焦点比赛与战报
const currentMatch = computed(() => {
  return matches.value.find(m => m.round === currentRound.value)
})

const currentNews = computed(() => {
  return news.value.find(n => n.round === currentRound.value)
})

// 当前轮次下比乙其他场次的完整赛果
const currentRoundOtherMatches = computed(() => {
  return roundMatches.value[String(currentRound.value)] || []
})

const articleParagraphs = computed(() => {
  if (!currentNews.value?.dongqiudi_article?.body) return []
  return currentNews.value.dongqiudi_article.body.split('\n\n')
})

const coachScoreColor = computed(() => {
  const score = currentNews.value?.hupu_thread?.coach_score || 0
  if (score >= 8.5) return 'text-emerald-400'
  if (score >= 7.0) return 'text-teal-400'
  return 'text-amber-400'
})

// 点赞互动
const likedComments = ref({})
const toggleLike = (matchId, cIdx) => {
  const key = `${matchId}_${cIdx}`
  likedComments.value[key] = !likedComments.value[key]
}
const isLiked = (matchId, cIdx) => !!likedComments.value[`${matchId}_${cIdx}`]
const getLikesCount = (matchId, cIdx, baseLikes) => {
  return isLiked(matchId, cIdx) ? baseLikes + 1 : baseLikes
}
</script>
