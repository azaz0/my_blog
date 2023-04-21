import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home.vue'


Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
            beforeEnter: (to, from, next) => {
                axios.get('/api/posts/')
                    .then(response => {
                        next({props: {posts: response.data}});
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
        }
        // {
        //     path: '/posts',
        //     name: 'posts',
        //     component: Posts,
        //     beforeEnter: (to, from, next) => {
        //         axios.get('/api/posts/')
        //             .then(response => {
        //                 next({props: {posts: response.data}});
        //             })
        //             .catch(error => {
        //                 console.log(error);
        //             });
        //     }
        // },
        // {
        //     path: '/posts/:id',
        //     name: 'post',
        //     component: Post,
        //     beforeEnter: (to, from, next) => {
        //         axios.get('/api/posts/' + to.params.id)
        //             .then(response => {
        //                 next({props: {post: response.data}});
        //             })
        //             .catch(error => {
        //                 console.log(error);
        //             });
        //     }
        // },
        // {
        //     path: '/categories',
        //     name: 'categories',
        //     component: Categories
        // },
        // {
        //     path: '/authors',
        //     name: 'authors',
        //     component: Authors
        // },
        // {
        //     path: '/authors/:id',
        //     name: 'author',
        //     component: Author
        // },
        // {
        //     path: '/tags',
        //     name: 'tags',
        //     component: Tags
        // }
    ]
})

export default router
