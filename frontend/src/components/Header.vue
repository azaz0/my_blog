<template>
  <div class="jumbotron jumbotron-fluid bg-primary text-white">
    <div class="container">
      <h1 class="display-4">{{ blogTitle }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  props: {
    blogTitle: {
      type: String,
      default: "My Blog"
    }
  }
};
</script>

<style scoped>
.jumbotron {
  margin-bottom: 0;
}
</style>
