<template>
  <div class="home ms-5">
   
    <!-- 자료가 없으면 스피너생김 -->
    <div v-if="movies.length === 0"   class="spinner-border" role="status">
    <span class="visually-hidden">Loading...</span>
    </div>

    <div class="row row-cols-1 row-cols-md-4 ms-5 ">
      <!-- 그리드 카드 형태로  -->
      <MovieCard v-for="(movie,idx) in movies" :key="idx" :movie="movie" />

      <MovieDetail />
    </div>


    <!-- <v-pagination :total="10" v-model="currentPage"></v-pagination> -->

    
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import MovieDetail from '@/components/MovieDetail'
import axios from 'axios'


const SERVER_URL = process.env.VUE_APP_SERVER_URL
// @ is an alias to /src

export default {
  name: 'Movie',
  
  data: function(){
    return{
      movies: [],
      inputText:'',
      

    }
  },
  components: {
    MovieCard,
    MovieDetail,
  
  },
  methods:{
  
    onClickBtn: function (){
      axios.get(`${SERVER_URL}/movies/`)
      .then((res) => {
        this.movies = res.data
      })
      // .catch((err) => {
      //   //console.log(err)
      // })
    

    },

  },
  created() {
    this.onClickBtn()
  },
  
  

}
</script>
<style>

</style>
