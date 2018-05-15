<template>
  <header>
    <div class="identity_bar">
      <img src="../assets/logo.png" alt="" id="logo">
      <div class="actions">
        <span v-if="isLoggedIn">Hello, <span="green">{{username}}</span></span>
        <a class="action" href="/signup">SIGN UP</a>
        <a class="action" href="/login">LOGIN</a>
      </div>
    </div>
    <div class="menulist">
      <nav>
        <ul>
          <li v-bind:class="{ active: isHome }">
            <MenuButton link="/" text="home"/>
          </li>
          <li><MenuButton link="/about" text="about"/></li>
          <li v-bind:class="{ active: isMen }">
            <MenuButton link="/category/1" text="men's"/>
          </li>
          <li v-bind:class="{ active: isWomen }">
            <MenuButton link="/category/2" text="women's"/>
          </li>
        </ul>
      </nav>
      <SearchBar/>
    </div>
  </header>
</template>

<script>
import MenuButton from '../components/MenuButton'
import SearchBar from '../components/Search'

export default {
  name: 'Navbar',
  props: {
    isLoggedIn: Boolean,
    username: String,
    currentRoute: Object
  },
  components: {
    MenuButton,
    SearchBar
  },
  computed: {
    isHome: function() {
      return this.$route.name == 'Index'
    },
    isMen: function() {
      return this.$route.name == 'Category' && this.$route.params.id == 1
    },
    isWomen: function() {
      return this.$route.name == 'Category' && this.$route.params.id == 2
    }
  }
}
</script>

<style>
header {
  padding: 2.4rem 5vw;
}

.identity_bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

#logo {
  width: 20vw;
}

.actions {
  display: flex;
  align-items: center;
  height: 100%;
  width: 15vw;
  justify-content: space-around;
}

a {
  text-decoration: none;
  text-transform: uppercase;
}

.menulist {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 2.4rem;
}

nav ul {
  padding: 0;
  margin: 0;
  display: flex;
}

nav ul li {
  list-style-type: none;
}

nav ul li:first-child {
  margin-right: 1rem;
}

nav ul li:not(:first-child) {
  margin-left: 1rem;
  margin-right: 1rem;
}

nav ul li:last-child {
  margin-right: 0;
}

nav li.active a {
  background-color: rgb(85, 125, 110);
}
</style>
