<template>
  <table class="table striped hover">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Title</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in textList" :key="item.id">
        <th scope="row">{{item.id}}</th>
        <td>{{item.title}}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { fetchTextList } from '../api';

export default {
  name: 'TextList',
  data() {
    return {
      textList: [],
    };
  },
  created() {
    fetchTextList().then((list) => {
      this.textList = list;
    });
  },
};
</script>
