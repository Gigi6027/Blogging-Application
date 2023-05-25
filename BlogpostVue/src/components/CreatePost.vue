<!-- eslint-disable -->
<template>
  <div class="container">
    <div class="create_post_container">
      <div>
        <div style="position: relative">
          <img id="image_container" src="" class="image_container" />
          <input
            type="file"
            name="Upload"
            id="uploadImage"
            @change="imageSelected"
          />
        </div>
      </div>
      <div>
        <input
          v-model="createPost.title"
          type="text"
          placeholder="Please Enter the Post Name"
        />
      </div>
      <div>
        <input
          v-model="createPost.description"
          type="text"
          placeholder="Please Enter the Post Description"
        />
      </div>
      <div>
        <input type="submit" value="Post" @click="submitPost(createPost, login)" />
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import CommonService from "@/service/CommonService";
debugger
export default {
  name: "Menu",
  components: {},
  props: [],
  inject: ["setSpinner"],

  data() {
    return {
      createPost: {
        title: "",
        description: "",
        user_id: "",
        filename: "",
        image: "",
        
      },
      login:""
    };
  },
  
  created() {
    // this.login = localStorage.getItem("BlogP-auth") ? JSON.parse(localStorage.getItem("BlogP-auth")) : null;
    this.login = localStorage.getItem("BlogP-auth") ? JSON.parse(localStorage.getItem("BlogP-auth")) : this.login;
    console.log(this.login);
  },

  methods: {
    delay(ms) {
      return new Promise((res) => setTimeout(res, ms));
    },
    imageSelected(e) {
      const filename = document.getElementById("uploadImage").files[0].name;
      let oFReader = new FileReader();
      oFReader.readAsDataURL(document.getElementById("uploadImage").files[0]);
      oFReader.onload = function (oFREvent) {
        document.getElementById("image_container").src = oFREvent.target.result;
        this.createPost.filename = filename;
        this.createPost.image1 = oFREvent.target.result;
        this.createPost.image = oFREvent.target.result.replace('data:', '').replace(/^.+,/, '');   
      }.bind(this);
    },
    async submitPost(postInfo, login) {
      this.setSpinner(true);
      // postInfo.user_id = login.userid
      //I'm mocking data here, this should be the actual Api call
      const post = await CommonService.createPost(postInfo, login);
      this.setSpinner(false);
      this.$router.push(`/blogP/dashboard/MyProfile`);
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
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.container {
  margin: 15px 400px 10px;
}
.create_post_container {
}

.image_container {
  height: 400px;
  width: 100%;
  border: 5px dotted blue;
  border-radius: 5px;
}

input[type="text"] {
  line-height: 30px;
  width: 100%;
  margin-top: 10px;
  border-radius: 5px;
}

input[type="submit"] {
  line-height: 30px;
  margin-top: 10px;
  border-radius: 5px;
  width: 30%;
  background-color: rgb(158, 223, 158);
  cursor: pointer;
}

input[type="file"] {
  position: absolute;
  margin-top: -200px;
  margin-left: -85px;
}
</style>
