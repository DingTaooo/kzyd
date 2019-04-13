<template>
  <div class="container">
    <div class="nav">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>图书管理</el-breadcrumb-item>
        <el-breadcrumb-item>图书详情</el-breadcrumb-item>
        <el-breadcrumb-item>章节编辑</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="main">
      <div class="edit">
        <div class="left">
          left
        </div>
        <div class="right">
          right
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'chapterDetail',
    data() {
      return {}
    },
    methods: {}
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .container {
    .main {
      .edit {
        display: flex;
        .left,
        .right {
          flex: 1;
        }
      }
    }
  }
</style>
