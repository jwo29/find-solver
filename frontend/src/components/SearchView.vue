<template>
  <div id="search-section">
    <input id="search-input" v-model="pno" type="text" placeholder="문제번호">
    <p>{{ pno }}를 푼 사람은 00명입니다</p>
    <main-view :pno="pno"></main-view>
  </div>
</template>

<script>
import axios from 'axios';
import MainView from './MainView.vue'

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

export default {
  name: 'SearchView',
  components: {
    MainView,
  },
  el: "#search-input",
  data() {
    return {
      pno: "",
    }
  },
}
</script>


<style>
#search-section {
  background-color: burlywood;
}
</style>
