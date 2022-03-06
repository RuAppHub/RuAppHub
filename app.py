from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from flask_login import UserMixin
from models import *


app = Flask(__name__)

#Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ksadjfk213kjfw8ejq3u8jf78342hrjskljfsdafqaakajfkljk3984jlkfzjdfklu4irbvjh87eryt[ihskdnfgkjahq3984tyqu'
db = SQLAlchemy(app)

# инициализация логин менеджера
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'




#ОБРАБОТЧИКИ

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#Обработчик главной страницы
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app/<surname>')
def get_app(surname):
    pass

#Обработчики логина/Регистрации
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('user')
    password = request.form.get('pass')

    if login and password:
        user = User.query.filter_by(username=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            return redirect('/')

        else:
            flash('Не верны Логин/Пароль')
    else:
        pass
    return render_template('login.html', filename='css/styles.css')


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('user')
    password = request.form.get('pass')
    password2 = request.form.get('pass2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Пожалуйста, заполните все поля!')
        elif login == '':
            flash('Пожалуйста, заполните все поля!')
        elif password != password2:
            flash('Пароли не совпадают!')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(username=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login_page'))

    return render_template('register.html')

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login_page'))
    

if __name__ == '__main__':
    app.run(debug=True, port=80, host='localhost')