<template>
  <div class="left-charts-5" style="height: 33%;display: flex;flex-direction: column;justify-content: center;align-items: center;">
    <div style="font-size: 20px;font-weight: bold;margin: 3%;">网站体验错误统计</div>
    <div ref="lc5-chart" id="lc5-chart" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import {mapGetters} from "vuex";

export default {
  name: 'LeftChart5',
  mounted() {
    this.$store.dispatch('fetch_data').then(() => {
      this.initChart();
    });
  },
  computed: {
    ...mapGetters(['calculated_data']),
    ...mapGetters(['event_name_array']),
    ...mapGetters(['char_array'])
  },
  methods: {
    initChart() {
      let myChart = echarts.init(this.$refs['lc5-chart']);
      let option = {
        tooltip: {
          trigger: 'item'
        },
        legend: {
          color: '#fff',
          textStyle: {
            color: '#fff',
            padding: [3, 0, 0, 0]
          }
        },
        series: [
          {
            name: '用户行为错误表',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 15,
                color: '#fff'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: this.event_name_array['Element Click'], name: '点击'},
              {value: this.event_name_array['Text Input'], name: '输入'},
              {value: this.event_name_array['Page Visit'], name: '访问'},
              {value: this.event_name_array['Viewport Stay'], name: '停留'},
              {value: this.event_name_array['Window Resizing'], name: '缩放'},
              {value: this.event_name_array['First Interaction'], name: '交互'}
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

</style>
