import axois from 'axios'
import store from '@/store'
axois.defaults.withCredentials = true;  // 在发送请求时 ，axios 默认是不带cookies的


export function request(config) {
    const instance = axois.create({
        baseURL: 'http://127.0.0.1:8000/api',
        timeout: 5000
    })

    instance.interceptors.request.use(config => {
        if (config.method === 'post') {
            config.headers['X-CSRFToken'] = store.state.token;
        }
        return config
    }, err => {
        return err
    })

    instance.interceptors.response.use(res => {
        return res
    }, err => {
        return err
    })

    return instance(config)
}
