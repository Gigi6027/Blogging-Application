/* eslint-disable */
const delay = (ms) => new Promise((res) => setTimeout(res, ms));

const CommonService = {
  async loginAuthentication(userName, password) {
      const response = await fetch('http://127.0.0.1:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id: 0,
        username: userName,
        password: password
      })
  });

  console.log(response)
  if (response.ok) {
    const data = await response.json();
    console.log(data)
    return {
      accessToken: data.access_token,
      refreshToken: data.refresh_token,
      userId: data.user_id
    };
  } else {
    throw new Error('Failed to authenticate user.');
  }
},
async registerUser(user) {
    const response = await fetch('http://127.0.0.1:5000/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      id: 0,
      username: user.userName,
      password: user.password,
      name: user.name,
      subname: user.subname,
      email: user.email,
      image: ""
    })
});

console.log(response)
if (response.ok) {
  const data = await response.json();
  console.log(data)
  return "Success"
} else {
  throw new Error('Failed to register user.');
}
},


  async createPost(postInfo, login) {
    debugger
    console.log("Input data " + postInfo)
    
    const response = await fetch('http://127.0.0.1:5000/add-post', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+login.accessToken
      },
      body: JSON.stringify({
        description: postInfo.description,
        title: postInfo.title,
        user_id: login.userId,
        filename: postInfo.title,
        image: postInfo.image
      })
  });

   
  if (response.ok) {
    const data = await response.json();
    console.log(data);
  } else {
    throw new Error('Failed to Add Post.');
  }
  },

  async editPost(postInfo, login) {
    const response = await fetch('http://127.0.0.1:5000/add-post/'+postInfo.postId, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+login.accessToken
      },
      body: JSON.stringify({
        description: postInfo.description,
        title: postInfo.title,
        postId: postInfo.postId, 
        user_id: login.userId,
        filename: postInfo.filename,
        image: postInfo.image
      })
  });

  
  if (response.ok) {
    const data = await response.json();
    console.log(data);
  } else {
    throw new Error('Failed to Edit Post.');
  }
  },

  async deletePost(postId, login) {
    const response = await fetch('http://127.0.0.1:5000/add-post/'+postId, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+login.accessToken
      }
  });

  console.log(response);
  if (response.ok) {
    const data = await response.json();
    console.log(data);
  } else {
    throw new Error('Failed to Delete Post.');
  }
  },

  
  async getInformation(action, login) {
    // fetch('https://localhost:8080/user/myFeed', {
    // Headers: {
    // authorization: 'sdfsdf'
    // }
    // })
    let response;

    await delay(1000);
    if (action === "followers") {

      const apiresponse = await fetch('http://127.0.0.1:5000/my-followers/'+login.userId, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+login.accessToken
      },
      });

      const data = await apiresponse.json();
      console.log(data)

      data.forEach(appendtag);
      function appendtag(item) {
        item.userProfileImage = "data:image/png;base64,"+item.userProfileImage;
      }

      let followers = data;
      // return followers
      
      response = {
      followers: data
      }

      /*
      response = {
        followers: [
          {
            name: "Abhi",
            subname: "@HelloTraveller",
            userId: "002345",
            imageSrc: "follower1.png",
            following: true,
            follower: true,
            hyperlink: "https://www.instagram.com/chinnu.HelloTraveller/",
          },
        ],
      };
      */

    } else if (action === "following") {
      debugger
      const apiresponse = await fetch('http://127.0.0.1:5000/following/'+login.userId, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+login.accessToken
      },
      });

      const data = await apiresponse.json();
      console.log(data)
      

      data.forEach(appendtag);
      function appendtag(item) {
        item.userProfileImage = "data:image/png;base64,"+item.userProfileImage;
      }

      let following = data;
        // return following
        
      response = {
        following: data
      }

      /*
      response = {
        following: [
          {
            name: "Abhi",
            subname: "@HelloTraveller",
            userId: "002345",
            imageSrc: "follower1.png",
            following: true,
            hyperlink: "https://www.instagram.com/chinnu.HelloTraveller/",
          },
          
        ],
      };
      */
    } else if (action === "MyProfile") {
      debugger 
      const apiresponse = await fetch('http://127.0.0.1:5000/profile/'+login.userId, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+login.accessToken
      },
      });
      const data = await apiresponse.json();
      response = data
      // response.posts[0].image = data.posts[0].image;
     
      console.log(data)
      response.posts.forEach(appendtag);
      function appendtag(item) {
        item.image = "data:image/png;base64,"+item.image;
      }
      
      console.log(response.posts)
      // let following = data;
        // return following
        
      
      /*
      response = {
        profileImage: "Profile.png",
        totalPost: 30,
        followers: 50,
        following: 70,
        userId: "007873",
        posts: [
          {
            imageSrc: "post1.jpg",
            like: 12,
            comment: 2,
          },
        ],
      };
      */
    } else if (action === "DashboardHome") {
      const apiresponse = await fetch('http://127.0.0.1:5000/my-feed/'+login.userId, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+login.accessToken
      },
      });
  
      const data = await apiresponse.json();
      console.log(data)
      let dashBoardContent = data;
      data.forEach(appendtag);
      function appendtag(item) {
        item.image = "data:image/png;base64,"+item.image;
        item.userProfileImage = "data:image/png;base64,"+item.userProfileImage;
      }
      // return following
          
      response = {
        dashBoardContent: data
      }

    
    }
    return response;
  },
  getFeedInformation() {
          // NOT USED
    return {
      dashBoardContent: [
        {
          userId: "002345",
          name: "HelloTraveller",
          subname: "Traveller, Karnataka Journey",
          imageSrc: "follower1.png",
          contentSrc: "post1.jpg",
          title: "Travelling Vlogs",
          caption: "Taj Mahal is one of the famous monument",
        },
      ],
    };
  },
  async searchUserInformation(userInput, login) {

    let response;

    //REPLACE TOKEN AFTER RETRIEVING

    debugger
    const apiresponse = await fetch('http://127.0.0.1:5000/all-users', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer '+login.accessToken
    },
    });

    const data = await apiresponse.json();
    console.log(data)

    data.forEach(appendtag);
    function appendtag(item) {
      item.userProfileImage = "data:image/png;base64,"+item.userProfileImage;
    }


    let userList = data.filter(user => user.name.toLowerCase().includes(userInput.toLowerCase()));;
        // return following
        
    response = {
        userList: userList
    }
      
     
    return response;
  },
};

export default CommonService;
