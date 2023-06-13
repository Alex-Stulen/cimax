<script setup>
import Search from '../films/Search.vue';
</script>

<template>
    <nav class="container-fluid d-flex justify-content-center">
        <div class="row w-100">
            <div class="col-sm-12 col-md-6 col-lg-3 d-flex justify-content-center align-items-center">
                <RouterLink class="navbar-brand" to="/">
                    <img src="@/assets/images/logo.png" alt="Logo Image" class="logo">
                </RouterLink>
            </div>
            <div class="col-sm-12 col-md-6 col-lg-5 d-flex justify-content-center align-items-center">
                <h1 class="text-white text-center">Cimax - твій онлайн кінотеатр</h1>
            </div>
            <div class="col-sm-12 col-lg-4 d-flex justify-content-end align-items-center">
                <Search></Search>
            </div>
        </div>
    </nav>
</template>

<script>

export default {
    name: 'Header',
    components: {
        Search
    },
    data() {
        return {
            search: ''
        }
    }
}
</script>

<style scoped lang="scss">
@import '../../assets/scss/colors.scss';


nav{
    background-color: rgba($color: $dark, $alpha: .4);
}

.logo {
    margin: 20px;
    padding: 0;
    max-width: 156px;
    border-radius: 20px;
    box-shadow: 0px 0px 40px rgba($color: #fff, $alpha: .04);
}
</style>
