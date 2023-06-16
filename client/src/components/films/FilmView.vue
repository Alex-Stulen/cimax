<script setup>
import FsLightbox from "fslightbox-vue/v3";
import VideoPlayer from "../plugins/videoPlayer/VideoPlayer.vue";

// Import Swiper styles
import "swiper/css";

import "swiper/css/effect-coverflow";
import 'swiper/css/navigation';

// import required modules
import { Swiper, SwiperSlide } from "swiper/vue";
import { EffectCoverflow, Navigation } from "swiper";
</script>

<template>
    <div class="row">
        <div class="col-sm-12 col-md-4">
            <img :src="film.poster" class="poster__image" alt="Poster Image"
                @click="openFilmImagesLightbox([film.poster], 1)">
            <FsLightbox :key="'Lightbox'" :ref="'Lightbox'" :slide="lightboxSlide" type="image" :types="[null, null, 'image']"
                :toggler="lightboxToggler" :sources="lightboxSources" />

            <div v-if="film.images.length > 0">
                <swiper :key="film.id" :effect="'coverflow'" :navigation="true" :grabCursor="true" :centeredSlides="true"
                    :slidesPerView="'auto'" :coverflowEffect="{
                        rotate: 50,
                        stretch: 0,
                        depth: 100,
                        modifier: 1,
                        slideShadows: false,
                    }" :pagination="true" :modules="filmImageSwiperModules">

                    <swiper-slide v-for="(file_image, index) in film.images" :key="index">
                        <img :src="file_image.image" alt="Film image" @click="openFilmImagesLightbox(film.images.map(image => image.image), index + 1)" />
                    </swiper-slide>
                </swiper>
            </div>

        </div>
        <div class="col-sm-12 col-md-8 mt-4">
            <h2 class="text-white text-center">{{ film.name }} ({{ film.film_year }})</h2>
            <h5 class="text-white text-center" style="opacity: 0.75;"><i>{{ film.original_name }}</i></h5>
            <hr class="text-white">
            <p class="text-white h4 mt-5">{{ film.description }}</p>
            <h5 class="text-white mt-5">Жанри:</h5>
            <p class="text-white" style="overflow-wrap: break-word;">{{ film_genres }}</p>
            <h4 class="text-white mt-5">Трейлер:</h4>
            <div class="row">
                <div class="col-sm-12 col-md-6 col-lg-4">
                    <div>
                        <VideoPlayer :key="film.id" :options="{
                            autoplay: false,
                            liveui: true,
                            userActions: {
                                hotkeys: true
                            },
                            controls: true,
                            fluid: true,
                            sources: [
                                { 'src': film.film_trailer },
                            ]
                        }"></VideoPlayer>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-sm-12 mt-5">
            <h4 class="text-white">Плеєр</h4>
            <div>
                <VideoPlayer :key="film.id" :options="{
                    autoplay: false,
                    liveui: true,
                    userActions: {
                        hotkeys: true
                    },
                    controls: true,
                    fluid: true,
                    sources: [
                        { src: film.film, type: 'video/mp4' },
                    ]
                }"></VideoPlayer>
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-12 text-end">
                <p class="textcolor-light" style="padding-right: 2px;">Додано: {{ film.created_at }}</p>
                <RouterLink to="/abuse" class="button button-outline-dark" style="font-size: 12px; letter-spacing: 1.5px;">
                    Для правовласника<i class="fa-solid fa-flag"
                        style="font-size: 14px; color: rgba(255, 0, 0, 0.4); margin-left: 7px;"></i></RouterLink>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'FilmPoster',
    props: {
        film: Object
    },
    data() {
        return {
            lightboxToggler: false,
            lightboxSources: [],
            lightboxSlide: 1,
            filmImageSwiperModules: [EffectCoverflow, Navigation],
        }
    },
    components: {
        FsLightbox, VideoPlayer, Swiper, SwiperSlide,
    },
    computed: {
        film_genres() {
            let categories = []
            this.film.categories.forEach(category => {
                categories.push(category.name)
            })
            return categories.join(' | ')
        }
    },
    methods: {
        openFilmImagesLightbox(sources, slide) {
            this.lightboxSources = sources
            this.lightboxToggler = !this.lightboxToggler;
            this.lightboxSlide = slide
        }
    }
}
</script>

<style scoped lang="scss">
.poster__image {
    max-width: 100%;
}

.poster__image:hover {
    cursor: pointer;
}

a {
    transition: 0.3s ease all;

    &:hover {
        transform: scale(1.1);
    }
}

.swiper {
    width: 100%;
    padding-top: 50px;
    padding-bottom: 50px;
}

.swiper-slide {
    background-position: center;
    background-size: cover;
    max-width: 250px;
    max-height: 250px;
}

.swiper-slide img {
    display: block;
    width: 100%;
}
</style>

<style lang="scss">
@import '../../assets/scss/colors.scss';

.swiper-button-prev,
.swiper-button-next {
    color: $light;
}
</style>