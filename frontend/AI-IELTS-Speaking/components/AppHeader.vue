<script setup lang="ts"></script>

<template>
  <!-- 公共头部 -->
  <header class="app-header">
    <a class="logo" href="#">
      <img src="@/assets/images/user.jpg" />
    </a>
    <van-icon name="like-o" size="25px" />
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
}
</style>
