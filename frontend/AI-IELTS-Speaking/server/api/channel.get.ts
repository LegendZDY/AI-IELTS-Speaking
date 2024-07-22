// get  /api/channel
import channel from '@/database/channel'

// 通过 defineEventHandler 定义接口
export default defineEventHandler(() => {
  return channel
})
