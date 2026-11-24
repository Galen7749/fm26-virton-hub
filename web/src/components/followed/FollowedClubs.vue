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
          <div class="text-[10px] text-slate-500">联赛战绩积分</div>
          <div class="font-bold font-mono text-slate-200 mt-0.5">
            {{ activeClub.stats.won }}胜 {{ activeClub.stats.drawn }}平 {{ activeClub.stats.lost }}负 ({{ activeClub.stats.points }}分)
          </div>
        </div>

        <!-- 主场球场 -->
        <div class="bg-slate-950/70 p-2 rounded-xl border border-slate-850">
          <div class="text-[10px] text-slate-500">主场球场</div>
          <div class="font-bold text-slate-300 truncate mt-0.5 inline-flex items-center gap-1">
            <Icon icon="mdi:soccer-field" class="w-3 h-3 text-slate-500 shrink-0" />
            <span class="truncate">{{ activeClub.stadium }}</span>
          </div>
        </div>
      </div>

      <!-- 近 5 场走势条 (W/D/L 紧凑圆形勋章) -->
      <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs relative z-10">
        <span class="text-[11px] text-slate-400 font-medium inline-flex items-center gap-1">
          <Icon icon="lucide:activity" class="w-3 h-3 text-emerald-400" />
          <span>近 5 场正赛走势</span>
        </span>
        <div class="flex items-center space-x-1.5">
          <span
            v-for="(res, idx) in activeClub.recent_form"
            :key="idx"
            :class="[
              'w-5 h-5 rounded-full flex items-center justify-center font-bold text-[10px] font-mono shadow-sm',
              res === 'W' ? 'bg-emerald-500 text-slate-950' :
              res === 'D' ? 'bg-amber-500 text-slate-950' : 'bg-rose-500 text-white'
            ]"
            :title="res === 'W' ? '胜' : res === 'D' ? '平' : '负'"
          >
            {{ res }}
          </span>
        </div>
      </div>
    </section>

    <!-- ─────────────────────────────────────────────────────────────
         第三层：底部【俱乐部全景四子 Tab 切换器】(动态 | 比赛 | 阵容 | 转会)
         ───────────────────────────────────────────────────────────── -->
    <section v-if="activeClub" class="space-y-3">
      <!-- 四子 Tab 按钮条 -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-1 flex items-center space-x-1 text-xs shadow-inner">
        <button
          v-for="sub in subTabs"
          :key="sub.key"
          @click="activeSubTab = sub.key"
          :class="[
            'flex-1 py-1.5 rounded-lg font-bold text-center transition inline-flex items-center justify-center gap-1.5',
            activeSubTab === sub.key
              ? 'bg-emerald-600 text-white shadow-sm'
              : 'text-slate-400 hover:text-white'
          ]"
        >
          <Icon :icon="sub.icon" class="w-3.5 h-3.5" />
          <span>{{ sub.name }}</span>
        </button>
      </div>

      <!-- ── 子 Tab 1: 【动态】(俱乐部快讯、球迷论坛置顶帖、赛事情报) ────── -->
      <div v-if="activeSubTab === 'dynamics'" class="space-y-2.5">
        <div
          v-for="item in activeClub.dynamics"
          :key="item.id"
          class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-1.5 shadow-sm hover:border-slate-700 transition"
        >
          <div class="flex items-center justify-between text-[10px]">
            <span class="inline-flex items-center gap-1 text-slate-400">
              <Icon icon="lucide:newspaper" class="w-2.5 h-2.5 text-emerald-400" />
              <span>{{ item.source }}</span>
            </span>
            <span class="text-slate-500 font-mono">{{ item.time }}</span>
          </div>
          <h3 class="text-xs sm:text-sm font-bold text-white leading-snug">
            {{ item.title }}
          </h3>
          <p class="text-[11px] text-slate-400 leading-relaxed line-clamp-2">
            {{ item.summary }}
          </p>
        </div>
      </div>

      <!-- ── 子 Tab 2: 【比赛】(已完赛记录 + 接下来 3 场赛程预告，点击进入比赛详情) ──── -->
      <div v-else-if="activeSubTab === 'matches'" class="space-y-3.5">
        <!-- 1. 已完赛赛果 -->
        <div class="space-y-2">
          <div class="flex items-center justify-between text-xs text-slate-300 px-1">
            <span class="font-bold inline-flex items-center gap-1.5">
              <Icon icon="lucide:check-circle" class="w-3.5 h-3.5 text-emerald-400" />
              <span>已完赛记录 ({{ activeClub.matches.completed.length }} 场)</span>
            </span>
            <span class="text-[10px] text-slate-500">点击卡片进入深度战报与阵容</span>
          </div>

          <div
            v-for="m in activeClub.matches.completed"
            :key="'comp-' + m.id"
            @click="$emit('select-match', m.id)"
            class="bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-emerald-500/70 rounded-xl p-3 space-y-2 shadow-sm cursor-pointer transition transform hover:-translate-y-0.5 group"
          >
            <div class="flex items-center justify-between text-[10px] text-slate-400 pb-1.5 border-b border-slate-800/80">
              <span class="font-bold text-slate-300 group-hover:text-emerald-400 transition">{{ m.round_label }}</span>
              <div class="inline-flex items-center gap-1.5">
                <span class="font-mono">{{ m.date }}</span>
                <span class="text-[9px] text-emerald-400 bg-emerald-950/80 border border-emerald-800/80 px-1.5 py-0.2 rounded font-bold">查看战报 ›</span>
              </div>
            </div>

            <div class="flex items-center justify-between py-1">
              <div class="flex-1 text-right font-bold text-xs text-white truncate pr-2">
                {{ m.home_team }}
              </div>
              <div class="px-3 py-1 bg-slate-950 rounded-lg border border-slate-800 text-center font-mono font-black text-sm tracking-wider text-white group-hover:border-emerald-500/60 transition">
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

      <!-- ── 子 Tab 3: 【阵容】(球员卡片可点击查看 FM 真实属性：爆发力、速度、精神、技术) ── -->
      <div v-else-if="activeSubTab === 'squad'" class="space-y-2.5">
        <!-- 提示条 -->
        <div class="flex items-center justify-between text-[10px] text-slate-400 bg-emerald-950/40 border border-emerald-900/60 p-2 rounded-xl">
          <span class="inline-flex items-center gap-1.5 text-emerald-300 font-medium">
            <Icon icon="lucide:sparkles" class="w-3.5 h-3.5 text-emerald-400 shrink-0" />
            <span>点击任意球员卡片，查看 FM 游戏内全维度真实属性（爆发力、速度、精神、技术等）</span>
          </span>
        </div>

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

        <!-- 球员详细列表 (可点击弹出 FM 全属性面板) -->
        <div class="space-y-1.5">
          <div
            v-for="player in filteredSquad"
            :key="player.number + player.name"
            @click="selectedPlayer = player"
            class="bg-slate-900 hover:bg-slate-850 border border-slate-800 hover:border-emerald-500/60 rounded-xl p-2.5 flex items-center justify-between gap-2 shadow-sm transition cursor-pointer group"
          >
            <!-- 左侧：号码、姓名、年龄、国籍、位置 -->
            <div class="flex items-center space-x-2.5 min-w-0 flex-1">
              <!-- 号码 -->
              <span class="w-6 h-6 rounded-md bg-slate-950 border border-slate-800 flex items-center justify-center font-mono font-black text-xs text-slate-300 shrink-0 group-hover:border-emerald-500/50 transition">
                {{ player.number }}
              </span>

              <!-- 姓名与基础信息 -->
              <div class="min-w-0 flex-1">
                <div class="flex items-center space-x-1.5">
                  <span class="text-xs font-bold text-white truncate group-hover:text-emerald-400 transition">{{ player.name_zh || player.name }}</span>
                  <Icon :icon="player.flag" class="w-3 h-3 rounded-full shrink-0" />
                </div>
                <div class="flex items-center space-x-2 text-[10px] text-slate-400 mt-0.5 font-mono">
                  <span class="text-slate-300 font-bold px-1 py-0.2 bg-slate-950 rounded text-[9px] border border-slate-800">
                    {{ player.position }}
                  </span>
                  <span>{{ player.age }}岁</span>
                  <span v-if="player.height_cm">{{ player.height_cm }}cm</span>
                  <span>到期: {{ player.contract_until?.slice(0, 4) || player.contract_until }}</span>
                </div>
              </div>
            </div>

            <!-- 右侧：CA/PA、周薪、身价与查看详情指示 -->
            <div class="flex items-center space-x-3 shrink-0 text-right">
              <!-- CA / PA 潜能 -->
              <div v-if="player.ca" class="text-[10px] text-slate-400 font-mono">
                <div class="text-[9px] text-slate-500">能力/潜力</div>
                <div class="font-bold text-slate-200">{{ player.ca }} <span class="text-slate-500">/</span> {{ player.pa }}</div>
              </div>

              <!-- 身价 -->
              <div class="w-16 text-right">
                <div class="text-[9px] text-slate-500">身价</div>
                <div class="text-xs font-mono font-bold text-emerald-400">{{ player.market_value }}</div>
              </div>

              <!-- 箭头 -->
              <Icon icon="lucide:chevron-right" class="w-3.5 h-3.5 text-slate-600 group-hover:text-emerald-400 transition shrink-0" />
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
            <span>夏季转入 ({{ activeClub.transfers.in.length }} 人)</span>
          </div>

          <div
            v-for="(tIn, idx) in activeClub.transfers.in"
            :key="'in-' + idx"
            class="bg-slate-900 border border-slate-800 rounded-xl p-2.5 flex items-center justify-between text-xs shadow-sm"
          >
            <div class="flex items-center space-x-2">
              <span class="w-5 h-5 rounded-full bg-emerald-950 text-emerald-400 border border-emerald-800 flex items-center justify-center text-[10px] font-bold">
                +
              </span>
              <div>
                <span class="font-bold text-white">{{ tIn.name }}</span>
                <span class="text-[10px] text-slate-400 font-mono ml-1.5">{{ tIn.pos }}</span>
              </div>
            </div>
            <div class="text-right text-[11px]">
              <div class="text-slate-400 text-[10px] truncate max-w-[120px]">{{ tIn.from_team }}</div>
              <div class="font-mono text-emerald-400 font-bold">{{ tIn.fee }}</div>
            </div>
          </div>
        </div>

        <!-- 转出 Out -->
        <div class="space-y-2 pt-1">
          <div class="text-xs font-bold text-rose-400 px-1 inline-flex items-center gap-1.5">
            <Icon icon="lucide:arrow-up-right" class="w-3.5 h-3.5" />
            <span>夏季转出 ({{ activeClub.transfers.out.length }} 人)</span>
          </div>

          <div
            v-for="(tOut, idx) in activeClub.transfers.out"
            :key="'out-' + idx"
            class="bg-slate-900 border border-slate-800 rounded-xl p-2.5 flex items-center justify-between text-xs shadow-sm"
          >
            <div class="flex items-center space-x-2">
              <span class="w-5 h-5 rounded-full bg-rose-950 text-rose-400 border border-rose-800 flex items-center justify-center text-[10px] font-bold">
                -
              </span>
              <div>
                <span class="font-bold text-white">{{ tOut.name }}</span>
                <span class="text-[10px] text-slate-400 font-mono ml-1.5">{{ tOut.pos }}</span>
              </div>
            </div>
            <div class="text-right text-[11px]">
              <div class="text-slate-400 text-[10px] truncate max-w-[120px]">{{ tOut.to_team }}</div>
              <div class="font-mono text-rose-400 font-bold">{{ tOut.fee }}</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ─────────────────────────────────────────────────────────────
         弹窗 1：FM 真实球员全属性面板 Modal (爆发力、速度、精神、技术)
         ───────────────────────────────────────────────────────────── -->
    <div
      v-if="selectedPlayer"
      class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-3 animate-in fade-in"
      @click.self="selectedPlayer = null"
    >
      <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-lg w-full max-h-[90vh] overflow-y-auto p-4 space-y-4 shadow-2xl relative select-none">
        
        <!-- 1. 球员名片头部 -->
        <div class="flex items-start justify-between pb-3 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <!-- 球衣号码徽章 -->
            <div class="w-11 h-11 rounded-xl bg-slate-950 border border-slate-700 flex items-center justify-center font-mono font-black text-lg text-emerald-400 shadow-inner">
              {{ selectedPlayer.number }}
            </div>
            <div>
              <div class="flex items-center space-x-2">
                <h3 class="text-base font-black text-white">{{ selectedPlayer.name_zh || selectedPlayer.name }}</h3>
                <Icon :icon="selectedPlayer.flag" class="w-4 h-4 rounded-full" />
                <span class="text-[10px] text-slate-400">{{ selectedPlayer.nation }}</span>
              </div>
              <div class="text-[11px] text-slate-400 font-mono mt-0.5">
                {{ selectedPlayer.name_en || selectedPlayer.name }} · {{ selectedPlayer.position }} · {{ selectedPlayer.age }}岁 · {{ selectedPlayer.height_cm }}cm
              </div>
            </div>
          </div>

          <!-- 关闭按钮 -->
          <button
            @click="selectedPlayer = null"
            class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition"
          >
            <Icon icon="lucide:x" class="w-5 h-5" />
          </button>
        </div>

        <!-- 2. 合同与能力指标卡 -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
          <div class="bg-slate-950 p-2 rounded-xl border border-slate-850">
            <div class="text-[10px] text-slate-500">当前能力 / 潜力</div>
            <div class="font-mono font-black text-white mt-0.5">
              <span class="text-emerald-400">{{ selectedPlayer.ca }}</span>
              <span class="text-slate-600 mx-1">/</span>
              <span class="text-amber-400">{{ selectedPlayer.pa }}</span>
            </div>
          </div>

          <div class="bg-slate-950 p-2 rounded-xl border border-slate-850">
            <div class="text-[10px] text-slate-500">转会预估身价</div>
            <div class="font-mono font-bold text-emerald-400 mt-0.5">{{ selectedPlayer.market_value }}</div>
          </div>

          <div class="bg-slate-950 p-2 rounded-xl border border-slate-850">
            <div class="text-[10px] text-slate-500">周薪待遇</div>
            <div class="font-mono font-bold text-slate-300 mt-0.5">{{ selectedPlayer.wage_weekly }}</div>
          </div>

          <div class="bg-slate-950 p-2 rounded-xl border border-slate-850">
            <div class="text-[10px] text-slate-500">合同到期日</div>
            <div class="font-mono font-bold text-slate-300 mt-0.5">{{ selectedPlayer.contract_until }}</div>
          </div>
        </div>

        <!-- 3. 三列 FM 经典属性面板 (身体属性 / 技术属性 / 精神属性) -->
        <div v-if="selectedPlayer.attributes" class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
          
          <!-- 列 1: 身体属性 (Physical) - 爆发力、速度首发高亮 -->
          <div class="bg-slate-950 p-3 rounded-xl border border-slate-850 space-y-2">
            <div class="font-bold text-slate-200 pb-1 border-b border-slate-800 text-[11px] inline-flex items-center gap-1.5 w-full">
              <Icon icon="lucide:zap" class="w-3.5 h-3.5 text-amber-400" />
              <span>身体属性 (Physical)</span>
            </div>
            <div class="space-y-1.5 text-[11px]">
              <div class="flex items-center justify-between">
                <span class="text-amber-300 font-bold">爆发力 (Acceleration)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.physical?.acceleration)]">
                  {{ selectedPlayer.attributes.physical?.acceleration }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-amber-300 font-bold">速度 (Pace)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.physical?.pace)]">
                  {{ selectedPlayer.attributes.physical?.pace }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">耐力 (Stamina)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.physical?.stamina)]">
                  {{ selectedPlayer.attributes.physical?.stamina }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">强壮 (Strength)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.physical?.strength)]">
                  {{ selectedPlayer.attributes.physical?.strength }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">弹跳 (Jumping Reach)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.physical?.jumping_reach)]">
                  {{ selectedPlayer.attributes.physical?.jumping_reach }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">灵活 (Agility)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.physical?.agility)]">
                  {{ selectedPlayer.attributes.physical?.agility }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">平衡 (Balance)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.physical?.balance)]">
                  {{ selectedPlayer.attributes.physical?.balance }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">体质 (Natural Fitness)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.physical?.natural_fitness)]">
                  {{ selectedPlayer.attributes.physical?.natural_fitness }}
                </span>
              </div>
            </div>
          </div>

          <!-- 列 2: 技术属性 (Technical) 或 守门属性 (Goalkeeping) -->
          <div class="bg-slate-950 p-3 rounded-xl border border-slate-850 space-y-2">
            <div class="font-bold text-slate-200 pb-1 border-b border-slate-800 text-[11px] inline-flex items-center gap-1.5 w-full">
              <Icon :icon="selectedPlayer.position === 'GK' ? 'lucide:shield' : 'lucide:crosshair'" class="w-3.5 h-3.5 text-emerald-400" />
              <span>{{ selectedPlayer.position === 'GK' ? '守门属性 (Goalkeeping)' : '技术属性 (Technical)' }}</span>
            </div>

            <!-- 非门将技术属性 -->
            <div v-if="selectedPlayer.position !== 'GK'" class="space-y-1.5 text-[11px]">
              <div class="flex items-center justify-between">
                <span class="text-slate-400">射门 (Finishing)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.technical?.finishing)]">
                  {{ selectedPlayer.attributes.technical?.finishing }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">头球 (Heading)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.technical?.heading)]">
                  {{ selectedPlayer.attributes.technical?.heading }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">盘带 (Dribbling)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.technical?.dribbling)]">
                  {{ selectedPlayer.attributes.technical?.dribbling }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">传球 (Passing)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.technical?.passing)]">
                  {{ selectedPlayer.attributes.technical?.passing }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">停球 (First Touch)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.technical?.first_touch)]">
                  {{ selectedPlayer.attributes.technical?.first_touch }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">技术 (Technique)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.technical?.technique)]">
                  {{ selectedPlayer.attributes.technical?.technique }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">抢断 (Tackling)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.technical?.tackling)]">
                  {{ selectedPlayer.attributes.technical?.tackling }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">传中 (Crossing)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.technical?.crossing)]">
                  {{ selectedPlayer.attributes.technical?.crossing }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">远射 (Long Shots)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.technical?.long_shots)]">
                  {{ selectedPlayer.attributes.technical?.long_shots }}
                </span>
              </div>
            </div>

            <!-- 门将专用守门属性 -->
            <div v-else class="space-y-1.5 text-[11px]">
              <div class="flex items-center justify-between">
                <span class="text-amber-300 font-bold">反应/扑救 (Reflexes)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.goalkeeping?.reflexes)]">
                  {{ selectedPlayer.attributes.goalkeeping?.reflexes }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">一对一 (One on Ones)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.goalkeeping?.one_on_ones)]">
                  {{ selectedPlayer.attributes.goalkeeping?.one_on_ones }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">手控球 (Handling)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.goalkeeping?.handling)]">
                  {{ selectedPlayer.attributes.goalkeeping?.handling }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">制空能力 (Aerial Reach)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.goalkeeping?.aerial_reach)]">
                  {{ selectedPlayer.attributes.goalkeeping?.aerial_reach }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">门线指挥 (Command of Area)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.goalkeeping?.command_of_area)]">
                  {{ selectedPlayer.attributes.goalkeeping?.command_of_area }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">球门球 (Kicking)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.goalkeeping?.kicking)]">
                  {{ selectedPlayer.attributes.goalkeeping?.kicking }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">沟通 (Communication)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.goalkeeping?.communication)]">
                  {{ selectedPlayer.attributes.goalkeeping?.communication }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">出击 (Rushing Out)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.goalkeeping?.rushing_out)]">
                  {{ selectedPlayer.attributes.goalkeeping?.rushing_out }}
                </span>
              </div>
            </div>
          </div>

          <!-- 列 3: 精神属性 (Mental) -->
          <div class="bg-slate-950 p-3 rounded-xl border border-slate-850 space-y-2">
            <div class="font-bold text-slate-200 pb-1 border-b border-slate-800 text-[11px] inline-flex items-center gap-1.5 w-full">
              <Icon icon="lucide:brain" class="w-3.5 h-3.5 text-teal-400" />
              <span>精神属性 (Mental)</span>
            </div>
            <div class="space-y-1.5 text-[11px]">
              <div class="flex items-center justify-between">
                <span class="text-slate-400">决断 (Decisions)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.mental?.decisions)]">
                  {{ selectedPlayer.attributes.mental?.decisions }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">预判 (Anticipation)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.mental?.anticipation)]">
                  {{ selectedPlayer.attributes.mental?.anticipation }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">镇定 (Composure)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.mental?.composure)]">
                  {{ selectedPlayer.attributes.mental?.composure }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">视野 (Vision)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.mental?.vision)]">
                  {{ selectedPlayer.attributes.mental?.vision }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">工作投入 (Work Rate)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.mental?.work_rate)]">
                  {{ selectedPlayer.attributes.mental?.work_rate }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">团队合作 (Teamwork)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.mental?.teamwork)]">
                  {{ selectedPlayer.attributes.mental?.teamwork }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">无球跑动 (Off the Ball)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.mental?.off_the_ball)]">
                  {{ selectedPlayer.attributes.mental?.off_the_ball }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">意志力 (Determination)</span>
                <span :class="['px-1.5 py-0.2 rounded font-mono text-center min-w-[24px]', attrClass(selectedPlayer.attributes.mental?.determination)]">
                  {{ selectedPlayer.attributes.mental?.determination }}
                </span>
              </div>
            </div>
          </div>

        </div>

        <!-- 底栏按钮 -->
        <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-xs">
          <span class="text-[10px] text-slate-500 font-mono">
            FM24 官方数据库原生属性 · 1-20 标准评分制
          </span>
          <button
            @click="selectedPlayer = null"
            class="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-bold transition shadow-sm"
          >
            完成查看
          </button>
        </div>
      </div>
    </div>

    <!-- ─────────────────────────────────────────────────────────────
         弹窗 2：+ 关注更多俱乐部 Modal
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

defineEmits(['select-match'])

const clubs = ref(followedClubsRaw)
const selectedClubId = ref(clubs.value[0]?.id || 'odra')
const showAddMoreModal = ref(false)
const selectedPlayer = ref(null)

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
  return activeClub.value.squad.filter(p => {
    const pos = p.position || ''
    if (selectedPositionFilter.value === 'GK') return pos === 'GK'
    if (selectedPositionFilter.value === 'DF') return pos.includes('D') || pos === 'DR' || pos === 'DL' || pos === 'DC'
    if (selectedPositionFilter.value === 'MF') return pos.includes('M') || pos === 'DM' || pos === 'MC' || pos === 'AML' || pos === 'AMR' || pos === 'AMC'
    if (selectedPositionFilter.value === 'FW') return pos.includes('ST') || pos === 'FW'
    return pos === selectedPositionFilter.value
  })
})

const attrClass = (val) => {
  const v = Number(val) || 0
  if (v >= 16) return 'bg-emerald-950 text-emerald-400 border border-emerald-600/80 font-black'
  if (v >= 12) return 'bg-teal-950 text-teal-300 border border-teal-800/60 font-bold'
  if (v >= 8) return 'bg-slate-900 text-slate-200 border border-slate-800 font-medium'
  return 'bg-slate-950 text-slate-500 border border-slate-900'
}
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