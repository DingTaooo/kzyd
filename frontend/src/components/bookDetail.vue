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
        <div class="intro-header">
          <div class="book-name">蠢卫星的书名<span>作者：蠢卫星</span></div>
          <el-button type="primary" plain>编辑简介</el-button>
          <el-button type="primary" plain>确认</el-button>
        </div>
        <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 5}" placeholder="请输入内容" v-model="textarea" :disabled="fff">
        </el-input>
      </div>
    </div>
    <div class="main-box">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#53c68c" text-color="#999" active-text-color="#fff">
        <el-menu-item index="1">目录</el-menu-item>
        <el-menu-item index="2">评论</el-menu-item>
      </el-menu>
      <div class="main">
        <div class="catalog">
          <div class="ol">
            <div class="li">
              <div class="chapter-name"><span>1.</span>第一章de名字</div>
              <div class="operate">
                <div><i class="el-icon-edit"></i> 编辑</div>
                <div><i class="el-icon-delete"></i> 删除</div>
              </div>
            </div>
          </div>
        </div>
        <div class="add" v-on:click="addChapter">
          <el-button type="primary" plain><i class="el-icon-plus"></i> 新增章节</el-button>
        </div>
        <div class="comment">
        </div>
      </div>
      <router-link to="/chapterDetail">第一章</router-link>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'bookDetail',
    data() {
      return {
        intro: '125434',
        fff: false,
        msg: 'Welcome to Your Vue.js App',
        textarea: '125434',
        activeIndex: '1',
        imgList:''
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      addChapter() {
        console.log("this is addChapter")
        let url = this.HOST + '/index'
        this.$axios.get(url)
          .then((res) => {
            console.log(res) //返回的数据
          })
          .catch((err) => {
            console.log(err) //错误信息
          })
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
        .intro-header {
          display: flex;
          justify-content: space-between;
          .book-name {
            display: inline-block;
            padding: 10px 0;
            font-weight: bold;
            span {
              font-weight: 100;
              font-size: 12px;
              color: #999;
              margin-left: 40px;
            }
          }
          .el-button {
            width: 60px;
            font-size: 12px;
            padding: 4px;
          }
        }
        .el-textarea {
          z-index: 999;
        }
      }
    }
    .main-box {
      margin-top: 20px;
      .main {
        // margin-top: 10px;
        .catalog {
          display: flex;
          flex-wrap: wrap;
          .ol {
            width: 50%; // display: flex;
            .li {
              margin: 10px;
              padding: 10px;
              border-radius: 6px;
              background-color: #f5f5f5;
              display: flex;
              justify-content: space-between;
              .chapter-name {
                span {
                  margin-right: 10px;
                }
              }
              .operate {
                font-size: 14px;
                color: #666;
                margin-right: 20px;
                div {
                  display: inline-block;
                  margin-right: 20px;
                  &:hover {
                    color: #53c68c;
                  }
                }
              }
            }
          }
        }
        .add {
          margin: 20px auto;
          text-align: center;
          .el-button {
            width: 200px;
          }
        }
      }
    }
  }
</style>
