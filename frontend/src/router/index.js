import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import TestCase from '../views/TestCase.vue'
import TestCaseResult from '../views/TestCaseResult.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/:testcase_slug',
    name: 'TestCase',
    component: TestCase
  },
  {
    path: '/:testcase_slug/result/',
    name: 'TestCaseResult',
    component: TestCaseResult
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
