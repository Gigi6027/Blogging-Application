<template>
  <div class="search-container">
    <input
      v-model="searchUserInput"
      class="search-user"
      type="text"
      placeholder="Please Search Here"
      @input="searchUser(searchUserInput, login)"
    />
    <div v-if="searching" class="spinner"></div>
    <div v-else-if="userList?.userList?.length">
      <div
        v-for="(item, index) in userList?.userList"
        :key="item.userId"
        class="search-list-container"
      >
        <img class="" :src="item.userProfileImage" alt="" width="50px" height="50px" />
        <div class="followers-name">
          <div class="follow-button">
            <div
              @click="visitProfile(item)"
              style="cursor: pointer; font-weight: bold"
            >
              {{ item.name }}
            </div>
          </div>
          <div>{{ item.subname }}</div>
        </div>
        <div
          style="cursor: pointer"
          @click="followAction(item, index, 'follow-action-button')"
          class="follow-action-button"
        >
          {{ item.following ? "Following" : "Follow" }}
        </div>
      </div>

    </div>
  </div>
</template>

<script>
/* eslint-disable */
import CommonService from "@/service/CommonService";
import actionMixin from "@/mixins/actionMixin";
import LoginScreen from "./LoginScreen.vue";
export default {
  name: "SearchUser",
  components: {},
  mixins: [actionMixin],
  data() {
    return {
      userList: [],
      searchUserInput: "",
      searching: false,
      debounce: null,
      login:"",
    };
  },
  created() {
    this.login = localStorage.getItem("BlogP-auth") ? JSON.parse(localStorage.getItem("BlogP-auth")) : null;
    console.log(this.login);
  },
 
  methods: {
    searchUser(userInput, login) {
      // search is implemented with debouncing and throttling to improve the performance
      debugger
      this.searching = true;
      clearTimeout(this.debounce);
      this.debounce = setTimeout(async () => {
      this.userList = await CommonService.searchUserInformation(userInput, login); //here the api call should be made
      this.searching = false;
      }, 600);
      
      
    },

  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
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
  border: 15px solid transparent;
  border-top: 15px solid blue;
  width: 50px;
  height: 50px;
  margin-top: 20px;
  border-radius: 50%;
  animation-name: spin;
  animation-duration: 2s;
  animation-timing-function: ease;
  animation-iteration-count: infinite;
}

.search-container {
  /* border: 2px solid blue; */
  margin-top: 25px;
  margin-left: 25px;
  margin-right: 25px;
}
.search-user {
  line-height: 40px;
  border-radius: 10px;
  width: 100%;
}

.search-list-container {
  display: grid;
  grid-template-columns: 100px 200px 200px;
  margin-top: 40px;
}

img {
  border-radius: 50%;
}

.follow-action-button {
  margin-left: 10px;
  border-radius: 10px;
  background-color: rgb(180, 180, 220);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 15px;
  transition: 1s;
}

#follow-action-button {
  background-color: rgb(80, 80, 222);
  color: white;
}
</style>
