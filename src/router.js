import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Logout from '@/components/Logout'
import Messages from '@/components/Messages'

Vue.use(Router)
export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Index,
      meta:{
        requiresAuth: true

      }
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages,
      meta: {
        requiresLogged: true
      }
    },

    {
      path: '/login',
      name: 'login',
      component: Login,
      meta:{
        requiresAuth: true

      }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        requiresLogged: true
      }
    },
    {
      path: '/logout',
      name: 'logout',
      component: Logout,
      meta: {
        requiresAuth: true
      }}

  ]
})
