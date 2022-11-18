<template>
  <div class="d-flex text-align:center  m-1">
    <div>
    <p class="st-font" style="margin-left: 1em; top:88%"  >좋아요 {{ numLike }}개</p>
    <vue-star animate="animated bounceIn" color="#F05654" style="top:84%">
      <i v-if="isLiking" @click="like" slot="icon" style="color:crimson" class="fa fa-heart"></i>
      <i v-else @click="like" slot="icon" style="color:white" class="fa fa-heart"></i>
    </vue-star>
    </div>

    <div>
    <p class="st-font" style="margin-left: 1em;">싫어요 {{ numDisLike }}개</p>
    <vue-star animate="animated bounceIn" style="top:84%">
      <i v-if="isDisLiking" @click="dislike" slot="icon" style="color:skyblue" class="fas fa-thumbs-down"></i>
      <i v-else @click="dislike" slot="icon" class="fas fa-thumbs-down"></i>
    </vue-star>
    </div>

    <div>
    <p class="st-font" style="margin-left: 1em;">보고싶어요 {{ numWish }}개</p>
    <vue-star animate="animated bounceIn"  style="top:84%">
      <i v-if="isWishing" @click="wish" slot="icon" style="color:yellow" class="far fa-grin-stars"></i>
      <i v-else @click="wish" slot="icon" class="far fa-grin-stars"></i>
    </vue-star>
    </div>

   <div>
    <button @click="handleClickButton" class ="btn btn-outline-danger" style="width: 60%;">더보기</button>
    </div>
    <app-modal title="More Info" :visible.sync="visible">
      <div>
        <h2 style="font-weight: bold;">{{ movie.title }} </h2>
        <hr>
        <div class="video-container">
          <iframe :src="src" frameborder="0" allow="fullscreen"></iframe>
        </div>
        <div class="movie-information-wrapper mt-4 d-flex align-items-center">
        <br>
       
    
        <div class="col">
          
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 28">장르 : 액션 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 12">장르 : 어드벤쳐 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 16">장르 : 애니메이션 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 35">장르 : 코미디 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 80">장르 : 범죄 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 99">장르 : 다큐멘터리 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 18">장르 : 드라마 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 10751">장르 : 가족 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 14">장르 : 판타지 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 36">장르 : 역사 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 27">장르 : 호러 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 10402">장르 : 음악 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 9648">장르 : 미스터리 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 10749">장르 : 로맨스 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 878">장르 : 공상과학 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 10770">장르 : TV Movie </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 53">장르 : 스릴러 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 10752">장르 : 전쟁 </h5>
        <h5 style="margin-bottom:10px" class="content-font" v-if="movie.genres[0] === 37">장르 : 서부 영화 </h5>
        
        <h5 style="margin-bottom:10px" class="content-font">평점 : {{ movie.vote_average }}점</h5>
        <h5 style="margin-bottom:10px" class="content-font">상영 시간 : {{ movie.runtime }}분</h5>
        <h5 style="margin-bottom:10px" class="content-font">개봉 일자 : {{ movie.release_date }}</h5>
        <h5 class="m-3">{{ movie.overview }}</h5>
        </div>
        </div>
        <hr>
        </div>
        
        <MovieReview 
          :movie="movie"
        />
      
    </app-modal>
  </div>
</template>

<script>
import Modal from './Modal'
import VueStar from 'vue-star'
import MovieReview from '@/components/MovieReview'
import _ from 'lodash'
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"



const SERVER_URL = process.env.VUE_APP_SERVER_URL
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'MovieDetail2',
  data: function () {
    return {
      visible: false,
      me: [],
      liking: '',
      numLike: '',

      disliking: '',
      numDisLike: '',

      wishing: '',
      numWish: '',

      src: '',
      videoId: '',
      rating: Number(this.movie.vote_average),

    }
  },
  props: {
        movie:{
            type: Object,
        },
  },
  components: {
    appModal: Modal,
    MovieReview,
    VueStar,

  },
  methods: {
    handleClickButton(){
      this.visible = !this.visible
      this.fetchVideo()
    },
    ratingToInt: function () {
      this.rating = Math.ceil(this.rating / 2)
    },
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
        this.me = res.data
        if (this.me.like_movies.includes(this.movie.id)) {
          this.liking = true
        } else {
          this.liking = false
        }
        if (this.me.dislike_movies.includes(this.movie.id)) {
          this.disliking = true
        } else {
          this.disliking = false
        }
         if (this.me.wish_movies.includes(this.movie.id)) {
          this.wishing = true
        } else {
          this.wishing = false
        }
      })
      // .catch( (err) => {
      //   //(err)
      // })
    },
    like: function () {
      const config = this.getToken()
      const item = {
        myId: this.me.id,
        movieId: this.movie.id,
      }
      axios.post(`${SERVER_URL}/movies/${this.me.id}/${this.movie.title}/like/`, item, config)
      .then( () => {
        this.getMyName()
        this.likecheck()
        // console.log(res)
      })
    },
    dislike: function () {
      const config = this.getToken()
      const item = {
        myId: this.me.id,
        movieId: this.movie.id,
      }
      axios.post(`${SERVER_URL}/movies/${this.me.id}/${this.movie.title}/dislike/`, item, config)
      .then( () => {
        this.getMyName()
        this.dislikecheck()
        // console.log(res)
      })
    },
    wish: function () {
      const config = this.getToken()
      const item = {
        myId: this.me.id,
        movieId: this.movie.id,
      }
      axios.post(`${SERVER_URL}/movies/${this.me.id}/${this.movie.title}/wish/`, item, config)
      .then( () => {
        this.getMyName()
        this.wishcheck()
        // console.log(res)
      })
    },
    likenumber: function () {
      this.numLike = this.movie.like_users.length
    },
    dislikenumber: function () {
      this.numDisLike = this.movie.dislike_users.length
    },
    wishnumber: function () {
      this.numWish = this.movie.wish_users.length
    },
    likecheck: function () {
      if (this.liking) {
        this.numLike -= 1
      } else {
        this.numLike += 1
      }
    },
    dislikecheck: function () {
      if (this.disliking) {
        this.numDisLike -= 1
      } else {
        this.numDisLike += 1
      }
    },
    wishcheck: function () {
      if (this.wishing) {
        this.numWish -= 1
      } else {
        this.numWish += 1
      }
    },
    fetchVideo() {
     const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.movie.title + '예고편'
      }
      axios.get(API_URL, {
        params, 
      })
      .then((res) => {
        this.videoId = res.data.items[0].id.videoId
        //console.log(this.videoId)
        // console.log(`https://www.youtube.com/embed/${this.videoId}?autoplay=1&mute=1`)
        
        this.src = `https://www.youtube.com/embed/${this.videoId}?autoplay=1&mute=1`
        // console.log(res.data.items)
        // this.src = 
        // console.log(this.src)
        // 선택 된 비디오가 없다면
        // if (!this.selectedVideo) {
        //   this.selectedVideo = this.videos[0]
        // }
      })
      // .catch((err) => {
      //   console.log(err)
      // })
  },

  },
  computed: {
    isLiking: function () {
      return this.liking
    },
    isDisLiking: function () {
      return this.disliking
    },
    isWishing: function () {
      return this.wishing
    },
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  },
  created: function () {
    this.getMyName()
    this.likenumber()
    this.dislikenumber()
    this.wishnumber()
    this.ratingToInt()
  }

}
</script>


<style>
.video-container > iframe {
  /* position: relative;   container를 기준으로 위치를 지정 */
  /* top: 0;               container의 가장 위쪽으로 위치를 지정 */
  /* left: 0; */
  width: 600px;
  height: 400px;
}
          
</style>
