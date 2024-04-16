<template>
  <div class="left-charts-4"
       style="height: 33%;display: flex;flex-direction: column;justify-content: center;align-items: center;">
    <div ref="lc4-chart" id="lc4-chart" style="width: 100%; height: 100%;margin-top: 5%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'LeftChart4',
  mounted() {
    this.$store.dispatch('fetch_data').then(() => {
      this.initChart();
    });
  },
  methods: {
    initChart() {
      let myChart = echarts.init(this.$refs['lc4-chart']);
      let option = {
        xAxis: {
          type: 'category',
          data: Object.keys(this.$store.state.processed_data),
          name: '行为',
        },
        yAxis: {
          type: 'value'
        },
        title: {
          text: '用户行为平均得分',
          left: 'center',
          top: '0',
          textStyle: {
            color: '#fff',
            fontSize: 20,
            weight: 'bold'
          }
        },
        series: [{
          data: Object.values(this.$store.state.processed_data).map(value => value['average_score']),
          name: '平均得分',
          type: 'bar'
        }]
      };
      myChart.setOption(option);
    }
  }
};
</script>

<style scoped lang="less">

</style>
