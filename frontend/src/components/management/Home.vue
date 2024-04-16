<script>
export default {
  name: "Home",
}
</script>

<template>
  <div class="home">
    <el-page-header @back="()=>this.$router.go(-1)" content="主页">
    </el-page-header>
    <el-row :gutter="16" style="margin-top: 3%;">
      <el-col :span="6">
        <el-card class="box-card" style="display: flex;justify-content: center;align-items: center;text-align: center;">
          <img src="../../assets/img/1.png" style="width: 55%;" alt="">
          <h1>迅速</h1>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="box-card" style="display: flex;justify-content: center;align-items: center;text-align: center;">
          <img src="../../assets/img/2.png" style="width: 55%;" alt="">
          <h1>精准</h1>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="box-card" style="display: flex;justify-content: center;align-items: center;text-align: center;">
          <img src="../../assets/img/3.png" style="width: 55%;" alt="">
          <h1>创新</h1>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="box-card" style="display: flex;justify-content: center;align-items: center;text-align: center;">
          <img src="../../assets/img/4.png" style="width: 55%;" alt="">
          <h1>准确</h1>
        </el-card>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="18" :offset="2" style="margin-top: 3%;">
        <h2>项目背景</h2>
        <p style="text-indent: 2em;line-height: 1.5">
          随着互联网的快速发展和普及，网站已经成为信息获取、在线购物、社交互动等多种活动的重要平台。然而，由于网站数量巨大和内容复杂多样，如何有效地评估和优化网站体验成为一个迫切需要解决的问题。特别是在竞争激烈的商业环境下，优秀的网站体验不仅能吸引更多的用户，还能提高用户满意度和忠诚度，进而带来更高的商业价值，基于用户行为数据的网站体验评分算法是目前市场需求和技术发展趋势的有机结合，具有广阔的应用前景和商业潜力。</p>
        <h2>产品优势</h2>
        <p style="text-indent: 2em;line-height: 1.5">
          随着互联网的快速发展和普及，网站已经成为信息获取、在线购物、社交互动等多种活动的重要平台。然而，由于网站数量巨大和内容复杂多样，如何有效地评估和优化网站体验成为一个迫切需要解决的问题。特别是在竞争激烈的商业环境下，优秀的网站体验不仅能吸引更多的用户，还能提高用户满意度和忠诚度，进而带来更高的商业价值，基于用户行为数据的网站体验评分算法是目前市场需求和技术发展趋势的有机结合，具有广阔的应用前景和商业潜力。</p>
        <ul style="line-height: 1.5">
          <li>深度分析用户行为，提供个性化建议</li>
          <li>全方位评估，细致指标选择</li>
          <li>满足用户需求，提供有价值建议</li>
          <li>用户为中心，智能化个性化服务</li>
          <li>技术创新，用户反馈，高效准确服务</li>
        </ul>
      </el-col>
    </el-row>
  </div>
</template>

<style scoped lang="less">

</style>