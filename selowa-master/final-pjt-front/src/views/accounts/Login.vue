<template>
    <div class="row d-flex justify-content-center align-items-center h-150" >
      <div class="card text-white bg-dark m-3 p-5 row d-flex justify-content-center align-items-center" style="width: 40%; ">
        <img src="../../assets/clapperboard.png" style="width: 40%;" class="card-img-top" alt="logo">
   
    <h1 style="color:#e0435e;">Login</h1>
    <div>
      <br>
      <label for="username" style="color:#e0435e;">아이디: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <br>
      <label for="password" style="color:#e0435e;">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password"
      @keypress.enter="login(credentials)">
    </div>
    <div>
      <hr>
      <!-- <p style="color:#e0435e;">소셜 로그인</p>
      <img @click="kakao_login()" src="../../assets/kakao.png" class="rounded mx-auto d-block" style="width:10%" alt="kakao">
      <hr> -->
      <p style="color:#e0435e;">회원이 아니라면?</p>
      <router-link :to="{ name: 'Signup' }" style="color:#e0435e;">회원가입</router-link>

    </div>
    <br>
    <button @click="login(credentials)" class ="btn btn-outline-danger">로그인</button>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
      .then((res) => {
        // console.log(res.data.token)
        // localstorage에 jwt 토큰 저장
        localStorage.setItem('jwt', res.data.token)
        // App 컴포넌트한테 로그인 됐습니다를 알려야 함.
        this.$emit('login') // 데이터는 안 담아서 보내도됨 (이벤트(신호)만 알리면 됨)
        this.$router.push({ name: 'Home' })
      })
      .catch((err) => {
        console.log(err)
        alert('회원정보가 존재하지 않습니다! 회원가입 해주세요.')
      })
    },
    // kakao_login: function () {
    //   axios.post(`${SERVER_URL}accounts/api-token-auth/`)
    //   .then((res) => {
    //     console.log(res.data.token)
    //     // localstorage에 jwt 토큰 저장
    //     localStorage.setItem('jwt', res.data.token)
    //     // App 컴포넌트한테 로그인 됐습니다를 알려야 함.
    //     this.$emit('login') // 데이터는 안 담아서 보내도됨 (이벤트(신호)만 알리면 됨)
    //     this.$router.push({ name: 'Home' })
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // }

  }
}
</script>