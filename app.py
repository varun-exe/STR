from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = ""
# app.config['SECRET_KEY'] = 'super secret key'
# db = SQLAlchemy(app)


# class Users(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), nullable=False, Unique=True)
#     password = db.Column(db.String(200), nullable=False)


# class General(db.Model):

#     id = db
#     name = db.Column(db.String(100))
#     gender = db.Column(db.String(100))
#     nationality = db.Column(db.String(100))
#     religion = db.Column(db.String(100))
#     fname = db.Column(db.String(100))
#     foccupation = db.Column(db.String(100))
#     foffice = db.Column(db.String(200))
#     femail = db.Column(db.String(100))
#     fmobile = db.Column(db.String(20))
#     mname = db.Column(db.String(100))
#     moccupation = db.Column(db.String(100))
#     moffice = db.Column(db.String(200))
#     memail = db.Column(db.String(100))
#     mmobile = db.Column(db.String(20))
#     permanent_address = db.Column(db.String(200))
#     bro_sis = db.Column(db.String(300))




@app.route("/")
def index():
    return "hello world"


@app.route("/editform", methods=['POST'])
def editform():
    return f'{ request.form.getlist("test") }'
    


@app.route("/general")
def general():
    return render_template("general.html", givenvar="test name")


@app.route("/semester<int:semester_number>")
def semester(semester_number):
    return render_template("semester.html")


@app.route("/testform")
def testform():
    
    return render_template("testform.html")