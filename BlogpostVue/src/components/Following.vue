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
        Following
      </div>

      <div
        v-for="(item, index) in componentInfo.following"
        :key="index"
        class="followers-list-container"
      >
        <img class="" :src="item.userProfileImage" alt="" width="50px" height="50px" />
        <div class="followers-name">
          <div class="follow-button">
            <div @click="visitProfile(item)" style="cursor: pointer">
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
