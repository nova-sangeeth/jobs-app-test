import Vue from 'vue'
import App from './App.vue'
import VueAxios from 'vue-axios'
import axios from 'axios'
import VueRouter from 'vue-router'
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
