<template>
    <div class="chat-container">
      <div class="messages">
        <div v-for="(msg, index) in messages" :key="index" class="message">
          {{ msg }}
        </div>
      </div>
      <div class="input-area">
        <van-button
          class="voice-button"
          :style="{ width: isVoiceInput ? voiceButtonWidth : '50%' }"
          @touchstart="startVoiceInput"
          @touchend="stopVoiceInput"
        >
          语音输入
        </van-button>
        <van-field
          v-if="!isVoiceInput"
          v-model="textInput"
          placeholder="请输入内容"
          @keyup.enter="sendText"
          clearable
        />
        <van-button v-if="!isVoiceInput" @click="sendText">发送</van-button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import RecordRTC from 'recordrtc';
  
  const messages = ref([]);
  const textInput = ref('');
  const isVoiceInput = ref(false);
  const voiceButtonWidth = ref('50%'); // 按钮的初始宽度
  let recorder;
  let audioBlob;
  
  const sendText = async () => {
    if (textInput.value.trim() === '') return;
  
    await sendToServer(textInput.value);
    messages.value.push(textInput.value);
    textInput.value = '';
  };
  
  const startVoiceInput = async () => {
    isVoiceInput.value = true;
    voiceButtonWidth.value = '100%'; // 改变按钮长度
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = RecordRTC(stream, {
      type: 'audio',
      mimeType: 'audio/wav',
    });
    recorder.startRecording();
  };
  
  const stopVoiceInput = async () => {
    isVoiceInput.value = false;
    voiceButtonWidth.value = '50%'; // 恢复按钮长度
    recorder.stopRecording(() => {
      audioBlob = recorder.getBlob();
      sendAudioToServer(audioBlob);
    });
  };
  
  const sendAudioToServer = async (audioBlob) => {
    const formData = new FormData();
    formData.append('audio', audioBlob, 'voice_input.wav');
  
    try {
      const response = await fetch('https://your-api-endpoint.com/audio', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      messages.value.push(data.response);
    } catch (error) {
      console.error('Error sending audio to server:', error);
    }
  };
  
  const sendToServer = async (input) => {
    try {
      const response = await fetch('https://your-api-endpoint.com/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: input }),
      });
      const data = await response.json();
      messages.value.push(data.response);
    } catch (error) {
      console.error('Error sending to server:', error);
    }
  };
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
  }
  .messages {
    flex: 1;
    overflow-y: auto;
  }
  .input-area {
    display: flex;
    padding: 10px;
  }
  .voice-button {
    margin-right: 10px;
  }
  </style>