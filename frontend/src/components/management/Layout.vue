<script>
import Sidebar from "./Sidebar.vue";
import Navbar from "./Navbar.vue";

export default {
  name: "Layout",
  components: {
    Navbar,
    Sidebar,
  },
  beforeCreate() {
    this.$store.dispatch('fetch_data');
  }
}
</script>

<template>
  <el-container>
    <el-aside width="20%">
      <Sidebar/>
    </el-aside>
    <!--      <el-header>-->
    <!--        <Navbar/>-->
    <!--      </el-header>-->
    <el-main width="80%">
      <RouterView/>
    </el-main>
  </el-container>
</template>

<style scoped lang="less">

</style>