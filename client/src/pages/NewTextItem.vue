<template>
  <form>
    <div class="form-group">
      <label for="text-title">Text Title</label>
      <input v-model="title" type="text" class="form-control" id="text-title" />
    </div>
    <div class="form-group">
      <label for="text-content">Text Content</label>
      <textarea
        v-model="content"
        rows="10"
        type="text"
        class="form-control"
        id="text-content"
      />
    </div>
    <button
      :disabled="!title || !content"
      type="submit"
      v-on:click="submit"
      class="btn btn-primary"
    >Save</button>
  </form>
</template>

<script>
import { addText } from '../api';

export default {
  name: 'NewTextItem',
  data() {
    return {
      title: '',
      content: '',
    };
  },
  methods: {
    async submit() {
      await addText({ title: this.title, content: this.content });
    },
  },
};
</script>
