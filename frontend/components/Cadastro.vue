<template>
  <div>
    <!-- <v-layout justify-center align-center>
      <v-btn color="success" v-if="!logged_user" @click="signup">
        Cadastre-se
      </v-btn>
    </v-layout> -->
    <form-area-dialog ref="signupdialog" />
  </div>
</template>

<script>
import FormAreaDialog from '~/components/FormAreaDialog.vue'

export default {
  components: {
    FormAreaDialog
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
    signup () {
      return this.$refs.signupdialog.open()
    }
  }
}
</script>

<style>
</style>
