<template>
  <div>
    <!-- <h2 style="margin-bottom:30px">제목과 버튼을 눌러 상세페이지로, 유저를 눌러 프로필로 넘어가보세요</h2> -->
    <div class="row d-flex justify-content-center align-items-center  " >
      <div class="card row d-flex justify-content-center align-items-center" style="border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.3);">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div style="cursor:pointer;" v-for="(community, idx) in communities" :key="idx">
          <br>
            <!-- <h3 @click="DetailCommunity(community)">{{community.id}}번 글</h3> -->
            <h2>{{community.title}}</h2>
            <button @click="DetailCommunity(community)" class ="btn btn-outline-danger">Detail</button>
            <h4>{{community.content}}</h4>
          <p  @click="moveToProfile(community.user, community.userName)">작성자:
              {{ community.userName }}
          </p>
        <hr>
        </div>
      </div>
    </div>
    </div>
  </div>

</template>


<script>
export default {
  name: 'CommunityList',
  props: {
    // Community에서 v-for을 이용해 보내준 게시글 한개의 데이터를 props를 통해 받고 보여준다.
    communities: [Array, Object]
  },
  methods: {
    DetailCommunity: function (community) {
      // console.log('디테일' + community.id)
      // this.$store.dispatch('createDetailCommunity', community)
      // console.log('디테일로 넘김')
      this.$router.push({ name: 'CommunityDetail', params: { community_pk: `${community.id}` }})
    },
    moveToProfile: function (user, username) {
      // console.log(user)
      this.$router.push({ name: "MyProfile", params: { user_pk: `${user}`, username: `${username}` }})
    },    
  }
}
</script>

<style>
</style>