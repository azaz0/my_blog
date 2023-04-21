<template>
  <div class="container py-5">
    <div class="row">
      <div class="col-md-8">
        <h2 class="mb-4">{{ post.title }}</h2>
        <p class="text-muted">{{ post.created_at }}</p>
        <div v-html="post.content"></div>
      </div>
      <div class="col-md-4">
        <h4 class="mb-4">Kategorie</h4>
        <ul class="list-unstyled">
          <li v-for="category in post.categories" :key="category.id">
            <router-link :to="'/categories/' + category.id">{{ category.name }}</router-link>
          </li>
        </ul>
        <h4 class="mb-4">Tagi</h4>
        <ul class="list-unstyled">
          <li v-for="tag in post.tags" :key="tag.id">
            <router-link :to="'/tags/' + tag.id">{{ tag.name }}</router-link>
          </li>
        </ul>
        <h4 class="mb-4">Autor</h4>
        <router-link :to="'/authors/' + post.author.id">{{ post.author.name }}</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['post']
};
</script>

<style scoped>
/* style */
</style>
