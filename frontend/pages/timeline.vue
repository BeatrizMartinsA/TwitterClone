/* eslint-disable indent */
/* eslint-disable no-debugger */
<template>
  <home :tweets="tweets" />
</template>

<script>

import home from '~/components/Home.vue'
import api from '~api'

export default {
  components: {
    home
  },
  data () {
    return {
    }
  },
  asyncData () {
    return api.list_tweets().then(result => {
      return {
        tweets: result.tweets
      }
    })
  }
}
</script>

<style>
</style>
