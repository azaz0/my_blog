<template>
  <div>
    <Navbar/>
    <Header/>
    <div className="container">
      <SearchBox/>
    </div>
    <PostList :posts="posts"/>
    <Footer/>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Header from "@/components/Header.vue";
import SearchBox from "@/components/SearchBox.vue";
import PostList from "@/components/PostList.vue";
import Footer from "@/components/Footer.vue";
import {mapState, mapActions} from "vuex";

export default {
  name: "Home",
  components: {
    Navbar,
    Header,
    SearchBox,
    PostList,
    Footer,
  },
  computed: {
    ...mapState(["posts"]),
  },
  created() {
    this.fetchPosts();
  },
  methods: {
    ...mapActions(["fetchPosts"]),
  },
};
</script>
