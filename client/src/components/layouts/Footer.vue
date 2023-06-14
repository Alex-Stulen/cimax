<template>
    <div class="d-flex flex-column align-items-center p-4">
        <div class="text-white h5 mt-2 text-center">Email: <span class="email">cimax.space.contact@gmail.com</span></div>
    </div>
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

.email{
    color:bisque;
}
</style>