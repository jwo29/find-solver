<template>
    <div>
        <div id="menu">
            <button class="menu-button" v-on:click="updateMember" :title="memberLastUpdateTime">Update Member</button>
            <button class="menu-button" v-on:click="updateProblem" :title="problemLastUpdateTime">Update Solved Problems</button>
        </div>
        <div id="main">
            <h1 id="main-title"><a class="link-tag" href="/">IS IT SOLVED?</a></h1>
            <div class="search-section">
                <input type="text" @change="input" @keyup.enter="searchSolver" placeholder="BOJ 문제 번호를 입력하세요">
                <!-- <button v-on:click="searchSolver">검색</button> -->
                <img class="search-icon" src="../assets/search.png" v-on:click="searchSolver">
            </div>
            <p class="main-desc">
                상명대학교 SCV 멤버들의 원활한 동아리 활동을 위해 만든 사이트입니다
                <br/>검색하고자 하는 문제의 번호를 검색하면,
                <br/>그룹 SCV 내에서 해당 문제를 푼 사람의 목록을 보여줍니다
            </p>
        </div>
        <div id="side">
            <BoardView :searchResult="searchResult" :problemNo="problemNo"></BoardView>
        </div>
    </div>
</template>

<script>
import BoardView from './BoardView.vue'
import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000';

export default {
  name: 'MainView',
  components: {
    BoardView,
  },
  data() {
    return {
        'problemNo': '',
        'searchResult': {},
        'memberLastUpdateTime': '',
        'problemLastUpdateTime': ''
    }
  },
  methods: {
    input(e) {
        return this.problemNo = e.target.value
    },
    searchSolver: function() {
        axios.get('/problems/' + this.problemNo).then(res => {

            this.searchResult = res.data

        })
    },
    updateMember: function() {
        axios.post('/members/').then(res => {

            this.memberLastUpdateTime = "마지막 업데이트 시간: \n" + res.data.last_update_time
            console.log(this.memberLastUpdateTime)


        })
    },
    updateProblem: function() {
        axios.post('/problems').then(res => {

            this.problemLastUpdateTime = "마지막 업데이트 시간: \n" + res.data.last_update_time
            console.log(this.problemLastUpdateTime)

        })
    }
  },
  mounted() {
    axios.get('lastUpdateTime').then(res => {
            this.memberLastUpdateTime = "마지막 업데이트 시간: \n" + res.data.member_last_udt
            this.problemLastUpdateTime = "마지막 업데이트 시간: \n" + res.data.problem_last_udt
        })
  }
}

</script>