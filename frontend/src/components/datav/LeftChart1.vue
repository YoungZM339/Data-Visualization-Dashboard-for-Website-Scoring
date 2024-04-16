<template>
  <div class="left-chart-1">
    <div class="lc1-header">网站问题情况分析</div>
    <div class="lc1-details">严重问题发生次数<span>15</span></div>
    <dv-capsule-chart class="lc1-chart" :config="config" />
    <dv-decoration-2 style="height:10px;" />
  </div>
</template>

<script>
export default {
  name: 'LeftChart1',
  data () {
    return {
      config: {
        data: [
          {
            name: '点击无响应',
            value: 167
          },
          {
            name: '跳出率较高',
            value: 67
          },
          {
            name: '重复点击',
            value: 123
          },
          {
            name: '页面打开慢',
            value: 55
          },
          {
            name: '点击后网络反馈慢',
            value: 98
          }
        ],
        colors: ['#00baff', '#3de7c9', '#fff', '#ffc530', '#469f4b'],
        unit: '次'
      }
    }
  }
}
</script>

<style lang="less">
.left-chart-1 {
  width: 100%;
  height: 37%;
  display: flex;
  flex-grow: 0;
  flex-direction: column;

  .lc1-header {
    text-align: center;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 30px;
    margin-bottom: 20px;
  }

  .lc1-details {
    height: 50px;
    font-size: 16px;
    display: flex;
    align-items: center;
    text-indent: 20px;

    span {
      color: #096dd9;
      font-weight: bold;
      font-size: 35px;
      margin-left: 20px;
    }
  }

  .lc1-chart {
    flex: 1;
  }
}
</style>
