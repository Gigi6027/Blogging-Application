<template>
  <div>
    <div v-if="componentInfo" class="my-profile">
      <div class="profile-info-container">
        <img
          class="profile-picture"
          src="../assets/Profile.png"
          alt=""
          width="100px"
          height="100px"
        />
        <div class="profile-information">
          <div>Total Posts</div>
          <div style="cursor: pointer">{{ componentInfo.totalPost }}</div>
        </div>
        <div class="profile-information">
          <div>Followers</div>
          <div
            style="cursor: pointer"
            @click="$emit('action', 'followers', componentInfo.userId)"
          >
            {{ componentInfo.followers }}
          </div>
        </div>
        <div class="profile-information">
          <div>Following</div>
          <div
            style="cursor: pointer"
            @click="$emit('action', 'following', componentInfo.userId)"
          >
            {{ componentInfo.following }}
          </div>
        </div>
      </div>
      <br /><br />
      <div class="flex-cotnainer-left-align myPost">My Post</div>
      <div class="profile-post-container">
        <div
          v-for="(item, index) in componentInfo.posts"
          :key="index"
          class="profile-post-items"
        >
          <img :src="item.image" alt="" width="300px" height="250px" 
          @click="editpost(item)"
          
          />
        <div class="profile-post-footer" style="margin-top: ">
          <div style="font-weight: bold">{{ item.title }}</div>
          <div style="margin-top: 5px">{{ item.description }}</div>
        </div>
          <div class="icons">
            <mdicon name="heart" color="white" />{{ item.like }}
            <mdicon name="comments" col /> {{ item.comments }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

/* eslint-disable */
export default {
  name: "Menu",
  components: {},
  props: ["componentInfo"],
  inject: ["setSpinner"],
  data() {
    return {};
  },
  created() {
    this.getComponentInformation(this.menuContentComponent, this.login);
  },
  methods: {
    editpost(selecteditem) {
      this.setSpinner(true);
      this.setSpinner(false);
      this.$router.push({name:`EditPost`,
        params: {selecteditem}
      });
    }
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.my-profile {
  margin-left: 40px;
  margin-right: 40px;
}
.profile-info-container {
  display: flex;
}

.profile-information {
  flex-grow: 1;
  font-family: "Trebuchet MS";
  font-size: 20px;
  margin-top: 25px;
}
.profile-picture {
  margin-left: 60px;
  margin-top: 15px;
}

.profile-post-container {
  display: grid;
  grid-template-rows: repeat(3, 1fr);
  grid-template-columns: repeat(3, 1fr);
  column-gap: 3px;
}

.flex-cotnainer-left-align {
  display: flex;
  align-items: flex-start;
}

.myPost {
  font-family: "Trebuchet MS";
  font-size: 20px;
  margin-bottom: 15px;
}

.profile-post-items:hover {
  cursor: pointer;
  opacity: 0.7;
}

.profile-post-items {
  position: relative;
}

.profile-post-items > .icons {
  position: relative;
  top: -130px;
  z-index: 1;
  color: rgb(226, 236, 233);
}

.profile-post-items:hover .icons {
  display: block;
}
</style>
