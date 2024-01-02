<template>
<div class="menu-bar">
      <ul>
            <li><a href="#">首页</a></li>
            <li><a href="#">项目简介</a></li>
            <li>
                <a href="#">项目内容 <i class="fas fa-caret-down"></i></a>
                <div class="dropdown-menu">
                    <ul>
                        <li><a href="#" @click="showImage('/image/1')&hideBottomContainer">同工位间隔时间</a></li>
                        <li><a href="#" @click="showTwoImages('/image/2','/image/2_2')">生产贴数</a></li>
                        <li>
                            <a href="#">药材用量 <i class="fas fa-caret-right"></i></a>
                            <div class="dropdown-menu-1">
                                <ul>
                                    <li><a href="#"  @click="showTwoImages('/image/3','/image/3_3')">茯苓</a></li>
                                    <li><a href="#" @click="showTwoImages('/image/4','/image/4_4')">丹参</a></li>
                                    <li><a href="#" @click="showTwoImages('/image/5','/image/5_5')">柴胡</a></li>
                                    <li><a href="#" @click="showTwoImages('/image/9','/image/9_9')">白术</a></li>
                                    <li><a href="#" @click="showTwoImages('/image/6','/image/6_6')">桂枝</a></li>
                                </ul>
                            </div>
                        </li>
                        <li><a href="#" @click="showImage('/image/7')&hideBottomContainer">加水量检测</a></li>
                        <li><a href="#" @click="showImage('/image/8')&hideBottomContainer">煎煮时间</a></li>
                    </ul>
                </div>
            </li>
            <li><a href="#">项目人员</a></li>
            <li><a href="#" >合作交流</a></li>
        </ul>
    </div>
  <div class="image-container">
    <div class="top-image-container">
      <img :src="topImage" v-if="topImage" alt="Image" class="top-image">
    </div>
    <div class="bottom-image-container">
    <img :src="bottomImage" v-if="bottomImage" alt="Image" class="bottom-image">
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
export default {
  name: 'App',
  data() {
    return {
      topImage: '',
      bottomImage: '',
      bottomContainerHidden: true,
    }
  },
  methods: {
    showImage(image) {
      this.topImage = "http://127.0.0.1:8010"+image;
      this.bottomContainerHidden = true;//隐藏bottom
    },
    showTwoImages(image1, image2) {
      this.topImage= "http://127.0.0.1:8010"+image1;
      this.bottomImage = "http://127.0.0.1:8010"+image2;
      this.bottomContainerHidden = false;//显示bottom


    },
    hideBottomContainer() {
      this.bottomContainerHidden = true;//隐藏bottom
  },
}
}

// This starter template is using Vue 3 experimental <script setup> SFCs
// Check out https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md
</script>

<style>
#app {
  margin-top: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;


}
.image-container {
  display: flex;
  flex-direction: column;
  height: 100vh; /* 设置容器高度为视口高度 */
}
/*你在这里改容器的大小，看多大顺眼*/
.top-image-container{
 flex: 1; /* 占据剩余空间，使容器位于上方 */
}
.bottom-image-container {
flex: 1; /* 占据剩余空间，使容器位于上方 */
}

.top-image{
  max-width: 100%; /* 图片最大宽度为容器宽度 */
  height: auto;
}
.bottom-image {
  max-width: 100%; /* 图片最大宽度为容器宽度 */
  height: auto; /* 根据宽度等比例调整高度 */
}

</style>
