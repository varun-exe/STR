from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

    def __repr__(self):
        return f"{self.record}"




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
        return render_template("general.html", general=general_info)


@app.route("/semester<int:semester_number>", methods=['GET', 'POST'])
def semester(semester_number):

    if request.method == 'POST':
        pass
    else:
        attendance_records = Attendance.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        iat_records = Iat.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        event_records = Event.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        mooc_records = Mooc.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        project_records = Project.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        counselling_records = Counselling.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        
        return render_template("semester.html", 
                               semester_number=semester_number,
                               attendance_records=attendance_records,
                               iat_records=iat_records,
                               event_records=event_records,
                               mooc_records=mooc_records,
                               project_records=project_records,
                               counselling_records=counselling_records)
    



@app.route("/semester<int:semester_number>-edit", methods=['GET', 'POST'])
def edit_semester(semester_number):
    if request.method == 'POST':
        attendance_rows = int(request.form.get('attendance-rows'))
        iat_rows = int(request.form.get('iat-rows'))
        event_rows = int(request.form.get('events-rows'))
        mooc_rows = int(request.form.get('mooc-rows'))
        project_rows = int(request.form.get('project-rows'))
        counselling_rows = int(request.form.get('counselling-rows'))


        prev_attendance = Attendance.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        if prev_attendance:
            for rec in prev_attendance:
                db.session.delete(rec)


        prev_iat = Iat.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        if prev_iat:
            for rec in prev_iat:
                db.session.delete(rec)

        
        prev_event = Event.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        if prev_event:
            for rec in prev_event:
                db.session.delete(rec)


        prev_mooc = Mooc.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        if prev_mooc:
            for rec in prev_mooc:
                db.session.delete(rec)

        
        prev_project = Project.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        if prev_project:
            for rec in prev_project:
                db.session.delete(rec)


        prev_counselling = Counselling.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        if prev_counselling:
            for rec in prev_counselling:
                db.session.delete(rec)


        db.session.commit()

        # for i in range(attendance_rows):
        #     code = request.form.get(f"attendance-row{i + 1}-code")
        #     subject = request.form.get(f"attendance-row{i + 1}-subject")
        #     t1 = request.form.get(f"attendance-row{i + 1}-T1")
        #     a1 = request.form.get(f"attendance-row{i + 1}-A1")
        #     t2 = request.form.get(f"attendance-row{i + 1}-T2")
        #     a2 = request.form.get(f"attendance-row{i + 1}-A2")
        #     t3 = request.form.get(f"attendance-row{i + 1}-T3")
        #     a3 = request.form.get(f"attendance-row{i + 1}-A3")

        #     record = Attendance(user_id=session['user_id'], code=code,
        #                         subject=subject, t1=t1, a1=a1, t2=t2, a2=a2, 
        #                         t3=t3, a3=a3, semester=semester_number)
            
        #     db.session.add(record)



        # for i in range(iat_rows):
        #     code = request.form.get(f"iat-row{i + 1}-code")
        #     subject = request.form.get(f"iat-row{i + 1}-subject")
        #     max = request.form.get(f"iat-row{i + 1}-max")
        #     iat1 = request.form.get(f"iat-row{i + 1}-iat1")
        #     iat2 = request.form.get(f"iat-row{i + 1}-iat2")
        #     iat3 = request.form.get(f"iat-row{i + 1}-iat3")

        #     record = Iat(user_id=session['user_id'], code=code, subject=subject,
        #                  max=max, iat1=iat1, iat2=iat2, iat3=iat3, semester=semester_number)
            
        #     db.session.add(record)


        # for i in range(event_rows):
        #     name = request.form.get(f"events-row{i + 1}-name")
        #     title = request.form.get(f"events-row{i + 1}-title")
        #     date = request.form.get(f"events-row{i + 1}-date")

        #     record = Event(user_id=session['user_id'], club_name=name, 
        #                    event_title=title, event_date=date, semester=semester_number)
            
        #     db.session.add(record)

        # for i in range(mooc_rows):
        #     under = request.form.get(f"mooc-row{i + 1}-under")
        #     title = request.form.get(f"mooc-row{i + 1}-title")
        #     start = request.form.get(f"mooc-row{i + 1}-start")
        #     completed = request.form.get(f"mooc-row{i + 1}-completed")
        #     score = request.form.get(f"mooc-row{i + 1}-score")

        #     record = Mooc(user_id=session['user_id'], under=under, title=title, 
        #                   start_date=start, completed_date=completed,
        #                     score=score, semester=semester_number)

        #     db.session.add(record)


        # for i in range(project_rows):
        #     title = request.form.get(f"project-row{i + 1}-title")
        #     hours = request.form.get(f"project-row{i + 1}-hours")
        #     start = request.form.get(f"project-row{i + 1}-start")
        #     completed = request.form.get(f"project-row{i + 1}-completed")

        #     record = Project(user_id=session['user_id'], title=title, man_hours=hours,
        #                      start_date=start, completed_date=completed, semester=semester_number)
            
        #     db.session.add(record)

        for i in range(counselling_rows):
            date = datetime.strptime(request.form.get(f"counselling-row{i + 1}-date"), "%Y-%m-%d").date()
            record = request.form.get(f"counselling-row{i + 1}-record")

            row = Counselling(user_id=session['user_id'], date=date, record=record, semester=semester_number)

            db.session.add(row)

        db.session.commit()

        return redirect(f"/semester{semester_number}")

    else:
        attendance_records = Attendance.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        iat_records = Iat.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        event_records = Event.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        mooc_records = Mooc.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        project_records = Project.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        counselling_records = Counselling.query.filter_by(user_id=session['user_id'], semester=semester_number).all()
        
        return render_template("semester-edit.html", 
                               attendance_records=attendance_records,
                               iat_records=iat_records,
                               event_records=event_records,
                               mooc_records=mooc_records,
                               project_records=project_records,
                               counselling_records=counselling_records)






@app.route("/general-edit", methods=['GET', 'POST'])
def edit_general():
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
        
        #delete existing record
        to_be_deleted = General.query.filter_by(user_id=session['user_id']).first()
        db.session.delete(to_be_deleted)

        #add new record
        db.session.add(general_info)
        db.session.commit()

        return redirect("/general")
    else:
        general_info = General.query.filter_by(user_id=session["user_id"]).first()
        return render_template("general-edit.html", general=general_info)


@app.route("/dummy", methods=['GET', 'POST'])
def dummy():
    if request.method == 'POST':
        print("*"*10)
        print(request.form.get('myname'))
        print("*"*10)
        return 'check terminal'
    else:
        return render_template("dummy.html")

        