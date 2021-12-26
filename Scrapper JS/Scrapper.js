const request = require('request')
request('https://br.ifunny.co/page10', function (
  error,
  response,
  body
) {
  console.error('error:', error)
  console.log('body:', body)
})
