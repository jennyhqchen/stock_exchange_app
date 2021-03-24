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
                            @click="register"
                            type="primary"
                            style="width: 100%">Register
                    </el-button>
                </el-form-item>
            </el-form>
</el-main>
</div>
</template>
<script>
import {getCSRFtoken,register} from '@/network/login'
import {request} from '@/network/request';
export default {
        created() {
                    this.getCSRFtoken()
                },
        data() {
            return {
                // 表单数据
                ruleForm: {
                    username: '',
                    password: '',
                },
                // 表单验证规则
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

            register() {
              this.$refs.ruleForm.validate((valid) => {
                                  if (valid) {
                                      register(this.ruleForm.username,this.ruleForm.password).then(res => {
                                        console.log(res)
                                       })
                                  } else { // 验证失败事件
                                      this.$message.error("invalid input!")
                                  }
                              })

            }
        }
    }
</script>
