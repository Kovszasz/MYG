<template>
    <div id="app">
    <v-app>
      <router-view/>
    </v-app>
    </div>
</template>
<script>

import { mapState, mapActions } from 'vuex'
import Navbar from './components/Navbar';

export default {
  name: 'App',
  data(){
    return{
    }
  },
  components: {
      Navbar
  },
  computed: mapState({
    IsAuthenticated:'authentication/login'
  }),
  methods: mapActions('post', [
    'addPost',
    'deletePost'
  ]),
  created() {
    this.$store.dispatch('')
  }
};
</script>
<style>
.title {
  font-size: 300px;
	font-weight: 900;
  background: -webkit-linear-gradient(right,#fe9a22, #fe5552);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
