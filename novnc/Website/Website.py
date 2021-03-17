from flask import Flask, render_template, request, redirect
import time

program = Flask(__name__)


# assigning a url to program

@program.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        authedR = open('usernames.txt', 'r')
        error = "ERROR USERNAME IS NOT REGISTERED"

        authorize = authedR.read()
        print(authorize)
        if username in authorize:
            return render_template('vnc.html')
            # Paste the url in here
            # return redirect("https://www.webnovnc.com", code=302)

        else:
            return error

    return render_template("login.html")


if __name__ == '__main__':
    program.run(debug=True)
