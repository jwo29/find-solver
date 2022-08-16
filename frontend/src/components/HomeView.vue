<template>
    <div id="home">
        <header-view></header-view>
        
        <search-view></search-view>

        <footer-view></footer-view>
  </div>
</template>

<script>
import HeaderView from './HeaderView.vue'
import SearchView from './SearchView.vue'
import FooterView from './FooterView.vue'

export default {
  components: { 
    HeaderView,
    SearchView,
    FooterView,
  },
  name: 'HomeView',
  
}
</script>