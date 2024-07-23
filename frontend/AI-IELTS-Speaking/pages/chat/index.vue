<template>
  <div class="chat-container">
    <div class="header">
      <AppHeader />
    </div>
    <!-- 聊天内容区域 -->
    <div class="chat-content">
      <!-- 聊天内容 -->
    </div>
    <!-- 录音按钮 -->
    <div class="record-button-container">
      <VioceChatInput />
    </div>

    <div class="bottom-menu">
      <AppBottom />
    </div>
  </div>
</template>
  
<script>

</script>
  
<style lang="scss">
.chat-container {
  /* 容器样式，可以根据需要设置高度、宽度、边距等 */
  display: flex;
  flex-direction: column;
  height: 100vh; /* 假设容器占据整个视口高度 */
  padding: 16px; /* 添加一些内边距，使内容不会紧贴边缘 */
}

.chat-content {
  /* 聊天内容区域的样式，可以设置高度、滚动等 */
  flex: 1; /* 占据剩余空间 */
  overflow-y: auto; /* 允许内容垂直滚动 */
  padding: 16px; /* 内容内边距 */
}

.record-button-container {
  /* 录音按钮容器的样式 */
  margin-bottom: 16px; /* 与底部菜单的距离 */
  text-align: center; /* 使按钮居中显示（如果需要） */
}

.bottom-menu {
  /* 底部菜单的样式 */
  position: sticky; /* 如果需要固定在底部 */
  bottom: 0;
  background-color: #f8f9fa; /* 示例背景色 */
  padding: 16px; /* 内边距 */
  text-align: center; /* 菜单项居中显示（如果需要） */
}
</style>