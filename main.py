from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from flask_login import UserMixin
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=80, host='localhost')