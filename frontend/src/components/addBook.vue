/*
 * @Author: 蠢卫星 
 * @Date: 2019-04-12 13:32:44 
 * @Last Modified by: 蠢卫星
 * @Last Modified time: 2019-04-12 15:01:23
 */

<template>
  <div class="container">
    <!-- ISBN -->
    <div class="nav">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>图书管理</el-breadcrumb-item>
        <el-breadcrumb-item>新增图书</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="main">
      <div class="search-box">
        <div class="title">请输入ISBN:</div>
        <el-input v-model="input" placeholder="ISBN" clearable>
          <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
      </div>
      <div class="book-detail">
        <div class="left">
          <!-- <div class="cover" style="background: url('https://cdn.dribbble.com/users/788099/screenshots/6323001/girl_architect_kit8-net.png') 100% no-repeat"> -->
          <img class="cover" src="https://cdn.dribbble.com/users/788099/screenshots/6323001/girl_architect_kit8-net.png">
          <!-- </div> -->
        </div>
        <div class="right">
          <div class="book-name">
            <div>蠢卫星的书名</div>
            <div class="author">作者:蠢卫星</div>
          </div>
          <div class="intro">简介:intro</div>
        </div>
      </div>
    </div>
    <el-button type="success" round class="sure-button">确认</el-button>
    <el-button type="warning" plain class="sure-button">没有你想要的图书哦,重新搜索下吧!</el-button>
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
    .main {
      margin: 20px 80px 0;
    }
    .search-box {
      max-width: 800px;
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
        .el-button {
          &:hover {
            font-size: 20px;
            color: #53c68c;
          }
        }
      }
    }
    .book-detail {
      height: 400px;
      margin-top: 40px;
      display: flex;
      .left {
        flex: none;
        width: 300px;
        .cover {
          height: 400px;
          width: 300px;
          border-radius: 20px;
          border: 2px solid #fff;
          box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        }
      }
      .right {
        flex: 1;
        margin-left: 20px;
        background-color: #f5f5f5;
        div {
          padding-left: 10px;
        }
        .book-name {
          font-size: 24px;
          padding: 14px 0;
          width: 100%;
          background-color: #f5f5f5;
          border-bottom: 4px solid #fff;
          .author {
            margin-top: 6px;
            font-size: 14px;
            color: #999;
          }
        }
        .intro {
          margin-top: 10px;
          overflow: hidden;
          text-overflow: ellipsis;
          display: -webkit-box;
          -webkit-line-clamp: 14;
          -webkit-box-orient: vertical;
        }
      }
    }
    .sure-button {
      display: block;
      margin: 20px auto 0;
    }
  }
</style>
