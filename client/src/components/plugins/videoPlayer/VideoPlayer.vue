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
      player: null,
      spaceTo: 'pause',
      defaultOptions: {
        autoplay: false,
        userActions: {
          hotkeys: true
        },
        controlBar: {
          skipButtons: {
            forward: 5,
            backward: 5,
          }
        },
        playbackRates: [0.5, 1, 1.5, 2],
        controls: true,
        fluid: true,
        responsive: true
      }
    }
  },
  methods: {
    getOptions() {
      return { ...this.options, ...this.defaultOptions }
    },
    initPlayer(options) {
      if (this.player) {
        this.player.dispose();
      }

      if (this.$refs.videoPlayer) {
        this.player = videojs(this.$refs.videoPlayer, options);
      }
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.initPlayer(this.getOptions());
    });
  },
  updated() {
    this.$nextTick(() => {
      if (!this.player && this.$refs.videoPlayer) {
        this.initPlayer(this.getOptions());
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
