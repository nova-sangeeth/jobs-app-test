<template>
  <div>
    <center><p class="display-4">Login</p></center>
    <input
      type="text"
      class="form-control"
      name="username"
      v-model="input.username"
      placeholder="Username"
    />
    <br />
    <input
      type="password"
      class="form-control"
      name="password"
      v-model="input.password"
      placeholder="Password"
    />
    <center>
      <button class="btn btn-light" type="button" v-on:click="login()">
        Login
      </button>
    </center>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      input: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    login() {
      if (this.input.username != "" && this.input.password != "") {
        if (
          this.input.username == this.$parent.fakeAccount.username &&
          this.input.password == this.$parent.fakeAccount.password
        ) {
          this.$emit("authenticated", true);
          this.$router.replace({ name: "Index" });
        } else {
          console.log("The username and / or password is incorrect");
        }
      } else {
        console.log("A username and password must be present");
      }
    },
  },
};
</script>

