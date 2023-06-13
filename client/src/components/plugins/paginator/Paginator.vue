<script setup>
import Paginator from 'primevue/paginator';
</script>

<template>
    <div>
        <Paginator :rows="rows" :totalRecords="totalRecords" @page="page" :pt="{
            pageButton: ({ props, state, context }) => ({
                class: context.active ? 'bg-primary' : undefined
            })
        }" :template="{
    '640px': 'PrevPageLink CurrentPageReport NextPageLink',
    '960px': 'FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink',
    '1300px': 'FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink',
    default: 'FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink'
}" />
    </div>
</template>

<script>

import { mapGetters, mapActions } from 'vuex';

export default {
    name: 'Paginator',
    props: {
        rows: Number,
        totalRecords: Number,
    },
    data(){
        return {
            currentPage: 1,
            pageRows: this.rows
        }
    },
    components: {
        Paginator
    },
    computed: {
        ...mapGetters(['getCurrentSearch', 'getFilmsPageData']),
    },
    emits: ['page', 'update:records'],
    methods: {
        ...mapActions(['setFilmsPageDataApi']),
        async page(event) {
            this.currentPage = event.page + 1
            this.$emit('page', this.currentPage);
            if(this.currentPage !== this.getFilmsPageData.currentPage){
                await this.updateRecords()
            }
        },
        async updateRecords(){
            await this.setFilmsPageDataApi({
                page: this.currentPage,
                search: this.getCurrentSearch
            })
        }
    }
}
</script>

<style scoped lang="scss">
@import '../../../assets/scss/colors.scss';

:deep(.p-paginator) {
    background: rgba($color: $dark, $alpha: .1) !important;
    border: none !important;
    box-shadow: 0px 0px 40px 0px rgba($color: white, $alpha: .03);
}

/* Change the color of the active page */
:deep(.p-paginator .p-paginator-page.p-highlight) {
    background-color: white !important;
    /* Change this to your desired color */
}

/* Change the color of the page numbers */
:deep(.p-paginator .p-paginator-page) {
    color: $dark;
    /* Change this to your desired color */
}
</style>
