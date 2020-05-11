<template>
  <div>
    <h2>{{text.title}}</h2>
    <table class="table striped hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Content</th>
        </tr>
      </thead>
      <tbody>
        <tr @click="showRelated(item)" v-for="(item, index) in sentences" :key="item.id">
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ item.content }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import router from '../router';
import { fetchSentences, fetchText } from '../api';

export default {
  name: 'TextItem',
  data() {
    return {
      sentences: [],
      text: {},
    };
  },
  methods: {
    showRelated(sentence) {
      router.push({
        name: 'RelatedSentences',
        params: {
          text_id: this.$route.params.text_id,
          sentence_id: sentence.id,
        },
      });
    },
  },
  created() {
    const textId = this.$route.params.text_id;

    fetchText(textId).then((text) => {
      this.text = text;
    });

    fetchSentences(textId).then((list) => {
      this.sentences = list;
    });
  },
};
</script>


<style scoped>
h2 {
  margin-bottom: 35px;
}
</style>
