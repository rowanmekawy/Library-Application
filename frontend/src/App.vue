<template>
  <v-app>
    <BookList />
  </v-app>
</template>

<script>
import BookList from './components/BookList.vue';

export default {
  name: 'App',
  components: {
    BookList,
  },
};
</script>
