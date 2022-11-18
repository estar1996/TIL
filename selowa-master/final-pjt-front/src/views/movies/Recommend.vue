<template>
  <div id="app">
    <h2 style="margin-bottom:60px">SELOWA 알고리즘이 {{user.username}}님에게 추천하는 영화 페이지</h2>
    <!-- 자료가 없으면 스피너생김 -->
    <div v-if="movies.length === 0" class="spinner-border" role="status">
    <span class="visually-hidden">Loading...</span>
    
    </div>
    
    <h3 class="content-font">랜덤 영화 추천</h3>
    
    <vue-glide v-if="movies.length"
      class="glide__track m-4"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1100: {perView: 4}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for = "(movie, idx) in movies"
        :key="idx">
        
        <MovieCard2
          :movie="movie"
        />
        
      </vue-glide-slide>
    </vue-glide>

    <h3 class="content-font" v-if="my_users_like_movies.length === 0"> 
      {{ user.username }} 님이 좋아하는 영화추천(취향이 일치하는 분이 없어요..) 
      <hr>
    </h3>

    <h3 class="content-font" v-if="my_users_like_movies.length > 0"> 
      {{ user.username }}님이 좋아하는 영화추천</h3>
    <vue-glide v-if="my_users_like_movies.length"
      class="glide__track m-4"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for = "(movie, idx) in my_users_like_movies"
        :key="idx">
        <MovieCard2
          :movie="movie"
        />
        
      </vue-glide-slide>
    </vue-glide>

    <!-- <h3 class="content-font" v-if="age_movies.length > 0">{{user.username}}님과 같은 나이대가 좋아하는 영화 추천</h3>
    <vue-glide v-if="age_movies.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: age_movies.length}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for = "(movie, idx) in age_movies"
        :key="idx">
        
        <MovieCard
          :movie="movie"
        />
        
      </vue-glide-slide>
    </vue-glide> -->




    <h3 class="content-font" v-if="favorite_movies.length === 10">높은 평점을 받은 영화</h3>
    <vue-glide v-if="favorite_movies.length"
      class="glide__track m-4"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 6}, 1100: {perView: 4}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for = "(movie, idx) in favorite_movies"
        :key="idx">
        
        <MovieCard2
          :movie="movie"
        />
        
      </vue-glide-slide>
    </vue-glide>





  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieCard2 from "@/components/MovieCard2"
import VueJwtDecode from "vue-jwt-decode"


const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: "Recommend",
  data: function () {
    return {
      movies: [],
      movie: '',
      favorite_movies: [],
      age_movies: [],
      users_movies: [],
      my_like_users_movies: [],
      user: '',
      my_users_like_movies: [],
      genre: [],
      swiperOption: { 
        slidesPerView: 1, spaceBetween: 30, loop: true, pagination: { 
          el: '.swiper-pagination', clickable: true 
          }, 
        navigation: { 
          nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' 
          } } }
    },
  
  components: {
    MovieCard2,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
    // Swiper,
    // SwiperSlide,
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
    getMovieDatas: function () {
      axios.get(`${SERVER_URL}/movies/`)
      .then( (res) => {
        //랜덤추천 
        const randomIdx = _.random(res.data.length-1)
        this.movie = res.data[randomIdx]
        const numbers = _.range(1, res.data.length);
        const sampleNums = _.sampleSize(numbers, 30);
        
        for (const key in sampleNums) {
          this.movies.push(res.data[sampleNums[key]])
          // console.log(this.movies)
        }
      })
      // .catch( (err) => {
      //   //console.log(err)
      // })
    },
    
    getRecommend: function () {
      const config = this.getToken()
      const item = {
        movies: this.user.like_movies,
      }
      // 내가 좋아하는 영화를 좋아하는 사람 찾기
      axios.post(`${SERVER_URL}/movies/${this.user.id}/like/users/`,item , config)
      .then( (res) => {
        const item = {
          users: res.data,
        }
        // 그 사람들이 좋아하는 영화 찾기
        axios.post(`${SERVER_URL}/accounts/info/`, item, config)
        .then( (res) => {
          this.my_like_users_movies = res.data[0]
          this.age_movies = res.data[1]
          // 추천 받기
          const item2 = {
            like_movies: this.my_like_users_movies,
            me_like: this.user.like_movies,
            me_age : this.age_movies
          }
          axios.post(`${SERVER_URL}/movies/recommend/`, item2, config)
          .then( (res) => {
            this.favorite_movies = res.data[0]
            this.my_users_like_movies = res.data[1]
            this.age_movies = res.data[2]
          })
          // .catch( (err) => {
          //   //console.log(err)
          // })
        })
        // .catch( (err) => {
        //  // console.log(err)
        // })
      })
      // .catch( (err) => {
      //   //console.log(err)
      // })
     },
    getMyName: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data
        this.getRecommend()
      })
      // .catch( (err) => {
      //   //console.log(err)
      // })
    },    
  },
  created: function () {
    this.getMovieDatas()
    this.getMyName()
   
  },
}
</script>

<style>

  
</style>