import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VModal from 'vue-js-modal'
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'


Vue.use(VModal, VueGlide, { dynamic:true })
Vue.config.productionTip = false


new Vue({
  el: '#app',
  router,
  render: h => h(App)
}).$mount('#app')
