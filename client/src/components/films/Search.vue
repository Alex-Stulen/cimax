<template>
    <form @submit.prevent="submit" class="d-flex w-100" role="search">
        <input v-model="search" class="form-control me-2" type="search" placeholder="Пошук..." aria-label="Пошук...">
        <button class="btn btn-outline-secondary" type="submit">Пошук</button>
    </form>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'

export default {
    name: 'Search',
    data() {
        return {
            search: ''
        }
    },
    computed: {
        ...mapGetters(['getFilmsPageData', 'getCurrentSearch']),
    },
    methods: {
        ...mapActions(['setFilmsPageDataApi']),
        ...mapMutations(['setSearch']),
        async submit(event) {
            this.$router.push({path: '/'})
            this.setSearch(this.search)
            await this.setFilmsPageDataApi({
                search: this.search
            })
        }
    },
    mounted(){
        this.search = this.getCurrentSearch
    }
}
</script>