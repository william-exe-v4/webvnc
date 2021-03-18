from flask import Flask, render_template, request, redirect
import re

program = Flask(__name__)


# assigning a url to program

@program.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # If the login button was pressed
        if request.form.get('Login'):
            # Gets username from the input box
            username = request.form.get('username')
            authedR = open('usernames.txt', 'r')
            error = "ERROR USERNAME IS NOT REGISTERED"
            authorize = authedR.read()
            # if username from input box is in the text file 'usernames.txt'
            if username in authorize:
                return render_template('vnc.html')
                # Paste the url in here
                # return redirect("https://www.webnovnc.com", code=302)
            else:
                return error
        elif request.form.get('Register'):
            # Gets the username from the input box
            username = request.form.get('regUsername')
            regUserWrite = open('usernames.txt', 'a')
            regUserRead = open('usernames.txt', 'r')
            a = regUserRead.read()
            error = "ERROR USERNAME IS ALREADY REGISTERED"
            if username in a:
                return error
            else:
                regUserWrite.write(username + '\n')
                return render_template('login.html')

    return render_template("login.html")


if __name__ == '__main__':
    program.run(debug=True)
