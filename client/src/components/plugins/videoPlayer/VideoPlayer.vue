<template>
  <div>
    <video ref="videoPlayer" class="video-js"></video>
  </div>
</template>

<script>
import videojs from 'video.js';

export default {
  name: 'VideoPlayer',
  props: {
    options: {
      type: Object,
      default() {
        return {};
      }
    }
  },
  data() {
    return {
      player: null
    }
  },
  methods: {
    initPlayer(options) {
      if (this.player) {
        this.player.dispose();
      }

      if (this.$refs.videoPlayer) {
        this.player = videojs(this.$refs.videoPlayer, options);
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initPlayer(this.options);
    });
  },
  updated() {
    this.$nextTick(() => {
      if (!this.player && this.$refs.videoPlayer) {
      this.initPlayer(this.options);
    }
    });
  },
  beforeDestroy() {
    if (this.player) {
      this.player.dispose();
    }
  }
}
</script>
