<template>
  <div id="app">
    <Navbar
      :currentRoute="$route"
      :username="username"
      :isLoggedIn="isLoggedIn"
      v-if="isLoggedIn"
      @logout="logouthandler"/>
    <Navbar :currentRoute="$route" v-else />
    <router-view @loggedIn="handler"/>
  </div>
</template>

<script>
import Navbar from './components/NavBar'
export default {
  name: 'App',
  components: {
    Navbar
  },
  data() {
    return {
      username: '',
      isLoggedIn: false
    }
  },
  methods: {
    handler(val) {
      console.log(val)
      if(val != '') {
        this.username = val
        this.isLoggedIn = true
      }
    },
    logouthandler(val) {
      this.username = ''
      this.isLoggedIn = false
    }
  }
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
