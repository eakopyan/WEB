//https://openclassrooms.com/courses/des-applications-ultra-rapides-avec-node-js/le-framework-express-js

const http = require('http')

var express = require('express')
var app = express()

/* Premiere approche
http.createServer( function (req, res) {
  console.log('${req.method} ${req.url}')
  res.end('Ceci n\'est pas une page web.')
}).listen(3000)

console.log('Le serveur est sur le port 3000.')
*/

app.get('/', function (req, res) {
  res.setHeader('Content-Type', 'text/plain')
  res.send('Voici l\'accueil. Essayez de retrouver les autres pages !')
})

app.get('/truth', function (req, res) {
  res.send('42')
})

app.get('/projet/:id', function(req, res) {
//  res.end('Voici le projet no'+ req.params.id)
  res.render('index.ejs', {identifiant: req.params.id})
  injectUser = function(req, res, next) {
      projectCollection.findOne({"_id": new mongo.ObjectID(req.params.id)}, function(err, result) {
        if (err || result === null) {
          return res.status(404).send("Pas d'utilisateur");
        } else {
          req.user = result;
          next();
        }
      });
    }
})

app.get('/index', function(req, res) {
})

app.use(function(req, res, next) {
  res.status(404).send('Page introuvable !')
})

app.listen(3000)
console.log('Le serveur est sur le port 3000.')
