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
            error = "ERROR USERNAME IS NOT REGISTERED"
            # if username from input box is in the text file 'usernames.txt'
            with open("usernames.txt", "r") as txtFile:
                for line in txtFile:
                    if re.search(username, line):
                        return render_template('vnc.html')
                    else:
                        return error
        elif request.form.get('Register'):
            # Gets the username from the input box
            username = request.form.get('regUsername')
            error = 'ERROR USERNAME ALREADY REGISTERED'
            print(username)
            with open("usernames.txt", "r") as txtFile:
                for line in txtFile:
                    if re.search(username, line):
                        return error
                    else:
                        regUserA = open('usernames.txt', 'a')
                        regUserA.write(username + '\n')
                        return render_template('login.html')

    return render_template("login.html")


if __name__ == '__main__':
    program.run(debug=True)
