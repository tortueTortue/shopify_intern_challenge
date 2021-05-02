<template>
  <div class="hello">
    <!--Welcome page header-->
    <!--TODO Add style and computed property Search throughout our (amount of pictures -1)+ library of images-->
    <div class="columns"><div class="column space"></div></div>
    <h1 class="title">Search throughout our library of images</h1>
    <!--Search bar -->
    <!--Carousel of actual images-->
    <div class="columns">
      <div class="column is-one-quarter"></div>
      <b-input
        v-model="keySearched"
        @keyup.native.enter="searchImages"
        class="column search-bar centered"
        placeholder="Search for a image"
      ></b-input>
      <div class="column is-one-quarter"></div>
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
      :class="this.isSearch() ? 'display-none' : ''"
    >
      <b-carousel-item v-for="(carousel, i) in carousels" :key="i">
        <!-- <section :class="``"> -->
        <b-image
          class="hero is-medium is-bold image hero-body has-text-centered carousel-img-height"
          :src="getImgUrl(i)"
        >
        </b-image>
        <!-- </section> -->
      </b-carousel-item>
    </b-carousel>

    <div id="image-grid">
      <div class="columns" v-for="img in searchedImages" :key="img.name">
        <b-image class="column is-half" :src="img.url" ratio="2by1"></b-image>
        <b-field class="column is-one-quarter" label="Name">
          <b-input disabled v-model="img.name"></b-input>
        </b-field>
        <b-field class="column is-one-quarter" label="Price">
          <b-input disabled type="number" v-model="img.price"></b-input>
        </b-field>
      </div>
    </div>
  </div>
</template>

<script lang='ts'>
import { Component, Prop, Vue } from "vue-property-decorator";
import axios from "axios";

declare function require(name: string);

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

  private columns: Array<object> = [
    {
      field: "name",
      label: "name",
      width: "40",
      numeric: false,
    },
    {
      field: "price",
      label: "price",
      width: "40",
      numeric: false,
    },
  ];

  private img_locations: Array<string> = null;

  private search: boolean = false;

  private keySearched: string = "";

  private searchedImages: Array<any> = null;

  public isSearch() {
    return this.search;
  }

  mounted() {
    axios
      .get("http://127.0.0.1:8000/get_pictures?amount=6")
      .then((response) => {
        this.img_locations = response.data.map((img) => img.fields.photo);
        console.log(this.img_locations);
      });
  }

  public getImgUrl(value) {
    return require("../../../BE/shopictures/media/" +
      this.img_locations[value]);
  }

  public searchImages() {
    this.search = true;
    axios
      .get(
        "http://127.0.0.1:8000/get_pictures_with_keyword?keyword=" +
          this.keySearched
      )
      .then((response) => {
        this.searchedImages = response.data.map((img) => {
          const curr_img: object = {};

          curr_img.name = img.fields.name;
          curr_img.price = img.fields.price;
          curr_img.url = require("../../../BE/shopictures/media/" +
            img.fields.photo);

          return curr_img;
        });
        console.log(this.searchedImages);
      });
    this.keySearched = "";
    this.$buefy.toast.open({
      message: "Here are the resultats from your search!",
      type: "is-success",
    });
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
  z-index: 500 !important;
}

.hello {
  background-color: rgb(248, 248, 248) !important;
  height: calc(100vh - 70px) !important;
}

.carousel .carousel-indicator .indicator-item .indicator-style a {
  background-color: #5e8e3e !important;
}

.carousel-img-height {
  max-height: 850px !important;
}
.space {
  margin-top: 20px;
  margin-bottom: 0px;
}
</style>
