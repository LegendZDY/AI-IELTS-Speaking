<script setup lang="ts"></script>

<template>
  <!-- 公共头部 -->
  <header class="app-header">
    <NuxtLink class="logo" to="/">
      <i class="iconfont Navbar_logo"></i>
    </NuxtLink>
    <a class="search" href="#">
      <i class="iconfont ic_search_tab"></i>
    </a>
    <a class="face" href="#">
      <img src="@/assets/images/login.png" />
    </a>
    <div class="down-app">下载 APP</div>
  </header>
</template>

<style lang="scss" scoped>
// 公共头部
.app-header {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  background-color: #fff;
  .logo {
    flex: 1;
    .Navbar_logo {
      color: #00C16A;
      font-size: 28px;
    }
  }
  .search {
    padding: 0 8px;
    .ic_search_tab {
      color: #ccc;
      font-size: 22px;
    }
  }
  .face {
    padding: 0 15px;
    img {
      width: 24px;
      height: 24px;
    }
  }
  .down-app {
    font-size: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #00C16A;
    color: #fff;
    border-radius: 5px;
    padding: 5px 10px;
  }
}
</style>
