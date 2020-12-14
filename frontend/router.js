import Vue from 'vue'
import Router from 'vue-router'
import Index from '~/pages/index.vue'
import Todos from '~/pages/todos.vue'
import Perfil from '~/pages/perfil.vue'
import User from '~/pages/user/_username/index.vue'
import Timeline from '~/pages/timeline.vue'
import Fotos from '~/pages/fotos.vue'

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  routes: [
    {path: '/', component: Index, name: 'index'},
    {path: '/todos', component: Todos, name: 'todos'},
    {path: '/perfil', component: Perfil, name: 'perfil'},
    {path: '/user/:username?', component: User, name: 'user'},
    {path: '/timeline', component: Timeline, name: 'timeline'},
    {path: '/fotos', component: Fotos, name: 'fotos'}
  ]
}

export function createRouter (ctx) {
  return new Router(routerOptions)
}
