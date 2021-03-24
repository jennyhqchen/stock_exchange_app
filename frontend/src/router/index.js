import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Market from '@/components/market'
import Login from '@/components/login'
import Register from '@/components/register'
import Sell from '@/components/sell'
import Buy from '@/components/buy'
import Portfolio from '@/components/portfolio'
import store from '@/store'
Vue.use(Router)

const router = new Router({
         routes: [
           {
             path: '/',
             name: 'Market',
             component: Market
           },
            {
               path: '/login',
               name: 'Login',
               component: Login
            },
            {
               path:'/register',
               name:'Register',
               component: Register

            },
              {
                    path:'/sell',
                    name:'Sell',
                    component: Sell,
                   meta: {
                      requireAuth: true
                    }

                 },
               {
                     path:'/buy',
                     name:'Buy',
                     component: Buy,
                      meta: {
                         requireAuth: true
                      }

                  },
                  {
                                       path:'/portfolio',
                                       name:'Portfolio',
                                       component: Portfolio,
                                        meta: {
                                           requireAuth: true
                                        }

                                    }

         ]
})
export default router
router.beforeEach((to, from, next) => {
    if (to.meta.requireAuth) {


        var user = sessionStorage.getItem('user')
        console.log(user)
        if (user) {
             next();
        }
		else {
            next({
                path: '/login'
            })
        }
    }
    else {
        next();
    }
})
