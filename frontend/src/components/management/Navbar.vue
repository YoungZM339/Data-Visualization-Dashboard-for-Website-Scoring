<script>

export default {
  name: "Navbar",
  methods: {
    handle_open_new_windows(url) {
      this.$router.push(url);
    },
    logout() {
      localStorage.removeItem('jwtToken');
      this.$router.push('/login');
    },
  },
}
</script>

<template>
  <el-menu class="el-menu-demo" mode="horizontal">
    <el-menu-item index="1" @click="()=>handle_open_new_windows('/setting')">管理中心</el-menu-item>
    <el-menu-item index="2" @click="()=>handle_open_new_windows('/LargeScreenDisplay')">数据大屏</el-menu-item>
    <el-menu-item index="3" @click="logout()">登出</el-menu-item>
  </el-menu>
</template>

<style scoped lang="less">
.el-menu-demo {
  width: 100%;
  text-align: center;
}
</style>