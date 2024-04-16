<script>
import api from "../../api";

export default {
  name: "Process",
  data() {
    return {
      form_data: new FormData(),
      fileList: [],
      task_data: [],
      intervalId: null
    };
  },
  methods: {
    submitUpload() {
      console.log(this.form_data);
      api.post('/algorithms/process-files/', this.form_data, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then((response) => {
        if (response.status === 200) {
          this.$message.success('上传成功');
          this.get_task();
          setTimeout(() => {
            this.$store.dispatch('fetch_data');
          }, 4000);
        } else {
          this.$message.error('上传失败：' + response.data.message);
        }
      }).catch((error) => {
        if (error.response.status === 401) {
          this.$message.error('上传失败：' + "登录失效或未登录，请重新登录");
          this.$router.push('/login?next=/process');
        } else {
          this.$message.error('上传失败：' + error.message);
        }
      });
    },
    handleChange(file, fileList) {
      this.form_data.append(file.name, file.raw);
    },
    handleRemove(file, fileList) {
      this.form_data.delete(file.name);
    },
    handleDownload(file_path) {
      console.log(file_path);
      file_path.map(path => {
        fetch(api.defaults.baseURL + path)
            .then(response => response.blob())
            .then(blob => {
              const url = window.URL.createObjectURL(blob);
              const a = document.createElement('a');
              a.href = url;
              a.download = path.replaceAll('/media/', ''); // 设置文件名
              document.body.appendChild(a);
              a.click();
              window.URL.revokeObjectURL(url);
            });
      });
    },
    get_task() {
      api.get('/tasks/')
          .then((response) => {
            this.task_data = response.data.map((item, index) => {
              let id = item.id;
              let timestamp = new Date(item.timestamp).toLocaleString();
              let status = item.status === true ? '处理完毕' : '正在处理';
              let file_path = item.file_path.replace('[', '').replace(']', '').split(',').map(path => path.trim().replace(/'/g, ''));
              return {id, timestamp, status, file_path};
            });
          })
          .catch((error) => {
            console.log(error);
          });
    }
  },
  beforeMount() {
    this.get_task();
    this.intervalId = setInterval(this.get_task, 5000);
  },
  beforeDestroy() {
    clearInterval(this.intervalId);
  },
}
</script>
<template>
  <div>
    <el-page-header @back="()=>this.$router.go(-1)" content="用户行为数据处理">
    </el-page-header>
    <el-row>
      <el-col :span="18" :offset="3" style="margin-top: 3%;">
        <el-alert
            title="提醒"
            type="info">
          <p>
            请上传用户行为数据文件，文件格式为json。上传成功后，系统将自动处理数据，处理完毕后，您可以访问分析大屏和建议分析查看解析结果。</p>
        </el-alert>
      </el-col>
    </el-row>
    <el-row style="margin: 3%">
      <el-col :span="12" :offset="6" style="text-align: center;">
        <el-upload
            action=""
            :on-change="handleChange"
            :file-list="fileList"
            :auto-upload="false"
            :handleRemove="handleRemove"
            accept=".json"
            multiple>
          <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
          <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器
          </el-button>
        </el-upload>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="18" :offset="4">
        <el-table
            :data="task_data"
            border
            style="width: 100%;">
          <el-table-column
              prop="id"
              label="序号"
              width="100"
              align="center"
          >
          </el-table-column>
          <el-table-column
              prop="timestamp"
              label="提交时间"
              width="180"
              align="center"
          >
          </el-table-column>
          <el-table-column
              label="用户数据下载"
              width="180"
              align="center"
          >
            <template slot-scope="scope">
              <el-button @click="handleDownload(scope.row.file_path)" type="text">下载</el-button>
            </template>
          </el-table-column>
          <el-table-column
              prop="status"
              label="状态"
              align="center"
          >
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>
<style scoped>
</style>