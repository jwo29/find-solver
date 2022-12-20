<template>
    <div id="board">
        <table>
        <caption class="table-caption">SOLVER: {{searchResult.solver_num}}</caption>
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
    searchResult: {
        type: Object,
        default: () => {
            return {
                solvers: [],
                solver_num: 0,
                result: 0
            }
        }
    }
  }
}
</script>