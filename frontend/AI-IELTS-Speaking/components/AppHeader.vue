<script setup lang="ts"></script>

<template>
  <!-- 公共头部 -->
  <header class="app-header">
    <a class="logo" href="#">
      <img src="@/assets/images/user.jpg" class="logo-img" />
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
    .logo-img {
        width: 25px; /* 设置图片宽度 */
        height: 25px; /* 设置图片高度 */
        border-radius: 50%; /* 将图片形状变为圆形 */
        object-fit-fit: cover; /* 确保图片在保持其纵横比的同时填充整个容器 */
        margin-right: 10px; /* 图片和文字之间的距离 */
    }
  }
}
</style>
