<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="success"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Cadastre-se
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          Cadastro
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="firstname"
                  label="First name*"
                  :error-messages="firstnameErrors"
                  :counter="30"
                  required
                  @input="$v.firstname.$touch()"
                  @blur="$v.firstname.$touch()"
                />
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="lastname"
                  label=" Last name*"
                  :error-messages="lastnameErrors"
                  :counter="30"
                  required
                  @input="$v.lastname.$touch()"
                  @blur="$v.lastname.$touch()"
                />
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="username"
                  label=" Username*"
                  :error-messages="usernameErrors"
                  :counter="20"
                  required
                  @input="$v.username.$touch()"
                  @blur="$v.username.$touch()"
                />
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="email"
                  :error-messages="emailErrors"
                  label="Email*"
                  required
                  @input="$v.email.$touch()"
                  @blur="$v.email.$touch()"
                />
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="password"
                  :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                  :error-messages="passwordErrors"
                  :type="show ? 'text' : 'password'"
                  label="Password*"
                  required
                  :counter="15"
                  @click:append="show = !show"
                  @change="$v.password.$touch()"
                  @blur="$v.password.$touch()"
                />
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn
            color="blue darken-1"
            text
            @click="close"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="clear"
          >
            Clear
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="save"
            :loading="loading" :disabled="loading"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, maxLength, minLength, email } from 'vuelidate/lib/validators'
import api from '~api'

export default {
  mixins: [validationMixin],

  validations: {
    firstname: { required, maxLength: maxLength(30) },
    lastname: { required, maxLength: maxLength(30) },
    username: { required, maxLength: maxLength(20) },
    email: { required, email },
    password: { required, maxLength: maxLength(15), minLength: minLength(8), emailMatch: () => (`The email and password you entered don't match`) }
  },
  data () {
    return {
      dialog: false,
      firstname: '',
      lastname: '',
      username: '',
      email: '',
      password: '',
      show: false,
      loading: false,
      error: false
    }
  },
  computed: {
    firstnameErrors () {
      const errors = []
      if (!this.$v.firstname.$dirty) { return errors }
      !this.$v.firstname.maxLength && errors.push('Must be at most 30 characters long')
      !this.$v.firstname.required && errors.push('Field is required.')
      return errors
    },
    lastnameErrors () {
      const errors = []
      if (!this.$v.lastname.$dirty) { return errors }
      !this.$v.lastname.maxLength && errors.push('Must be at most 30 characters long')
      !this.$v.lastname.required && errors.push('Field is required.')
      return errors
    },
    usernameErrors () {
      const errors = []
      if (!this.$v.username.$dirty) { return errors }
      !this.$v.username.maxLength && errors.push('Must be at most 20 characters long')
      !this.$v.username.required && errors.push('Field is required.')
      return errors
    },
    emailErrors () {
      const errors = []
      if (!this.$v.email.$dirty) { return errors }
      !this.$v.email.email && errors.push('Must be valid e-mail')
      !this.$v.email.required && errors.push('Field is required')
      return errors
    },
    passwordErrors () {
      const errors = []
      if (!this.$v.password.$dirty) { return errors }
      !this.$v.password.minLength && errors.push('Password must be at a minimun of 8 characters long')
      !this.$v.password.maxLength && errors.push('Password must be at most 15 characters long')
      !this.$v.password.required && errors.push('Password is required.')
      return errors
    }
  },
  methods: {
    clear () {
      this.$v.$reset()
      this.firstname = ''
      this.lastname = ''
      this.username = ''
      this.email = ''
      this.password = ''
    },
    async save () {
      this.loading = true
      await api.signup(this.username, this.firstname, this.lastname, this.email, this.password)
      const user = await api.login(this.username, this.password)
      if (user) {
        this.$store.commit('auth/setCurrentUser', user)
        this.loading = false
        this.dialog = false
        this.$router.push({ name: 'timeline' })
      } else {
        this.error = true
        this.loading = false
      }
    },
    close () {
      this.clear()
      this.dialog = false
    }
  }
}
</script>

<style>
</style>
