<template>
  <div>
  <v-app-bar app color="default">
    <v-toolbar-title><router-link :to = "{ name:'home' }" >MixYourGenes</router-link></v-toolbar-title>
    <!--<v-switch v-model="switch1" inset ></v-switch>-->
    <v-spacer></v-spacer>
    <v-text-field
    class="mx-4"
    flat
    hide-details
    label="Search"
    solo-inverted
  ></v-text-field>
    <v-spacer v-if="!IsAuthenticated"></v-spacer>
    <v-menu bottom >
      <template v-slot:activator="{ on }">
        <v-btn icon v-on="on">
          <img src="@/assets/settings.png" height="40%" width="40%">
        </v-btn>
      </template>
      <v-list>
          <v-list-item ><v-list-item-title><router-link :to = "{ name:'messages' }" class="dropdown-item">Message</router-link></v-list-item-title></v-list-item>
          <v-list-item v-if="!IsAuthenticated "><v-list-item-title><router-link :to = "{ name:'register' }" class="dropdown-item">Register</router-link></v-list-item-title></v-list-item>
          <v-list-item v-if="!IsAuthenticated "><v-list-item-title><router-link :to = "{ name:'login' }" class="dropdown-item">LogIn</router-link></v-list-item-title></v-list-item>
          <v-list-item v-if="IsAuthenticated "><v-list-item-title><router-link :to = "{ name:'logout' }" class="dropdown-item">LogOut</router-link></v-list-item-title></v-list-item>
      </v-list>
    </v-menu>
    </v-app-bar>
    </div>

</template>
<script>

import { mapState, mapActions } from 'vuex'
import Vue from 'vue';
import {NavbarPlugin} from 'bootstrap-vue';
Vue.use(NavbarPlugin);
export default {
  name: 'Navbar',
  props:{
  },
  data(){
    return{
    User:'User'
    }
  },
  components: {
  }, computed:{ ...mapState('authentication',{IsAuthenticated:'login',user:'user',IsAdmin:'is_superuser'})},
  methods:{
  IMGurl:function(img){
          return require(`../assets${img.avatar}`)
          }
  }

};
</script>
<style>
  .sidemenu{
  margin-top:80px;

  }
</style>
