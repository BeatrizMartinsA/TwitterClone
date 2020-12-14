<template>
  <div>
    <v-btn color="success" outlined rounded block v-if="logged_user" @click="gotweet">
      Novo Tweet
    </v-btn>
    <text-area-dialog ref="newtweetdialog" />
  </div>
</template>

<script>
import TextAreaDialog from '~/components/TextAreaDialog.vue'
import api from '~api'

export default {
  components: {
    TextAreaDialog
  },
  data () {
    return {}
  },
  computed: {
    logged_user () {
      return this.$store.getters['auth/loggedIn']
    }
  },
  methods: {
    gotweet () {
      return this.$refs.newtweetdialog.open({
        title: 'Novo tweet',
        label: 'Diga alguma coisa',
        value: '',
        action: 'Enviar',
        actionFunc: value => {
          return api.tweet(value).then(tweet => {
            this.$emit('newtweet', tweet)
          })
        }
      })
    }
  }
}
</script>

<style>
</style>
