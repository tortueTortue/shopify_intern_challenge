<template>
  <div id="app">
    <Navbar/>
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import WelcomePage from "./views/WelcomePage.vue";
import Navbar from './components/navbar.vue'

@Component({
  components: {
    Navbar
  },
})
export default class App extends Vue {}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  height: 100vh!important;
}
.navbar {
  height: 70px;
}
.logo {
  height: 40px !important;
  width: auto;
}
.navbar-item img {
  max-height: 2.5rem !important;
}
.shopicolor {
  background-color: #95bf46 !important;
}
.shopicolor-bside {
  background-color: #5e8e3e !important;
}
.shopicolor-nav a:hover a:active {
  color: #5e8e3e !important;
}
.text-white {
  color: #ffffff !important;
}
</style>
