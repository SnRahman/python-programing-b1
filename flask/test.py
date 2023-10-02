from flask import Flask, redirect ,url_for

import flask
from flask import Flask


app = Flask(__name__)


# create route
@app.route('/')
def home():
   return 'hello world!'


@app.route('/show')
def show():
   return 'hello Flask!'

# second method to create route
def index_function():
   return '<h1> This is index page </h1>'
app.add_url_rule('/index','index', index_function)


# pass variable through route
@app.route('/name/<name>')
def display_name(name):
   return f" Name is : {name}"


# pass variable of specific data type
@app.route('/age/<int:age>')
def display_age(age):
   return f" Age is : {age}"


# route example
@app.route('/python/')
def python():
   return 'this is python'

# redirect

@app.route('/google')
def redirect_google():
   return redirect('https://www.google.com')

# redirect example
@app.route('/display/<fuc_name>/<value>')
def display(fuc_name,value):
    if(fuc_name == 'name'):
      return redirect(f'http://127.0.0.1:5000/name/{value}')
    
    if(fuc_name == 'age'):
      return redirect(f'http://127.0.0.1:5000/age/{value}')


# redirect to a url using function name (url_for)

# redirect example
@app.route('/url/<fuc_name>/<value>')
def display_url(fuc_name,value):
    if(fuc_name == 'show'):
      return flask.redirect(url_for('show'))
    
    if(fuc_name == 'age'):
      return redirect(url_for('display_age',age=value))


if __name__ == '__main__':
   # auto restart the server after any change
   app.debug = True

   # run the app server
   app.run()
