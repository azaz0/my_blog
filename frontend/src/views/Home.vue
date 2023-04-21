<template>
  <div>
    <Navbar/>
    <Header/>
    <div class="container">
      <SearchBox/>
    </div>
    <PostList :posts="posts"/>
    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Header from '@/components/Header.vue';
import SearchBox from '@/components/SearchBox.vue';
import PostList from '@/components/PostList.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'Home',
  components: {
    Navbar,
    Header,
    SearchBox,
    PostList,
    Footer,
  },
  data() {
    return {
      posts: [],
    };
  },
  beforeRouteEnter(to, from, next) {
    next((vm) => {
      vm.posts = to.params.posts;
    });
  },
};
</script>

<style>
/* Importowanie stylów Bootstrapa */
@import "~bootstrap/dist/css/bootstrap.min.css";

/* Dodawanie stylów dla komponentu PostList */
.container {
  max-width: 800px;
  margin: 0 auto;
}
</style>
