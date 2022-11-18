<template>

<transition name="modal" appear>
  <div class="my-modal d-flex align-items-center justify-content-center" 
    v-if="visible" @click.self="handleWrapperClick">
    <div class="my-modal__dialog ">
      <header class="my-modal__header">
        <span>{{title}}</span>
        <!-- update:visible', !visible 모달 바깥을 클릭해서 모달을 닫음 -->
        <div class="my-modal_btn">
        <button @click="$emit('update:visible', !visible)" class ="btn btn-outline-danger m-4">X</button>
        </div>
      </header>
      <div class="my-modal__body">
        <slot></slot>
      </div>
    </div>
  </div>
</transition>

</template>

<script>
export default {
  name: 'my-modal',
  props: {
    visible: {
      type: Boolean,
      require: true,
      default: false
    },
    title: {
      type: String,
      require: false,
    },
  },
  methods: {
    handleWrapperClick(){
      this.$emit('update:visible', false)
    },
  },
}
</script>

<style lang="scss">
$module: 'my-modal';
.#{$module} {
  
  // This is modal bg
  // align-items: center;
  // justify-content: center;
  // 모달이 맨 위로 나오게 하기
  z-index: 10000;
  // display: inline-block;
  vertical-align: middle;
  // top: 0;
  // left: 0;

  // width: 100%;
  // height: 100%;
  // background-color: rgba(0, 0, 0, 0.993);

  // display: table;
  // transition: opacity .3s ease;
  
  background-color: rgba(0, 0, 0, 0.726);
  top: 0; right: 0; bottom: 0; left: 0;
  position: fixed;
  display:flex; /* 내용을 중앙정렬 하기위해 flex 사용 */
	align-items:center; /* 위아래 기준 중앙정렬 */
	justify-content:center; /* 좌우 기준 중앙정렬 */
  overflow: auto;
  margin: 0;
 
  &__dialog{    
    display: flex;
    border: 2px solid rgb(119, 74, 92);
    // display: flex;

    vertical-align: middle;
    // left: 22%;
    
    width: 1000px;

    // position: fixed;

    margin-bottom: 50px;
  }
  &container{
    width: 300px;
    margin: 0px auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.664);
    transition: all .3s ease;
    // position: static;
  }

  &_header {
    font-size: 28px;
    font-weight: bold;
    line-height: 1.29;
    padding: 16px 16px 0 25px;
    position: static;
  }
  &__body {
    padding: 25px;
    min-height: 150px;
    max-height: 500px;
    overflow-y: scroll;
  }
  &_btn {
    float: right;
  }
}
</style>