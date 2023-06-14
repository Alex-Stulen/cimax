<script setup>
import Header from '../components/layouts/Header.vue';
import Footer from '../components/layouts/Footer.vue';
import FilmPosterList from '../components/films/FilmPosterList.vue';
</script>

<template>
  <main class="container-fluid wrapper">
      <Header></Header>
      <section class="section__films mt-5">
        <FilmPosterList></FilmPosterList>
      </section>
      <div class="container">
        <Footer></Footer>
      </div>
  </main>
</template>

<script>

export default {
  components: {
    Header, Footer, FilmPosterList
  }
}
</script>
