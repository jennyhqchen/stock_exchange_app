import {request} from './request';
import store from '@/store'
export function getCSRFtoken() {
    return request({
        url: '/get_token',
        method: 'get'
    })
}

export function register(username,password) {
      let params = new URLSearchParams();
      params.append('username',username);
      params.append('password',password);
      return request({
          url: '/register',
          method:'POST',
          data:params,
      })
}

export function login(username,password) {
    let params = new URLSearchParams();
    params.append('username',username);
    params.append('password',password);
    return request({
        url: '/login',
        method:'POST',
        data:params,
    })
}
