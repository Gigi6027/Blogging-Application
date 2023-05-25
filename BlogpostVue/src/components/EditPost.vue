<template>
    <div class="container">
      <div class="create_post_container">
        <div>
          <div style="position: relative">
            <img id="image_container" :src=createPost.editImage class="image_container" />
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
          <input class="savebutton" type="submit" value="Post" @click="submitPost(createPost, login)" />
          <input class="deletebutton" type="submit" value="Delete" @click="deletePost(createPost.postId, login)" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  /* eslint-disable */
  import CommonService from "@/service/CommonService";
  export default {
    name: "Menu",
    components: {},
    props: ["EditPost"],
    inject: ["setSpinner"],
    data() {
      return {
        createPost: {
          postId: "",
          title: "",
          description: "",
          user_id: "",
          filename: "",
          image: "",
          postId: "",
          editImage: "",
        },
        login:""
      };
    },
    created() {
      this.login = localStorage.getItem("BlogP-auth") ? JSON.parse(localStorage.getItem("BlogP-auth")) : null;
      console.log(this.login);    
      // console.log(this.$route.params.selecteditem);
      this.createPost = this.$route.params.selecteditem;
      this.createPost.editImage = this.$route.params.selecteditem.image;
      this.createPost.image = this.$route.params.selecteditem.image.replace('data:', '').replace(/^.+,/, '')
      console.log(this.$route.params.selecteditem);
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
          this.createPost.editImage = oFREvent.target.result;
          this.createPost.image = oFREvent.target.result.replace('data:', '').replace(/^.+,/, '');   
        }.bind(this);
      },
      async submitPost(postInfo, login) {
        this.setSpinner(true);
        // console.log(login);
        //I'm mocking data here, this should be the actual Api call
        const post = await CommonService.editPost(postInfo, login);
        this.setSpinner(false);
        this.$router.push(`/BlogP/dashboard/MyProfile`);
      },
      
      async deletePost(postId, login) {
        this.setSpinner(true);
        console.log(login);
        //I'm mocking data here, this should be the actual Api call
        const post = await CommonService.deletePost(postId, login);
        this.setSpinner(false);
        this.$router.push(`/BlogP/dashboard/MyProfile`);
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
  
  .savebutton {
    line-height: 30px;
    margin-top: 10px;
    border-radius: 5px;
    width: 30%;
    background-color: rgb(158, 223, 158);
    cursor: pointer;
    margin-right: 50px;
  }
  .deletebutton {
    line-height: 30px;
    margin-top: 10px;
    border-radius: 5px;
    width: 30%;
    background-color: rgb(239, 137, 137);
    cursor: pointer;
  }
  
  
  input[type="file"] {
    position: absolute;
    margin-top: -200px;
    margin-left: -85px;
  }
  </style>
  