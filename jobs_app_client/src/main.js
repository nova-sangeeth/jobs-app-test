import Vue from 'vue'
import App from './App.vue'
import VueAxios from 'vue-axios'
import axios from 'axios'
import VueRouter from 'vue-router'

Vue.use(VueRouter);
Vue.use(VueRouter, axios);

Vue.config.productionTip = false

const router = new VueRouter({ mode: 'history' })


new Vue({
  render: h => h(App),
  router
}).$mount('#app')
