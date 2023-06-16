import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import ipControlMiddleware from '../middleware/ipControl/middleware'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/view/:filmId',
      name: 'view',
      component: () => import('../views/ViewFilmView.vue')
    },
    {
      path: '/abuse',
      name: 'abuse',
      component: () => import ('../views/AbuseView.vue')
    },
    {
      path: '/403',
      name: '403',
      component: () => import('../views/errors/403View.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: '404',
      component: () => import('../views/errors/404.vue')
    }
  ]
})

router.beforeResolve(async (to, from, next)  => {
  await ipControlMiddleware({ to, router })
  next()
})

export default router
