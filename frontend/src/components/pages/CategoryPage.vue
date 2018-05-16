<template>
  <div>
    <h1> {{ category.name }}</h1>
    <ul>
      <li v-for="item in category.items">
        <ItemListing
          :name="item.name"
          :image_url="item.picture"
          :lent_by="item.lent_by"
          :size="item.size"
          :brand="item.brand"
          :price="item.price"
        />
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import ItemListing from '../ItemListing'

export default {
  name: 'CategoryPage',
  data() {
    return {
      category: {}
    }
  },
  beforeMount() {
    axios.get(`http://opencloset.local/api/section/${this.$route.params.id}`)
    .then(res => {
      this.category = res.data
    })
    .catch(err => {
      console.log(err)
    })
  },
  components: {
    ItemListing
  }
}
</script>

<style scoped>
  h1 {
    text-align: left;
    padding-left: 5vw;
    color: rgb(85, 125, 110);
  }

  ul {
    margin-left: 5vw;
    width: 80%;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(2, 40%);
    grid-gap: 2.4rem;
  }

  li {
    list-style-type: none;
  }
</style>
