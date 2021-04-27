import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './../types';
import axios from 'axios';

Vue.use(Vuex);

const store: StoreOptions<RootState> = {
    state: {
      latestTopicMessage: {},
    },
    mutations: {
        setLatestTopicMessage(state) {
            console.log("On demande pour le message le plus recent.");
            
            axios
              .get("http://127.0.0.1:8000/mtl_client/get_message")
              .then(function(response) {
                console.log(response);
                state.latestTopicMessage  = response.data
              })
              .catch(function(error) {
                // handle error
                console.log(error);
              })
              .then(function() {
                // always executed
              });

        },
        startNewTopic(state, topicName) {
          console.log("On .");
          
          axios
            .get("http://127.0.0.1:8000/mtl_client/"+topicName)
            .then(function(response) {
              console.log(response);
              // state.latestTopicMessage  = response.data
            })
            .catch(function(error) {
              // handle error
              console.log(error);
            })
            .then(function() {
              // always executed
            });

      }
    },
    modules: {
    },
  };
  
  export default new Vuex.Store<RootState>(store);