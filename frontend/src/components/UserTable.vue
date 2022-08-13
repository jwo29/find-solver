<template>
    <div id="table-section">
        <table id="table-for-solver">
          <caption>Solver</caption>
            <th>BOJ ID</th>
            <tr v-for="item in items" :key="item.uid">
                <td v-if="item.solved.includes(problem_no)">{{ item.uid }}</td>
            </tr> 
        </table>

        <table id="table-for-unsolver">
            <caption>Unsolver</caption>
            <th>BOJ ID</th>
            <tr v-for="item in items" :key="item.uid">
                <td v-if="!item.solved.includes(problem_no)">{{ item.uid }}</td>
            </tr> 
        </table>
    </div>
</template>

<script>
import solved_db from "@/assets/solved-db.json";

export default {
  name: 'UserTable',
  props: {
    problem_no: String
  },
  data() {
    return {
        items: solved_db,
    }
  },
  
//   computed: {
//     solveds() {
//         return solved_db.map((items) => {
//             return items;
//         })
//     }
//   }

}
</script>


<style>

#table-for-solver {
  width: 35%;

  background-color: darkgray;

  /* float: left; */
  margin: auto;

}

#table-for-unsolver {
  width: 35%;

  background-color: darksalmon;

  /* float: left; */
  margin: auto;
}


</style>
