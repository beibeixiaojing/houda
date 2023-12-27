<template>
  <div class="image-container">
    <div class="left-image-container">
      <img :src="getImageUrl()" alt="Image" class="left-image">
    </div>
    <div class="right-image-container">
    <img :src="getImageUrl2()" alt="Image" class="right-image">
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
export default {
  name: 'App',
  components: {
    HelloWorld
  },
  methods:{
    getImageUrl() {
      const hostname='http://127.0.0.1:8010'
      const path='/image'
      return `${hostname}${path}`
    },
    getImageUrl2() {
      const hostname='http://127.0.0.1:8010'
      const path='/image2'
       return `${hostname}${path}`
    }
  }
}
// This starter template is using Vue 3 experimental <script setup> SFCs
// Check out https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.image-container {
  display: flex;
}

.left-image-container{
  width: 50%;
  float: left;
  height: 433px; /* 设置一个固定的高度 */
  overflow-y: auto; /* 当内容溢出时显示垂直滚动条 */
}
.right-image-container {
  width: 50%; /* 将容器分为左右两部分，每部分宽度为50% */
  height: 100%;
}

.left-image{
  max-width: 100%; /* 图片最大宽度为容器宽度 */
  height: auto;
}
.right-image {
  max-width: 100%; /* 图片最大宽度为容器宽度 */
  height: auto; /* 根据宽度等比例调整高度 */
}

</style>
