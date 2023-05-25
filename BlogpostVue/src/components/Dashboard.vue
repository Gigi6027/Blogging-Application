<!-- eslint-disable -->
<template>
  <div>
    <Menu :login="login" />
    <component
      :is="menuContentComponent"
      :componentInfo="myProfile"
      @action="handleAction"
    />
  </div>
</template>

<script>
/* eslint-disable */
import CommonService from "@/service/CommonService";
import Menu from "../components/Menu.vue";
export default {
  name: "Dashboard",
  components: {
    Menu,
    DashboardHome: () => import("@/components/DashboardHome.vue"),
    MyProfile: () => import("@/components/MyProfile.vue"),
    Followers: () => import("@/components/Followers.vue"),
    Following: () => import("@/components/Following.vue"),
    SearchUser: () => import("@/components/SearchUser.vue"),
    CreatePost: () => import("@/components/CreatePost.vue"),
    EditPost: () => import("@/components/EditPost.vue"),
  },
  inject: ["setSpinner"],
  data() {
    return {
      menuContentComponent: "DashboardHome",
      myProfile: {},
      login: null,
      userId:null
    };
  },
  created() {
    this.login = localStorage.getItem("BlogP-auth") ? JSON.parse(localStorage.getItem("BlogP-auth")) : this.login;
    this.getComponentInformation(this.menuContentComponent, this.login);
    this.userId=login.userId
  },
  methods: {
    handleAction(actionName, login) {
      this.$router.push(`/BlogP/dashboard/${actionName}`);
    },
    async getComponentInformation(componentName, login) {
      this.setSpinner(true);
      //I'm mocking data here, this should be the actual Api call
      this.myProfile = await CommonService.getInformation(
        componentName,
        login
      );
      this.setSpinner(false);
    },
  },
  watch: {
    async $route(to, from) {
      this.menuContentComponent = to.params.subMenu || "DashboardHome";
      this.myProfile = {};
      this.getComponentInformation(this.menuContentComponent, this.login);
    },
  },
};
</script>

<style lang="scss" scoped></style>
