<template>
    <!-- 표 그리기 -->
    <div>
        <table id="my-table">
            <th>BOJ ID</th>
            <tr v-for="item in items" :key="item.uid">
                <td v-if="item.solved.includes(pno)">{{ item.uid }}</td>
                <!-- <td>{{ item.solved }}</td> -->
            </tr> 
            <!-- <tr> -->
                <!-- <td>{{ pno }}</td> -->
                <!-- <td>{{ item.solved }}</td> -->
            <!-- </tr> -->
        </table>
    </div>
</template>

<script>
import solved_db from "@/assets/solved_db.json";

export default {
  name: 'UserTable',
  props: {
    pno: String
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

</style>
