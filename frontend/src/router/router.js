import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Post from '../views/Post.vue';
import store from '../store/index.js';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/posts/:id',
      name: 'post',
      component: Post,
      props: true,
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (from.path === '/') {
    next();
  } else {
    store.dispatch('fetchPosts').then(() => next());
  }
});

export default router;
