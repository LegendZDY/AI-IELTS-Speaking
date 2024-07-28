export default defineNuxtRouteMiddleware((to, from, next) => {
    if (to.path === '/') {
        return navigateTo('/chat')
      }
    
    const passURLs = ['/chat', '/card', '/friends', '/user']
    if (!passURLs.includes(to.path)) {
      const token = ""
      if (import.meta.client) {
        token.value = localStorage.getItem('token')
      }

      if (!token) {
        return navigateTo({
            path: '/login',
            query: {
                code: 401,
                message: 'Unauthorized access'
            }
        })
      }
    }
  })