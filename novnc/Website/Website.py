from flask import Flask, render_template

# program is the name of the app i cant think of any names lmfao
program = Flask(__name__)


# assigning a url to program
@program.route('/')
def index():
    # template for the website
    return render_template("login.html")


# if this file is the main file, do this
if __name__ == '__main__':
    program.run(debug=True)
