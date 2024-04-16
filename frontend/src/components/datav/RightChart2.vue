<template>
  <div class="right-charts-2">
    <div class="left">
      <div style="margin-bottom: 5%;font-size: 18px;font-weight: bold;">行为编号</div>
      <div style="display:flex;flex-direction: row;justify-content: center;align-items: center;">
        <button @click="reduce" style="height: 20px;background-color: #0edcf6;width: 20px;text-align: center;">-</button>
        <div class="number">{{ index + 1 }}</div>
        <button @click="plus" style="height: 20px;background-color: #0edcf6;width: 20px;text-align: center;">+</button>
      </div>
    </div>
    <div class="right">
      <div ref="rc2-chart" id="rc2-chart" style="width: 100%; height: 100%;margin: 3%;"></div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'RightChart2',
  data() {
    return {
      index: 1
    }
  },
  mounted() {
    this.initChart();
    console.log(this.$store.state.processed_data)
  },
  methods: {
    plus() {
      this.index += 1;
      this.initChart();
    },
    reduce() {
      if (this.index - 1 >= 0) {
        this.index -= 1;
      }
      this.initChart();
    },
    initChart() {
      let myChart = echarts.init(this.$refs['rc2-chart']);
      let option = {
        title: {
          text: '单次用户行为得分表',
          left: 'left',
          textStyle: {
            color: '#fff',
            fontSize: 20,
            weight: 'bold'
          }
        },
        tooltip: {
          trigger: 'item'
        },
        series: [
          {
            name: '单次用户行为得分表',
            type: 'pie',
            radius: '50%',
            data: [
              {value: this.$store.state.processed_data[this.index]['user_experience_score'], name: '用户体验'},
              {value: this.$store.state.processed_data[this.index]['bounce_rate_score'], name: '跳转率'},
              {value: this.$store.state.processed_data[this.index]['click_error_score'], name: '点击错误'},
              {value: this.$store.state.processed_data[this.index]['page_load_error_score'], name: '页面刷新'},
              {value: this.$store.state.processed_data[this.index]['blank_page_score'], name: '空白页'},
              {value: this.$store.state.processed_data[this.index]['first_input_delay_score'], name: '首次输入延迟'}
            ]
          }
        ]
      };
      myChart.setOption(option);
    }
  }
};
</script>

<style scoped lang="less">
.right-charts-2 {
  height: 100%;
  display: flex;
  flex: 1;
}

.left {
  width: 30%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.right {
  flex: 1;
}

.number {
  height: 36px;
  font-size: 36px;
  color: #096dd9;
  font-weight: bold;
  margin: 12px;
}
</style>
