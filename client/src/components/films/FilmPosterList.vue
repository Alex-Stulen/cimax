<script setup>
import Paginator from '@/components/plugins/paginator/Paginator.vue';
import Loading from '../utils/Loading/Loading.vue';
</script>

<template>
    <div>
        <div class="container section__container p-5">
            <div class="row" v-if="getFilmsPageData.count < 1 && !loading">
                <div class="col">
                    <h2 class="text-center text-white">Здається список порожній :(</h2>
                </div>
            </div>
            <div class="row" v-else>
                <div class="d-flex w-100 justify-content-center" v-if="loading">
                    <Loading></Loading>
                </div>
                <div class="col-12" v-else v-for="film of getFilmsPageData.results">
                    <FilmPoster :film="film" :key="film.id"></FilmPoster>
                    <hr class="text-white" style="margin-top: 75px; margin-bottom: 75px;">
                </div>
                <div class="col-12" v-if="!loading">
                    <Paginator :rows="pageSize" :totalRecords="getFilmsPageData.count"></Paginator>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import FilmPoster from './FilmPoster.vue';
import { mapGetters, mapActions } from 'vuex';

import { defaultPageSize } from './config';

export default {
    name: 'FilmPosterList',
    components: {
        FilmPoster
    },
    data() {
        return {
            loading: true,
            filmsData: {},
            pageList: [],
            pageSize: defaultPageSize,
            totalRecords: 0
        }
    },
    computed: {
        ...mapGetters(['getFilmsPageData', 'getCurrentSearch'])
    },
    methods: {
        ...mapActions(['setFilmsPageDataApi']),

        async loadFilms(data) {
            this.loading = true
            try {
                const filmsData = await this.setFilmsPageDataApi(data)
                if(filmsData.status === 'fail'){
                    alert(filmsData.status, filmsData.code)
                }
                else{
                    this.filmsData = filmsData
                    this.pageList = this.filmsData.results,
                    this.totalRecords = this.filmsData.count
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
        const search = this.getCurrentSearch
        await this.loadFilms({page: 1, pageSize: this.pageSize, search: search})
    }
}
</script>
