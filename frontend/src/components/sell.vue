<template>
  <div id="app" class="top_container">
  <head-view>
  </head-view>
  <el-main>
      <el-table
           :data="shareholdingList"
           style="width: 100%">
           <el-table-column
             prop="code"
             label="Stock Code"
             width="180">
           </el-table-column>
           <el-table-column
             prop="code_name"
             label="Stock Name"
             width="180">
           </el-table-column>
           <el-table-column
             prop="price"
             label="Price">
           </el-table-column>
            <el-table-column
                   prop="volume"
                   label="Volume">
            </el-table-column>
            <el-table-column label="action">
                  <template slot-scope="scope">
                    <el-button
                      size="mini"
                      @click="handleSell(scope.$index, scope.row)">sell</el-button>
                   </template>
             </el-table-column>
         </el-table>

  </el-main>
  </div>
  </template>
  <script>
  import {sell} from '@/network/trade'
  export default {
      data() {
           return {
                input: '',
                shareholdingList: [],
                index:{}
              }
        },
      methods: {

        loadAll() {
          this.$http.get('http://127.0.0.1:8000/api/get_shareholdings?username=' + sessionStorage.getItem('user'))
                  .then((response) => {
                    console.log(response)
                    var res = response.data
                    if (res.error_num === 0) {
                      this.shareholdingList = res.list
                    } else {
                      this.$message.error('fail to query stocks')
                      console.log(res.msg)
                    }
                  })


        },
        handleSell(index, row) {
              this.$prompt('Please enter price', 'tip', {
                        confirmButtonText: 'submit',
                        cancelButtonText: 'cancel'
                      }).then(({ value }) => {
                          sell(row.id, row.code,row.code_name, row.volume, row.price, value).then(res => {
                            console.log(res)
                            if(res.data.msg=='success') {
                                this.$message.success('Sell Success')
                            } else {
                                this.$message.error('Sell Fail!')
                            }
                           })
                       });
                console.log(index, row);
         }
      },
      mounted() {
       this.loadAll();
      }
    }
  </script>
  </script>
