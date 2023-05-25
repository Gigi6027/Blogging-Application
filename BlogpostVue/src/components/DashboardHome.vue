<template>
  <div class="container">
    <div class="dashboard-container">
      <div v-for="item in componentInfo.dashBoardContent" :key="item.user_id">
        <div class="dashboard-feed-header" @click="visitProfile(item)">
          <img
            class=""
            :src="item.userProfileImage"
            alt=""
            width="40px"
            height="40px"
          />
          <div class="followers-name">
            <div>{{ item.name }}</div>
            <div>{{ item.subname }}</div>
          </div>
        </div>
        <div class="dashboard-feed-content" style="margin-top: 10px">
          <img
            :src="item.image"
            alt=""
            srcset=""
            width="400px"
            height="250px"
            align-self="left"
          />
        </div>
        <div class="dashboard-feed-footer" style="margin-top: ">
          <div style="font-weight: bold">{{ item.title }}</div>
          <div style="margin-top: 5px">{{ item.description }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import actionMixin from "@/mixins/actionMixin";
export default {
  name: "Menu",
  components: {},
  mixins: [actionMixin],
  props: ["componentInfo"],
  data() {
    return {};
  },

  methods: {
    convertBase64ToImage(base64) {
      if (base64) {
        const image = new Image();
        image.src = base64;
        return URL.createObjectURL(this.base64ToBlob(base64));
      }
    },
    base64ToBlob(base64) {
      const byteString = atob(base64.split(",")[1]);
      const mimeString = base64.split(",")[0].split(":")[1].split(";")[0];
      const ab = new ArrayBuffer(byteString.length);
      const ia = new Uint8Array(ab);
      for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }
      return new Blob([ab], { type: mimeString });
    },
  },
  //export (base64ToBlob)
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.container {
  margin: 40px;
}
.dashboard-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  row-gap: 30px;
  column-gap: 50px;
}

.dashboard-feed-header {
  display: flex;
  cursor: pointer;
  padding-left: 40px;
}

.followers-name {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-left: 10px;
  font-size: 22px;
  /* margin-left: 10px; */
}

.dashboard-feed-footer {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  font-size: 25px;
  padding-left: 40px;
}
</style>
