<template>
  <div class="hello">
    <!--Welcome page header-->
    <!--TODO Add style and computed property Search throughout our (amount of pictures -1)+ library of images-->
    <h1 class="title">
      Search throughout our (amount of pictures -1)+ library of images
    </h1>
    <!--Search bar -->
    <!--Carousel of actual images-->
<div class="columns">
    <div class="column is-one-quarter">
  </div>
    <b-input class="column search-bar centered" placeholder="Search for a image"></b-input>
        <div class="column is-one-quarter">
  </div>
</div>
    <b-carousel
      v-model="carousel"
      :animated="animated"
      :has-drag="drag"
      :autoplay="autoPlay"
      :pause-hover="pauseHover"
      :pause-info="pauseInfo"
      :pause-info-type="pauseType"
      :interval="interval"
      :repeat="repeat"
      @change="info($event)"
    >
      <b-carousel-item v-for="(carousel, i) in carousels" :key="i">
        <!-- <section :class="``"> -->
          <b-image
            class="hero is-medium is-bold image hero-body has-text-centered"
            :src="getImgUrl(i)"
          >

          </b-image>
        <!-- </section> -->
      </b-carousel-item>
    </b-carousel>
  </div>
</template>

<script lang='ts'>
import { Component, Prop, Vue } from "vue-property-decorator";
import axios from "axios";

@Component
export default class WelcomePage extends Vue {
  @Prop() private msg!: string;

  private carousel: number = 0;
  private animated: string = "fade";
  private drag: boolean = false;
  private autoPlay: boolean = false;
  private pauseHover: boolean = false;
  private pauseInfo: boolean = false;
  private repeat: boolean = false;
  private pauseType: string = "is-primary";
  private interval: number = 3000;
  private carousels: Array<object> = [
    { title: "Slide 1", color: "dark" },
    { title: "Slide 2", color: "primary" },
    { title: "Slide 3", color: "info" },
    { title: "Slide 4", color: "success" },
    { title: "Slide 5", color: "warning" },
    { title: "Slide 6", color: "danger" },
  ];

  private img_locations: Array<string> = null;

  mounted() {
    axios.get("http://127.0.0.1:8000/get_pictures?amount=6")
      .then(response => {
        console.log("Data" + response.data)
        this.img_locations = response.data.map(img => img.fields.photo);
        
        console.log(this.img_locations)
      });
  }

  public getImgUrl(value) {
    return `https://picsum.photos/id/43${value}/1230/500`;
  }
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
.search-bar {
  z-index: 500!important;
}

.hello {
  background-color: rgb(248, 248, 248)!important;
  height: calc(100vh - 70px)!important;
}

.carousel .carousel-indicator .indicator-item .indicator-style a{
  background-color: #5e8e3e!important;
}
</style>
