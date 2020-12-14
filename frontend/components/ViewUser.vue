<template>
  <div>
    <usercard :user="user" />
    <timeline :tweets="tweets" />
  </div>
</template>

<script>

import timeline from '~/components/Timeline.vue'
import usercard from '~/components/UserCard.vue'

export default {
  components: {
    timeline,
    usercard
  },
  props: ['user', 'tweets'],
  data () {
    return {}
  }
}
</script>

<style>
</style>
