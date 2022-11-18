<template>
  <div>
    <div v-if="reviewupdate">
      <!-- <app-update-modal :visible.sync="visible"> -->
        <div>
            <h3>리뷰 수정</h3>
              <div class="row">
                  <div class="col-lg-8 mx-auto">
                      <div>
                          <label>한줄평:</label>
                          <input v-model.trim="content" id="content" type="text" :placeholder="review.content"/>
                      </div>

                      <span>영화 평점:</span>
                      <select v-model="myMovieRate2" @change="changeIdx">
                        <option>5</option>
                        <option>4</option>
                        <option>3</option>
                        <option>2</option>
                        <option>1</option>
                      </select>
                  </div>
              </div>
        </div>
    </div>

    <div v-else>
          작성자 : {{ review.userName }}
          <div v-if="review.rank==5"> 
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i> 
          </div>
           
          <div v-else-if="review.rank==4">
            <i class="fas fa-star" style="color:yellow"></i> 
            <i class="fas fa-star" style="color:yellow"></i> 
            <i class="fas fa-star" style="color:yellow"></i> 
            <i class="fas fa-star" style="color:yellow"></i> 
            
          </div>
          <div v-else-if="review.rank==3">
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i> 
            
          </div>
          <div v-else-if="review.rank==2">
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i> 
            
          </div>
          <div v-else-if="review.rank==1">
            <i class="fas fa-star" style="color:yellow"></i> 
          </div>
          {{ review.content }}
    </div>
    <!-- 리뷰작성자가 아니면 수정,삭제 버튼 안나옴 -->
      <button v-if="name.username === review.userName" class="btn btn-secondary m-1" @click="reviewModify(review)">수정</button>
      <button v-if="name.username === review.userName" class="btn btn-secondary m-1" @click="reviewDelete(review)">삭제 </button>
      <hr>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
// import updateModal from './updateModal'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'MovieReviewDetail',
  components: {
    // appUpdateModal: updateModal,
  },
  props: {
    review: {
      type: Object,
    },
    movie: {
      type: Object
    }
  },
  data: function () {
    return {
      ori_content: this.review.content,
      myMovieRate2: this.review.rank,
      visible: false,
      reviewupdate: false,
      content: this.content,
      rank: this.rank,
      name : '',
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
    getMyName: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.name = res.data
      })
      // .catch( (err) => {
      //   //console.log(err)
      // })
    },
    changeIdx: function (e){
      this.myMovieRate2 = e.target.value
    },
    // 리뷰수정
    // reviewModify: function() { //수정버튼 눌렀을 때 
    //   this.visible = !this.visible
    // },
    reviewModify: function (review) {
      if(this.reviewupdate === false){
        this.reviewupdate = true;
      }
      else{
        const config = this.getToken()
        // 내용수정안할때 예외처리
        if(this.content==undefined) this.content=this.ori_content
        const reviewItem = {
          content: this.content,
          rank: this.myMovieRate2,
          movie: review.movie,
        }
        axios.put(`${SERVER_URL}/movies/review/${review.id}/`, reviewItem, config)
        .then(() => {
          //console.log(res)
          this.content = null
          this.$emit("reviews-updated")
        })
        // .catch(err => {
        //   //console.log(err)
        // })
        this.reviewupdate = false
      }
    },
   // 리뷰 삭제
    reviewDelete: function(review) {
            this.$emit('reviewDelete',review.id)
    },


    
  },
  // created: function () {
  //   this.getMyName()
  // },
  mounted() {
    this.getMyName()
  }
}
</script>

<style>

</style>