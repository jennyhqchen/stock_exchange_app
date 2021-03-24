import {request} from './request';
import store from '@/store'

export function buy(stock,volume,price) {
    let params = new URLSearchParams();
    console.log('stock' + stock)
    console.log('volume' + volume)
    console.log('price' + price)
    params.append('stock',stock);
    params.append('volume',volume);
    params.append('price',price);
    params.append('username',sessionStorage.getItem('user'));
    return request({
        url: '/buy',
        method:'POST',
        data:params,
    })
}

export function sell(order_id,code, code_name,volume,cost,price) {
    let params = new URLSearchParams();
    params.append('code',code);
    params.append('code_name',code_name);
    params.append('volume',volume);
    params.append('cost',cost);
    params.append('price',price);
    params.append('order_id',order_id);
    params.append('username',sessionStorage.getItem('user'));
    return request({
        url: '/sell',
        method:'POST',
        data:params,
    })
}
