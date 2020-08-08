import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import ImageClassifier from '@/components/ImageClassifier'
import SoundClassifier from '@/components/SoundClassifier'
import PoseClassifier from '@/components/PoseClassifier'

import Helloworld from '@/components/test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
      meta: {
        title: 'HomePage'
      }
    },
    {
      path: '/test',
      name: 'test',
      component: Helloworld,
      meta: {
        title: 'test'
      }
    },
    {
      path: '/ImageClassifier',
      name: 'ImageClassifier',
      component: ImageClassifier
    },
    {
      path: '/SoundClassifier',
      name: 'SoundClassifier',
      component: SoundClassifier
    },
    {
      path: '/PoseClassifier',
      name: 'PoseClassifier',
      component: PoseClassifier
    }
  ],
  mode: 'history'
})
