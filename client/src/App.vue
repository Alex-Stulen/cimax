<script setup>
import { RouterView } from 'vue-router'
import ScrollUpButton from './components/utils/Loading/ScrollUpButton.vue';
</script>

<template>
  <RouterView />
  <scrollUpButton />
</template>

<script>
export default {
  name: 'App',
  components: {
    ScrollUpButton
  }
}
</script>
