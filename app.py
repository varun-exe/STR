from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
app.config['SECRET_KEY'] = 'super secret key'
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    general_info = db.relationship('General', backref='user')
    attendance_info = db.relationship('Attendance', backref='user')
    iat_info = db.relationship('Iat', backref='user')
    event_info = db.relationship('Event', backref='user')
    mooc_info = db.relationship('Mooc', backref='user')
    project_info = db.relationship('Project', backref='user')
    counselling_info = db.relationship('Counselling', backref='user')


class General(db.Model):
    __tablename__ = 'general_information'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    nationality = db.Column(db.String(100))
    religion = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    foccupation = db.Column(db.String(100))
    foffice = db.Column(db.String(200))
    femail = db.Column(db.String(100))
    fmobile = db.Column(db.String(20))
    mname = db.Column(db.String(100))
    moccupation = db.Column(db.String(100))
    moffice = db.Column(db.String(200))
    memail = db.Column(db.String(100))
    mmobile = db.Column(db.String(20))
    permanent_address = db.Column(db.String(200))
    bro_sis = db.Column(db.String(300))



class Attendance(db.Model):
    __tablename__ = 'attendance_information'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    code = db.Column(db.String(10))
    subject = db.Column(db.String(50))
    t1 = db.Column(db.Integer)
    a1 = db.Column(db.Integer)
    t2 = db.Column(db.Integer)
    a2 = db.Column(db.Integer)
    t3 = db.Column(db.Integer)
    a3 = db.Column(db.Integer)
    semester = db.Column(db.Integer)



class Iat(db.Model):
    _tablename__ = 'iat_information'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    code = db.Column(db.String(10))
    subject = db.Column(db.String(50))
    max = db.Column(db.Integer)
    iat1 = db.Column(db.Integer)
    iat2 = db.Column(db.Integer)
    iat3 = db.Column(db.Integer)
    semester = db.Column(db.Integer)


class Event(db.Model):
    __tablename__ = 'events_information'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    club_name = db.Column(db.String(100))
    event_title = db.Column(db.String(200))
    event_date = db.Column(db.Date)
    semester = db.Column(db.Integer)



class Mooc(db.Model):
    __tablename__ = 'mooc_information'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    under = db.Column(db.String(100))
    title = db.Column(db.String(200))
    start_date = db.Column(db.Date)
    completed_date = db.Column(db.Date)
    score = db.Column(db.Integer)
    semester = db.Column(db.Integer)



class Project(db.Model):
    __tablename__ = 'project_information'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(200))
    man_hours = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    completed_date = db.Column(db.Date)
    semester = db.Column(db.Integer)


class Counselling(db.Model):
    __tablename__ = 'counselling_information'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.Date)
    record = db.Column(db.String(300))
    semester = db.Column(db.Integer)




@app.route("/")
def index():
    return "hello world"


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        existing_user = Users.query.filter_by(email=email).first()

        if existing_user is None:
            new_user = Users(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('login.html')
        else:
            # TODO
            return 'user already exists'
    else:
        return render_template("register.html")
        

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user = Users.query.filter_by(email=email).first()
        
        if user.password == password:
            session["user_id"] = user.id
            return redirect("/general")
        else:
            # TODO
            return 'wrong password or user doesnt exists'
    else:
        return render_template("login.html")
        


@app.route("/general", methods=['GET', 'POST'])
def general():
    if request.method == 'POST':
        # TODO
        pass
    else:
        General.query.filter_by(id=session["user_id"]).first()
        return render_template("general.html")


@app.route("/semester<int:semester_number>")
def semester(semester_number):
    return render_template("semester.html")


@app.route("/testform")
def testform():
    
    return render_template("testform.html")