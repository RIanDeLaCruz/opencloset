<template>
  <div>
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
    <div class="login">
      <div class="login_form">
        <h1>Sign In</h1>
        <form>
          <input
              type="text"
              name="username"
              id="username"
              placeholder="Username"
              v-model="username">
          <input
              type="password"
              name="password"
              id="password"
              placeholder="Password"
              v-model="password">
          <button @click="submitForm">Login</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'IndexPage',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm(evt) {
      evt.preventDefault()
      axios.post('http://opencloset.local/api/login/', {
        username: this.username,
        password: this.password
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err.response)
      })
    }
  }
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

  .login {
    height: 80vh;
    background-image: url('../../assets/signin.png');
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding: 5vw;
  }

  .login_form {
    width: 30vw;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .login_form input[type="text"],
  .login_form input[type="password"] {
    width: 70%;
    margin: 1em 0;
    padding: 1em;
    border-radius: 1rem;
    border-style: solid;
    float: left;
  }

  .login_form button {
    width: 30%;
    float: left;
    height: 36px;
    border-radius: 1rem;
    margin-top: 1rem;
    border-style: solid;
    background-color: rgb(85, 125, 110);
    color: white;
  }
</style>
