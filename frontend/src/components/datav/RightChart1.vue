<template>
  <div class="right-chart-1">
    <div class="rc1-header">网站体验平均评分</div>

    <div class="rc1-chart-container">
      <div class="left">
        <div style="margin-bottom: 5%;font-size: 18px;">综合得分</div>
        <div class="number">{{ calculated_data['average_score']['average'].toFixed(2) }}</div>
      </div>
      <div class="right">
        <dv-capsule-chart :config="config" style="width:300px;height:200px"/>
      </div>
    </div>
  </div>
</template>

<script>

import {mapGetters} from "vuex";
import * as echarts from "echarts";

export default {
  name: 'RightChart1',
  computed: {
    ...mapGetters(['calculated_data']),
    config() {
      return {
        data: [
          {
            name: '用户体验',
            value: this.calculated_data.user_experience_score.average
          },
          {
            name: '跳转率',
            value: this.calculated_data.bounce_rate_score.average
          },
          {
            name: '点击错误',
            value: this.calculated_data.click_error_score.average
          },
          {
            name: '页面刷新',
            value: this.calculated_data.page_load_error_score.average
          },
          {
            name: '空白页',
            value: this.calculated_data.blank_page_score.average
          },
          {
            name: '首次输入延迟',
            value: this.calculated_data.first_input_delay_score.average
          },
        ],
        colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff'],
        unit: '分'
      }
    },
  },
  mounted() {
    this.$store.dispatch('fetch_data').then(() => {
      this.initChart();
    });
  },
  methods: {
    initChart() {
      let myChart = echarts.init(this.$refs['right-chart-1']);
      let option = {
        yAxis: {
          type: 'category',
          data: Object.keys(this.$store.state.processed_data),
          name: '行为',
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
}

</script>

<style lang="less">
.right-chart-1 {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;

  .rc1-header {
    align-self: center;
    margin: 20px 20px;
    font-size: 24px;
    font-weight: bold;
    height: 30px;
    line-height: 30px;
  }

  .rc1-chart-container {
    flex: 1;
    display: flex;
  }

  .left {
    width: 30%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .number {
      font-size: 34px;
      color: #096dd9;
      font-weight: bold;
      margin-bottom: 30px;
    }
  }

  .right {
    flex: 1;
  }
}
</style>
