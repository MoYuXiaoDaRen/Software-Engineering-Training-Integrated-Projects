// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import jq from 'jquery'
import qs from 'qs'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import ProgressBar from 'vue-simple-progress'
Vue.prototype.$qs = qs
Vue.prototype.$jq = jq
Vue.use(ElementUI)
Vue.config.productionTip = false

Vue.directive('title', {
  inserted: function (el, binding) {
    document.title = el.dataset.title
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App, ProgressBar },
  template: '<App/>'
})

