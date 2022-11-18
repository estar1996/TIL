<template>
  <div id="app">
    <h2>{{ user.username }}님의 마이페이지</h2>
    <hr>
    <h2>{{ user.username }}님이 좋아요한 영화</h2>
    <vue-glide v-if="my_like_movies.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for = "(movie, idx) in my_like_movies"
        :key="idx">
        
        <MovieCard2
          :movie="movie"
        />
      </vue-glide-slide>
    </vue-glide>

    <h2>{{ user.username }}님이 싫어요한 영화</h2>
    <vue-glide v-if="my_dislike_movies.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for = "(movie, idx) in my_dislike_movies"
        :key="idx">
        
        <MovieCard2
          :movie="movie"
        />
      </vue-glide-slide>
    </vue-glide>


    <h2>{{ user.username }}님이 보고싶어요한 영화</h2>
    <vue-glide v-if="my_wish_movies.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for = "(movie, idx) in my_wish_movies"
        :key="idx">
        
        <MovieCard2
          :movie="movie"
        />
      </vue-glide-slide>
    </vue-glide>


    <div class="card" style="border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.3);">
    <h2>{{ user.username }}님이 커뮤니티에 작성한 글 제목 <i class="fab fa-readme" style="color:tomato"></i></h2>
    <h2 v-for="(community, idx) in communitys" :key="idx">
    <h2  v-if="user.username === community.userName" style="color:white">{{ community.title }}</h2>
    </h2>
    </div>
    <br>

  
    <div class="card" style="border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.3);">
    <h2>영화에 남긴 나의 한마디 <i class="fas fa-head-side-cough" style="color:hotpink"></i></h2>
    <h2 v-for="(review, idx) in reviews" :key="idx">
      [{{ review.movie_title }}] -
      {{ review.content }}
    </h2>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieCard2 from "@/components/MovieCard2"
import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MyProfile",
  data: function () {
    return { 
      like_movies: [],
      dislike_movies: [],
      wishing_movies: [],
      my_like_movies: [],
      my_dislike_movies: [],
      my_wish_movies: [],
      reviews: [],
      communitys: [],
      comments: [],
      user: '',
    }
  },
  components: {
    MovieCard2,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
   methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },

     getMyName: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data
        this.like_movies = res.data.like_movies
        this.dislike_movies = res.data.dislike_movies
        this.wishing_movies = res.data.wish_movies
        
        axios.get(`${SERVER_URL}/movies/review/${this.user.id}`, config)
        
        .then( (res) => {
          // console.log(res.data.content)
          this.reviews = res.data
          
        
        })
      })
      // .catch( (err) => {
      //   //console.log(err)
      // })
    },
    getMovieDatas: function () {
      axios.get(`${SERVER_URL}/movies/`)
      .then( (res) => {
        for(var i = 0; i < this.like_movies.length; i++){
          this.my_like_movies.push(res.data[this.like_movies[i]-1])
        }
        for(var j = 0; j<this.dislike_movies.length; j++){
          this.my_dislike_movies.push(res.data[this.dislike_movies[j]-1])
        }
        for(var k = 0; k<this.wishing_movies.length; k++){
          this.my_wish_movies.push(res.data[this.wishing_movies[k]-1])
        }

      })
      // .catch( (err) => {
      //   //console.log(err)
      // })
    },
     getCommunity: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      
      .then( (res) => {
        this.user = res.data
        
        axios.get(`${SERVER_URL}/community/`, config)
        
        .then( (res) => {
          
          this.communitys = res.data
          
        
        })
      })
      // .catch( (err) => {
      //   //(err)
      // })
    },
     
   },
  created: function () {
    this.getMyName()
    this.getMovieDatas()
    this.getCommunity()
   
  },
  
}
</script>

<style>

</style>