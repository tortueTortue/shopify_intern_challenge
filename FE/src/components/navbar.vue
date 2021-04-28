<template>
  <div >
    <b-navbar class="navbar">
      <template #brand>
        <b-navbar-item>
          <img
            src="../assets/shopictures_logo.png"
            alt="Shopictures official logo"
            class="logo"
          />
        </b-navbar-item>
      </template>

      <template #end>
        <b-navbar-item tag="div">
          <div class="buttons">
            <router-link class="button shopicolor" to="/">
              <strong>Search</strong>
            </router-link>
          </div>
        </b-navbar-item>
        <b-navbar-item tag="div">
          <div class="buttons">
            <router-link class="button shopicolor-bside text-white" to="/upload">
              <strong>Upload</strong>
            </router-link>
          </div>
        </b-navbar-item>
      </template>
    </b-navbar>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

export default class Navbar extends Vue {
    private name: String = 'Navbar';
}
</script>

<style>

</style>
