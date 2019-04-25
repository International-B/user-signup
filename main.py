from flask import Flask, request, redirect, render_template
import os, jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_temps = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    template = jinja_temps.get_template('index-file.html')
    return render_template('index-file.html')


@app.route('/2', methods=['POST'])
def validation():
    template = jinja_temps.get_template('index-file.html')

    #username
    username = request.form['username']
    unerror = ""
    if not username:
        unerror = "Please enter a username."
    if len(username) < 3 or len(username) > 20:
        unerror = "Choose a username between 3 and 20 characters."
    if " " in username:
        unerror = "Please remove spaces from the username."

    #password
    password = request.form['password']
    pwerror = ""
    if not password:
        pwerror = "Please enter a password"
    if len(password) < 3 or len(password) > 20:
        pwerror = "Choose a password between 3 and 20 characters."
    if " " in password:
        pwerror = "Please remove spaces from the password."

    #PW Confirm
    pw_match =""
    pw_confirm = request.form['pw_confirm']
    if not pw_confirm:
        pw_match = "Confirm your password."
    if pw_confirm != password:
        pw_match = "Passwords do not match, try again."

    #Validate Email
    email = request.form['email']
    email_error = ""
    if email != "":
        if " " in email: 
            email_error ="Please enter a valid email address."
        if "@" not in email:
            email_error = "Please enter a valid email address."
        if "." not in email:
            email_error = "Please enter a valid email address."
        if len(email) < 3 or len(email) > 40:
            email_error = "Your email is too short/long for me."

    
    if email_error != "" or pw_match != "" or pwerror != "" or unerror != "":
        return template.render(email_error=email_error, pw_match=pw_match, pwerror=pwerror, unerror=unerror, username=username, email=email)
    else:
        template = jinja_temps.get_template('welcomepage.html')
        return template.render(username=username)



if __name__ == '__main__':
    app.run()