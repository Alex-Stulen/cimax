<template>
    <div class="d-flex flex-column justify-content-center align-items-center section__403">
        <h1 class="text-white text-center error__header">404</h1>
        <h2 class="text-white text-center error__desc">Oopss..! Не вдалося знайти сторінку!</h2>
        <RouterLink to="/">Повернутися на головну</RouterLink>
    </div>
</template>

<script>
export default {
    name: '404'
}
</script>

<style scoped lang="scss">

a{
    color:bisque;
}

.error__header {
    font-size: 5rem;
}

.section__403 {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
}

</style>