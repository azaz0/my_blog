<template>
  <div>
      <router-view />
      <div v-if="$route.matched.length === 0">
        <p>Nie znaleziono strony.</p>
      </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'App',
  created() {
    this.$router.push({ name: 'home' });
  },
};
</script>

<style>
/* style */
</style>
