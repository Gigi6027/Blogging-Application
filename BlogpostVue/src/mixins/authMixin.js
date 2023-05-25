import CommonService from "@/service/CommonService";
export default {
  name: "Authentication Mixin",
  methods: {
    async login(userName, password, htmlContainer) {
      const targetElement = document.querySelectorAll(`.${htmlContainer}`);
      console.log(targetElement);
      targetElement[0].style.opacity = 0.5
      //I'm mocking the results here. data should come from APIf
      this.setSpinner(true);
      const loginResponse = await CommonService.loginAuthentication(
        userName,
        password
      );
      this.setSpinner(false);
      if (loginResponse?.accessToken) {
        localStorage.setItem("BlogP-auth", JSON.stringify(loginResponse));
        this.$router.push("/BlogP/dashboard");
      } else {
        //Show Some pop-up for invalid user
      }
    },
    
    async register(registerUser, htmlContainer) {
      const targetElement = document.querySelectorAll(`.${htmlContainer}`);
      console.log(targetElement);
      targetElement[0].style.opacity = 0.5
      //I'm mocking the results here. data should come from APIf
      this.setSpinner(true);
      const registerResponse = await CommonService.registerUser(registerUser);
      
      console.log(registerResponse);
      this.setSpinner(false);
      if(registerResponse == "Success"){
        this.$router.push("/BlogP/login");
      }
    },
  },
};
