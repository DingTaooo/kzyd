<template>
  <div class="container">
    <div class="nav">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>图书管理</el-breadcrumb-item>
        <el-breadcrumb-item>图书详情</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="header">
      <div class="cover">
        <img src="https://cdn.dribbble.com/users/788099/screenshots/6323001/girl_architect_kit8-net.png">
      </div>
      <div class="book-intro">
        <div class="book-name">蠢卫星的书名<span>作者：蠢卫星</span></div>
        <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 5}" placeholder="请输入内容" v-model="textarea" :disabled="fff">
        </el-input>
        <el-button type="primary" icon="el-icon-edit" circle></el-button>
        <el-button type="success" icon="el-icon-check" circle></el-button>
      </div>
    </div>
    <div class="main">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#53c68c" text-color="#999" active-text-color="#fff">
        <el-menu-item index="1">目录</el-menu-item> 
        <el-menu-item index="2">评论</el-menu-item>
      </el-menu>
      <router-link to="/chapterDetail">第一章</router-link>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'bookDetail',
    data() {
      return {
        fff: true,
        msg: 'Welcome to Your Vue.js App',
        textarea: '',
        activeIndex: '1',
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .container {
    .header {
      position: relative;
      display: flex;
      height: 160px;
      margin-top: 20px;
      .cover {
        width: 120px;
        flex: none;
        img {
          height: 160px;
          width: 120px;
          border-radius: 10px;
          border: 2px solid #fff;
          box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        }
      }
      .book-intro {
        margin-left: 30px;
        flex: 1;
        .book-name {
          padding: 10px 0;
          font-weight: bold;
          span {
            font-weight: 100;
            font-size: 12px;
            color: #999;
            margin-left: 40px;
          }
        }
        .el-textarea {
          .el-textarea__inner {
            padding-right: 100px;
          }
        }
        .el-button {
          position: absolute;
          right: -20px;
          bottom: 74px;
        }
      }
    }
    .main{
      margin-top: 20px;
      ul{
        .el-menu-item{
          width: 100px;
          text-align: center;
        }
      }
    }
  }
</style>
