<script>
import api from "../../api";

export default {
  name: 'Login',
  data() {
    return {
      login_status: false,
      loginForm: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    login() {
      this.login_status = true;
      api.post('/login/', this.loginForm)
          .then((response) => {
            this.login_status = false;
            if (response.status === 200) {
              this.$message.success('登录成功');
              console.log(response.data['access']);
              localStorage.setItem('jwtToken', response.data['access']);
              this.$router.push('/home');
            } else {
              this.$message.error('登陆失败：' + response.data.message);
            }
          })
          .catch((error) => {
            this.login_status = false;
            this.$message.error('登陆失败：' + error.message);
          });
    }
  }
}
</script>

<template>
  <el-form :model="loginForm" ref="loginForm" label-position="left" label-width="0px"
           class="demo-ruleForm login-container">
    <h3 class="title">系统登录</h3>
    <el-form-item prop="username">
      <el-input type="text" v-model="loginForm.username" auto-complete="off" placeholder="账号"
                @keyup.enter.native="$refs.password.focus()"></el-input>
    </el-form-item>
    <el-form-item prop="password">
      <el-input type="password" ref="password" v-model="loginForm.password" auto-complete="off" placeholder="密码"
                @keyup.enter.native="login"></el-input>
    </el-form-item>
    <el-form-item style="width:100%;">
      <el-button type="primary" style="width:50%;margin-left: 25%;" @click.native.prevent="login"
                 :loading="login_status">登 录
      </el-button>
    </el-form-item>
  </el-form>
</template>

<style scoped>
.login-container {
  -webkit-border-radius: 5px;
  border-radius: 5px;
  -moz-border-radius: 5px;
  background-clip: padding-box;
  margin: 180px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;

  .title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
  }
}
</style>