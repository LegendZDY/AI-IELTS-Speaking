<script setup lang="ts">
import { ref } from 'vue';
const active = ref(0);
</script>

<template>
  <!-- 公共头部 -->
<van-tabbar class="bottom-tabbar" v-model="active">
    <van-tabbar-item name="card" to="/card"  icon="card">场景</van-tabbar-item>
    <van-tabbar-item name="chat" to="/chat" icon="chat">对话</van-tabbar-item>
    <van-tabbar-item name="friends" to="/friends" icon="friends">朋友</van-tabbar-item>
    <van-tabbar-item name="user" to="/user" icon="user">我的</van-tabbar-item>
</van-tabbar>
</template>

<style lang="scss" scoped>
// 公共头部
.bottom-tabbar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 999;
}
</style>
