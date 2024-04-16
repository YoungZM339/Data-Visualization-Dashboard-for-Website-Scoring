import Vue from 'vue'
import dataV from '@jiaminghi/data-view'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import App from './App.vue'
import store from './store';
import router from './router';

Vue.config.productionTip = false

Vue.use(dataV)
Vue.use(ElementUI)


new Vue({
    store,
    router,
    render: h => h(App)
}).$mount('#app')
