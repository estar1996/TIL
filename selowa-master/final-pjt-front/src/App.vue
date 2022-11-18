<template>
  <div id="app">
    <br>
    <img src="@/assets/logo1.png" alt="logo" style="width: 300px">
    <div class='column'>

  <div class='search'>
    <div class='search_bar'>
      <input id='searchOne' type='checkbox'>
      <label for='searchOne'  @click="cleanKeyword">
       <!-- 닫힐 때 키워드 초기화해주기 -->
        <i class="fas fa-search font-weight-bolder " ></i>
        <p>| X</p>

      </label>
      <input @keypress.enter="onInputSearch(keyword)" @input="submitAutoComplete" placeholder='영화제목 입력 후 enter!' type='text' v-model="keyword" autofocus >
    </div>
 
<div v-if="keyword" class="autocomplete disabled card m-1" style="width:300px; border: 2px solid rgb(76, 56, 192); background-color: black">
  <div 
    @click="searchSkillAdd(i)"
       style="cursor: pointer"
       v-for="(res,i) in result"
       :key="i"
       >{{ result[i] }}

  </div>
  </div>
</div>

  </div>
    
    <!-- <Menu style="position:fixed; top:0; z-index:3;"></Menu> -->
    <div id="nav" class="card m-4" style="border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.726);">
      
      <span v-if="login">
        <!-- <router-link :to="{ name: 'Home' }" >Home</router-link> | -->
        <router-link :to="{ name: 'Home' }" class="fas fa-home font-weight-bolder " style="text-decoration:none"> Home</router-link> |
        <router-link :to="{ name: 'Movie' }" class="fas fa-film font-weight-bolder " style="text-decoration:none"> Movie</router-link> |
        <router-link :to="{ name: 'Recommend' }" class="fas fa-video font-weight-bolder " style="text-decoration:none"> Recommended Movie</router-link> |
        <router-link :to="{ name: 'Community' }" class="fas fa-comment font-weight-bolder " style="text-decoration:none"> Community</router-link> | 
        <span v-if="login"><router-link :to="{ name: 'MyProfile' }" class="fas fa-id-card-alt font-weight-bolder " style="text-decoration:none"> MyProfile</router-link></span> |
        <router-link @click.native="logout" to="#" class="fas fa-sign-out-alt font-weight-bolder " style="text-decoration:none"> LOGOUT</router-link> 
        <!-- 로그아웃하면 클릭시 로그인화면으로 보내기 -->
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }" class="fas fa-user-plus font-weight-bolder " style="text-decoration:none"> Signup</router-link> |
        <router-link :to="{ name: 'Login' }" class="fas fa-sign-in-alt font-weight-bolder " style="text-decoration:none">Login</router-link> 
      </span>

      
    </div>
    <router-view @login="login = true"/>

    

    <Slide id="page-wrap">
    <!-- 로그인했을 때 -->
    <span v-if="login"><router-link :to="{ name: 'Home' }" class="fas fa-home font-weight-bolder " style="color:#e0435e;text-decoration:none"> Home</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Movie' }" class="fas fa-film font-weight-bolder " style="color:#e0435e;text-decoration:none"> Movie</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Recommend' }" class="fas fa-video font-weight-bolder " style="color:#e0435e;text-decoration:none"> Recommended Movie</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Community' }" class="fas fa-comment font-weight-bolder " style="color:#e0435e;text-decoration:none"> Community</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'MyProfile' }" class="fas fa-id-card-alt font-weight-bolder " style="color:#e0435e; text-decoration:none"> MyProfile</router-link></span>
    <span v-if="login"><router-link @click.native="logout" to="#" class="fas fa-sign-out-alt font-weight-bolder " style="color:#e0435e;text-decoration:none"> Logout</router-link></span>
   <!-- 로그인 안했을 때 -->
    <span v-if="!login"><router-link :to="{ name: 'Signup' }" class="fas fa-user-plus font-weight-bolder " style="color:#e0435e; text-decoration:none"> Signup</router-link></span>
    <span v-if="!login"><router-link :to="{ name: 'Login' }" class="fas fa-sign-in-alt font-weight-bolder " style="color:#e0435e; text-decoration:none"> Login</router-link></span>
    
    
  </Slide>
  


  </div>

</template>

<script>
import { Slide } from 'vue-burger-menu'
import skills from "@/skills.js";
export default {
  name: 'App',
  components: {
    Slide,
  },
  props: {
    login_info: Boolean
  },
  data: function () {
    return {
      login: false, //flag
      keyword : '',
      articleObj: null,
    isResult: false,
    searchQuery: '',
    
      result: '',
    }
  },
  methods: {
    searchSkillAdd(i){
      this.keyword =this.result[i]

    },
    cleanKeyword(){
      this.keyword = ''

    },
    submitAutoComplete() {
      if (this.keyword) {
        
        this.result = skills.filter((skill) => {
          return skill.match(new RegExp("^" + this.keyword, "i"))
          // 해당 글자로 시작하는 키워드를 뽑아내기 위해 ^ 를 사용하고, 대소문자 구분 없이 찾아내기 위해 i 옵션을 사용한다.
         
        })
      } 
    },
    onInputSearch: function (keyword) {
    //  console.log(keyword)
     this.$router.push({name: 'SearchBar', query: {keyword: keyword}})
      this.keyword = ''
      
    },
    
    logout: function() {
      // console.log('logout 됨')
      // 로그아웃 처리
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },



    
  },
  created: function () {
    //1. vue instance가 생성된 직후에 jwt를 가져오는 함수 실행하기
    const token = localStorage.getItem('jwt')
    // 2. 토큰이 있따면..
    if (token) {
      this.login = true
    }
  },
}
</script>


<style>
#app {
  font-family:'Raleway','Sunflower', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  
}


#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: white;
}

#nav a.router-link-exact-active {
  color: #e0435e;
}

#nc-main {
    position: relative;
    height: 100vh;
    overflow-x: hidden;
    -webkit-box-shadow: 0 0 30px #241d20;
    box-shadow: 0 0 30px #241d20;
    -webkit-transition: -webkit-transform 0.4s;
    transition: -webkit-transform 0.4s;
    transition: transform 0.4s;
    transition: transform 0.4s, -webkit-transform 0.4s;
}

.column {
  /* background: #F6F792; */
  height: 90px;
  float: left;
  width: 100%;
  position: relative;
  z-index:100000;
}
.search {
  position: absolute;
  left: 0;
  right: 0;
  margin: auto;
  top: 60%;
  transform: translateY(-50%);
  width: 100%;
  text-align: center;
  overflow: hidden;
}
.search_bar {
  width: 580px;
  position: relative;
  margin: 0 auto;
}
.search_bar input[type=text] {
  width: 15px;
  background: transparent;
  transition: border 0.3s 0s, width 0.2s 0.3s cubic-bezier(0.225, 0.01, 0.475, 1.01), text-indent 0.2s 0.3s;
  padding: 20px;
  border-color: #441ee9;
  text-indent: 30px;
  outline: none;
  border: 0px solid #441ee9;
  font-size: 15px;
  color: #ac88e7;
  border-radius: 5px;
  font-family: "Nunito", sans-serif;
}
.search_bar ::-webkit-input-placeholder {
  /* Safari, Chrome and Opera */
  color: #ac88e7;
  font-weight: 400;
  font-family: "Nunito", sans-serif;
}
.search_bar ::-moz-input-placeholder {
  /* Safari, Chrome and Opera */
  color: #441ee9;
  font-weight: 400;
  font-family: "Nunito", sans-serif;
}
.search_bar ::-o-input-placeholder {
  /* Safari, Chrome and Opera */
  color: #441ee9;
  font-weight: 400;
  font-family: "Nunito", sans-serif;
}
.search_bar input[type=checkbox] {
  display: none;
}
.search_bar input[type=checkbox]:checked + label + input {
  width: 530px;
  border: 5px solid #441ee9;
  text-indent: 0px;
}
.search_bar input[type=checkbox]:checked + label i {
  right: 0px;
  transform: translateY(-50%) translateX(50%) rotate(360deg) scale(0);
  color: #441ee9;
}
.search_bar input[type=checkbox]:checked + label .last {
  left: 220px;
  transform: translateY(-50%) rotate(360deg) scale(1);
}
.search_bar input[type=checkbox]:checked + label p {
  top: 50%;
  transition: all 0.3s 0.45s;
}
.search_bar input[type=checkbox]:not(checked) + label p {
  top: -50%;
  transition: all 0.3s 0s;
}
.search_bar .last {
  transform: translateY(-50%) rotate(0deg) scale(0);
}
.search_bar i {
  position: absolute;
  font-size: 30px;
  top: 50%;
  transform: translateY(-50%) translateX(50%) rotate(0deg) scale(1);
  cursor: pointer;
  z-index: 2;
  margin: auto;
  border-radius: 4px;
  width: 56px;
  right: 50%;
  height: 54px;
  background: transparent;
  transition: right 0.3s 0.3s, transform 0.3s 0.3s, color 0.3s;
  line-height: 60px;
  color: #b12273;
}
.search_bar i:hover {
  color: #441ee9;
}
.search_bar p {
  position: absolute;
  margin: 0;
  right: 52px;
  color: #b12273;
  font-weight: 700;
  font-size: 30px;
  top: -50%;
  transform: translateY(-50%) rotate(0deg) scale(1);
}
.autocomplete{
  position: relative;
  left:42%;

}



</style>
