<template>
  <div id="app">
    <div v-if="spinner" class="spinner"></div>
    <router-view>
      <BlogLite />
    </router-view>
  </div>
</template>

<script>
/* eslint-disable */
import BlogLite from "./components/BlogLite.vue";

export default {
  name: "App",
  components: {
    BlogLite,
  },
  data() {
    return {
      spinner: false,
    };
  },
  methods: {
    setSpinner: function (spinnerValue) {
      this.spinner = spinnerValue;
    },
  },
  // Instead of Prop Drilling into the each application. I'm using injection concet to check the spinner status across the component
  // Instead of Inject I can use VueX also as alternative for this
  provide: function () {
    return {
      setSpinner: this.setSpinner,
    };
  },
  watch: {
    spinner: {
      handler(val) {
        const appContainer = document.querySelectorAll("#app");
        if (val) {
          appContainer[0].style.opacity = 0.5;
        } else {
          appContainer[0].style.opacity = 1;
        }
      },
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  50% {
    transform: rotate(360deg);
  }
  100% {
    transform: rotate(720deg);
  }
}

.spinner {
  border: 20px solid transparent;
  border-top: 20px solid rgb(87, 87, 188);
  position: absolute;
  bottom: 50%;
  left: 45%;
  width: 50px;
  height: 50px;
  /* margin-top: 20px; */
  border-radius: 50%;
  animation-name: spin;
  animation-duration: 1s;
  animation-timing-function: ease;
  animation-iteration-count: infinite;
}
</style>
