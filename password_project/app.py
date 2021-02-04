from types import WrapperDescriptorType
from flask import Flask, render_template, redirect, session, url_for, request
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
db = SQLAlchemy(app)


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(), nullable = False)
    passw = db.Column(db.String(), nullable = False)


    def __repr__(self):
        return 'account' + str(self.id)

db.create_all()

@app.route('/')
def home():
    
    return render_template('index.html')
    #hashpash = bcrypt.hashpw(request.form['pass'], bcrypt.genSalt())

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_reg = request.form['username']
        passw_reg = request.form['password']
        new_user = UserInfo(user = user_reg, passw = passw_reg)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods = ['GET', 'POST'])
def loginpage():
    wrong_user = False
    if request.method == 'POST':
        user_input = request.form['username']
        passw_input = request.form['password']
        if UserInfo.query.filter_by(user = user_input).all() != []:
            if UserInfo.query.filter_by(passw = passw_input).all() == UserInfo.query.filter_by(user = user_input).all():
                wrong_user = False
                return redirect('/account')
                
            else:
                return redirect('/wrong')
        else:
            wrong_user = True
            return render_template('login.html', wrong_user = wrong_user)
            
    return render_template('login.html', wrong_user = wrong_user)

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/wrong')
def wrong():
    return render_template('wrong.html')


            
if __name__ == "__main__":
    app.run(debug=True)