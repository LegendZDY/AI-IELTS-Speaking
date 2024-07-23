<template>
    <div class="voice-chat-input">
      <div class="input-wrapper">
        <van-input
          v-model="message"
          placeholder="请输入消息..."
          show-password
          type="text"
          :readonly="isRecording"
        />
        <van-button
          v-if="!isRecording"
          type="primary"
          icon="chat-o"
          @click="startRecording"
        >
          语音输入
        </van-button>
        <van-button
          v-else
          type="danger"
          icon="close"
          @click="stopRecording"
        >
          停止录音
        </van-button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        message: '',
        isRecording: false
      };
    },
    methods: {
      startRecording() {
        // 开始录音逻辑
        this.isRecording = true;
      },
      stopRecording() {
        // 停止录音逻辑
        this.isRecording = false;
      }
    }
  };
  </script>
  
  <style scoped>
  .voice-chat-input {
    padding: 10px;
  }
  
  .input-wrapper {
    display: flex;
    align-items: center;
  }
  
  .input-wrapper /deep/ .van-field__control {
    flex: 1;
  }
  
  .input-wrapper /deep/ .van-button {
    margin-left: 10px;
  }
  </style>