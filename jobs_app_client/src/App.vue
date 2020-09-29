<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
</style>

<template>
  <div id="app" class="container">
    <nav class="navbar navbar-expand-sm bg-light">
      <ul class="navbar-nav">
        <h4>
          <router-link :to="{ name: 'Index' }" class="nav-link"
            >Job-finder</router-link
          >
        </h4>
        <router-link :to="{ name: 'Create' }" class="btn btn-outline-primary"
          >Add new job</router-link
        >
      </ul>
      <ul>
        <router-link
          v-if="authenticated"
          to="/login"
          v-on:click.native="logout()"
          replace
        >
          Logout
        </router-link>
      </ul>
    </nav>
    <!-- <router-view @authenticated="setAuthenticated" /> -->
    <transition name="fade">
      <div class="gap">
        <router-view @authenticated="setAuthenticated" />
      </div>
    </transition>
  </div>
</template>


<script>
export default {
  name: "App",
  data() {
    return {
      authenticated: false,
      fakeAccount: {
        username: "recruiter@screel.in",
        password: "password123",
      },
    };
  },
  mounted() {
    if (!this.authenticated) {
      this.router.replace({ name: "Login" });
    }
  },
  methods: {
    setAuthenticated(status) {
      this.authenticated = status;
    },
    logout() {
      this.authenticated = false;
    },
  },
};
</script>


