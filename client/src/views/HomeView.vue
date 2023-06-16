<script setup>
import Header from '../components/layouts/Header.vue';
import Footer from '../components/layouts/Footer.vue';
import FilmPosterList from '../components/films/FilmPosterList.vue';
</script>

<template>
  <div class="container-fluid wrapper">
    <Header></Header>
    <main>
      <section class="section__films mt-5 mb-5">
        <FilmPosterList></FilmPosterList>
      </section>
    </main>
    <Footer></Footer>
  </div>
</template>

<script>

export default {
  components: {
    Header, Footer, FilmPosterList
  }
}
</script>
