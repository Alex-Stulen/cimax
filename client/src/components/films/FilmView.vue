<script setup>
import FsLightbox from "fslightbox-vue/v3";
import VideoPlayer from "../plugins/videoPlayer/VideoPlayer.vue";
</script>

<template>
    <div class="row">
        <div class="col-sm-12 col-md-4">
            <img :src="film.poster" class="poster__image" alt="Poster Image"
                @click="showFsLightboxPoster = !showFsLightboxPoster">
            <FsLightbox :toggler="showFsLightboxPoster" :sources="[film.poster]" />
        </div>
        <div class="col-sm-12 col-md-8 mt-4">
            <h2 class="text-white text-center">{{ film.name }} ({{ film.film_year }})</h2>
            <h5 class="text-white text-center" style="opacity: 0.75;"><i>{{ film.original_name }}</i></h5>
            <hr class="text-white">
            <p class="text-white h4 mt-5">{{ film.description }}</p>
            <h5 class="text-white mt-5">Жанри:</h5>
            <ul>
                <li v-for="category of film.categories">
                    <h6 class="text-white"><em>{{ category.name }}</em></h6>
                </li>
            </ul>
        </div>
        <div class="col-sm-12 mt-5">
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