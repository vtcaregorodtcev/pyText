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
        <tr v-for="([sent, text], index) in relatedList" :key="index">
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ sent }}</td>
          <td><a href="javascript:void(0)" @click="goToText(text)">{{ text.title }}</a></td>
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
    goToText(text) {
      router.push({ name: 'TextItem', params: { text_id: text.id } });
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
h2 {
  margin-bottom: 35px;
}
tbody tr td:not(:first-child) {
  width: 40%;
}
</style>
