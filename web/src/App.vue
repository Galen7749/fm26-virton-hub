<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 flex flex-col items-center select-none">
    
    <!-- 主视口容器 (限制移动端最大宽度 448px) -->
    <main class="w-full max-w-md bg-slate-950 min-h-screen flex flex-col pb-20 shadow-2xl relative">

      <!-- ==================== 1. 公域 Header (完全去主角化，严格中立门户) ==================== -->
      <header class="bg-slate-900 border-b border-slate-800 px-4 py-3 flex items-center justify-between sticky top-0 z-30 shadow-md">
        <div class="flex items-center space-x-2.5">
          <div class="w-8 h-8 rounded-lg bg-emerald-600 flex items-center justify-center font-black text-white text-base tracking-tighter shadow-sm">
            FH
          </div>
          <div>
            <h1 class="text-sm font-black text-white tracking-wide flex items-center space-x-1.5">
              <span>FootHub · 懂球云</span>
              <span class="text-[9px] bg-slate-800 text-teal-300 font-normal px-1.5 py-0.2 rounded border border-teal-900/40">比利时专区</span>
            </h1>
            <p class="text-[9px] text-slate-400 font-sans">欧洲职业足球即时比分与数据门户</p>
          </div>
        </div>

        <!-- 私人入口：主帅信箱按钮 (右上角私域抽屉开关，隔离公域) -->
        <button
          @click="showMailbox = true"
          class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs px-2.5 py-1.5 rounded-lg flex items-center space-x-1 transition shadow-sm relative group"
        >
          <span class="text-xs">💼</span>
          <span class="font-bold text-[11px] text-emerald-400">主帅信箱</span>
          <span class="w-2 h-2 rounded-full bg-amber-400 absolute -top-0.5 -right-0.5 ring-2 ring-slate-900 animate-pulse"></span>
        </button>
      </header>

      <!-- 轮次切换条 -->
      <div class="bg-slate-900/90 border-b border-slate-800/80 px-4 py-2 flex items-center justify-between text-xs">
        <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar">
          <button
            v-for="m in matches"
            :key="m.round"
            @click="currentRound = m.round"
            :class="[
              'px-3 py-1 rounded-full text-xs font-semibold shrink-0 transition flex items-center space-x-1',
              currentRound === m.round
                ? 'bg-emerald-600 text-white font-bold shadow-sm'
                : 'bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-slate-200'
            ]"
          >
            <span>{{ m.round_label || ('第 ' + m.round + ' 轮') }}</span>
            <span v-if="m.result" :class="[
              'text-[9px] px-1 py-0.2 rounded font-mono',
              m.result === 'W' || m.result === '胜' ? 'bg-emerald-500/30 text-emerald-300' :
              m.result === 'D' || m.result === '平' ? 'bg-amber-500/30 text-amber-300' : 'bg-rose-500/30 text-rose-300'
            ]">{{ m.result }}</span>
          </button>
        </div>
        <span class="text-[10px] text-slate-400 shrink-0 ml-2">2025/26 赛季</span>
      </div>

      <!-- 公域主导航 Tab (6大功能模块，支持丝滑横向轻扫) -->
      <nav class="flex border-b border-slate-800 bg-slate-900 sticky top-14 z-20 overflow-x-auto no-scrollbar scroll-smooth">
        <button
          v-for="tab in tabs"
          :key="tab.key"
          @click="activeTab = tab.key"
          :class="[
            'px-3.5 py-2.5 text-xs font-medium text-center relative transition-colors shrink-0 whitespace-nowrap',
            activeTab === tab.key
              ? 'text-emerald-400 font-bold'
              : 'text-slate-400 hover:text-slate-200'
          ]"
        >
          <span>{{ tab.label }}</span>
          <span
            v-if="activeTab === tab.key"
            class="absolute bottom-0 left-2 right-2 h-0.5 bg-emerald-500 rounded-full"
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
              <div class="truncate text-right font-medium text-slate-300">
                <span :class="m.home === '维尔通精英' ? 'text-emerald-400 font-bold' : ''">
                  {{ m.home }}
                </span>
              </div>

              <!-- 3. 比分药丸 (固定46px，水平严格居中对齐) -->
              <div class="flex justify-center">
                <span class="font-mono font-bold bg-slate-950 text-slate-100 px-2 py-0.5 rounded text-[11px] border border-slate-800 text-center w-[46px] block tracking-wider">
                  {{ m.score }}
                </span>
              </div>

              <!-- 4. 客队 (1fr 弹性宽度，向左对齐贴向比分) -->
              <div class="truncate text-left font-medium text-slate-300">
                <span :class="m.away === '维尔通精英' ? 'text-emerald-400 font-bold' : ''">
                  {{ m.away }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- 世界背景板 2：欧洲主要联赛同日/同期快讯 (比甲 + 五大联赛) -->
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

      <!-- ==================== TAB 2: 👥 阵容&战术 (2D绿茵场 + 球员硬核数据 + 六维雷达图) ==================== -->
      <section v-if="activeTab === 'lineup' && currentMatch" class="p-4 space-y-4">
        
        <!-- 顶栏切换模式 (2D绿茵战术板 vs 详细列表) -->
        <div class="flex items-center justify-between text-xs">
          <div>
            <div class="font-bold text-white flex items-center space-x-1.5">
              <span>首发阵型：4-2-3-1</span>
              <span class="text-[9px] bg-emerald-950 text-emerald-400 border border-emerald-800 px-1.5 rounded">高位压迫</span>
            </div>
            <div class="text-[10px] text-slate-400 mt-0.5">点击场上球员圆点，查看单场硬核数据与雷达图</div>
          </div>
          <div class="bg-slate-900 border border-slate-800 rounded-lg p-0.5 flex space-x-1">
            <button
              @click="lineupViewMode = 'pitch'"
              :class="['px-2.5 py-1 rounded text-[11px] font-semibold transition', lineupViewMode === 'pitch' ? 'bg-emerald-600 text-white font-bold' : 'text-slate-400 hover:text-white']"
            >
              2D球场
            </button>
            <button
              @click="lineupViewMode = 'list'"
              :class="['px-2.5 py-1 rounded text-[11px] font-semibold transition', lineupViewMode === 'list' ? 'bg-emerald-600 text-white font-bold' : 'text-slate-400 hover:text-white']"
            >
              列表对比
            </button>
          </div>
        </div>

        <!-- 1. 绿茵场 2D 俯视战术板 (4-2-3-1 阵型草坪布阵) -->
        <div v-show="lineupViewMode === 'pitch'" class="relative w-full aspect-[4/4.8] max-w-sm mx-auto rounded-2xl overflow-hidden border border-emerald-600/40 shadow-2xl bg-gradient-to-b from-emerald-950 via-emerald-900 to-emerald-950 p-2 select-none">
          <!-- 球场草皮条纹交替背景 -->
          <div class="absolute inset-0 flex flex-col pointer-events-none opacity-20">
            <div v-for="i in 8" :key="i" class="flex-1 odd:bg-black/25 even:bg-white/10"></div>
          </div>

          <!-- 球场白线标识 (SVG) -->
          <svg class="absolute inset-2 w-[calc(100%-16px)] h-[calc(100%-16px)] pointer-events-none stroke-emerald-300/40 fill-none" viewBox="0 0 100 120" preserveAspectRatio="none">
            <!-- 边线与中线 -->
            <rect x="2" y="2" width="96" height="116" stroke-width="0.8" rx="2" />
            <line x1="2" y1="60" x2="98" y2="60" stroke-width="0.8" />
            <circle cx="50" cy="60" r="14" stroke-width="0.8" />
            <circle cx="50" cy="60" r="1" fill="#34d399" />
            <!-- 上方禁区 (对方半场) -->
            <rect x="22" y="2" width="56" height="20" stroke-width="0.8" />
            <rect x="36" y="2" width="28" height="7" stroke-width="0.8" />
            <path d="M 38 22 A 12 12 0 0 0 62 22" stroke-width="0.8" />
            <!-- 下方禁区 (我方半场守门员侧) -->
            <rect x="22" y="98" width="56" height="20" stroke-width="0.8" />
            <rect x="36" y="111" width="28" height="7" stroke-width="0.8" />
            <path d="M 38 98 A 12 12 0 0 1 62 98" stroke-width="0.8" />
          </svg>

          <!-- 11位球员战术棋子 -->
          <div
            v-for="p in formationPlayers"
            :key="p.name_en || p.name"
            @click="selectedPlayer = p"
            :style="{ top: p.pitch_top, left: p.pitch_left }"
            :class="[
              'absolute -translate-x-1/2 -translate-y-1/2 cursor-pointer flex flex-col items-center group transition-all duration-200 z-10',
              selectedPlayer?.name_en === p.name_en ? 'scale-110 z-20' : 'hover:scale-105'
            ]"
          >
            <!-- 棋子圆点 -->
            <div :class="[
              'w-8 h-8 rounded-full border-2 flex items-center justify-center shadow-lg text-[10px] font-black transition relative',
              selectedPlayer?.name_en === p.name_en
                ? 'bg-amber-400 text-slate-950 border-white ring-4 ring-amber-400/50 shadow-amber-500/50'
                : p.is_mvp
                  ? 'bg-emerald-500 text-slate-950 border-amber-300 ring-2 ring-emerald-400/40 shadow-emerald-500/50'
                  : 'bg-slate-900/95 text-white border-emerald-400/80 hover:border-emerald-300'
            ]">
              <span>{{ p.pos }}</span>
              <!-- MVP 标记 -->
              <span v-if="p.is_mvp" class="absolute -top-2 -right-1 text-[8px] bg-amber-400 text-slate-950 rounded-full px-1 font-black shadow">★</span>
              <!-- 评分小角标 -->
              <span :class="[
                'absolute -bottom-1 -right-2 text-[8px] font-bold px-1 rounded-full shadow border border-slate-900',
                p.rating >= 7.5 ? 'bg-emerald-500 text-slate-950 font-black' :
                p.rating >= 7.0 ? 'bg-teal-500 text-slate-950' : 'bg-slate-800 text-slate-200'
              ]">
                {{ p.rating }}
              </span>
            </div>
            <!-- 中文姓名气泡 -->
            <div :class="[
              'mt-1 px-1.5 py-0.2 rounded text-[9px] font-bold tracking-tight whitespace-nowrap shadow backdrop-blur transition border',
              selectedPlayer?.name_en === p.name_en
                ? 'bg-amber-400 text-slate-950 font-black border-amber-300'
                : 'bg-slate-950/85 text-slate-200 border-slate-800'
            ]">
              {{ p.name_zh || p.name }}
            </div>
          </div>
        </div>

        <!-- 2. 选中球员详情卡片 (硬核数据 + 六维雷达图) -->
        <div v-if="activePlayer" class="bg-slate-900 rounded-xl border border-slate-800 p-3.5 space-y-3 shadow-lg animate-in fade-in duration-200">
          <!-- 球员名片顶栏 -->
          <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
            <div class="flex items-center space-x-2.5">
              <span class="w-8 h-8 rounded-lg bg-emerald-950 text-emerald-400 border border-emerald-800 flex items-center justify-center font-black text-xs">
                {{ activePlayer.pos }}
              </span>
              <div>
                <div class="font-black text-sm text-white flex items-center space-x-1.5">
                  <span>{{ activePlayer.name_zh || activePlayer.name }}</span>
                  <span v-if="activePlayer.is_mvp" class="text-[9px] bg-amber-400 text-slate-950 font-black px-1.5 py-0.2 rounded">全场最佳</span>
                </div>
                <div class="text-[10px] text-slate-400 mt-0.5">
                  {{ activePlayer.name_en || activePlayer.name }} · 出场 {{ activePlayer.min || 90 }} 分钟
                </div>
              </div>
            </div>

            <!-- 赛后评分徽章 -->
            <div class="text-right">
              <div :class="[
                'text-lg font-black px-2.5 py-0.5 rounded-lg border inline-block',
                activePlayer.rating >= 7.5 ? 'bg-emerald-950 text-emerald-400 border-emerald-800' :
                activePlayer.rating >= 7.0 ? 'bg-teal-950 text-teal-300 border-teal-800' :
                'bg-slate-850 text-slate-300 border-slate-700'
              ]">
                {{ activePlayer.rating }}
              </div>
              <div class="text-[9px] text-slate-500 mt-0.5">FM 赛后评分</div>
            </div>
          </div>

          <!-- 六维雷达图与指标透视 -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center">
            
            <!-- SVG 六维雷达图 -->
            <div class="flex flex-col items-center justify-center bg-slate-950 rounded-lg p-2 border border-slate-850 relative">
              <div class="text-[10px] font-bold text-slate-400 mb-1">六维赛场发挥雷达</div>
              <svg class="w-44 h-44 overflow-visible" viewBox="0 0 180 180">
                <!-- 背景多边形同心网格 (25%, 50%, 75%, 100%) -->
                <polygon
                  v-for="lvl in [0.25, 0.5, 0.75, 1.0]"
                  :key="lvl"
                  :points="getRadarPolygonPoints(activePlayer.radar, 90, 90, 60 * lvl, true)"
                  class="stroke-slate-800/80 fill-none"
                  stroke-width="1"
                />
                <!-- 轴线 -->
                <line
                  v-for="(axis, aIdx) in (activePlayer.radar || [])"
                  :key="aIdx"
                  :x1="90"
                  :y1="90"
                  :x2="getRadarVertexCoord(aIdx, activePlayer.radar.length, 90, 90, 60).x"
                  :y2="getRadarVertexCoord(aIdx, activePlayer.radar.length, 90, 90, 60).y"
                  class="stroke-slate-800"
                  stroke-width="1"
                />
                <!-- 真实数据多边形 -->
                <polygon
                  :points="getRadarPolygonPoints(activePlayer.radar, 90, 90, 60)"
                  class="fill-emerald-500/30 stroke-emerald-400 transition-all duration-300"
                  stroke-width="2"
                />
                <!-- 各顶点小圆点 -->
                <circle
                  v-for="(pt, pIdx) in getRadarPointCoords(activePlayer.radar, 90, 90, 60)"
                  :key="pIdx"
                  :cx="pt.x"
                  :cy="pt.y"
                  r="3"
                  class="fill-emerald-400 stroke-slate-950"
                  stroke-width="1"
                />
                <!-- 维度标签文字 -->
                <text
                  v-for="(item, tIdx) in (activePlayer.radar || [])"
                  :key="'t_' + tIdx"
                  :x="getRadarVertexCoord(tIdx, activePlayer.radar.length, 90, 90, 75).x"
                  :y="getRadarVertexCoord(tIdx, activePlayer.radar.length, 90, 90, 75).y + 3"
                  class="fill-slate-400 text-[9px] font-sans font-medium text-center"
                  text-anchor="middle"
                >
                  {{ item.subject }}
                </text>
              </svg>
            </div>

            <!-- 6项硬核单场技战术统计 -->
            <div class="grid grid-cols-2 gap-2 text-xs">
              <div
                v-for="(val, key) in (activePlayer.stats || {})"
                :key="key"
                class="bg-slate-950 p-2 rounded-lg border border-slate-850"
              >
                <div class="text-[10px] text-slate-400 truncate">{{ key }}</div>
                <div class="font-black text-sm text-white mt-0.5 tracking-tight">{{ val }}</div>
              </div>
            </div>

          </div>

        </div>

        <!-- 3. 全队列表对比视图 (无论在哪个模式下都可查看) -->
        <div class="space-y-1.5 pt-1">
          <div class="text-[11px] font-bold text-slate-400 mb-1 flex items-center justify-between">
            <span>全队首发清单 · 点击任一球员即可定位</span>
            <span class="text-[10px] text-slate-500">共 11 人首发</span>
          </div>

          <div
            v-for="p in currentMatch.lineup"
            :key="p.name_en || p.name"
            @click="selectedPlayer = p"
            :class="[
              'flex items-center justify-between p-2.5 rounded-lg border text-xs cursor-pointer transition',
              selectedPlayer?.name_en === p.name_en
                ? 'bg-slate-850 border-emerald-500 shadow-sm'
                : 'bg-slate-900 border-slate-800 hover:border-slate-700'
            ]"
          >
            <div class="flex items-center space-x-2.5">
              <span class="w-7 text-[10px] font-bold text-slate-400 text-center bg-slate-800 px-1 py-0.5 rounded shrink-0">
                {{ p.pos }}
              </span>
              <div>
                <div class="font-bold text-slate-200 flex items-center space-x-1.5">
                  <span>{{ p.name_zh || p.name }}</span>
                  <span v-if="p.is_mvp" class="text-[9px] bg-amber-500 text-slate-950 font-black px-1 rounded">MVP</span>
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

      <!-- ==================== TAB 3: 📊 球队分析 (战术体系 + 攻防走廊 + 技战术雷达 + 优劣势透视) ==================== -->
      <section v-if="activeTab === 'analysis'" class="p-4 space-y-4">
        
        <!-- 战术身份徽章 -->
        <div class="bg-gradient-to-r from-slate-900 to-slate-950 border border-slate-800 rounded-xl p-3.5 space-y-2.5">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="text-base">📋</span>
              <h3 class="font-black text-white text-xs">维尔通精英 · 战术哲学架构</h3>
            </div>
            <span class="text-[9px] bg-emerald-950 text-emerald-400 border border-emerald-800 px-2 py-0.5 rounded-full font-bold">
              徐指导战术档案
            </span>
          </div>

          <div class="grid grid-cols-3 gap-2 text-center text-xs">
            <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
              <div class="text-[10px] text-slate-400">核心阵型</div>
              <div class="font-black text-white mt-0.5">{{ teamAnalysis?.tactical_system?.formation || teamAnalysis?.tactical_overview?.formation || '4-2-3-1' }}</div>
            </div>
            <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
              <div class="text-[10px] text-slate-400">战术风格</div>
              <div class="font-bold text-emerald-400 mt-0.5 truncate text-[11px]">{{ teamAnalysis?.tactical_system?.style_name || teamAnalysis?.tactical_overview?.mentality || '全场高位反抢' }}</div>
            </div>
            <div class="bg-slate-950 p-2 rounded-lg border border-slate-850">
              <div class="text-[10px] text-slate-400">战术节奏</div>
              <div class="font-black text-white mt-0.5">{{ teamAnalysis?.tactical_system?.tempo || '极快节奏' }}</div>
            </div>
          </div>
        </div>

        <!-- 三路进攻推进走廊分布 -->
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-2.5">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-white flex items-center space-x-1.5">
              <span>🏹</span>
              <span>三路进攻发起权重 (Attack Channels)</span>
            </span>
            <span class="text-[10px] text-emerald-400 font-bold">右路托明走廊占优</span>
          </div>

          <!-- 分布走廊三段进度条 -->
          <div class="w-full bg-slate-950 h-3 rounded-full overflow-hidden flex border border-slate-800">
            <div class="bg-teal-600 h-full flex items-center justify-center text-[8px] text-white font-black" :style="{ width: `${teamAnalysis?.attack_channels?.left_wing || teamAnalysis?.attack_channels?.left || 29}%` }">
              左 {{ teamAnalysis?.attack_channels?.left_wing || teamAnalysis?.attack_channels?.left || 29 }}%
            </div>
            <div class="bg-slate-700 h-full flex items-center justify-center text-[8px] text-slate-200 font-black" :style="{ width: `${teamAnalysis?.attack_channels?.center || 28}%` }">
              中 {{ teamAnalysis?.attack_channels?.center || 28 }}%
            </div>
            <div class="bg-emerald-500 h-full flex items-center justify-center text-[8px] text-slate-950 font-black" :style="{ width: `${teamAnalysis?.attack_channels?.right_wing || teamAnalysis?.attack_channels?.right || 43}%` }">
              右 {{ teamAnalysis?.attack_channels?.right_wing || teamAnalysis?.attack_channels?.right || 43 }}%
            </div>
          </div>

          <div class="grid grid-cols-3 gap-2 text-center text-[10px] text-slate-400 pt-1">
            <div>左路发起 ({{ teamAnalysis?.attack_channels?.left_wing || teamAnalysis?.attack_channels?.left || 29 }}%)</div>
            <div>中路渗透 ({{ teamAnalysis?.attack_channels?.center || 28 }}%)</div>
            <div class="text-emerald-400 font-bold">右路突击 ({{ teamAnalysis?.attack_channels?.right_wing || teamAnalysis?.attack_channels?.right || 43 }}% ★)</div>
          </div>
        </div>

        <!-- 技战术能力指标 vs 联赛平均水准对比条 -->
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-3">
          <div class="flex items-center justify-between text-xs font-bold text-white">
            <span class="flex items-center space-x-1.5">
              <span>📈</span>
              <span>核心战术指标对标 (维尔通 vs 比乙平均)</span>
            </span>
            <span class="text-[10px] text-slate-400 font-normal">基于前8轮官方数据</span>
          </div>

          <div class="space-y-2.5">
            <div
              v-for="m in (teamAnalysis?.team_radar || [])"
              :key="m.label"
              class="space-y-1 text-xs"
            >
              <div class="flex justify-between items-center text-[11px]">
                <span class="text-slate-300 font-bold">{{ m.label }}</span>
                <div class="flex items-center space-x-2 font-mono">
                  <span class="text-emerald-400 font-black">{{ m.value }}分</span>
                  <span class="text-slate-500 text-[10px]">(比乙均值: {{ m.league_avg }})</span>
                </div>
              </div>
              
              <!-- 双层对比条 -->
              <div class="w-full bg-slate-950 h-2 rounded-full overflow-hidden relative border border-slate-800">
                <!-- 联赛基准线 (灰色) -->
                <div class="bg-slate-700/60 h-full absolute top-0 left-0" :style="{ width: `${m.league_avg}%` }"></div>
                <!-- 维尔通实力线 (翡翠绿) -->
                <div class="bg-emerald-500 h-full rounded-full transition-all duration-500 relative z-10" :style="{ width: `${m.value}%` }"></div>
              </div>
              <div class="text-[9px] text-slate-500">{{ m.desc }}</div>
            </div>
          </div>
        </div>

        <!-- 战术优劣势透视 -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <!-- 优势 -->
          <div class="bg-slate-900 border border-emerald-900/60 rounded-xl p-3 space-y-1.5">
            <div class="text-xs font-bold text-emerald-400 flex items-center space-x-1">
              <span>✅</span>
              <span>主帅体系核心优势</span>
            </div>
            <ul class="space-y-1 text-[11px] text-slate-300">
              <li v-for="(str, sIdx) in (teamAnalysis?.strengths || [])" :key="sIdx" class="leading-relaxed">
                • {{ str }}
              </li>
            </ul>
          </div>

          <!-- 隐患 -->
          <div class="bg-slate-900 border border-rose-900/60 rounded-xl p-3 space-y-1.5">
            <div class="text-xs font-bold text-rose-400 flex items-center space-x-1">
              <span>⚠️</span>
              <span>潜在技战术与阵容隐患</span>
            </div>
            <ul class="space-y-1 text-[11px] text-slate-300">
              <li v-for="(c, cIdx) in (teamAnalysis?.concerns || [])" :key="cIdx" class="leading-relaxed">
                • {{ c }}
              </li>
            </ul>
          </div>
        </div>

        <!-- 欧洲名宿战术点评 -->
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-1.5">
          <div class="text-xs font-bold text-slate-200 flex items-center space-x-1.5">
            <span>📰</span>
            <span>外媒专栏 · 战术观察哨</span>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed font-sans bg-slate-950 p-2.5 rounded-lg border border-slate-850">
            {{ teamAnalysis?.analyst_quote || teamAnalysis?.media_quote?.content || '暂无外媒点评' }}
          </p>
        </div>

      </section>

      <!-- ==================== TAB 4: 📰 战报资讯 (客观公域战报) ==================== -->
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
            <span>当地媒体《L'Avenir》社论摘要</span>
          </div>
          <p class="text-[11px] text-slate-400 leading-relaxed italic">
            “{{ currentNews.local_media_snippet?.quote || '维尔通在战术执行力上展现出惊人纪律，但能否在紧密的赛程下保持高位逼抢的体能负荷，将是未来数周的最大考验。' }}”
          </p>
          <div class="text-[9px] text-slate-500 text-right mt-1">
            —— 首席记者 {{ currentNews.local_media_snippet?.journalist || 'Philippe De Witte' }}
          </div>
        </div>
      </section>

      <!-- ==================== TAB 5: 🔥 球迷热评 (虎扑风格热评区) ==================== -->
      <section v-if="activeTab === 'comments' && currentNews" class="p-4 space-y-4">
        
        <!-- 主帅评分卡片 -->
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 flex items-center justify-between shadow-sm">
          <div>
            <div class="text-xs text-slate-400">本场主帅综合战术评分</div>
            <div class="text-xs text-slate-500 mt-0.5">超过 2,481 名球迷参与投票</div>
          </div>
          <div class="text-right">
            <span :class="['text-3xl font-black tracking-tight', coachScoreColor]">
              {{ currentNews.hupu_thread.coach_score }}
            </span>
            <span class="text-xs text-slate-400 font-bold ml-0.5">/ 10</span>
          </div>
        </div>

        <!-- 虎扑高亮热评列表 -->
        <div class="space-y-3">
          <div class="flex justify-between items-center text-xs text-slate-400">
            <span class="font-bold text-slate-200">🔥 虎扑亮了·全网热议</span>
            <span>按赞同排序</span>
          </div>

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

      <!-- ==================== TAB 6: 🏆 榜单大盘 (积分榜 + 比乙射手榜 + 助攻榜 + 纪律榜) ==================== -->
      <section v-if="activeTab === 'standings'" class="p-4 space-y-3">
        
        <!-- 榜单类型子切换条 (积分 / 射手 / 助攻 / 纪律) -->
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-1 flex items-center space-x-1 text-xs">
          <button
            @click="standingsSubTab = 'points'"
            :class="['flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1', standingsSubTab === 'points' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white']"
          >
            <span>🏆</span>
            <span>联赛积分榜</span>
          </button>
          <button
            @click="standingsSubTab = 'scorers'"
            :class="['flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1', standingsSubTab === 'scorers' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white']"
          >
            <span>⚽</span>
            <span>比乙射手榜</span>
          </button>
          <button
            @click="standingsSubTab = 'assists'"
            :class="['flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1', standingsSubTab === 'assists' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white']"
          >
            <span>👟</span>
            <span>比乙助攻榜</span>
          </button>
          <button
            @click="standingsSubTab = 'discipline'"
            :class="['flex-1 py-1.5 rounded-lg font-bold text-center transition flex items-center justify-center space-x-1', standingsSubTab === 'discipline' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white']"
          >
            <span>🟨</span>
            <span>纪律榜</span>
          </button>
        </div>

        <!-- ===== 子视图 1: 欧洲各大联赛完整积分榜 (七大联赛完整收录) ===== -->
        <div v-show="standingsSubTab === 'points'" class="space-y-3">
          <!-- 七大联赛横向切换选择器 (比乙、比甲、英超、西甲、意甲、德甲、法甲) -->
          <div class="relative flex items-center bg-slate-900 rounded-xl p-1 border border-slate-800">
            <!-- 左滑箭头 -->
            <button
              @click="scrollLeagues(-100)"
              class="w-6 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs shrink-0 transition"
              title="向左滚动"
            >
              ‹
            </button>

            <!-- 滚动按钮区 -->
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

            <!-- 右滑箭头 -->
            <button
              @click="scrollLeagues(100)"
              class="w-6 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs shrink-0 transition"
              title="向右滚动"
            >
              ›
            </button>
          </div>

          <!-- 当前选中联赛的提示信息 -->
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
        </div>

        <!-- ===== 子视图 2: 比乙官方射手榜 ===== -->
        <div v-show="standingsSubTab === 'scorers'" class="space-y-3">
          <div class="bg-slate-900 border border-slate-800 rounded-lg p-2.5 flex items-center justify-between text-xs">
            <span class="font-bold text-white">🇧🇪 比乙联赛 · 官方金靴射手榜</span>
            <span class="text-[10px] text-emerald-400 font-medium">保罗·韦德 2球排第4</span>
          </div>

          <div class="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden text-xs">
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="bg-slate-850 text-slate-400 border-b border-slate-800 text-[10px]">
                  <th class="py-2.5 px-2 text-center w-8">#</th>
                  <th class="py-2.5 px-2">球员 / 俱乐部</th>
                  <th class="py-2.5 px-1 text-center w-8">场次</th>
                  <th class="py-2.5 px-1 text-center w-8">射门</th>
                  <th class="py-2.5 px-2 text-center font-bold w-10">进球</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="s in leaderboards.scorers"
                  :key="s.rank"
                  :class="[
                    'border-b border-slate-800/60 transition hover:bg-slate-850',
                    s.is_virton ? 'bg-emerald-950/60 font-bold text-emerald-300 border-l-2 border-emerald-500' : 'text-slate-300'
                  ]"
                >
                  <td class="py-2 px-2 text-center font-bold">
                    <span :class="[
                      'w-5 h-5 rounded flex items-center justify-center text-[10px] mx-auto',
                      s.rank === 1 ? 'bg-amber-400 text-slate-950 font-black' :
                      s.rank <= 3 ? 'bg-amber-400/20 text-amber-300 font-bold' : 'text-slate-400'
                    ]">
                      {{ s.rank }}
                    </span>
                  </td>
                  <td class="py-2 px-2 truncate max-w-[140px]">
                    <div class="flex items-center space-x-1.5">
                      <span class="font-bold text-slate-200">{{ s.player_zh }}</span>
                      <span v-if="s.is_virton" class="text-[9px] bg-emerald-600 text-white px-1 rounded font-normal">本队</span>
                    </div>
                    <div class="text-[10px] text-slate-500 truncate">{{ s.team_short }}</div>
                  </td>
                  <td class="py-2 px-1 text-center text-slate-400">{{ s.matches }}</td>
                  <td class="py-2 px-1 text-center text-slate-400">{{ s.shots }}</td>
                  <td class="py-2 px-2 text-center font-black text-amber-400 text-sm">{{ s.goals }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- ===== 子视图 3: 比乙官方助攻榜 ===== -->
        <div v-show="standingsSubTab === 'assists'" class="space-y-3">
          <div class="bg-slate-900 border border-slate-800 rounded-lg p-2.5 flex items-center justify-between text-xs">
            <span class="font-bold text-white">🇧🇪 比乙联赛 · 官方助攻榜</span>
            <span class="text-[10px] text-emerald-400 font-bold">泰伦·托明 2次并列第1</span>
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
                  v-for="a in leaderboards.assists"
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

        <!-- ===== 子视图 4: 比乙纪律榜 (红黄牌与停赛风险) ===== -->
        <div v-show="standingsSubTab === 'discipline'" class="space-y-3">
          <div class="bg-slate-900 border border-slate-800 rounded-lg p-2.5 flex items-center justify-between text-xs">
            <span class="font-bold text-white">🇧🇪 比乙联赛 · 纪律榜与停赛监控</span>
            <span class="text-[10px] text-amber-400 font-bold">梅扎古 2黄预警</span>
          </div>

          <div class="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden text-xs">
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="bg-slate-850 text-slate-400 border-b border-slate-800 text-[10px]">
                  <th class="py-2.5 px-2 text-center w-8">#</th>
                  <th class="py-2.5 px-2">球员 / 俱乐部</th>
                  <th class="py-2.5 px-1 text-center w-8">🟨 黄</th>
                  <th class="py-2.5 px-1 text-center w-8">🟥 红</th>
                  <th class="py-2.5 px-2 text-center font-bold w-14">状态</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="d in leaderboards.discipline"
                  :key="d.rank"
                  :class="[
                    'border-b border-slate-800/60 transition hover:bg-slate-850',
                    d.is_virton ? 'bg-amber-950/20 font-bold border-l-2 border-amber-500' : 'text-slate-300'
                  ]"
                >
                  <td class="py-2 px-2 text-center font-bold text-slate-400">{{ d.rank }}</td>
                  <td class="py-2 px-2 truncate max-w-[140px]">
                    <div class="flex items-center space-x-1.5">
                      <span class="font-bold text-slate-200">{{ d.player_zh }}</span>
                      <span v-if="d.is_virton" class="text-[9px] bg-amber-600 text-white px-1 rounded font-normal">本队</span>
                    </div>
                    <div class="text-[10px] text-slate-500 truncate">{{ d.team_short }}</div>
                  </td>
                  <td class="py-2 px-1 text-center text-amber-400 font-bold">{{ d.yellow_cards ?? d.yellow ?? 0 }}</td>
                  <td class="py-2 px-1 text-center text-rose-500 font-bold">{{ d.red_cards ?? d.red ?? 0 }}</td>
                  <td class="py-2 px-2 text-center">
                    <span :class="[
                      'text-[9px] px-1.5 py-0.5 rounded font-bold',
                      (d.status || d.suspension_warning || '').includes('停赛') ? 'bg-rose-950 text-rose-400 border border-rose-800' :
                      (d.status || d.suspension_warning || '').includes('警告') ? 'bg-amber-950 text-amber-300 border border-amber-800' : 'bg-slate-800 text-slate-400'
                    ]">
                      {{ d.status || d.suspension_warning || '正常' }}
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
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
import { ref, computed, watch } from 'vue'

import matchesData from './data/matches.json'
import newsData from './data/news.json'
import multiLeaguesData from './data/standings.json'
import mailboxData from './data/mailbox.json'
import roundMatchesData from './data/round_matches.json'
import worldNewsData from './data/world_news.json'
import teamAnalysisData from './data/team_analysis.json'
import leaderboardsData from './data/leaderboards.json'

const matches = ref(matchesData)
const news = ref(newsData)
const mailbox = ref(mailboxData)
const roundMatches = ref(roundMatchesData)
const worldNews = ref(worldNewsData)
const availableLeagues = ref(multiLeaguesData.leagues || [])
const teamAnalysis = ref(teamAnalysisData)
const leaderboards = ref(leaderboardsData)

// 选中的轮次 (默认最新轮次)
const currentRound = ref(matches.value.length ? matches.value[matches.value.length - 1].round : 8)

// 选中的公域主导航 Tab (6大功能模块)
const activeTab = ref('matches')
const tabs = [
  { key: 'matches', label: '⚽ 赛事大盘' },
  { key: 'lineup', label: '👥 阵容&战术' },
  { key: 'analysis', label: '📊 球队分析' },
  { key: 'report', label: '📰 战报资讯' },
  { key: 'comments', label: '🔥 球迷热评' },
  { key: 'standings', label: '🏆 榜单大盘' }
]

// 阵容视图模式：2D绿茵战术板 vs 详细列表
const lineupViewMode = ref('pitch')

// 选中的球员 (用于展示六维雷达图与具体技术统计)
const selectedPlayer = ref(null)

// 榜单子Tab：积分榜 vs 射手榜 vs 助攻榜 vs 纪律榜
const standingsSubTab = ref('points')

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

// 控制私域主帅信箱弹窗显示/隐藏
const showMailbox = ref(false)

// 联赛大盘中选中的联赛 (默认比乙)
const selectedLeagueId = ref('bel_d2')
const currentDisplayLeague = computed(() => {
  return availableLeagues.value.find(l => l.id === selectedLeagueId.value) || availableLeagues.value[0]
})

// 五大联赛官方矢量 Icon 映射 (基于阿里 Iconfont Symbol JS)
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

// 4-1-1-3-1 非对称密集短传 绿茵战术板阵型坐标映射
const formationPlayers = computed(() => {
  if (!currentMatch.value?.lineup) return []
  const lineup = currentMatch.value.lineup
  const coords = {
    'GK': { top: '89%', left: '50%' },
    'DL': { top: '70%', left: '16%' },
    'DC1': { top: '74%', left: '38%' },
    'DC2': { top: '74%', left: '62%' },
    'DR': { top: '70%', left: '84%' },
    'DM': { top: '56%', left: '38%' },
    'MC': { top: '48%', left: '64%' },
    'AML': { top: '30%', left: '20%' },
    'AMC': { top: '30%', left: '50%' },
    'AMR': { top: '30%', left: '80%' },
    'ST': { top: '12%', left: '50%' }
  }
  let dcCount = 0
  return lineup.map((p) => {
    let posKey = p.pos
    if (posKey.includes('DC')) {
      dcCount++
      posKey = dcCount === 1 ? 'DC1' : 'DC2'
    }
    const coord = coords[posKey] || { top: '50%', left: '50%' }
    return {
      ...p,
      pitch_top: coord.top,
      pitch_left: coord.left
    }
  })
})

// 默认选中的活跃球员
const activePlayer = computed(() => {
  if (selectedPlayer.value) {
    // 匹配当前轮次阵型里的该球员
    const matchInCur = formationPlayers.value.find(p => p.name_en === selectedPlayer.value.name_en || p.name === selectedPlayer.value.name)
    if (matchInCur) return matchInCur
  }
  // 默认取 MVP 或前锋
  return formationPlayers.value.find(p => p.is_mvp) || formationPlayers.value[formationPlayers.value.length - 1] || formationPlayers.value[0]
})

// 切换轮次时自动选定焦点球员
watch(currentRound, () => {
  selectedPlayer.value = null
})

// SVG 雷达图数学几何计算函数
const getRadarPolygonPoints = (radar, cx = 90, cy = 90, r = 60, isBackground = false) => {
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

const getRadarVertexCoord = (i, n = 6, cx = 90, cy = 90, r = 60) => {
  const angle = (i * 2 * Math.PI / n) - (Math.PI / 2)
  return {
    x: Number((cx + r * Math.cos(angle)).toFixed(1)),
    y: Number((cy + r * Math.sin(angle)).toFixed(1))
  }
}

const getRadarPointCoords = (radar, cx = 90, cy = 90, r = 60) => {
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
