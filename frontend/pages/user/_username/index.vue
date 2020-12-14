<template>
  <viewuser :user="user" :tweets="tweets" />
</template>

<script>
import viewuser from '~/components/ViewUser.vue'
import api from '~api'

export default {
  components: {
    viewuser
  },
  data () {
    return {
      tweets: []
    }
  },
  asyncData (context) {
    const username = context.params.username
    return Promise.all([
      api.get_user_details(username),
      api.list_tweets(username)
    ]).then(results => {
      return {
        user: results[0],
        tweets: results[1].tweets
      }
    })
  }
}
</script>

<style>
</style>
