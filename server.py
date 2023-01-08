from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "eml": request.form['eml']
    }
    User.save(data)
    return redirect('/display_user')


@app.route('/display_user')
def display_user():
    users = User.get_all()
    print(users)
    return render_template('display_user.html', all_users=users)


if __name__ == "__main__":
    app.run(debug=True)
