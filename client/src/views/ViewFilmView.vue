<script setup>
import Header from '../components/layouts/Header.vue';
import Footer from '../components/layouts/Footer.vue';
import FilmView from '../components/films/FilmView.vue';
import Loading from '../components/utils/Loading/Loading.vue';
</script>

<template>
    <div class="container-fluid wrapper">
        <Header></Header>
        <main>
            <section class="section__film mt-5">
                <div class="d-flex w-100 justify-content-center" v-if="loading">
                    <Loading></Loading>
                </div>
                <div v-else class="container section__container p-5">
                    <FilmView :film="film"></FilmView>
                </div>
            </section>
        </main>
        <Footer></Footer>
    </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
    components: {
        Header, Footer, FilmView, Loading
    },
    data() {
        return {
            loading: true,
            film: Object
        }
    },
    methods: {
        ...mapActions(['getFilmByIdApi']),
        async loadFilm(id) {
            this.loading = true
            try {
                const filmResponse = await this.getFilmByIdApi(id)
                if (filmResponse.status === 'fail') {
                    alert(filmResponse.status, filmResponse.code)
                }
                else {
                    this.film = filmResponse
                }
            }
            catch (error) {
                console.log(error)
            }
            finally {
                this.loading = false
            }
        }
    },
    async mounted() {
        await this.loadFilm(this.$route.params.filmId)
    }
}
</script>
