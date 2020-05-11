import Vue from 'vue';
import Router from 'vue-router';

import TextList from '@/pages/TextList';
import NewTextItem from '@/pages/NewTextItem';
import TextItem from '@/pages/TextItem';
import RelatedSentences from '@/pages/RelatedSentences';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'TextList',
      component: TextList,
    },
    {
      path: '/new',
      name: 'NewTextItem',
      component: NewTextItem,
    },
    {
      path: '/:text_id',
      name: 'TextItem',
      component: TextItem,
    },
    {
      path: '/:text_id/:sentence_id',
      name: 'RelatedSentences',
      component: RelatedSentences,
    },
  ],
});
