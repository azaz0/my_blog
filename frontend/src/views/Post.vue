<template>
  <div>
    <Navbar/>
    <div class="container my-4">
      <div class="card">
        <div class="card-header">
          {{ post.title }}
        </div>
        <div class="card-body">
          <p class="card-text">{{ post.body }}</p>
        </div>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import {mapState} from 'vuex';

export default {
  name: 'PostView',
  components: {
    Navbar,
    Footer,
  },
  async created() {
    await this.$store.dispatch('fetchPosts');
  },
  computed: {
    ...mapState(['posts']),
    post() {
      const postId = parseInt(this.$route.params.id);
      const post = this.posts.find(post => post.id === postId);
      if (!post) {
        return null; // lub inny stan ładowania
      }
      return post;
    },
  },
};
</script>


<style>
.card {
  max-width: 600px;
  margin: 0 auto;
}
</style>
