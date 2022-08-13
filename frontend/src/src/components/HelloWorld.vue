<template>
  <div>
    <!-- 메인 화면 윗부분(변하지 않음) -->
    <div> 
      <h1>is solved..?</h1>
      <div>
        <input id="search-input" v-model="pno" type="text" placeholder="문제번호">
        <p>현재 입력 문제번호: {{ pno }}</p>
      </div>
    </div>

    <!-- 검색 결과 부분 -->
    <div>
      테이블 위
      <user-table :pno="pno"></user-table>
      테이블 아래
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
      pno: "",
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
