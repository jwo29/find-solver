<template>
  <div>
    <!-- 메인 화면 윗부분(변하지 않음) -->
    <div> 
      <h1>is solved..?</h1>
      <div>
        <input type="text" placeholder="문제번호">
        <button>검색</button>
      </div>
    </div>

    <!-- 검색 결과 부분 -->
    <div>
      테이블 위
      <user-table></user-table>
      테이블 아래
    </div>
  </div>
</template>

<script>
import UserTable from './UserTable.vue'

export default {
  components: { UserTable },
  name: 'HelloWorld',
  props: {
    msg: String
  }
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
