<script>
export default {
  name: "Sidebar",
  methods: {
    handle_router_push(url) {
      this.$router.push(url);
    },
    handle_open_new_windows(url) {
      window.open(url);
    },
    logout() {
      localStorage.removeItem('jwtToken');
      this.$router.push('/login');
    },
  },
}
</script>

<template>
  <el-menu class="el-menu-vertical-demo">
    <el-menu-item index="1" style="margin: 20px">
      <el-image :src="require('../../assets/img/icon2.png')" fit="cover" style="width: 50px; height: 50px;"></el-image>
    </el-menu-item>
    <el-menu-item index="2" @click="() => handle_router_push('/home')">
      <i class="el-icon-s-home"></i>
      <span slot="title">系统主页</span>
    </el-menu-item>
    <el-menu-item index="3" @click="() => handle_router_push('/process')">
      <i class="el-icon-document"></i>
      <span slot="title">数据处理</span>
    </el-menu-item>
    <el-menu-item index="4" @click="()=> handle_router_push('/LargeScreenDisplay')">
      <i class="el-icon-data-analysis"></i>
      <span slot="title">分析大屏</span>
    </el-menu-item>
    <el-menu-item index="5" @click="()=> handle_router_push('/advice')">
      <i class="el-icon-info"></i>
      <span slot="title">分析建议</span>
    </el-menu-item>
    <!--    <el-menu-item index="5" @click="() => handle_router_push('/setting')">-->
    <!--      <i class="el-icon-setting"></i>-->
    <!--      <span slot="title">设置</span>-->
    <!--    </el-menu-item>-->
    <el-menu-item index="6" @click="logout()">
      <i class="el-icon-setting"></i>
      <span slot="title">登出</span>
    </el-menu-item>
  </el-menu>
</template>

<style scoped lang="less">
.el-menu-vertical-demo {
  height: 100vh;
  text-align: center;
}
</style>