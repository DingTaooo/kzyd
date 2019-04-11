
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>index</h2>
    <button v-on:click="getNewsInfo">222</button>
  </div>
</template>

<script>
  export default {
    name: 'index',
    data: {
      info: null
    },
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    methods: {
      getNewsInfo: function() {
        console.log('hello')
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
<style scoped>
  h1,
  h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
