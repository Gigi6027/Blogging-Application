<template>
  <div>
    <div class="register-container">
      <div class="register-fields-container">
        <div class="register-title">Register for Blog Lite</div>
        <input
          v-model="registerFields.name"
          class="register-fields"
          type="text"
          name="name"
          placeholder="Name"
        />
        <input
          v-model="registerFields.subname"
          class="register-fields"
          type="text"
          name="subname"
          placeholder="SubName"
        />
        <input
          v-model="registerFields.userName"
          class="register-fields"
          type="text"
          name="userName"
          placeholder="UserName"
        />
        <input
          v-model="registerFields.email"
          class="register-fields"
          type="text"
          name="email"
          placeholder="Email"
        />
        <input
          v-model="registerFields.password"
          class="register-fields"
          type="password"
          name="password"
          placeholder="Password"
        />
        <input
          v-model="registerFields.confirmPassword"
          class="register-fields"
          type="password"
          name="confirmPassword"
          placeholder="Confirm Password"
        />
        <input
          class="register-fields register-button"
          :disabled="!passwordsMatch" 
          type="button"
          value="Register"
          @click="
            register(registerFields,'register-container')"
        />
      </div>
      <div class="register-logo-container">
        <img src="../assets/Company_Logo.png" alt="Company Logo" />
      </div>
    </div>
  </div>
</template>
<script>
// import CommonService from "../service/CommonService";
import authMixin from "@/mixins/authMixin";
export default {
  name: "RegisterScreen",
  mixins: [authMixin],
  inject: ["setSpinner"],
  data() {
    return {
      registerFields: {
        name: "",
        subname: "",
        userName: "",
        email: "",
        password: "",
        confirmPassword: "",
      },
    };
  },
  created() {},
  computed: {
    passwordsMatch() {
      return this.registerFields.password === this.registerFields.confirmPassword;
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

.register-container {
  height: 100vh;
  width: 100vw;
  display: flex;
}

.register-container > .register-fields-container {
  flex-grow: 3;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.register-fields-container > .register-fields {
  margin: 12px;
  border-radius: 10px;
  border-width: 0;
  line-height: 50px;
}

input {
  background-color: rgb(242, 243, 195);
}

.register-fields-container > .register-button {
  background-color: rgb(112, 112, 213);
  color: white;
  font-family: ui-serif;
}

.register-fields-container > .register-title {
  font-family: cursive;
  font-size: 30px;
}

.register-logo-container {
  flex-grow: 1;
}

.register-logo-container > img {
  height: 90%;
}

.register-button:hover {
  background-color: green;
  transition: 1s;
  cursor: pointer;
}
</style>