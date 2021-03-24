<template>
    <el-container style="height:100%;">
       <el-header style="text-align: right; font-size: 12px">
           <el-menu
             :default-active="this.$route.path"
             class="el-menu-demo"
             mode="horizontal"
             background-color="#545c64"
             text-color="#fff"
             active-text-color="#ffd04b" router>
             <el-menu-item index="/">Market</el-menu-item>
             <el-submenu index="2">
               <template slot="title">My Stock</template>
               <el-menu-item index="sell">Sell</el-menu-item>
               <el-menu-item index="buy">Buy</el-menu-item>
               <el-menu-item index="portfolio">Portfolio Analysis</el-menu-item>
             </el-submenu>
             <el-menu-item key="2-1" index="/login">Login</el-menu-item>
           </el-menu>
       </el-header>
   </el-container>
</template>
<script>
     export default {
       methods: {
         handleOpen(key, keyPath) {
           console.log(key, keyPath);
         },
         handleClose(key, keyPath) {
           console.log(key, keyPath);
         }
       }
     }
</script>
