<template>
  <div>
    <header>
      <!-- Nagłówek -->
    </header>
    <main>
      <router-view></router-view>
    </main>
    <footer>
      <!-- Stopka -->
    </footer>
    <div v-if="$route.matched.length === 0">
      <!-- Komunikat o błędzie -->
      <p>Nie znaleziono strony.</p>
    </div>
  </div>
</template>

<script>
export default {
  created() {
    this.$router.push({name: 'home'})
  }
}
</script>

<style>
/* style */
</style>
