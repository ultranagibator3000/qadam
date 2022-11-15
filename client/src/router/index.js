import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('')
    },
    {
      path: 'login/',
      name: 'login',
      component: () => import('../views/auth/AuthView.vue')
    }
  ]
})

export default router