<template>
  <v-flex>
    <v-card
      color="#385F73"
      dark
    >
      <v-card-title class="headline">
        {{user.username}}
      </v-card-title>
      <v-card-subtitle>{{user.description}}</v-card-subtitle>
      <v-avatar
        class="ma-3"
        size="125"
      >
        <v-img :src="'https://cdn.vuetifyjs.com/images/lists/1.jpg'" />
      </v-avatar>

      <v-card-actions>
        <v-btn v-if="show_follow" :loading="loading" color="success" @click="follow">
          Seguir
        </v-btn>
        <v-btn v-else-if="show_unfollow" :loading="loading" color="danger" @click="unfollow">
          Seguindo
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-flex>
</template>

<script>
import api from '~api'
import Snacks from '~/helpers/Snacks.js'

export default {
  props: ['user'],
  data () {
    return {
      loading: false
    }
  },
  computed: {
    logged_user () {
      return this.$store.getters['auth/loggedIn']
    },
    show_follow () {
      return this.logged_user && !this.user.ifollow
    },
    show_unfollow () {
      return this.logged_user && this.user.ifollow
    }
  },
  methods: {
    follow () {
      this.loading = true
      api.follow(this.user.username).then(() => {
        this.user.ifollow = true
        this.loading = false
        Snacks.show(this.$store, {
          text: 'Você está seguindo ' + this.user.username + '!'
        })
      })
    },
    unfollow () {
      this.loading = true
      api.unfollow(this.user.username).then(() => {
        this.user.ifollow = false
        this.loading = false
        Snacks.show(this.$store, {
          text: 'Você deixou de seguir ' + this.user.username + '.',
          color: 'error'
        })
      })
    }
  }
}

</script>
<style />
