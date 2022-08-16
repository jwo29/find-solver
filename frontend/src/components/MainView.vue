<template>
    <div id="main-section">
        <table id="table-for-solver">
            <th>Solver</th>
            <tr v-for="item in items" :key="item.id">
              <td v-if="item.solved.includes(pno)">{{ item.id }}</td>
            </tr> 
        </table>
    </div>
</template>

<script>
import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

export default {
  name: 'MainView',
  props: {
    pno: String
  },
  data() {
    return {
        items: [],
    }
  },
  methods: {
    getSolver: function () {
        axios.get("solver")
            .then((res) => {
                this.items = res.data
            })
    }
  },
  beforeMount() {
    this.getSolver()
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#main-section {
  background-color: tomato;
}
/* h3 {
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
} */
</style>