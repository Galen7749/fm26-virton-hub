<template>
  <div class="p-4 space-y-4 animate-in fade-in duration-150">
    
    <!-- 1. 顶栏：主帅私人工作台标识卡 -->
    <div class="bg-gradient-to-r from-slate-900 via-slate-850 to-slate-900 border border-slate-800 rounded-xl p-3.5 space-y-2.5 shadow-sm">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="text-base">💼</span>
          <div>
            <h3 class="text-xs font-bold text-white tracking-wide">主帅私人工作台 · 绝密信箱</h3>
            <p class="text-[9px] text-amber-400/90 font-mono">CONFIDENTIAL // MANAGER ONLY</p>
          </div>
        </div>
        <span class="text-[9px] bg-amber-950 text-amber-300 border border-amber-800 px-2 py-0.5 rounded-full font-bold">
          私域工作台
        </span>
      </div>

      <!-- 档案状态卡 -->
      <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
        <div class="flex items-center justify-between">
          <div>
            <div class="font-black text-sm text-white">{{ mailbox.manager_profile.name }}</div>
            <div class="text-[10px] text-emerald-400 mt-0.5">{{ mailbox.manager_profile.club_name }}</div>
          </div>
          <span class="text-[10px] bg-emerald-950 text-emerald-300 border border-emerald-800 px-2 py-0.5 rounded-full font-bold">
            {{ mailbox.manager_profile.role }}
          </span>
        </div>
        <div class="text-[10px] text-slate-400 pt-1 border-t border-slate-800/80 flex justify-between">
          <span>助理教练: {{ mailbox.manager_profile.assistant_name }}</span>
          <span>合同期至: 2026-06</span>
        </div>
      </div>
    </div>

    <!-- 2. 足协合规倒计时 (60天豁免期) -->
    <div class="bg-amber-950/25 border border-amber-900/60 rounded-xl p-3.5 space-y-2.5 shadow-sm">
      <div class="flex items-center justify-between text-xs">
        <span class="font-bold text-amber-300 flex items-center space-x-1">
          <span>⚠️</span>
          <span>比利时皇家足协(KBVB)临时执教豁免期</span>
        </span>
        <span class="font-mono text-amber-400 font-black">
          第 {{ mailbox.manager_profile.waiver_days_used }} / {{ mailbox.manager_profile.waiver_days_total }} 天
        </span>
      </div>

      <!-- 进度条 -->
      <div class="w-full bg-slate-900 h-2 rounded-full overflow-hidden border border-slate-800">
        <div
          class="bg-amber-400 h-full rounded-full transition-all duration-500 shadow-sm shadow-amber-500/50"
          :style="{ width: `${(mailbox.manager_profile.waiver_days_used / mailbox.manager_profile.waiver_days_total) * 100}%` }"
        ></div>
      </div>

      <p class="text-[10px] text-amber-200/80 leading-relaxed font-sans">
        依据比利时足协条款，无职业级执照主帅享有最多 60 天代理执教豁免期。请在期满前完成资格注册或由持证助教大卫·齐特利签署相关掩护文件。
      </p>
    </div>

    <!-- 3. 董事会与重要往来信件列表 -->
    <div class="space-y-2.5">
      <div class="font-bold text-slate-300 text-xs flex items-center justify-between">
        <span class="flex items-center space-x-1.5">
          <span>📩</span>
          <span>往来直达信件 (董事会 / 坎特 / 媒体直通)</span>
        </span>
        <span class="text-[10px] text-slate-500 font-normal">共 {{ mailbox.messages.length }} 封通讯</span>
      </div>

      <div class="space-y-2.5">
        <div
          v-for="msg in mailbox.messages"
          :key="msg.id"
          class="bg-slate-900 p-3.5 rounded-xl border border-slate-800 space-y-2 hover:border-slate-700 transition shadow-sm"
        >
          <div class="flex items-center justify-between text-xs">
            <div class="flex items-center space-x-2">
              <span class="text-base">{{ msg.avatar }}</span>
              <span class="font-bold text-slate-200">{{ msg.from }}</span>
            </div>
            <span class="text-[9px] bg-slate-800 text-teal-300 px-2 py-0.5 rounded-full font-mono border border-slate-700">
              {{ msg.type }}
            </span>
          </div>

          <div class="text-[11px] text-emerald-400 font-bold">
            {{ msg.subject }}
          </div>

          <p class="text-xs text-slate-300 leading-relaxed font-sans bg-slate-950 p-2.5 rounded-lg border border-slate-850">
            {{ msg.content }}
          </p>

          <div class="text-[9px] text-slate-500 text-right font-mono">
            {{ msg.date }}
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
defineProps({
  mailbox: {
    type: Object,
    required: true
  }
})
</script>
