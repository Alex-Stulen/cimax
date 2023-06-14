<template>
    <div class="d-flex flex-column justify-content-center align-items-center section__403">
        <h1 class="text-white text-center error__header">403</h1>
        <h2 class="text-white text-center error__desc">Доступ заборонено! Перевірте наявність доступу!</h2>
        <h5 class="text-white text-center error__desc">або зв'яжіться з нами через Email: <a href="mailto:cimax.space.contact@gmail.com" target="_blank">cimax.space.contact@gmail.com</a></h5>
    </div>
</template>

<script>
export default {
    name: '403'
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