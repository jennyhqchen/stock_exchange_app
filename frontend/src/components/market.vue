<template>
<div id="app" class="top_container">
<head-view>
</head-view>
<el-main>
<el-input placeholder="Search Stock" @clear='showStock' size="small" v-model="input" clearable>
                 <el-button slot="append" @click='showStock'  icon="el-icon-search"></el-button>
</el-input>
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
        prop="close"
        label="Current Price">
      </el-table-column>
       <el-table-column
              prop="open"
              label="Open Price">
       </el-table-column>
       <el-table-column
           prop="high"
          label="Highest Price">
              </el-table-column>
       <el-table-column
              prop="pctChg"
              label="Change">
       </el-table-column>
       <el-table-column
                     prop="volume"
                     label="Volume">
              </el-table-column>
            <el-table-column
                             prop="amount"
                             label="Amount">
                      </el-table-column>
    </el-table>
</el-main>
</div>
</template>
<script>
export default {
  name: 'market',
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
      this.$http.get('http://127.0.0.1:8000/api/show_stock?search='+this.input)
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
