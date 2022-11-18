<template>
  <div>
    <CreateReview 
      @reviews-updated="reviewsUpdated"
      :movie="movie"
      style="margin-bottom:30px"
    />
    <hr>
    <ReviewList 
      :reviews="reviews"
      :movie="movie"
     
      @reviewDelete="deleteReview"
      @reviews-updated="reviewsUpdated"
    />
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList'
import CreateReview from '@/components/CreateReview'
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'Review',
  components: {
    CreateReview,
    ReviewList,
  },
  props: {
    movie: {
      type: Object,
    }
  },
  data: function () {
    return {
      reviews: [],
    }
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
    getReviews: function () {
      const config = this.getToken()
      axios.get(`${SERVER_URL}/movies/${this.movie.id}/reviews/`, config)
      .then((res) => {
        this.reviews = res.data
      })
      // .catch((err) => {
      //   //console.log(err)
      // })
    },
    deleteReview: function (review_id) {

      const config = this.getToken()
      // console.log(config)
      axios.delete(`${SERVER_URL}/movies/review/${review_id}/`, config)
        .then((res) => {
          // console.log(res.data.id)
          // 리뷰 리스트 중에 삭제할 인덱스값을 넣어서 삭제해주기
          const targetReviewId = this.reviews.findIndex((rv)=>{
            return rv.id === res.data.id

          })
          this.reviews.splice(targetReviewId, 1)
        })

    },
    reviewsUpdated: function () {
      this.getReviews()
    },
  },
  // created에서 watch로 바꿨더니 데이터가 바뀔 때마다 바로 바뀐다.
  // watch: function () { 
  //   this.getReviews()
  // },
  created: function () { 
    this.getReviews()
  },
}
</script>

<style>
</style>