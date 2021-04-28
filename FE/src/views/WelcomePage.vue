<template>
  <div class="hello">
    <!--Welcome page header-->
    <!--TODO Add style and computed property Search throughout our (amount of pictures -1)+ library of images-->
    <h1> Search throughout our (amount of pictures -1)+ library of images</h1>
    <!--Search bar -->
    <!--Carousel of actual images-->

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
        <section :class="`hero is-medium is-${carousel.color} is-bold`">
          <div class="hero-body has-text-centered">
            <h1 class="title">{{ carousel.title }}</h1>
            <b-input :placeholder="carousel.title"></b-input>
            <p>A link that <a href="#arrow">goes to arrow</a></p>
          </div>
        </section>
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
  private animated: string = 'fade';
  private drag: boolean = false;
  private autoPlay: boolean = false;
  private pauseHover: boolean = false;
  private pauseInfo: boolean = false;
  private repeat: boolean = false;
  private pauseType: string = 'is-primary';
  private interval: number = 3000;
  private carousels: Array<object> = [
      { title: 'Slide 1', color: 'dark' },
      { title: 'Slide 2', color: 'primary' },
      { title: 'Slide 3', color: 'info' },
      { title: 'Slide 4', color: 'success' },
      { title: 'Slide 5', color: 'warning' },
      { title: 'Slide 6', color: 'danger' }
  ];


  private columns: Array<object> = [
    {
      field: "CreateUtc",
      label: "Creation date",
      numeric: true,
    },
    {
      field: "Desc",
      label: "Topic name",
    },
    {
      field: "ExpiryUtc",
      label: "Expiration date",
    },
    {
      field: "Status",
      label: "Status",
      centered: true,
    },
    {
      field: "Unit",
      label: "Unit",
    },
  ];

  // public sendFile() {
  //   console.log("path : ", this.filePath);
  //   axios
  //     .post("http://127.0.0.1:8000/mtl_client/compute_stats_file", {
  //       fileName: this.filePath,
  //     })
  //     .then(function (response) {
  //       // handle success
  //       console.log(response);
  //     })
  //     .catch(function (error) {
  //       // handle error
  //       console.log(error);
  //     })
  //     .then(function () {
  //       // always executed
  //     });
  // }

  // public uploadFile() {
  //   let buefy = this.$buefy;
  //   console.log("path : ", this.filePath);
  //   axios
  //     .post(
  //       "http://127.0.0.1:8000/mtl_client/compute_stats_file_upload",
  //       this.file,
  //       {
  //         headers: {
  //           "Content-Type": "multipart/form-data",
  //         },
  //       }
  //     )
  //     .then(function (response) {
  //       // handle success
  //       console.log(response);
  //       buefy.dialog.alert(
  //         "Voici les statistiques de votre fichier : " + response.data
  //       );
  //     })
  //     .catch(function (error) {
  //       // handle error
  //       console.log(error);
  //     })
  //     .then(function () {
  //       // always executed
  //     });
  // }

  // public start_mtl_client() {
  //   console.log("On instancie un nouveau client.");
  //   axios
  //     .get("http://127.0.0.1:8000/mtl_client/")
  //     .then(function (response) {
  //       // handle success
  //       console.log(response);
  //     })
  //     .catch(function (error) {
  //       // handle error
  //       console.log(error);
  //     })
  //     .then(function () {
  //       // always executed
  //     });
  // }

  // public compute_stats() {
  //   console.log("On calcul des stats!");

  //   const xhr = new XMLHttpRequest();

  //   xhr.onload = () => {
  //     // process response
  //     if (xhr.status === 200) {
  //       // parse JSON data
  //       this.$buefy.dialog.alert("Le calcul de stats a commencé!");
  //       console.log(JSON.parse(xhr.response));
  //     } else {
  //       console.error("Error!");
  //       this.$buefy.dialog.alert({
  //         title: "Error",
  //         message:
  //           "Something's went wrong in the server <b>icon</b> and <b>type</b>",
  //         type: "is-danger",
  //         hasIcon: true,
  //         icon: "times-circle",
  //         iconPack: "fa",
  //         ariaRole: "alertdialog",
  //         ariaModal: true,
  //       });
  //     }
  //   };

  //   // create a `GET` request
  //   xhr.open("POST", "http://127.0.0.1:8000/mtl_client/compute_stats");

  //   let selectTopics: Array<any> = [];
  //   this.selectedOptions.forEach((topic) => selectTopics.push(topic.path));

  //   // send request
  //   xhr.send(
  //     JSON.stringify({
  //       topics: selectTopics,
  //       agregators: this.selectedStatistics,
  //     })
  //   );
  // }

  // public get_latest_message() {
  //   console.log("On demande pour le message le plus recent.");
  //   this.$store.commit("setLatestTopicMessage");
  // }

  // public listen_topic(topicName: string) {
  //   console.log("On ecoute nouveau topic ", topicName);
  //   this.$store.commit("startNewTopic", topicName);
  // }

  // public get getTopicData(): Array<object> {
  //   return [this.$store.state.latestTopicMessage];
  // }


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
