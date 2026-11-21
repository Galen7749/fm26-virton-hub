<template>
  <div
    class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
    @click.self="$emit('close')"
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
          @click="$emit('close')"
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
            <span class="text-[10px] text-slate-500 font-normal">共 {{ mailbox.messages.length }} 封通讯</span>
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
          @click="$emit('close')"
          class="w-full bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs py-2 rounded-xl transition"
        >
          关闭并返回公域门户
        </button>
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

defineEmits(['close'])
</script>
