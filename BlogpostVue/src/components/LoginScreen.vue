<template>
  <div>
    <div class="login-container">
      <div class="login-fields-container">
        <div class="login-title">Blog Lite</div>
        <input
          v-model="loginFields.userName"
          class="login-fields"
          type="text"
          name="emailId"
          placeholder="Email Id"
        />
        <input
          v-model="loginFields.password"
          class="login-fields"
          type="password"
          name="password"
          placeholder="Password"
        />
        <input
          class="login-fields login-button"
          type="button"
          value="Login"
          @click="
            login(loginFields.userName, loginFields.password, 'login-container')
          "
        />
        <input
          class="login-fields login-button"
          type="button"
          value="Register"
          @click="$router.push('/BlogP/Register')"
        />
      </div>
      <div class="login-logo-container">
        <img src="../assets/Company_Logo.png" alt="Company Logo" />
      </div>
    </div>
  </div>
</template>

<script>
// import CommonService from "../service/CommonService";
import authMixin from "@/mixins/authMixin";
export default {
  name: "LoginScreen",
  mixins: [authMixin],
  inject: ["setSpinner"],
  data() {
    return {
      loginFields: {
        userName: "",
        password: "",
      },
    };
  },
  created() {
    //checking the user is a known user or unknown
    const loginCache = localStorage.getItem("BlogP-auth");

    // if known user, rerouting to dashboard directly or asking the user to login
    if (loginCache) {
      this.$router.push("/BlogP/dashboard");
    } else {
      this.$router.push("/BlogP/login");
    }
  },
  methods: {},
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.login-container {
  height: 100vh;
  width: 100vw;
  display: flex;
}
.login-container > .login-fields-container {
  flex-grow: 3;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.login-fields-container > .login-fields {
  margin: 12px;
  border-radius: 10px;
  border-width: 0;
  line-height: 50px;
}
input {
  background-color: rgb(242, 243, 195);
}
.login-fields-container > .login-button {
  background-color: rgb(112, 112, 213);
  color: white;
  font-family: ui-serif;
}

.login-fields-container > .login-title {
  font-family: cursive;
  font-size: 30px;
}
.login-logo-container {
  flex-grow: 1;
}

.login-logo-container > img {
  height: 90%;
}

.login-button:hover {
  background-color: green;
  transition: 1s;
  cursor: pointer;
}
</style>
