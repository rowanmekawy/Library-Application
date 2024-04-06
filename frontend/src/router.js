import { createRouter, createWebHistory } from 'vue-router';
import BookList from './components/BookList.vue';

const routes = [
    {
      path: '/BookList',
      name: 'BookList',
      component: { template: '<div>This is a test route.</div>' },
    },
    // other routes...
  ];
  

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
