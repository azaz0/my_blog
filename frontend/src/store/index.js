import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    posts: [],
  },
  mutations: {
    SET_POSTS(state, posts) {
      state.posts = posts;
    },
  },
  actions: {
    fetchPosts({ commit }) {
      axios
        .get('/posts/')
        .then(response => {
          commit('SET_POSTS', response.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  getters: {
    posts: state => state.posts,
  },
});

export default store;
