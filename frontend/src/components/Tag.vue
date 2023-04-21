<template>
  <div class="tag-list">
    <span v-for="tag in tags" :key="tag.id" class="badge badge-secondary">{{ tag.name }}</span>
  </div>
</template>

<script>
export default {
  props: {
    tags: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
.tag-list {
  margin-top: 10px;
}
</style>
