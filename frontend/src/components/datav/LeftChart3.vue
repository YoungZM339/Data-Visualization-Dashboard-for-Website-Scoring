<template>
  <div class="left-chart-3">
    <div class="lc3-header"></div>
    <div class="lc3-details">一般问题发生次数<span>245</span></div>
    <dv-capsule-chart class="lc3-chart" :config="config" />
  </div>
</template>

<script>
export default {
  name: 'LeftChart3',
  data () {
    return {
      config: {
        data: [
          {
            name: '点击报错',
            value: 78
          },
          {
            name: '页面加载报错',
            value: 54
          },
          {
            name: '页面加载白屏',
            value: 123
          },
          {
            name: '多个同时出现',
            value: 167
          },
          {
            name: '其他',
            value: 77
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
.left-chart-3 {
  width: 100%;
  height: 33%;
  display: flex;
  flex-direction: column;

  .lc3-header {
    height: 20px;
    line-height: 20px;
    font-size: 16px;
    text-indent: 20px;
    margin-top: 10px;
  }

  .lc3-details {
    height: 40px;
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

  .lc3-chart {
    flex: 1;
  }
}
</style>
