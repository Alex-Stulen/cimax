<script setup>
import FsLightbox from "fslightbox-vue/v3";
import VideoPlayer from "../plugins/videoPlayer/VideoPlayer.vue";
</script>

<template>
    <div class="row">
        <div class="col-sm-12 col-md-4">
            <img :src="film.poster" class="poster__image" alt="Poster Image"
                @click="showFsLightboxPoster = !showFsLightboxPoster">
            <FsLightbox type="image" :types="[null, null, 'image']" :toggler="showFsLightboxPoster"
                :sources="[film.poster]" />
        </div>
        <div class="col-sm-12 col-md-8 mt-4">
            <h2 class="text-white text-center">{{ film.name }} ({{ film.film_year }})</h2>
            <h5 class="text-white text-center" style="opacity: 0.75;"><i>{{ film.original_name }}</i></h5>
            <div class="row">
                <div class="col-12 d-flex justify-content-end">
                    <RouterLink :to="'/view/' + film.id">
                        <h4 class="text-secondary"><i class="fa-regular fa-circle-play"></i> Дивитися</h4>
                    </RouterLink>
                </div>
            </div>
            <hr class="text-white">
            <p class="text-white h4 mt-5">{{ film.description }}</p>
            <h5 class="text-white mt-5">Жанри:</h5>
            <p class="text-white" style="overflow-wrap: break-word;">{{ film_genres }}</p>
            <hr class="text-white">
            <h4 class="text-white mt-5">Трейлер:</h4>
            <div class="row">
                <div class="col-sm-12 col-md-8 col-lg-6">
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
        <div class="row mt-3">
            <div class="col-12 text-end">
                <p class="textcolor-light" style="padding-right: 2px;">Додано: {{ film.created_at }}</p>
                <RouterLink to="/abuse" class="button button-outline-dark" style="font-size: 12px; letter-spacing: 1.5px;">Для правовласника<i class="fa-solid fa-flag" style="font-size: 14px; color: rgba(255, 0, 0, 0.4); margin-left: 7px;"></i></RouterLink>
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
            showFsLightboxPoster: false,
        }
    },
    computed: {
        film_genres(){
            let categories = []
            this.film.categories.forEach(category => {
                categories.push(category.name)
            })
            return categories.join(' | ')
        }
    },
    components: {
        FsLightbox, VideoPlayer
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
</style>