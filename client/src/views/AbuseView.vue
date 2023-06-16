<script setup>
import Header from '../components/layouts/Header.vue';
import Footer from '../components/layouts/Footer.vue';
</script>

<template>
    <div class="container-fluid wrapper">
        <Header></Header>
        <main>
            <section class="section__abuse mt-5">
                <div class="container section__container">
                    <div class="section__item">
                        <h2 class="text-white h1">Для правовласників</h2>
                    </div>
                    <div class="section__item mt-3">
                        <p class="text-white h4">Якщо ви маєте ексклюзивні права на будь-які матеріали, посилання з цим
                            сайтом, і не бажаєте, щоб ця інформація поширювалася без вашої згоди, ми з радістю допоможемо
                            вам і видалимо відповідні посилання з сайту.</p>
                    </div>
                    <div class="section__item mt-3">
                        <h4 class="text-white section__item__header">Для цього потрібно надіслати електронний лист з
                            наступною інформацією:</h4>
                        <p class="text-white h5 mt-3">- Документ, що підтверджує наявність виключних прав на матеріал,
                            розміщений на сайті: це може бути відсканована копія з печаткою або контактною інформацією, що
                            дозволяє ідентифікуватися як власник виключних прав на відповідні матеріали.</p>
                        <p class="text-white h5 mt-3">- Прямі посилання на сторінки ресурсу, з якого повинна бути видалена
                            інформація. Посилання повинні бути такого типу https://cimax.space/view/3 або схожі.</p>
                    </div>
                    <div class="section__item mt-3">
                        <h4 class="text-white section__item__header">Ви отримаєте відповідь протягом декількох годин або не
                            пізніше 3 робочих днів після відправки листа.</h4>
                    </div>
                    <div class="section__item mt-3">
                        <p class="text-white h5">Також хочемо нагадати, що платформа Cimax не виробляє нелегальний контент,
                            всі матеріали беруться з вільного відкритого коду. Сайт cimax.space - не зберігає незаконні
                            копії творів.</p>
                    </div>
                    <div class="section__item mt-3">
                        <h4 class="text-white section__item__header">Використовуйте наступні контакти:</h4>
                        <p class="text-white h5"><i class="fa-regular fa-envelope"></i> Email: <a
                                href="mailto:cimax.space.contact@gmail.com" target="_blank"
                                style="color: bisque;">cimax.space.contact@gmail.com</a></p>
                    </div>
                </div>
            </section>
        </main>
        <Footer></Footer>
    </div>
</template>

<script>
export default {
    name: 'AbuseView',
    components: {
        Header, Footer
    }
}
</script>

<style scoped lang="scss">
.section__item {
    padding: 10px;

    &__header {
        font-weight: 600;
        text-decoration: underline;
    }
}
</style>
