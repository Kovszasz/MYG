<template>
  <div>
    <Navbar/>
    <v-content>
        <h1>MixYourGenes</h1>
    </v-content>
  </div>
</template>
<script>
  import Vue from 'vue';
  import { NavbarPlugin } from 'bootstrap-vue'
  Vue.use(NavbarPlugin)
  import Navbar from './Navbar.vue'
  import { mapState, mapActions } from 'vuex'
  export default {
    name: 'Index',
    components:{
     Navbar,
     },
    data: function(){
        return{
          isActive: false
        }
    },
    resolve: {
      alias: {
        'vue$': 'vue/dist/vue.esm.js'
      }
    },
    computed: mapState({
      IsAuthenticated:'authentication/login'
    }),
    methods: mapActions('post', [
      'addPost',
      'deletePost'
    ]),
    created() {
      //this.$store.dispatch()
    }
    }
</script>
<style scope>
  .sidemenu{
  margin-top:80px;

  }
</style>
