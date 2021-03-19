from flask import Flask, render_template, request, redirect

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
            if len(username) <= 4:
                return 'username has to be 5 or more characters'
            with open('usernames.txt', 'r') as content:
                if username in content.read():
                    return render_template('vnc.html')
                else:
                    return error

        elif request.form.get('Register'):
            # Gets the username from the input box
            username = request.form.get('regUsername')
            error = 'ERROR USERNAME ALREADY REGISTERED'
            if len(username) <= 4:
                return 'username has to be 5 characters or more.'
            with open('usernames.txt', 'a+') as content:
                if username in content.read():
                    return error
                else:
                    content.write(username + '\n')
                    return render_template('login.html')

    return render_template("login.html")


if __name__ == '__main__':
    program.run(debug=True)
