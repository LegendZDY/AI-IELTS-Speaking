<script setup lang="ts">
// SEO 优化
useSeoMeta({
  title: 'AI-IELTS-Speaking - 基于 Nuxt.js 的 IELTS 口语评测系统',
  description: 'AI-IELTS-Speaking 是一个基于 Nuxt.js 的 IELTS 口语评测系统，提供视频、文章、词汇、语法、阅读、写作、口语、听力、口语评测等功能。',
})

</script>

<template>
  <!-- 页面顶部导航栏 -->
  <NuxtLink to="/"> 首页 </NuxtLink>
  <NuxtLink to="/video"> 视频页 </NuxtLink>
  <!-- Nuxt 基于路由的动态组件 -->
  <!-- Nuxt 页面路由，相当于 RouterView -->
  <NuxtPage />
</template>

<style>
:root {
  /* CSS 变量设置组件主题色 */
  --van-primary-color: #FB7299 !important;
}
</style>
