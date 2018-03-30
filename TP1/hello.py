#IMPORTS:
#'request'  useful for HTTP GET requests
#'url_for'  useful for URL generation
#'redirect' useful for automatic URL changes
#'abort'    useful for sending error codes

from flask import Flask, request, url_for, redirect, abort
app = Flask(__name__)
app.logger.debug('Launching application...') #nothing appears unless debug mode activates

#Functions defined on path http://localhost:5000/ (main route)
@app.route('/')
def hey():
    app.logger.warning('Default route') #warning msg on terminal
    return 'It has changed!' #text that appears on the page

#Functions defined on path http://localhost:5000/excellence
@app.route('/excellence')
def excellence():
    app.logger.error('You are at INSA') #error msg on terminal
    return 'Standford'

#Functions defined on path http://localhost:5000/user/eako
@app.route('/user/<name>')
def user(name):
    return 'User: %s' % name #displays 'User: eako' in our case

#Functions defined on path http://localhost:5000/profile/42/backflip
@app.route('/profile/<int:uid>/<action>')
def profile(uid, action):
    return 'UID: %d / Action: %s' % (uid, action) #displays 'UID: 42 / Action: backflip'

#Creating an HTTP request-supporting path
@app.route('/plop', methods=['GET', 'POST'])
def plop():
    if request.method == 'GET': #'request' contains information about ongoing HTTP request
        return "This was an HTTP GET"
    else:
        return "This was an HTTP POST"

#This page displays the following existing routes
@app.route('/show-routes')
def show_routes():
    routes = ''
    with app.test_request_context():
        routes = routes + url_for('excellence') + '\n'
        routes = routes + url_for('plop') + '\n'
        routes = routes + url_for('excellence', aeres=True) + '\n'
        routes = routes + url_for('profile', uid = 706, action = 'save') + '\n'
    return routes

#this page automatically redirects to the Excellence page
@app.route('/vortex')
def vortex():
    return redirect(url_for('excellence', vortex=1)) #vortex=1 is proof of the redirection

#this page displays an Error message
@app.route('/fail')
def fail():
    abort(500) #code for an internal server error

#Error messages can be handled through the following process:
@app.errorhandler(500) #catches the following error code and modifies its behaviour
def internal_error(error):
    return 'Wooops!'

@app.errorhandler(404)
def not_found(error):
    return 'ERROR 404: RESPECT NOT FOUND'

if __name__ == '__main__':
    app.run(debug=True)
