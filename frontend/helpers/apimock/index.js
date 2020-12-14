import { zuck } from './db_people'
import { todos } from './db_todos'
import { tweets } from './db_tweets'
import { mockasync } from './mockutils'

const keepLoggedIn = true

export default {
  login (username, password) {
    return mockasync(zuck)
  },
  logout () {
    return mockasync({})
  },
  whoami () {
    const iam = {authenticated: keepLoggedIn}
    if (iam.authenticated) {
      iam.user = zuck
    }
    return mockasync(iam)
  },
  settings () {
    return mockasync({
      SENTRY_DSN_FRONT: ''
      // SENTRY_DSN_FRONT: 'https://abcd1234@sentry.example.com/10'
    })
  },
  list_todos () {
    return mockasync(todos)
  },
  add_todo (newtask) {
    return mockasync({description: newtask, done: false})
  },
  list_tweets (username) {
    return mockasync(tweets)
  },
  get_user_details (username) {
    const avatar = {
      '@vitor': 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
      '@osvaldo': 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
      '@bia': 'https://cdn.vuetifyjs.com/images/lists/3.jpg'
    }[username]
    return mockasync({
      username,
      avatar,
      description: 'penso, logo existo',
      ifollow: false
    })
  },
  follow (username) {
    return mockasync()
  },
  unfollow (username) {
    return mockasync()
  },
  tweet (text) {
    const d = new Date()
    const _1min = 60000
    const d1 = new Date(d - 15 * _1min)
    return mockasync({
      avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
      author_name: 'Vitor',
      author_username: zuck.username,
      created_at: d1.toISOString(),
      text
    })
  },
  signup (username, firstname, lastname, email, password) {
    return mockasync(zuck)
  }
}
