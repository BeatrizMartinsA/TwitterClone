<template>
  <v-list two-line>
    <template v-for="(tweet, index) in sortedTweets">
      <v-divider
        v-if="tweet.divider"
        :key="index"
        :inset="tweet.inset"
      />

      <v-list-item
        v-else
        :key="tweet.author_name"
      >
        <v-list-item-avatar>
          <v-img :src="tweet.avatar" />
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>
            <router-link style="text-decoration: none;" :to="{name: 'user', params: {username: tweet.author_username}}">
              {{tweet.author_name}}
            </router-link>
            {{tweet.author_username}}
            {{tweet.created_at | timeago}}
          </v-list-item-title>
          <v-list-item-subtitle v-html="tweet.text" />
        </v-list-item-content>
      </v-list-item>
      <v-divider :key="index" />
    </template>
  </v-list>
</template>

<script>
export default {
  props: ['tweets'],
  data () {
    return {}
  },
  computed: {
    sortedTweets () {
      return this.tweets.concat().sort((t1, t2) => new Date(t2.created_at) - new Date(t1.created_at))
    }
  }
}
</script>

<style>
</style>
