<template>
  <div id="app">
    <div
      class="d-flex flex-column flex-md-row align-items-center
      p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm"
    >
      <h5 @click="goHome" class="my-0 mr-md-auto font-weight-normal">PyText</h5>
      <a class="btn btn-outline-primary" href="#/new">New Text</a>
    </div>
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
import router from './router';

export default {
  name: 'App',
  methods: {
    goHome() {
      router.push({ name: 'TextList' });
    },
  },
};
</script>

<style>
header {
  height: 60px;
}
tr, h5 {
  cursor: pointer;
  background: white;
}
.striped tr:nth-child(2n) {
  filter: brightness(95%)
}
.hover tr:hover {
  filter: brightness(85%)
}
.hover thead tr:hover {
  filter: brightness(100%)
}
</style>
