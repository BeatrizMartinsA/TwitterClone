const d = new Date()
const _1min = 60000
const _1h = 60 * _1min
const d1 = new Date(d - 15 * _1min)
const d2 = new Date(d - 2 * _1h)
const d3 = new Date(d - 48 * _1h)

export const tweets = {
  tweets: [
    {
      avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
      author_name: 'Vitor',
      author_username: '@vitor',
      created_at: d1.toISOString(),
      text: `I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`
    },
    {
      avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
      author_name: 'Osvaldo',
      author_username: '@osvaldo',
      created_at: d2.toISOString(),
      text: `Wish I could come, but I'm out of town this weekend.`
    },
    {
      avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
      author_name: 'Bia',
      author_username: '@bia',
      created_at: d3.toISOString(),
      text: 'Do you have Paris recommendations? Have you ever been?'
    }
  ]
}
