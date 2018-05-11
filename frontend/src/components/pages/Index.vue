<template>
  <div class="hero">
    <div class="introduction">
      <h2>
        Welcome to <span class="green">OpenCloset</span>,<br>
        your one-stop destinatiion for fashion rentalsi
      </h2>
      <div class="icons">
        <figure>
          <img src="../../assets/search-icon.png" alt="">
          <figcaption>
            Browse
          </figcaption>
        </figure>
        <figure>
          <img src="../../assets/select-icon.png" alt="">
          <figcaption>
            Select
          </figcaption>
        </figure>
        <figure>
          <img src="../../assets/pay-icon.png" alt="">
          <figcaption>
            Rent
          </figcaption>
        </figure>
        <figure>
          <img src="../../assets/return-icon.png" alt="">
          <figcaption>
            Return
          </figcaption>
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexPage'
}
</script>

<style>
.hero {
  height: 80vh;
  background-image: url('../../assets/startpage.png');
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding: 5vw;
}

.hero h2 {
  font-weight: 300;
}

.hero h2 span {
  font-weight: 700;
}

.introduction {
  width: 20vw;
}

.introduction .icons {
  width: 100%;
  display: grid;
  grid-template-rows: repeat(2, 1fr);
  grid-template-columns: repeat(2, 1fr);
}

.introduction .icons img {
  width: 100%;
}
</style>
