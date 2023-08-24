<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-menu">
        <div class="navbar-end">
        <div class="navbar-item">
          <router-link to="/" class="button is-light">Home</router-link>
        </div>
          <template v-if="$store.state.isAuthenticated">
              <div class="navbar-item">
                <button @click="logout()" class="button is-danger">Log out</button>
              </div>
          </template>

          <template v-else>
            <div class="navbar-item">
              <router-link to="/log-in" class="button is-light">Log In</router-link>
            </div>
            <div class="navbar-item">
              <router-link to="/sign-up" class="button is-light">Sign Up</router-link>
            </div>
          </template>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
      logout() {
          axios.defaults.headers.common["Authorization"] = ""

          localStorage.removeItem("token")
          localStorage.removeItem("username")
          localStorage.removeItem("userid")

          this.$store.commit('removeToken')

          this.$router.push('/')
      },
},
}
</script>
<style lang="scss">
@import '../node_modules/bulma';

</style>
