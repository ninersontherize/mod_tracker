import Vue from 'vue';
import VueRouter from 'vue-router';
import Mods from '../components/Mods.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Mods',
    component: Mods,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: () => import(/* webpackChunkName: "about" */ '../views/Ping.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
