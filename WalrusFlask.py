from flask import Flask
from flask import url_for
from flask import render_template
app = Flask(__name__)

@app.route('/')
def Hworld():
    return ('INDEX')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def sprofile(username):
    return ('User %s' % username)

with app.test_request_context():
    print (url_for('hello'))
    print (url_for('sprofile', username='Joe King'))

app.run()
#app.run(host='0.0.0.0')
