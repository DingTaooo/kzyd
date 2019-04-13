import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import index from '@/components/index'
import user from '@/components/user'
import addBook from '@/components/addBook'
import bookDetail from '@/components/bookDetail'
import chapterDetail from '@/components/chapterDetail'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/index',
      name: 'index',
      component: index
    },
    {
      path: '/user',
      name: 'user',
      component: user
    },
    {
      path: '/addBook',
      name: 'addBook',
      component: addBook
    },
    {
      path: '/bookDetail',
      name: 'bookDetail',
      component: bookDetail
    },
    {
      path: '/chapterDetail',
      name: 'chapterDetail',
      component: chapterDetail
    }
  ]
})
