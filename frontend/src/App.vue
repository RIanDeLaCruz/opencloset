<template>
  <div id="app">
    <Navbar :currentRoute="$route"/>
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/NavBar'
export default {
  name: 'App',
  components: {
    Navbar
  },
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
