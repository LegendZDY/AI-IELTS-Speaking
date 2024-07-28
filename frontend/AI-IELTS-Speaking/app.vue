<script setup lang="ts">
useSeoMeta({
  title: 'AI-IELTS-Speaking - 基于 Nuxt.js 的 IELTS 口语评测系统',
  description: 'AI-IELTS-Speaking 是一个基于 Nuxt.js 的 IELTS 口语评测系统，提供视频、文章、词汇、语法、阅读、写作、口语、听力、口语评测等功能。',
})

</script>

<template>
  <NuxtPage :keepalive="{ max: 10 }" />
</template>

<style lang="scss">
// 基础样式
@import './assets/styles/base.scss';
:root {
  /* CSS 变量设置组件库主题 */
  --van-primary-color: #fb7299 !important;
}
</style>
