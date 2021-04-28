<template>
  <div class="upload">
    <!--Welcome page header-->
    <!--TODO Add style and computed property Search throughout our (amount of pictures -1)+ library of images-->
    <h1> Upload an image!</h1>
    <!--Search bar -->
    <!--Carousel of actual images-->

  </div>
</template>

<script lang='ts'>
import { Component, Prop, Vue } from "vue-property-decorator";
import axios from "axios";

@Component
export default class UploadImage extends Vue {



}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.large-size-input {
  width: 360px !important;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
