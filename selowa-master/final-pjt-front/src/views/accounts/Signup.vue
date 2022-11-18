<template>
  <div class="row d-flex justify-content-center align-items-center h-150" >
      <div class="card text-white bg-dark m-3 p-5 row d-flex justify-content-center align-items-center" style="width: 40%; ">
        <img src="../../assets/clapperboard.png" style="width: 40%;" class="card-img-top" alt="logo">
   
    <!-- <img alt="selowa" src="../../assets/selowa.png" width="300"> -->
    <!-- <img alt="selowa" src="@/assets/selowa.png" width="200"> -->
    <!-- 윈도우는 백슬레시 사용 유닉스(리눅스,맥os의 조상)는 슬레시 -->
    <h1 style="color:#e0435e;">Signup</h1>
    <br>
    <div>
    <div>
      <label for="username" style="color:#e0435e;">아이디: </label>
      <input type="text" id="username" v-model="credentials.username">

    </div>
    <div>
       <br>
      <label for="username" style="color:#e0435e;">나이: </label>
      <input type="text" id="username" v-model="credentials.age">
    </div>
      <br>
      <label for="password" style="color:#e0435e;">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <br>
      <label for="passwordConfirmation" style="color:#e0435e;">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation"
      @keypress.enter="signup(credentials)">
    </div>

    <br/>
    <button @click="signup(credentials)" class ="btn btn-outline-danger">회원가입</button>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        age:'',
      }
    }
  },
  methods: {
    signup: function () {
      // console.log(credentials)
      // 회원 가입 시켜주세요 -> Django (jwt)
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
      .then(() => {
        // console.log(res)
        this.$router.push({ name: 'Login'})
      })
      .catch(() => {
        //console.log(err)
        alert('회원가입 실패!')
      })
    }
  }
}
</script>