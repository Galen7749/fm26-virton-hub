<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-md animate-in fade-in duration-200">
    <!-- 点击外部遮罩关闭 -->
    <div class="absolute inset-0" @click="$emit('close')"></div>

    <!-- 手机机身容器 -->
    <div class="relative w-full max-w-sm bg-slate-900 border-2 border-slate-700/80 rounded-[36px] shadow-2xl overflow-hidden flex flex-col max-h-[90vh] z-10">
      
      <!-- 手机顶部刘海与状态栏 -->
      <div class="bg-slate-950 px-5 pt-3 pb-2 flex items-center justify-between border-b border-slate-800 text-[11px] text-slate-400 select-none">
        <span class="font-bold text-white font-mono">20:26</span>
        <div class="w-20 h-4 bg-slate-900 rounded-full border border-slate-800 mx-auto"></div>
        <div class="flex items-center space-x-1.5 font-mono">
          <span>5G</span>
          <span>🔋 100%</span>
        </div>
      </div>

      <!-- 手机工作台标题栏 -->
      <div class="bg-gradient-to-r from-slate-900 via-slate-850 to-slate-900 px-4 py-3 border-b border-slate-800 flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="text-base">📱</span>
          <div>
            <h3 class="text-xs font-black text-white">主帅私人工作终端 (Manager OS)</h3>
            <p class="text-[9px] text-emerald-400 font-mono">加密通道 · 仅主帅可见</p>
          </div>
        </div>
        <button
          @click="$emit('close')"
          class="w-6 h-6 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs transition"
        >
          ✕
        </button>
      </div>

      <!-- 主帅身份卡片 -->
      <div class="p-3 bg-slate-950 border-b border-slate-800/80 text-xs">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-full bg-emerald-600/30 border border-emerald-500/50 flex items-center justify-center text-base font-black text-emerald-400 shrink-0">
            徐
          </div>
          <div class="flex-1 min-w-0">
            <div class="flex items-center space-x-2">
              <span class="font-black text-white text-sm truncate">{{ phoneData.manager.name }}</span>
              <span class="text-[9px] bg-red-950 text-red-300 border border-red-800 px-1.5 py-0.2 rounded font-bold">
                {{ phoneData.manager.league }}
              </span>
            </div>
            <div class="text-[10px] text-slate-400 mt-0.5 truncate">
              现任：<strong class="text-emerald-400">{{ phoneData.manager.club_name }}</strong> · {{ phoneData.manager.role }}
            </div>
          </div>
        </div>
      </div>

      <!-- 手机内部子功能切换 -->
      <div class="bg-slate-900 px-3 py-2 border-b border-slate-800 flex items-center space-x-1.5 text-xs">
        <button
          @click="phoneTab = 'badge'"
          :class="[
            'flex-1 py-1 rounded-lg font-bold text-center transition text-[11px] flex items-center justify-center space-x-1',
            phoneTab === 'badge' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white bg-slate-950'
          ]"
        >
          <span>📜</span>
          <span>欧足联考证</span>
        </button>
        <button
          @click="phoneTab = 'mailbox'"
          :class="[
            'flex-1 py-1 rounded-lg font-bold text-center transition text-[11px] flex items-center justify-center space-x-1',
            phoneTab === 'mailbox' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white bg-slate-950'
          ]"
        >
          <span>📬</span>
          <span>董事会私信</span>
          <span class="w-1.5 h-1.5 rounded-full bg-amber-400 inline-block ml-0.5"></span>
        </button>
        <button
          @click="phoneTab = 'career'"
          :class="[
            'flex-1 py-1 rounded-lg font-bold text-center transition text-[11px] flex items-center justify-center space-x-1',
            phoneTab === 'career' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white bg-slate-950'
          ]"
        >
          <span>📁</span>
          <span>执教履历</span>
        </button>
      </div>

      <!-- 手机内容展示区（带滚动） -->
      <div class="flex-1 overflow-y-auto p-3.5 space-y-3 text-xs custom-scrollbar bg-slate-950/60">

        <!-- 视图 1: 欧足联执照进修看板 -->
        <template v-if="phoneTab === 'badge'">
          <!-- 进修状态总览 -->
          <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 space-y-2.5">
            <div class="flex items-center justify-between">
              <div>
                <span class="text-[10px] text-slate-400 font-bold">进修目标</span>
                <div class="text-sm font-black text-amber-400 mt-0.5">{{ phoneData.coaching_badge.target_level }}</div>
              </div>
              <div class="text-right">
                <span class="text-[9px] bg-emerald-950 text-emerald-300 border border-emerald-800 px-2 py-0.5 rounded-full font-bold">
                  {{ phoneData.coaching_badge.compliance_status }}
                </span>
              </div>
            </div>

            <!-- 进度条 -->
            <div class="space-y-1">
              <div class="flex justify-between text-[10px]">
                <span class="text-slate-400">研习与实操考评进度</span>
                <span class="text-emerald-400 font-black font-mono">{{ phoneData.coaching_badge.progress_percent }}%</span>
              </div>
              <div class="w-full h-2 bg-slate-950 rounded-full overflow-hidden border border-slate-800">
                <div
                  class="h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-full transition-all duration-500"
                  :style="{ width: phoneData.coaching_badge.progress_percent + '%' }"
                ></div>
              </div>
            </div>

            <!-- 资助与合规信息 -->
            <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-850 space-y-1 text-[10px]">
              <div class="flex justify-between">
                <span class="text-slate-400">学费出资赞助方：</span>
                <span class="text-slate-200 font-bold">{{ phoneData.coaching_badge.sponsor }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">目前持有资质：</span>
                <span class="text-slate-200">{{ phoneData.coaching_badge.current_level }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">预计结业考证：</span>
                <span class="text-amber-400 font-bold font-mono">{{ phoneData.coaching_badge.expected_completion }}</span>
              </div>
            </div>

            <p class="text-[10px] text-slate-400 leading-relaxed bg-slate-950/80 p-2 rounded border border-slate-850">
              💡 <strong>重要保障：</strong>在奥波莱俱乐部全资赞助与官方担保下，徐指导已获得欧足联官方注册教练员学籍，彻底免除比甲/波甲“无证主帅巨额罚款”，扫清执教资质障碍！
            </p>
          </div>

          <!-- 进修课程模块列表 -->
          <div class="space-y-1.5">
            <div class="text-[11px] font-bold text-slate-300">进修考核科目明细：</div>
            <div
              v-for="mod in phoneData.coaching_badge.modules"
              :key="mod.id"
              class="bg-slate-900 border border-slate-800 rounded-lg p-2.5 flex items-center justify-between text-[11px]"
            >
              <div class="flex items-center space-x-2">
                <span :class="[
                  'w-5 h-5 rounded-full flex items-center justify-center text-[10px] font-bold shrink-0',
                  mod.status === '已通过' ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' :
                  mod.status === '在读中' ? 'bg-amber-950 text-amber-400 border border-amber-800' :
                  'bg-slate-800 text-slate-400'
                ]">
                  {{ mod.status === '已通过' ? '✓' : mod.status === '在读中' ? '●' : '○' }}
                </span>
                <span class="text-slate-200 font-medium">{{ mod.name }}</span>
              </div>
              <span :class="[
                'text-[10px] font-bold font-mono',
                mod.status === '已通过' ? 'text-emerald-400' : mod.status === '在读中' ? 'text-amber-400' : 'text-slate-500'
              ]">
                {{ mod.score }}
              </span>
            </div>
          </div>
        </template>

        <!-- 视图 2: 董事会私信与球员信函 -->
        <template v-else-if="phoneTab === 'mailbox'">
          <div class="space-y-2.5">
            <div
              v-for="msg in phoneData.messages"
              :key="msg.id"
              @click="activeMessageId = activeMessageId === msg.id ? null : msg.id"
              class="bg-slate-900 border border-slate-800 hover:border-slate-700 rounded-xl p-3 space-y-2 cursor-pointer transition shadow-sm"
            >
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-2">
                  <span class="text-base">{{ msg.avatar }}</span>
                  <span class="font-bold text-white text-xs truncate max-w-[150px]">{{ msg.sender }}</span>
                </div>
                <span class="text-[9px] bg-slate-800 text-teal-300 px-1.5 py-0.2 rounded border border-teal-900/40">
                  {{ msg.badge }}
                </span>
              </div>

              <div class="text-[11px] font-bold text-slate-200">
                {{ msg.subject }}
              </div>

              <!-- 正文（支持折叠展开） -->
              <p :class="[
                'text-[11px] text-slate-300 leading-relaxed whitespace-pre-line',
                activeMessageId === msg.id ? '' : 'line-clamp-2'
              ]">
                {{ msg.content }}
              </p>

              <div class="flex items-center justify-between text-[9px] text-slate-500 pt-1 border-t border-slate-800/60 font-mono">
                <span>{{ msg.date }}</span>
                <span class="text-emerald-400 hover:underline">
                  {{ activeMessageId === msg.id ? '收起详情 ▲' : '查看全文 ▼' }}
                </span>
              </div>
            </div>
          </div>
        </template>

        <!-- 视图 3: 执教履历历史备忘 -->
        <template v-else-if="phoneTab === 'career'">
          <div class="space-y-2.5">
            <!-- 当前第二站：奥波莱奥德拉 -->
            <div class="bg-gradient-to-r from-red-950/60 to-slate-900 border border-red-900/60 rounded-xl p-3 space-y-2">
              <div class="flex items-center justify-between text-xs">
                <span class="font-black text-white flex items-center space-x-1.5">
                  <span>🇵🇱</span>
                  <span>奥波莱奥德拉 (Odra Opole)</span>
                </span>
                <span class="text-[9px] bg-red-950 text-red-300 border border-red-800 px-1.5 py-0.5 rounded font-bold">
                  执教中 (进行中)
                </span>
              </div>
              <p class="text-[11px] text-slate-300 leading-relaxed">
                2026年7月签约出任主帅。首轮2-1绝杀开门红，俱乐部全资赞助攻读欧足联A/Pro执照。
              </p>
              <div class="text-[10px] text-slate-400 flex items-center space-x-3 pt-1 border-t border-red-900/30">
                <span>战绩：1战1胜0负</span>
                <span>进失球：2-1</span>
                <span>胜率：100%</span>
              </div>
            </div>

            <!-- 第一站：维尔通精英 -->
            <div class="bg-gradient-to-r from-emerald-950/60 to-slate-900 border border-emerald-900/60 rounded-xl p-3 space-y-2">
              <div class="flex items-center justify-between text-xs">
                <span class="font-black text-white flex items-center space-x-1.5">
                  <span>🇧🇪</span>
                  <span>维尔通精英 (R.E. Virton)</span>
                </span>
                <span class="text-[9px] bg-emerald-950 text-emerald-300 border border-emerald-800 px-1.5 py-0.5 rounded font-bold">
                  冲甲冠军 🏆 (已离任)
                </span>
              </div>
              <p class="text-[11px] text-slate-300 leading-relaxed">
                2025年8月至2026年5月执教。以升班马身份单季狂轰61球，附加赛客场0-2落后次回合4-1惊天逆转绝杀冲入比甲。因管理层U23政策与拒资助考证体面辞职。
              </p>
              <div class="text-[10px] text-slate-400 flex items-center space-x-3 pt-1 border-t border-emerald-900/30">
                <span>总场次：32场</span>
                <span>战绩：18胜9平5负</span>
                <span>总荣誉：比乙升甲附加赛总冠军</span>
              </div>
            </div>
          </div>
        </template>

      </div>

      <!-- 手机底部 Home Bar -->
      <div class="bg-slate-950 py-2.5 flex justify-center border-t border-slate-800">
        <div class="w-32 h-1 bg-slate-600 rounded-full"></div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import phoneDataRaw from '../../data/manager_phone.json'

defineProps({
  isOpen: {
    type: Boolean,
    default: false
  }
})

defineEmits(['close'])

const phoneData = ref(phoneDataRaw)
const phoneTab = ref('badge') // 'badge' | 'mailbox' | 'career'
const activeMessageId = ref('phone_msg_01')
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #334155;
  border-radius: 9999px;
}
</style>
