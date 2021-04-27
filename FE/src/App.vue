<template>
  <div id="app">
        <b-navbar class="navbar">
        <template #brand>
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <img
                    src="./assets/shopictures_logo.png"
                    alt="Shopictures official logo"
                    class="logo"
                >
            </b-navbar-item>
        </template>
        <template #start>
            <b-navbar-item href="#" class="shopicolor-nav">
                Home
            </b-navbar-item>
            <b-navbar-item href="#" class="shopicolor-nav">
                Documentation
            </b-navbar-item>
            <b-navbar-dropdown label="Info">
                <b-navbar-item href="#" class="shopicolor-nav">
                    About
                </b-navbar-item>
                <b-navbar-item href="#" class="shopicolor-nav">
                    Contact
                </b-navbar-item>
            </b-navbar-dropdown>
        </template>

        <template #end>
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button shopicolor">
                        <strong>Search</strong>
                    </a>
                    <a class="button shopicolor-bside text-white">
                        Upload
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
    <WelcomePage msg="Lecture de topic de la STM"/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import WelcomePage from './components/WelcomePage.vue';

@Component({
  components: {
    WelcomePage,
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
}
.navbar {
  height: 70px;
}
.logo {
  height: 40px!important;
  width: auto;
}
.navbar-item img {
    max-height: 2.5rem!important;    
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
