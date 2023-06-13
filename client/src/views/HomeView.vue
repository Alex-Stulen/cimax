<script setup>
import Header from '../components/layouts/Header.vue';
import FilmPosterList from '../components/films/FilmPosterList.vue';
</script>

<template>
  <main class="container-fluid wrapper">
      <Header></Header>
      <section class="section__films mt-5">
        <FilmPosterList></FilmPosterList>
      </section>
  </main>
</template>

<script>

export default {
  components: {
    Header, FilmPosterList
  }
}
</script>
