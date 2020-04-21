var config = require('config')
var express = require('express')
var app = express()
var data = require ('./public/widgets.json')

app.set('port', (process.env.PORT || 5000))
app.use(express.static(__dirname + '/public'))

app.get('/', function(request, response) {
  response.send('<b>Hello World! My Name is = <em>' + process.env.MYNAME + '</em <br/> My Node Environment is:' + config.util.getEnv('NODE_ENV')+'</em> <br> API available at ' + ("<a href='/api'>/api</a>") + '</b>')
})

app.get('/api', function(request, response) {
  response.send(JSON.stringify(data))
})
app.get('/env',function(request, response) {
  if (config.util.getEnv("NODE_ENV")==="Testing"){
    response.send('<b>You are working in the <em>TEST</em> environment.</b>')
  }
  else if (config.util.getEnv("NODE_ENV")==="HerokuTest"){
    response.send('<b>You are working in the <em>TEST</em> environment that is in Heroku.</b>')
  }
  if (config.util.getEnv("NODE_ENV")==="Production"){
      response.send('<b>You are working in Production')
  }
  else {
    response.send('<b>environment is unknown</b>')
}
})
app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})
