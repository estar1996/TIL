<template>
  <div>
    <h2 style="margin-bottom:30px">Review List</h2>
    <ul>
      <!-- review로 바꿨더니 됨 -->
        <MovieReviewDetail v-for="(review, idx) in reviews" :key="idx"
          :review="review"
          :movie="movie"
          @reviewDelete="deleteReview"
          @reviews-updated="updateRiview"
        />
       
    </ul>
  </div>
</template>

<script>
import MovieReviewDetail from '@/components/MovieReviewDetail'


export default {
  name: "ReviewList",
  components: {
    MovieReviewDetail,
    
  },
  props: {
    reviews: {
      type: [Array, Object],
    },
    movie: {
      type: Object,
    },
  },
  data: function () {
    return {

    }
  },
  methods: {
    deleteReview: function (review_id) {
      this.$emit('reviewDelete',review_id)
    },
    updateRiview: function () {
      this.$emit('reviews-updated')
    }
  },
}
</script>

<style>
</style>
