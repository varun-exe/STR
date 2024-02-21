import re
from datetime import datetime
from flask import redirect, session
from functools import wraps

def validate(mandatory, optional_numbers):
    
    for word in mandatory:
        if not word.strip():
            return False
        
    for num in optional_numbers:
        if num and not num.isnumeric():
            return False
        

    return True


def number_or_none(value):
    if value:
        if value.isnumeric():
            return int(value)
    else:
        return None
    

def date_or_none(date):
    if date:
        if re.search(r"^\d{4}-\d{2}-\d{2}$", date):
            return datetime.strptime(date, "%Y-%m-%d").date()
        elif re.search(r"^\d{2}/\d{2}/\d{4}$", date):
            return datetime.strptime(date, "%d/%m/%Y").date()
        else: 
            return None

def strip_if_not_none(value):
    if value:
        return value.strip()
    else:
        return None
    

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function