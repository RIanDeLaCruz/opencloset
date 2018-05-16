<template>
  <div class="login_form">
    <h2>Sign Up</h2>
    <form>
      <input
          type="email"
          name="email"
          id="email"
          placeholder="Email Address"
          v-model="email">
      <input
          type="text"
          name="username"
          id="username"
          placeholder="Username"
          v-model="username">
      <input
          type="text"
          name="first_name"
          id="first_name"
          placeholder="First Name"
          v-model="first_name">
      <input
          type="text"
          name="last_name"
          id="last_name"
          placeholder="Last Name"
          v-model="last_name">
      <input
          type="password"
          name="password"
          id="password"
          placeholder="Password"
          v-model="password">
      <button @click="submitForm">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUpPage',
  data() {
    return {
      email: '',
      username: '',
      first_name: '',
      last_name: '',
      password: ''
    }
  },
  methods: {
    submitForm(evt) {
      evt.preventDefault()
      axios.post('http://opencloset.local/api/users/', {
        email: this.email,
        username: this.username,
        last_name: this.last_name,
        first_name: this.first_name,
        password: this.password
      })
      .then(res => {
        window.localstorage.setItem('username', res.data.username)
        this.$emit('loggedIn', window.localStorage.getItem('username'))
        this.$router.push({name: 'Index'})
      })
      .catch(err => {
        console.log(err.response)
      })
    }
  }
}
</script>

<style scoped>
  .login_form {
    margin: 0 auto;
    width: 30vw;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .login_form input[type="email"],
  .login_form input[type="text"],
  .login_form input[type="password"] {
    width: 100%;
    margin: 1em 0;
    padding: 1em;
    border-radius: 1rem;
    border-style: solid;
    float: left;
  }

  .login_form button {
    width: 30%;
    height: 36px;
    border-radius: 1rem;
    margin-top: 1rem;
    border-style: solid;
    background-color: rgb(85, 125, 110);
    color: white;
  }
</style>
