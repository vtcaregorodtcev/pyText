<template>
  <table class="table striped hover">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Title</th>
      </tr>
    </thead>
    <tbody>
      <tr @click="gotoItem(item)" v-for="(item, index) in textList" :key="item.id">
        <th scope="row">{{index + 1}}</th>
        <td>{{item.title}}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { fetchTextList } from '../api';
import router from '../router';

export default {
  name: 'TextList',
  data() {
    return {
      textList: [],
    };
  },
  methods: {
    gotoItem(item) {
      router.push({ name: 'TextItem', params: { text_id: item.id } });
    },
  },
  created() {
    fetchTextList().then((list) => {
      this.textList = list;
    });
  },
};
</script>
