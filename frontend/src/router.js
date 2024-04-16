/* eslint-disable */
import Vue from 'vue';
import VueRouter from 'vue-router';
import api from "./api";

Vue.use(VueRouter);


function checkAuth() {
    const token = localStorage.getItem('jwtToken');
    return !!token;
}

const management_routes = [
    {
        path: 'home',
        name: 'Home',
        component: () => import('./components/management/Home.vue'),
        meta: {requiresAuth: true}
    },
    {
        path: 'process',
        name: 'Process',
        component: () => import('./components/management/Process.vue'),
        meta: {requiresAuth: true}
    },
    {
        path: 'advice',
        name: 'Advice',
        component: () => import('./components/management/Advice.vue'),
        meta: {requiresAuth: true}
    },
    {
        path: 'setting',
        name: 'Setting',
        component: () => import('./components/management/Setting.vue'),
        meta: {requiresAuth: true}
    }
]
const routes = [
    {
        path: '/',
        name: 'Layout',
        redirect: '/home',
        component: () => import('./components/management/Layout.vue'),
        children: management_routes,
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('./components/management/Login.vue'),
    },
    {
        path: '/LargeScreenDisplay',
        name: 'LargeScreenDisplay',
        component: () => import('./components/LargeScreenDisplay.vue')
    }
];
const router = new VueRouter({
    mode: 'history',
    routes
});
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        const isAuthenticated = checkAuth(); // 检查用户是否已登录
        if (!isAuthenticated) {
            next({
                path: '/login',
                query: {redirect: to.fullPath} // 将要访问的路径保存在query参数中
            });
        } else {
            next();
        }
    } else {
        next();
    }
});
export default router;