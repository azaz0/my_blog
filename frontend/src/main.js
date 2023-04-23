import {createApp} from 'vue'
import App from './App.vue'
import router from './router/router.js'
import store from './store/index.js';
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'
const app = createApp(App)
app.use(store)
app.use(router)
app.config.globalProperties.$http = axios
app.mount('#app');

