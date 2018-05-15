<template>
  <router-link :to="{ path: link }">{{text}}</router-link>
</template>

<script>
export default {
  name: 'MenuButton',
  props: {
    text: String,
    link: String
  }
}
</script>

<style scoped>
a {
  display: inline-block;
  padding: 1em 3rem;
  border-radius: 1.2rem;
  background-color: black;
  color: white;
  text-transform: uppercase;
  text-decoration: none;
  font-size: 0.69rem;
}
</style>
