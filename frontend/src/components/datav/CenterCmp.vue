<template>
  <div class="center-cmp">
    <div class="cc-header">
      <dv-decoration-1 style="width:200px;height:50px;"/>
      <div>会话数据信息</div>
      <dv-decoration-1 style="width:200px;height:50px;"/>
    </div>

    <div class="cc-details">
      <div style="margin-right:3%">用户行为总数</div>
      <div class="card" v-for="(char, index) in char_array" :key="index">{{ char }}</div>
    </div>

    <div class="cc-main-container">
      <div class="center-cmp-left">
        <div class="station-info">
          点击行为数<span>{{ event_name_array['Element Click'] ? event_name_array['Element Click'] : 0 }}</span>
        </div>
        <div class="station-info">
          输入行为数<span>{{ event_name_array['Text Input'] ? event_name_array['Text Input'] : 0 }}</span>
        </div>
        <div class="station-info">
          访问行为数<span>{{ event_name_array['Page Visit'] ? event_name_array['Page Visit'] : 0 }}</span>
        </div>
      </div>

      <div class="center-cmp-middle">
        <dv-active-ring-chart :config="config" style="width:100%;height:100%"/>
      </div>

      <div class="center-cmp-right">
        <div class="station-info">
          停留行为数<span>{{ event_name_array['Viewport Stay'] ? event_name_array['Viewport Stay'] : 0 }}</span>
        </div>
        <div class="station-info">
          缩放行为数<span>{{ event_name_array['Window Resizing'] ? event_name_array['Window Resizing'] : 0 }}</span>
        </div>
        <div class="station-info">
          首次交互数<span>{{
            event_name_array['First Interaction'] ? event_name_array['First Interaction'] : 0
          }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LabelTag from './LabelTag'
import {mapGetters} from "vuex";
import * as echarts from "echarts";

export default {
  name: 'center-cmp',
  computed: {
    ...mapGetters(['calculated_data']),
    ...mapGetters(['event_name_array']),
    ...mapGetters(['char_array']),
    config() {
      return {
        radius: '50%',
        activeRadius: '60%',
        lineWidth: 60,
        data: [
          {
            name: '点击行为',
            value: this.event_name_array['Element Click'] ? this.event_name_array['Element Click'] : 0
          },
          {
            name: '输入行为',
            value: this.event_name_array['Text Input'] ? this.event_name_array['Text Input'] : 0
          },
          {
            name: '访问行为',
            value: this.event_name_array['Page Visit'] ? this.event_name_array['Page Visit'] : 0
          },
          {
            name: '停留行为',
            value: this.event_name_array['Viewport Stay'] ? this.event_name_array['Viewport Stay'] : 0
          },
          {
            name: '缩放行为',
            value: this.event_name_array['Window Resizing'] ? this.event_name_array['Window Resizing'] : 0
          },
          {
            name: '首次交互',
            value: this.event_name_array['First Interaction'] ? this.event_name_array['First Interaction'] : 0
          }
        ],
        digitalFlopStyle: {
          fontSize: 25
        },
        showOriginValue: true
      }
    }
  },
  components: {
    LabelTag
  },
}
</script>

<style lang="less">
.center-cmp {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;

  .cc-header {
    height: 10%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 30px;
  }

  .cc-details {
    height: 20%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-size: 30px;

    .card {
      background-color: rgba(4, 49, 128, .6);
      color: #08e5ff;
      height: 70px;
      width: 70px;
      font-size: 40px;
      font-weight: bold;
      line-height: 70px;
      text-align: center;
      margin: 10px;
    }
  }

  .cc-main-container {
    height: 70%;
    display: flex;

    .center-cmp-middle {
      width: 50%;
      height: 100%;
    }

    .center-cmp-left,
    .center-cmp-right {
      width: 25%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      text-align: center;
      font-size: 30px;
      white-space: nowrap;
      overflow: hidden;
      margin: 0 3% 0 3%;

      span {
        margin-left: 10px;
        font-size: 40px;
        font-weight: bold;
      }

      .station-info {
        height: 80px;
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        text-align: center;
      }
    }

    .center-cmp-left {
      align-items: flex-end;
    }

    .center-cmp-right {
      align-items: flex-start;
    }
  }
}
</style>
