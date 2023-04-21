<template>
  <form className="form-inline my-2 my-lg-0 mx-auto">
    <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"
           v-model="searchQuery">
    <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: ""
    };
  },
  methods: {
    onSubmit() {
      this.$emit("search", this.searchQuery);
    }
  }
};
</script>

<style scoped>
/* Importowanie stylów Bootstrapa */
@import "~bootstrap/dist/css/bootstrap.min.css";
</style>
