<template>
  <div class="bottom-right-table-1">
    <dv-border-box-6>
      <div class="table-name">
        <img src="../../assets/img/icon1.png"/>详细故障记录
      </div>

      <dv-scroll-board :config="config"/>
    </dv-border-box-6>
  </div>
</template>

<script>
export default {
  name: 'BottomRightTable1',
  computed: {
    config() {
      return {
        data: [
          ['故障一', '用户找不到删除功能。'],
          ['故障二', '用户可能收不到验证码。'],
          ['故障三', '页面打开速度较慢，用户频繁刷新。'],
          ['故障四', '用户找不到删除功能。'],
          ['故障五', '用户可能收不到验证码。'],
          ['故障六', '页面打开速度较慢，用户频繁刷新。'],
          ['故障七', '用户找不到删除功能。'],
          ['故障八', '用户可能收不到验证码。'],
          ['故障九', '页面打开速度较慢，用户频繁刷新。']
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
.bottom-right-table-1 {
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
