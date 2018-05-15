import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import IndexPage from '@/components/pages/Index'
import CategoryPage from '@/components/pages/CategoryPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: IndexPage
    },
    {
      path: '/category/:id',
      name: 'Category',
      component: CategoryPage
    }
  ]
})
