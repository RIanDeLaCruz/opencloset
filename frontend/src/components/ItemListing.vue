<template>
  <figure class="listing">
    <div class="image_wrapper">
      <img :src="image_url" alt="">
    </div>
    <figcaption class="listing_caption">
      <h2>{{ name }}</h2>
      <h3>{{ lent_by }}</h3>
      <p><strong>Size:</strong> {{ size }}</p>
      <p><strong>Brand:</strong> {{ brand }}</p>
      <p><strong>P{{ price }}</strong></p>
    </figcaption>
  </figure>
</template>

<script>
export default {
  name: 'ItemListing',
  props: [
    'name', 'image_url', 'lent_by', 'size', 'brand', 'price'
  ]
}
</script>

<style>
.listing {
  width: 100%;
  height: 100%;
  margin: 0;
  display: flex;
  align-items: center;
}

.listing img {
  width: 100%;
}

.image_wrapper {
  width: 50%;
  height: 100%;
}

.listing_caption {
  width: 50%;
  min-height: 70%;
  padding: 1rem;
  border-radius: 0 1.2rem 1.2rem 0;
  background-color: rgb(215, 212, 213);
  text-align: left;
  display: flex;
  flex-direction: column;
}

.listing_caption h2,
.listing_caption h3,
.listing_caption p {
  margin: 0;
}

.listing_caption h2 {
    color: rgb(85, 125, 110);
}

.listing_caption h3 {
  font-style: italic;
  font-weight: 300;
  font-size: 1em;
}

.listing_caption p:first-of-type {
  margin-top: 1rem;
}

.listing_caption p:last-of-type {
  margin-top: 1rem;
}
</style>
