/*
 * @Author: 蠢卫星 
 * @Date: 2019-04-12 13:32:44 
 * @Last Modified by: 蠢卫星
 * @Last Modified time: 2019-04-12 15:01:23
 */

<template>
  <div class="container">
    <!-- ISBN -->
    <div class="search-box">
      <div class="title">请输入ISBN:</div>
      <el-input v-model="input" placeholder="ISBN" clearable>
        <el-button slot="append" icon="el-icon-search"></el-button>
      </el-input>
    </div>
    <div class="book-detail">
      <div class="left">
        <div class="cover" style="background: url('https://cdn.dribbble.com/users/788099/screenshots/6323001/girl_architect_kit8-net.png') 100% no-repeat">
          <!-- <img src="https://cdn.dribbble.com/users/788099/screenshots/6323001/girl_architect_kit8-net.png"> -->
        </div>
      </div>
      <div class="right">
        <div class="deader">蠢卫星的书名</div>
        <div class="author">蠢卫星</div>
        <div class="intro">intro</div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'addBook',
    data() {
      return {
        input: ''
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .container {
    margin: 0 80px;
    .search-box {
      display: flex;
      .title {
        line-height: 40px;
        flex: none;
        width: 120px;
        font-size: 16px;
        font-weight: bold;
      }
      .el-input {
        flex: 1;
      }
    }
    .book-detail {
      display: flex;
      .left {
        .cover{
          height: 400px;
          width: 300px;
        }
      }
    }
  }
</style>
