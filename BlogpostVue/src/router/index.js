import Vue from "vue";
import VueRouter from "vue-router";
import LoginScreen from "../components/LoginScreen";
import Register from "../components/Register";
import Dashboard from "../components/Dashboard";
import EditPost from "@/components/EditPost";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Login",
    component: LoginScreen,
  },
  {
    path: "/BlogP/login",
    name: "Login",
    component: LoginScreen,
  },
  {
    path: "/BlogP/Register",
    name: "Register",
    component: Register,
  },
  {
    path: "/BlogP/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/BlogP/dashboard/:subMenu",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/BlogP/dashboard/EditPost",
    name: "EditPost",
    component: EditPost,
    props: true
  },
];

const router = new VueRouter({
  routes,
});

export default router;
