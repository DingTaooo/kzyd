/*
 * @Author: 蠢卫星 
 * @Date: 2019-04-12 13:32:50 
 * @Last Modified by: 蠢卫星
 * @Last Modified time: 2019-04-18 12:25:05
 */

<template>
  <div class="container">
    <div class="header">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>图书管理</el-breadcrumb-item>
      </el-breadcrumb>
      <router-link to="/addBook">
        <div class="book-add"><i class="el-icon-plus"></i> 新增图书</div>
      </router-link>
    </div>
    <router-link to="/bookDetail">
      <div class="books-box">
        <div v-for="book in books" :key="book.index" class="book-box">
          <img :src="book.coverUrl" class="book-cover" />
          <div class="book-name">{{ book.name }}</div>
        </div>
      </div>
    </router-link>
    <button v-on:click="getNewsInfo">222</button>
  </div>
</template>

<script>
  export default {
    name: 'index',
    data() {
      return {
        books: [{
            coverUrl: 'https://cdn.dribbble.com/users/13157/screenshots/6321894/6.png',
            name: '冲浪的小女孩'
          },
          {
            coverUrl: 'https://cdn.dribbble.com/users/13157/screenshots/6321894/6.png',
            name: '冲浪的小女孩'
          },
          {
            coverUrl: 'https://cdn.dribbble.com/users/13157/screenshots/6321894/6.png',
            name: '冲浪的小rgdgdfgd法的规定符合规范的话女孩'
          },
          {
            coverUrl: 'https://cdn.dribbble.com/users/13157/screenshots/6321894/6.png',
            name: '冲浪的小女孩'
          },
          {
            coverUrl: 'https://cdn.dribbble.com/users/13157/screenshots/6321894/6.png',
            name: '冲浪的小女孩'
          },
        ],
        info: null
      }
    },
    created: function() {
      console.log('hello')
    },
    methods: {
      getNewsInfo: function() {
        console.log('getNewsInfo')
        this.$http.get({
          url: this.$url + 'index',
          // method: 'get',
        }).then(function(response) {
          console.log(response)
        }).catch(function(error) {
          console.log('error', error)
        })
      }
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .container {
    .header {
      display: flex;
      justify-content: space-between;
      height: 40px;
      line-height: 40px;
      .book-add {
        margin-right: 80px;
        height: 40px;
        padding: 0 20px;
        background-color: #f5f5f5;
        border-radius: 20px;
        text-align: center;
        color: #53c68c;
        border: 1px solid #53c68c;
        line-height: 40px;
        &:hover {
          background-color: #53c68c;
          color: #fff;
        }
      }
    }
    .books-box {
      .book-box {
        display: inline-block;
        margin: 20px 50px;
        .book-cover {
          border: 2px solid #fff;
          width: 120px;
          height: 160px;
          border-radius: 10px;
          background-color: #fff;
          text-align: center;
          color: #53c68c;
          box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
          &:hover {
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.2);
          }
          i {
            margin-top: 60px;
            font-size: 30px;
          }
        }
        .book-name {
          margin-left: -10px;
          width: 140px;
          text-align: center;
          overflow: hidden;
          white-space: nowrap;
          text-overflow: ellipsis;
        }
      }
    }
  }
</style>
