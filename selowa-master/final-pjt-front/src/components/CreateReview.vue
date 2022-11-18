<template>
  <div class="container">
    <h2>Reviews</h2>
    <div class="row">
      <div class="col-lg-8 mx-auto">
          <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
        <div class="control-group">
            <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                <label>한줄 평:</label>
                <input v-model.trim="content" class="form-control" id="content" type="text" placeholder="reviewContent" required="required" data-validation-required-message="Please enter your review title." />
                <p class="help-block text-danger"></p>
            </div>
        </div>
      <!-- <div class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                <label>영화 제목: {{ movie.title }}</label>
                <p class="help-block text-danger"></p>
            </div> -->
        </div>
    

      <!-- <label style="margin-right: 15px" class="content-font" for="rank">내가 생각하는 영화 평점</label> -->
      <div class="select-wrapper" style="margin-right: 15px; margin-bottom:15px">            
        <!-- <select name="rate" id="rate" v-model="myMovieRate" class="content-font">
          <option style="color: black;" class="content-font" :value="rate" v-for="(rate, idx) in this.$store.state.reviewRate" :key="idx">{{ rate }}</option>
        </select> -->
        <!-- <h4 id="reviews">Reviews</h4> -->
          <span>영화 평점: </span>
          <select v-model="myMovieRate" id="myMovieRate" @change="changeIdx">
            <option>5</option>
            <option>4</option>
            <option>3</option>
            <option>2</option>
            <option>1</option>
          </select>
      </div>

      <!-- <div class="control-group">
          <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
              <label>리뷰 내용</label>
              <textarea v-model.trim="content" class="form-control" id="content" rows="5" placeholder="Content" required="required" data-validation-required-message="Please enter a content."></textarea>
              <p class="help-block text-danger"></p>
          </div>
      </div> -->
        <!-- <br /> -->
         </div>
        <div id="success"></div>
        <div class="st-font form-group">
          <button @click="createReview" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">작성 !</button>
        </div>  
                     
    </div>
  
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: "CreateReview",
  props: {
    movie: {
      type: Object
    },
  },
  data: function () {
    return {
      title: '',
      content: '',
      myMovieRate: '',
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
    createReview: function () {
      const config = this.getToken()
      const reviewItem = {
        // title: this.title,
        content: this.content,
        rank: this.myMovieRate,
        movie: this.movie.id,
      }
      if (reviewItem.content) {
        axios.post(`${SERVER_URL}/movies/${this.movie.id}/reviews/`, reviewItem, config)
          .then(() => {
            //console.log(res)
            this.$emit('reviews-updated')
            // this.title = ""
            this.content = ""
            this.rank = 0
            this.MyMovieRate= ''
          })
          // .catch((err) => {
          //   //console.log(err)
          // })
      }
      else{
        alert("내용을 입력해주세요!")
      } 
    },
    changeIdx: function (e){
      this.myMovieRate = e.target.value
    }
  },
  created: function () {
  },
}
</script>

<style>
/* #reviewTitle {
  color: white;
  border: 2px solid white;
} */
#reviewRate {
  color: black;
}
#reviewContent {
  color: black;
  border: 2px solid black;
}
#movieRate {
  color: black;
}
</style>