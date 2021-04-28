import Vue from 'vue'
import VueRouter from 'vue-router'

import WelcomePage from "../src/views/WelcomePage.vue";
import UploadImage from "../src/views/Upload.vue";

Vue.use(VueRouter);

export default new VueRouter({
  routes: [
    {
      path: '/',
      component: WelcomePage,
      name: 'home'
    },
    { 
      path: '/upload',
      component: UploadImage,
      name: 'upload'
    },
  ],
  mode: 'history'
})