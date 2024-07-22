// get /api/video/id
import video from '@/database/video'

export default defineEventHandler((event) => {
  // 获取路由参数
  const { id } = event.context.params || {}

  // 根据 id 查找视频
  return video.find((v) => v.bvid === id)
})
