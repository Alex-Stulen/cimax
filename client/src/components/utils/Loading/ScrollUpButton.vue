<template>
    <div class="scrollUpButton" @click.prevent="upToTop"></div>
  </template>
  
  <script>
  export default {
    name: 'ScrollUpButton',
    methods: {
      upToTop() {
        document.querySelector('#header').scrollIntoView({
          behavior: 'smooth',
        });
      },
    },
  };
  </script>

<style scoped lang="scss">
@import '../../../assets/scss/colors.scss';

.scrollUpButton {
    position: fixed;
    display: inline-block;
    text-align: center;
    right: 50px;
    bottom: 50px;
    width: 50px;
    height: 50px;
    background-color: #333;
    border-radius: 4px;
    transition: 0.3s ease all;

    &::after {
        content: "\f077";
        font-family: FontAwesome;
        font-weight: normal;
        font-style: normal;
        font-size: 2em;
        line-height: 50px;
        color: #fff;
    }

    &:hover {
        cursor: pointer;
        background-color: #666;
    }
}
</style>