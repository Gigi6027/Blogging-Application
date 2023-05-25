<template>
  <div>
    <div class="menuContainer">
      <div
        style="cursor: pointer"
        class="user-invite"
        @click="$router.push('/BlogP/dashboard')"
      >
        Welcome User
      </div>
      <div class="navigationMenus">
        <div
          class="create_post_icon"
          @click="$router.push('/BlogP/dashboard/CreatePost')"
        >
          <mdicon name="plus-circle" color="white" size="40" />
        </div>
        <div @click="$router.push('/BlogP/dashboard/SearchUser')">
          Search
        </div>
        <div @click="$router.push('/BlogP/dashboard/MyProfile')">
          My Profile
        </div>
        <div @click="logout(userId)">Logout</div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "Menu",
  components: {},
  props: ["userId"],
  inject: ["setSpinner"],
  methods: {
    delay(ms) {
      return new Promise((res) => setTimeout(res, ms));
    },
    async logout(userId) {
      this.setSpinner(true);
      // Api Call to logout and clear cache
      await this.delay(2000); //To get the fell of API
      this.setSpinner(false);
      localStorage.removeItem("BlogP-auth");
      this.$router.push("/BlogP/login");
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.menuContainer {
  display: flex;
  justify-content: flex-start;
  background-color: rgb(228, 240, 200);
  line-height: 60px;
  font-size: 30px;
}

.user-invite {
  flex-grow: 1;
  display: flex;
  align-items: flex-start;
  margin-left: 30px;
  font-family: Book Antiqua;
}

.navigationMenus {
  display: flex;
  font-family: Garamond;
}

.navigationMenus > div {
  padding-right: 8px;
  padding-left: 8px;
}
.navigationMenus :hover {
  cursor: pointer;
  background-color: rgb(194, 161, 225);
  transition: 2s;
}
</style>
