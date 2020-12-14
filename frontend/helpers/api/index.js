import {get, post} from './ajaxutils'

export default {
  login (username, password) {
    return post('/api/login', {username, password})
  },
  logout () {
    return post('/api/logout')
  },
  whoami () {
    return get('/api/whoami')
  },
  settings () {
    return get('/api/settings')
  },
  list_todos () {
    return get('/api/list_todos')
  },
  add_todo (newtask) {
    return post('/api/add_todo', {new_task: newtask})
  },
  list_tweets (username) {
    return get('/api/list_tweets', {username})
  },
  get_user_details (username) {
    return get('/api/get_user_details', {username})
  },
  follow (username) {
    return post('/api/follow', {username})
  },
  unfollow (username) {
    return post('/api/unfollow', {username})
  },
  tweet (text) {
    return post('/api/tweet', {text})
  },
  signup (username, firstname, lastname, email, password) {
    return post('/api/signup', {username, first_name: firstname, last_name: lastname, email, password})
  }
}
