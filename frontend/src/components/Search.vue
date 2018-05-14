<template>
  <div>
    <img src="../assets/search-icon.png" alt="">
    <input type="search">
  </div>
</template>

<script>
export default {
  name: 'SeearchBar'
}
</script>

<style scoped>
div {
  display: flex;
  align-items: center;
}

img {
  width: 36px;
  height: 36px;
  margin-left: 1.2rem;
}

input {
  height: 36px;
  width: 30vw;
  border-radius: 1.2rem;
  border-style: solid;
}
</style>
