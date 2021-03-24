<template>
<div id="app" class="top_container">
<head-view>
</head-view>
<el-main>
     <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
                <el-form-item prop="username">
                    <el-input placeholder="username"
                              v-model="ruleForm.username">
                        <i slot="prefix" class="el-icon-user"></i>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input placeholder="password"
                              v-model="ruleForm.password"
                              show-password>
                        <i slot="prefix" class="el-icon-lock"></i>
                    </el-input>
                </el-form-item>
                <el-form-item>
                    <el-button
                            @click="login"
                            type="primary"
                            >Login
                    </el-button>
                      <el-button
                               @click="register"
                                type="primary"
                                >register
                      </el-button>
                </el-form-item>
            </el-form>
</el-main>
</div>
</template>
<script>
import {getCSRFtoken,login} from '@/network/login'
import {request} from '@/network/request';
export default {
        data() {
            return {
                // data
                ruleForm: {
                    username: '',
                    password: '',
                },
                // rules
                rules: {
                    username: [
                        {
                            require: true,
                            message: 'username should not be empty',
                            triangle: 'blur'
                        }
                    ],
                    password: [
                        {
                            require: true,
                            message: 'password should not be empty',
                            triangle: 'blur'
                        }
                    ]
                }
            }
        },
        methods:{

            login() {
              this.$refs.ruleForm.validate((valid) => {
                                  if (valid) {
                                      login(this.ruleForm.username,this.ruleForm.password).then(res => {

                                        if(res.data.msg=='success') {
                                            this.$store.commit('setUser',this.ruleForm.username)
                                            console.log(this.$store.state.user)
                                            this.$message.success('Login Success')
                                        } else {
                                            this.$message.error('Login Fail!')
                                        }
                                       })
                                  } else {
                                      this.$message.error("invalid input!")
                                  }
                              })

            },
            register() {
                this.$router.push('/register')

            }
        }
    }
</script>
