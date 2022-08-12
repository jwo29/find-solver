<template>
  <div>
    <header-view></header-view>
    <hello-world></hello-world>
    <!-- 푸터 -->
  </div>
</template>

<script>
import HeaderView from './components/HeaderView.vue'
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HeaderView,
    HelloWorld,
  }
}
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
</style>
