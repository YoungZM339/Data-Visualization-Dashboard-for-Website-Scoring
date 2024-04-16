<template>
  <div class="bottom-right-table-4">
    <dv-border-box-6>
      <div class="table-name">
        <img src="../../assets/img/icon3.png" />故障排行榜
      </div>

      <dv-scroll-board :config="config" />
    </dv-border-box-6>
  </div>
</template>

<script>
export default {
  name: 'BottomRightTable4',
  computed: {
    config() {
      return {
        data: [
          ['无响应', '累计：8起'],
          ['点击错误', '累计：3起'],
          ['白屏', '累计：3起'],
          ['页面刷新错误', '累计：4起'],
          ['点击错误', '累计：1起'],
          ['交互延迟', '累计：1起']
        ],
        index: true,
        columnWidth: [30, 100],
        align: ['center'],
        oddRowBGC: 'rgba(9, 37, 50, 0.4)',
        evenRowBGC: 'rgba(10, 32, 50, 0.3)'
      }
    }
  }
}
</script>

<style lang="less">
.bottom-right-table-4 {
  width: calc(~"45% + 10px");
  height: 100%;
  margin: 0 -5px;

  .border-box-content {
    padding: 20px;
    box-sizing: border-box;
  }

  .table-name {
    height: 45px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 15px 15px;

    img {
      width: 40px;
      height: 40px;
      margin-right: 5px;
    }
  }

  .dv-scroll-board {
    display: flex;
    justify-content: center;
    align-self: center;
    height: calc(~"100% - 60px");
  }
}
</style>
