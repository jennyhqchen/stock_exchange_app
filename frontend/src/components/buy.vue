<template>
  <div id="app" class="top_container">
  <head-view>
  </head-view>
  <el-main>
      <el-form :model="sellForm" ref="sellForm" :rules="rules" label-width="80px">
        <el-form-item label="Stock" prop="stock">
          <el-autocomplete
            width="100%"
            v-model="state1"
            :fetch-suggestions="querySearch"
            placeholder="Stock Code"
            @select="handleSelect" ></el-autocomplete>
          </el-form-item>
          <el-form-item prop="volume" label="Volume">
          <el-input-number v-model="volume" :min="100" :step="100"></el-input-number>
          </el-form-item>
          <el-form-item prop="price" label="Price">

                  <el-input-number v-model="price" :precision="2" :step="0.1" :max="10"></el-input-number>
           </el-form-item>
          <el-form-item>
                              <el-button
                                    @click="buy"
                                      type="primary"
                                      >Buy
                              </el-button>
           </el-form-item>
      </el-form>


  </el-main>
  </div>
  </template>
  <script>
  import {buy} from '@/network/trade'
  export default {
      data() {
        return {
           sellForm: {
                stock: '',
                volume: '',
                price:''
          },
          rules: {
                              stock: [
                                  {
                                      require: true,
                                      message: 'stock should not be empty',
                                      triangle: 'blur'
                                  }
                              ],
                              volume: [
                                  {
                                      require: true,
                                      message: 'volume should not be empty',
                                      triangle: 'blur'
                                  }
                              ],
                              price: [
                                 {
                                     require: true,
                                     message: 'price should not be empty',
                                     triangle: 'blur'
                                 }
                               ]
           },
          stocks: [],
          state1: '',
          volume: 100,
          price:0.1
        };
      },
      methods: {
        querySearch(queryString, cb) {
          var stocks = this.stocks;

          var results = queryString ? stocks.filter(this.createFilter(queryString)) : stocks;
          console.log(results)
          cb(results);
        },
        createFilter(queryString) {
          return (stock) => {
            return (stock.code.indexOf(queryString) === 0);
          };
        },
        loadAll() {
          this.$http.get('http://127.0.0.1:8000/api/get_stock')
                  .then((response) => {
                    //console.log(response)
                    var res = response.data
                    if (res.error_num === 0) {
                      this.stocks = res.list
                    } else {
                      this.$message.error('fail to query stocks')
                      console.log(res.msg)
                    }
                  })


        },
        buy() {

                buy(this.state1,this.volume,this.price).then(res => {
                  console.log(res)
                  if(res.data.msg=='success') {


                      this.$message.success('Buy Success')
                  } else {
                      this.$message.error('Buy Fail!')
                  }
                 })

          },
        handleSelect(item) {
          console.log(item);
        }
      },
      mounted() {
       this.loadAll();
      }
    }
  </script>
  </script>
