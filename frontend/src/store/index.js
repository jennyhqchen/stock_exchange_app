import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    setUser (state, user) {
      state.user = user
      sessionStorage.setItem('user', state.user);
    }
  }
})
export default store
