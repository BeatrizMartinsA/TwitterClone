/* eslint-disable no-debugger */
<template>
  <div>
    <newtweet @newtweet="addToTimeline($event)" />
    <timeline :tweets="tweets" />
  </div>
</template>

<script>

import timeline from '~/components/Timeline.vue'
import newtweet from '~/components/NewTweet.vue'

export default {
  components: {
    timeline, newtweet
  },
  props: ['tweets'],
  data () {
    return {}
  },
  methods: {
    addToTimeline (tweet) {
      this.tweets.push(tweet)
    }
  }
}
</script>

<style>
</style>
