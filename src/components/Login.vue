<template>
<div>
  <Navbar></Navbar>
  <LoginCore/>
</div>
</template>

<script>
import Navbar from './Navbar.vue'
import LoginCore from './LoginCore.vue'
  export default {
    name: 'login',
    components: {
        Navbar,
        LoginCore
    },
    props:{
      IsEmbed:Boolean
    },
    data () {
      return {
        username: '',
        password: '',
        wrongCred: false // activates appropriate message if set to true
      }
    },
    methods:{
      loginUser () { // call loginUSer action
        this.$store.dispatch('authentication/loginUser', {
          username: this.username,
          password: this.password
        }).then(() => {
              this.wrongCred = false
              this.$router.push({ name: 'home' })
            })
          .catch(err => {
            this.wrongCred = true // if the credentials were wrong set wrongCred to true
          })
        }
      }
  }
</script>
