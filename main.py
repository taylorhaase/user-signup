from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_signup.html')


@app.route('/validate-signup', methods=['POST'])
def validate_inputs():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    for i in username:
        if i.isspace():
            username_error = 'Username must not contain spaces.'
        
        else:
            username = str(username)
            if len(username) < 3 or len(username) > 20:
                username_error = 'Username must be 3-20 characters'
    
  
    if not len(username):
        username_error = 'Not a valid username' 

    for i in password:
        if i.isspace():
            password_error = 'Password must not contain spaces.'
            password = ''
        else:
            password = str(password)
            if len(password) < 3 or len(password) > 20:
                password_error = 'Password must be 3-20 characters and not contain spaces.'
                password = ''
    if password != verify:
        verify_error = 'Passwords do not match'
        verify = ''
        password = ''
    
    if not len(password):
        password_error = 'Not a valid password'

    for i in email:
        if i.isspace():
            email_error = 'This is not a valid email'
            if len(email) < 3 or len(email) > 20:
                email_error = 'Email must be 3-20 characters'
        else:
            email = str(email)
            if "@" not in email:
                email_error = 'This is not a valid email'
   
            if "." not in email:
                email_error = 'This is not a valid email'

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome-page?username={0}'.format(username))
    else:
        return render_template('user_signup.html', username_error=username_error,
            password_error=password_error,
            verify_error=verify_error, email_error=email_error, 
            username=username, password=password,verify=verify, email=email)

@app.route('/welcome-page')
def welcome():
    username=request.args.get('username')
    return render_template('welcome_page.html', username=username)

app.run()