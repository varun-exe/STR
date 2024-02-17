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

    def __repr__(self):
        return f"{self.id} {self.email}"
    

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

    def __repr__(self):
        return f"{self.user_id} {self.name}"



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
        
        if user and user.password == password:
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
        general_info = General.query.filter_by(user_id=session["user_id"]).first()
        print("*" * 10)
        print(general_info)
        print("*" * 10)
        return render_template("general.html", general=general_info)


@app.route("/semester<int:semester_number>", methods=['GET', 'POST'])
def semester(semester_number):

    if request.method == 'POST':
        #TODO
        pass
    else:
        return render_template("semester.html")
    


@app.route("/general-edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        name = request.form.get('name')
        gender = request.form.get('gender')
        nationality = request.form.get('nationality')
        religion = request.form.get('religion')
        fname = request.form.get('fname')
        foccupation = request.form.get('f-occupation')
        foffice = request.form.get('f-office-address')
        femail = request.form.get('f-email')
        fnum = request.form.get('f-num')
        mname = request.form.get('m-name')
        moccupation = request.form.get('m-occupation')
        moffice = request.form.get('m-address')
        memail = request.form.get('m-email')
        mnum = request.form.get('m-number')
        address = request.form.get('permanent-address')
        bro_sis = request.form.get('bro-sis')

        general_info = General(user_id=session['user_id'], name=name,
                               gender=gender, nationality=nationality, religion=religion,
                               fname=fname, foccupation=foccupation, foffice=foffice, femail=femail,
                               fmobile=fnum, mname=mname, moccupation=moccupation, moffice=moffice,
                               memail=memail, mmobile=mnum, permanent_address=address, bro_sis=bro_sis)
        
        to_be_deleted = General.query.filter_by(user_id=session['user_id']).first()
        db.session.delete(to_be_deleted)
        db.session.add(general_info)
        db.session.commit()

        return redirect("/general")
    else:
        general_info = General.query.filter_by(user_id=session["user_id"]).first()
        return render_template("general-edit.html", general=general_info)



@app.route("/dummy")
def dummy():
    test = None
    return render_template("dummy.html", test=test)