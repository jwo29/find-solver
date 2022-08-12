<template>
  <div id="main-wrapper">
    <!-- 검색 부분 -->
    <div id="search-section">
      <input id="search-input" v-model="problem_no" type="text" placeholder="문제번호">
      <p>Check {{ problem_no }} is solved in SCV</p>
    </div>
    
    <!-- 검색 결과 부분 -->
    <div id="result-section">
      <user-table :problem_no="problem_no"></user-table>
    </div>
  </div>
</template>

<script>
import UserTable from './UserTable.vue'

export default {
  components: { UserTable },
  name: 'HelloWorld',
  el: "#search-input",
  data() {
    return {
      problem_no: "",
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
