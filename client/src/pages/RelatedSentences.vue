<template>
  <div>
    <a @click="backToSentence" href="#">Back to Sentence</a>
    <h2>Related Sentences</h2>
    <table class="table striped hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Content</th>
          <th scope="col">Text Title</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in relatedList" :key="item.id">
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ item.content }}</td>
          <td>comming soon..</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import router from '../router';
import { fetchRelatedSentences } from '../api';

export default {
  name: 'RelatedSentences',
  data() {
    return {
      relatedList: [],
    };
  },
  methods: {
    backToSentence() {
      router.back();
    },
  },
  created() {
    // eslint-disable-next-line camelcase
    const { text_id, sentence_id } = this.$route.params;

    fetchRelatedSentences(text_id, sentence_id).then((relatedList) => {
      this.relatedList = relatedList;
    });
  },
};
</script>

<style scoped>
a {
  margin-bottom: 5px;
  display: inline-block;
}
h2 {margin-bottom:35px;}
</style>
