<template>
    <div id="board">
        <table v-if="searchResult.solvers != null">
        <caption class="table-caption">Solver list for <b>{{problemNo}}</b>: {{searchResult.solver_num}}</caption>
          <thead>
            <tr>
              <th>No.</th>
              <th>BOJ ID</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(solver, idx) in searchResult.solvers" :key=solver>
              <td>{{ idx+1 }}</td>
              <td>{{ solver }}</td>
            </tr>
          </tbody>
        </table>
    </div>
</template>

<script>
export default {
  name: 'BoardView',
  props: {
    problemNo: {
        type: String
    },
    searchResult: {
        type: Object,
        default: () => {
            return {
                solvers: null,
                solver_num: 0,
                result: 0
            }
        }
    }
  }
}
</script>