<template>
<div id="app" class="top_container">
<head-view>
</head-view>
<el-main>
<!--
<div style="display: flex; margin-top: 20px; height: 100px;">
<div class="index-box" :data="index.close">上证指数</div>
<div class="index-box">指数</div>
<div class="index-box">指数</div>
<div class="index-box">指数</div>
<div class="index-box">指数</div>
<div class="index-box">指数</div>
</div>-->
   <el-table
      :data="stockList"
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
        prop="cost"
        label="Cost">
      </el-table-column>
      <el-table-column
              prop="sell_price"
              label="Sell Price">
            </el-table-column>
       <el-table-column
              prop="volume"
              label="Volume">
       </el-table-column>
       <el-table-column
           prop="profit"
          label="Profit">
              </el-table-column>
    </el-table>
</el-main>
</div>
</template>
<script>
export default {
  name: 'portfolio',
  data () {
    return {
      input: '',
      stockList: [],
      index:{}
    }
  },
  mounted: function () {
    this.showStock()
  },
  methods: {
    showStock () {
      console.log(this.input)
      this.$http.get('http://127.0.0.1:8000/api/get_portfolio?username='+sessionStorage.getItem('user'))
        .then((response) => {
          console.log(response)
          var res = response.data
          console.log(res)
          if (res.error_num === 0) {
            this.stockList = res['list']
          } else {
            this.$message.error('fail to query stocks')
            console.log(res['msg'])
          }
        })
    }

  }
}
</script>

<style>
  .index-box {
    margin-bottom: 10px;
    width: 200px;
    height: 100px;
    border-radius: 4px;
    background-color: #409EFF;
    text-align: center;
    color: #fff;
    padding: 40px 20px;
    box-sizing: border-box;
    margin-right: 20px;
  }
</style>
