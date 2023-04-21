<template>
  <div class="card mb-3">
    <div class="card-body">
      <h5 class="card-title">{{ post.title }}</h5>
      <p class="card-text">{{ post.content }}</p>
      <p class="card-text"><small class="text-muted">{{ post.date_posted }}</small></p>
      <router-link :to="'/posts/' + post.id" class="btn btn-primary">Czytaj więcej</router-link>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    post: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
.card {
  border: 1px solid rgba(0, 0, 0, .125);
  border-radius: .25rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, .15);
}
</style>
