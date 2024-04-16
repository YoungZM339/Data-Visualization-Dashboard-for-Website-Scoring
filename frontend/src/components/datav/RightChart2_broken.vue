<template>
  <div class="right-chart-2">
    <div class="rc1-header">诊断数据上传</div>

    <div class="rc1-chart-container">
      <div class="left">
        <label for="file-upload" class="custom-file-upload">选择文件</label>
        <input id="file-upload" type="file" multiple @change="handleFileUpload">
      </div>
      <dv-decoration-12 class="dv-12" style="width:150px;height:150px;" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'RightChart2',
  data() {
    return {
      files: []
    }
  },
  methods: {
    handleFileUpload(e) {
      this.files = e.target.files;
      const formData = new FormData();
      for (let i = 0; i < this.files.length; i++) {
        formData.append('files', this.files[i]);
      }
      axios.post('http://localhost:8000/algorithms/process-files/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(res => {
        console.log(res);
      }).catch(err => {
        console.log(err);
      });
    }
  }
}
</script>

<style lang="less">
.right-chart-2 {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;

  .rc1-header {
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
    font-size: 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .right {
    flex: 1;
    padding-bottom: 20px;
    padding-right: 20px;
    box-sizing: border-box;
  }
}

.custom-file-upload {
  display: inline-block;
  padding: 10px 20px;
  cursor: pointer;
  background-color: blue;
  color: white;
  border: 1px solid blue;
  border-radius: 5px;
  font-size: 16px;
}

input[type="file"] {
  display: none;
}

.dv-12 {
  display: flex;
  margin-left: 75px;
  justify-content: center;
  align-items: center;
}
</style>
