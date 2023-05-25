<!-- eslint-disable -->
<template>
  <div>
    <div class="followers-container">
      <div
        class="flex-cotnainer-left-align"
        
        style="
          margin-top: 15px;
          margin-bottom: 25px;
          font-family: 'Trebuchet MS';
        "
      >
        Followers
      </div>

      <div
        v-if="componentInfo?.followers?.length"
        v-for="(item, index) in componentInfo.followers"
        :key="index"
        class="followers-list-container"
      >
        <img class="" :src="item.userProfileImage" alt="" width="50px" height="50px" />
        <div class="followers-name">
          <div class="follow-button">
            <div @click="visitProfile(item)" style="cursor: pointer">
              {{ item.name }}
            </div>
            <div
              v-if="!item.following"
              style="font-size: 10px; margin-left: 10px; cursor: pointer"
              @click="followUser(item)"
            >
              Follow
            </div>
          </div>
          <div>{{ item.subname }}</div>
        </div>
        <div
          style="cursor: pointer"
          @click="removeFollower(item, index, 'remove-button')"
          class="remove-button"
        >
          {{ !item.follower ? "Remove" : "Removed" }}
        </div>
        <div class="remove-icon" style=" margin-top: 7px">
          <mdicon
            :name="item.follower ? 'checkbox-marked-circle' : 'cancel'"
            color="white"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import actionMixin from "@/mixins/actionMixin";
export default {
  name: "Followers",
  components: {},
  props: ["componentInfo"],
  mixins: [actionMixin],
  methods: {},
};
</script>

<style scoped>
.remove-icon {
  transition: 1s;
  position: absolute;
  margin-left: 425px;
  
}
.followers-container {
  margin-left: 40px;
}
.followers-list-container {
  display: flex;
  margin-bottom: 20px;
}
.followers-list-item {
  display: flex;
  align-items: center;
  justify-content: center;
}

.followers-name {
  margin-left: 5px;
}

.remove-button {
  position: absolute;
  margin-left: 300px;
  border-radius: 10px;
  background-color: rgb(180, 180, 220);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 15px;
  transition: 1s;
}

#remove-button {
  background-color: green;
}

.flex-cotnainer-left-align {
  display: flex;
  align-items: flex-start;
}

img {
  border-radius: 50%;
}

.follow-button {
  display: flex;
}
</style>
