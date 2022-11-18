<template>
<div class="col" >

<!-- <button class="btn btn-sm btn-dark m-4" type="submit"> -->
  <div class="card m-2 bg-dark" style="width: 21rem;">
      
      <img :src="movieImage" alt="poster_path" style="width:320px" class="m-2" >
       
        <MovieDetail2 :movie="movie"/>
        <br>
       
        
  </div>
<!-- </button> -->
</div>
</template>

<script>
import MovieDetail2 from '@/components/MovieDetail2'

export default {
    name:'MovieCard2',
    components: {
        MovieDetail2,
    },
    props: {
        movie:{
            type: Object,
        }
    },
    computed:{
       movieImage: function () {
          //  if(this.movie.poster_path!=null)
           return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
           //https://image.tmdb.org/t/p/w500/를 붙여서 리턴
       },

    },
    methods:{
    movieDetail: function () {
        // 여기서 각 무비 id에 해당하는 object데이터를 디테일로 넘겨줘야할듯?.?
        // console.log(this.movie)
    },


    
    
  }

}
</script>

<style scoped>
/* 영화 하나 커서 올렸을 때 확대 됨 */
.card:hover {
     transform: scale(1.05);
     z-index: 2000;
  box-shadow: 0 10px 20px rgba(238, 234, 236, 0.698), 0 4px 8px rgba(0,0,0,.06);
}

</style>