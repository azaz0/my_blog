<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="container">
      <router-link class="navbar-brand" to="/">Strona główna</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="#o-mnie">O mnie</a>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/rejestracja">Zarejestruj</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/logowanie">Zaloguj</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar-brand {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-link {
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .navbar-brand {
    font-size: 1.2rem;
  }

  .nav-link {
    font-size: 1rem;
  }
}
</style>
