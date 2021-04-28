<template>
  <div class="upload">
    <!--Welcome page header-->
    <!--TODO Add style and computed property Search throughout our (amount of pictures -1)+ library of images-->

    <!-- Form -->
    <section>
      <h1 class="title">Upload an image</h1>
      <b-field
        horizontal
        label="Name"
        type="is-success"
      >
        <b-input name="imgname" placeholder="What's this picture called?" expanded></b-input>
      </b-field>

      <b-field
        horizontal
        type="is-success"
        label="Price"
      >
        <b-input type="number" name="price" placeholder="How much for this picture?" expanded></b-input>
      </b-field>

      <b-field horizontal class="file is-success" :class="{ 'has-name': !!file }">
        <b-upload v-model="file" class="file-label">
          <span class="file-cta">
            <b-icon class="file-icon" icon="upload"></b-icon>
            <span class="file-label">Click to upload</span>
          </span>
          <span class="file-name" v-if="file">
            {{ file.name }}
          </span>
        </b-upload>
      </b-field>

      <b-field horizontal
        ><!-- Label left empty for spacing -->
        <p class="control">
          <b-button @click="uploadImage" label="Submit" type="is-success" />
        </p>
      </b-field>
    </section>
  </div>
</template>

<script lang='ts'>
import { Component, Prop, Vue } from "vue-property-decorator";
import axios from "axios";

@Component
export default class UploadImage extends Vue {

  private file: any;
  private name: string;
  private price: number;

  public uploadImage() {
    axios
      .post("http://127.0.0.1:8000/add_image", {
        name: this.name,
        price: this.price,
        owner: 'browser_user',
        photo: this.file
      },
      {
        headers: {
          // "Content-Type": "multipart/form-data",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods":
            "POST, GET, PUT, OPTIONS, DELETE",
          "Access-Control-Allow-Headers":
            "Access-Control-Allow-Methods, Access-Control-Allow-Origin, Origin, Accept, Content-Type",
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      })
  }
}
</script>

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
