<template>
    <div id="footer-section">
        <p><button @click="updateMember">멤버 업데이트</button></p>
        <p><button @click="updateProblem">푼 문제 업데이트</button></p>
    </div>
</template>

<script>
import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

export default {
    name: 'FooterView',
    data() {
        return {
            member_last_updated: "",
            problem_last_updated:"",
        }
    },
    // 테스트 성공!
    // api 연결은 다음에!
    methods: {
        updateMember: function () {
            axios.post('member')
                .then((res) => {
                    this.solveds = res.data
                    // 서버로부터의 응답의 정보는 아래와 같다. 참고하기
                    // res.data
                    // res.status
                    // res.statusText
                    // res.headers
                    // res.config
                })
                .catch(err => console.log(err))
        },
        updateProblem: function () {
            axios.post('problem')
                .then((res) => {
                    this.uid = res.data.id
                })
                .catch(err => console.log(err))
        }
    },
}
</script>

<style>
#footer-section {
    background-color: darkgreen;
}
</style>