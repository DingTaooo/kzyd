<template>
  <div id="app">
    <el-container id="body">
      <el-header>
        <div class="header-title">
          扩展阅读系统管理端
        </div>
        <div class="header-user">
          <el-dropdown>
            <span class="el-dropdown-link">蠢卫星<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item icon="el-icon-star-off">蠢卫星</el-dropdown-item>
              <el-dropdown-item icon="el-icon-news">消息<span class="news-number">2</span></el-dropdown-item>
              <el-dropdown-item icon="el-icon-back">退出</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <img class="header-user-img" src="https://cdn.dribbble.com/users/19849/screenshots/6317537/eric_2x.png" />
        </div>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <el-row>
            <el-col>
              <el-menu default-active="1">
                <router-link to="/index">
                  <el-menu-item index="1">
                    <i class="el-icon-tickets"></i>
                    <span slot="title">图书管理</span>
                  </el-menu-item>
                </router-link>
                <router-link to="/user">
                  <el-menu-item index="2">
                    <i class="el-icon-more-outline"></i>
                    <span slot="title">数据中心</span>
                  </el-menu-item>
                </router-link>
                <router-link to="/">
                  <el-menu-item index="3">
                    <i class="el-icon-bell"></i>
                    <span slot="title">消息通知</span>
                  </el-menu-item>
                </router-link>
                <router-link to="/">
                  <el-menu-item index="4">
                    <i class="el-icon-news"></i>
                    <span slot="title">用户中心</span>
                  </el-menu-item>
                </router-link>
              </el-menu>
            </el-col>
          </el-row>
        </el-aside>
        <el-main>
          <router-view/>
        </el-main>
      </el-container>
      <footer>@蠢卫星 e-mail: chunweixing@outlook.com</footer>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>

<style lang="scss">
  @import url(assets/commonstyle.scss);
</style>

