<template>
    <AppHeader />
    <div class="chat">
      <div class="chat-messages">
        <div v-for="message in messages" :key="message.id" class="chat-message">
          {{ message.text }}
        </div>
      </div>
      <div class="chat-input">
        <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="输入消息..." />
        <button @click="sendMessage">发送</button>
      </div>
    </div>
    <AppBottom />
  </template>
  
  <script>
  export default {
    data() {
      return {
        messages: [],
        newMessage: ''
      };
    },
    methods: {
      sendMessage() {
        if (this.newMessage.trim() !== '') {
          const newMessage = {
            id: Date.now(),
            text: this.newMessage
          };
          this.messages.push(newMessage);
          this.newMessage = '';
        }
      }
    }
  };
  </script>
  
  <style>
  .chat {
    display: flex;
    flex-direction: column;
    height: 100vh;
    padding: 20px;
  }
  
  .chat-messages {
    flex: 1;
    overflow-y: scroll;
  }
  
  .chat-message {
    margin-bottom: 10px;
  }
  
  .chat-input {
    display: flex;
    align-items: center;
    margin-top: 10px;
  }
  
  .chat-input input {
    flex: 1;
    padding: 5px;
    margin-right: 10px;
  }
  
  .chat-input button {
    padding: 5px 10px;
  }
  </style>