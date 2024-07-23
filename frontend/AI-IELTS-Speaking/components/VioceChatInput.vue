<template>
  <div>
    <van-button
      round
      block
      type="primary"
      :loading="isRecording"
      @click.stop="toggleRecording"
      @touchstart="startRecording"
      @touchend="stopRecording"
      @touchcancel="stopRecording"
    >
      {{ isRecording ? '正在录音...' : '录音' }}
    </van-button>
    <audio :src="audioURL" controls v-if="audioURL"></audio>
  </div>
</template>

<script setup>
import { ref, onBeforeUnmount } from 'vue'
import { RecordRTC } from 'recordrtc' // 假设 RecordRTC 已被正确引入
import { Button } from 'vant' // 引入 Vant 组件

// 注册 Vant 组件
defineComponent({
  components: {
    [Button.name]: Button,
  },
})

const isRecording = ref(false)
const audioURL = ref(null)
let recorder
let stream

async function startRecording() {
  if (isRecording.value) return // 避免重复开始录音

  try {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    recorder = new RecordRTC(stream, {
      type: 'audio'
      // 其他配置...
    })
    recorder.startRecording()
    isRecording.value = true
  } catch (err) {
    console.error('Error accessing the microphone', err)
  }
}

async function stopRecording() {
  if (!recorder) return // 如果没有开始录音，则不执行停止操作

  try {
    const blob = await recorder.stopRecording()
    audioURL.value = URL.createObjectURL(blob)
    isRecording.value = false
  } catch (err) {
    console.error('Error stopping the recording', err)
  }
}

function toggleRecording() {
  if (isRecording.value) {
    stopRecording()
  } else {
    startRecording()
  }
}

onBeforeUnmount(() => {
  // 清理资源
  if (recorder) {
    recorder.destroy()
    recorder = null
  }
  if (stream) {
    stream.getTracks().forEach(track => track.stop())
    stream = null
  }
  if (audioURL.value) {
    URL.revokeObjectURL(audioURL.value)
    audioURL.value = null
  }
})
</script>


