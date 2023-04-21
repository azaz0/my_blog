<template>
  <div class="container">
    <h1 class="mt-5">Posty</h1>
    <div class="card-deck">
      <post-preview v-for="post in posts" :key="post.id" :post="post"/>
    </div>
  </div>
</template>

<script>
import PostPreview from '@/components/PostPreview.vue'

export default {
  components: {
    PostPreview
  },
  props: {
    posts: {
      type: Array,
      required: true
    }
  }
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
