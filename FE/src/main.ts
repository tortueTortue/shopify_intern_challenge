import Vue from 'vue';
import App from './App.vue';
import Buefy from 'buefy';
import store from './store/store';
import router from './router'
import VueRouter from 'vue-router'
import 'buefy/dist/buefy.css';

Vue.config.productionTip = false;
Vue.use(Buefy);
// Vue.use(VueRouter);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
