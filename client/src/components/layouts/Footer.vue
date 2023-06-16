<template>
    <footer class="container-fluid mt-3">
        <div class="row pt-5">
            <div class="col-4 text-center">
                <a href="#header" class="textcolor-light h5">Пошук</a>
            </div>
            <div class="col-4 text-center">
                <RouterLink to="/abuse" class="textcolor-light h5">Для правовласників</RouterLink>
            </div>
            <div class="col-4 text-center">
                <div>
                    <h5 class="textcolor-light">Контакти</h5>
                    <span class="textcolor-light">Email: <a href="mailto:cimax.space.contact@gmail.com"
                            target="_blank" style="color: bisque;">cimax.space.contact@gmail.com</a></span>

                </div>
            </div>
        </div>
        <hr class="textcolor-light">
        <div class="row mt-5">
            <div class="col-12">
                <h6 class="text-center textcolor-light">{{ currentYear }} © Copyright: Cimax</h6>
            </div>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'Footer',
    computed: {
        currentYear() {
            return new Date().getFullYear()
        }
    }
}
</script>

<style scoped lang="scss">
@import '../../assets/scss/colors.scss';

footer {
    background-color: rgba($color: #000, $alpha: .4);
}

.email {
    color: bisque;
}
</style>