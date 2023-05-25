/* eslint-disable */
export default {
  name: "Action Mixin",
  methods: {
    visitProfile(item) {
      //Api Call is required to visit the Profile
      window.open(item.name, "_blank");
    },
    followUser(item) {
      //here Api Call should happend to follow the user
    debugger
    let login = localStorage.getItem("BlogP-auth") ? JSON.parse(localStorage.getItem("BlogP-auth")) : null;

      fetch('http://127.0.0.1:5000/follow/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer '+login.accessToken
        },
        body: JSON.stringify({
          "following": item.following,
          "leader_user_id": item.userId,
          "follower_user_id": login.userId
        })
        });


      item.following = !item.following;
    },
    removeFollower(item, index, targetElement) {
      //here Api Call should happend to remove the follower
      debugger
      let login = localStorage.getItem("BlogP-auth") ? JSON.parse(localStorage.getItem("BlogP-auth")) : null;
      

      fetch('http://127.0.0.1:5000/remove-follower', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer '+login.accessToken
      },
      body: JSON.stringify({
          "leader_user_id": login.userId,
          "block": true,
          "follower_user_id": item.userId
      })
      });


      item.follower = false;
      const removeBtn = document.querySelectorAll(`.${targetElement}`);
      removeBtn[index].style.opacity = 0.7;
    },
    followAction(item, index, targetElement) {
      //here Api Call should happend to remove the follower
      let login = localStorage.getItem("BlogP-auth") ? JSON.parse(localStorage.getItem("BlogP-auth")) : null;

      debugger

      fetch('http://127.0.0.1:5000/follow', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer '+login.accessToken
      },
      body: JSON.stringify({
          "following": !item.following, 
          "leader_user_id": item.userId,
          "follower_user_id": login.userId
      })
      });


      item.following = !item.following;
      //Change the style of follow, unfollow button on the action
      const followActionBtn = document.querySelectorAll(`.${targetElement}`);
      if (item.following) {
        followActionBtn[index].removeAttribute("id");
      } else {
        followActionBtn[index].setAttribute("id", `${targetElement}`);
      }
    },
  },
};
