import Vue from 'vue';
import App from './App.vue';
import router from './router/router.js';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';

new Vue({
    router,
    render: h => h(App),
}).$mount('#app');
