<template>
  <figure>
    <div class="image_wrapper">
      <img :src="image_url" alt="">
    </div>
    <figcaption>
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
figure {
  width: 100%;
  height: 100%;
  margin: 0;
  display: flex;
  align-items: center;
}

figure img {
  width: 100%;
}

.image_wrapper {
  width: 50%;
  height: 100%;
}

figcaption {
  width: 50%;
  min-height: 70%;
  padding: 1rem;
  border-radius: 0 1.2rem 1.2rem 0;
  background-color: rgb(215, 212, 213);
  text-align: left;
  display: flex;
  flex-direction: column;
}

figcaption h2,
figcaption h3,
figcaption p {
  margin: 0;
}

figcaption p:first-of-type {
  margin-top: 1rem;
}

figcaption p:last-of-type {
  margin-top: 1rem;
}
</style>
