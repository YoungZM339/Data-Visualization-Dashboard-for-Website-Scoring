<template>
  <div id="data-view">
    <dv-full-screen-container>
      <div class="main-header">
        <div class="mh-left"></div>
        <div class="mh-middle">基于用户行为数据的网站体验评分系统</div>
        <div class="mh-right">
          <dv-border-box-2 style="width: 120px; height: 50px; line-height: 50px; text-align:center;margin-right:200px;">
            报告分析页
          </dv-border-box-2>
        </div>
      </div>

      <dv-border-box-1 class="main-container">

        <dv-border-box-3 class="left-chart-container">
          <LeftChart4/>
          <dv-decoration-6 style="width:100%;height:30px;" />
          <LeftChart5/>
          <dv-decoration-6 style="width:100%;height:30px;" />
          <LeftChart6/>
<!--          <Left-Chart-1/>-->
<!--          <Left-Chart-2/>-->
<!--          <Left-Chart-3/>-->
        </dv-border-box-3>

        <div class="right-main-container">
          <div class="rmc-top-container">

            <dv-border-box-3 class="rmctc-left-container">
              <Center-Cmp/>
            </dv-border-box-3>

            <div class="rmctc-right-container">

              <dv-border-box-3 class="rmctc-chart-1">
                <Right-Chart-1/>
              </dv-border-box-3>

              <dv-border-box-9 class="rmctc-chart-2">
                <Right-Chart-2/>
              </dv-border-box-9>

            </div>
          </div>

          <dv-border-box-4 class="rmc-bottom-container">
            <BottomRightTable1/>
            <BottomRightTable4/>
          </dv-border-box-4>

        </div>
      </dv-border-box-1>

    </dv-full-screen-container>
  </div>
</template>

<script>
import LeftChart1 from './datav/LeftChart1.vue'
import LeftChart2 from './datav/LeftChart2.vue'
import LeftChart3 from './datav/LeftChart3.vue'

import CenterCmp from './datav/CenterCmp.vue'

import RightChart1 from './datav/RightChart1.vue'
import RightChart2 from './datav/RightChart2.vue'

import BottomRightTable1 from './datav/BottomRightTable1.vue'
import BottomRightTable4 from './datav/BottomRightTable4.vue'
import LeftChart4 from "./datav/LeftChart4.vue";
import LeftChart5 from "./datav/LeftChart5.vue";
import LeftChart6 from "./datav/LeftChart6.vue";

export default {
  name: 'LargeScreenDisplay',
  components: {
    LeftChart6,
    LeftChart5,
    LeftChart4,
    LeftChart1,
    LeftChart2,
    LeftChart3,
    CenterCmp,
    RightChart1,
    RightChart2,
    BottomRightTable1,
    BottomRightTable4
  },
  mounted() {
    document.querySelector('body').classList.add('custom-body-style');
    document.querySelector('html').classList.add('custom-body-style');
  },
  beforeDestroy() {
    document.querySelector('body').classList.remove('custom-body-style');
    document.querySelector('html').classList.remove('custom-body-style');
  }
}
</script>

<style lang="less">
.custom-body-style {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  background-image: url('../assets/img/bg.png');
  background-size: 100% 100%;
}

#data-view {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 100%;
  height: 100%;
  background-color: #030409;
  color: #fff;

  #dv-full-screen-container {
    box-shadow: 0 0 3px blue;
    display: flex;
    flex-direction: column;
  }

  .main-header {
    height: 80px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;

    .mh-middle {
      font-size: 30px;
    }

    .mh-left,
    .mh-right {
      width: 20%;
    }
  }

  .main-container {
    height: calc(~"100%");

    .border-box-content {
      padding: 20px;
      box-sizing: border-box;
      display: flex;
    }
  }

  .left-chart-container {
    width: 22%;
    padding: 10px;
    box-sizing: border-box;

    .border-box-content {
      flex-direction: column;
    }
  }

  .right-main-container {
    width: 78%;
    padding-left: 5px;
    box-sizing: border-box;
  }

  .rmc-top-container {
    height: 65%;
    display: flex;
  }

  .rmctc-left-container {
    width: 65%;
  }

  .rmctc-right-container {
    width: 35%;
  }

  .rmc-bottom-container {
    height: 35%;
  }

  .rmctc-chart-1,
  .rmctc-chart-2 {
    height: 50%;
  }
}
</style>
