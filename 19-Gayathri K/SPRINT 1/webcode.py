from flask import *
from src.dbconnect import *

app=Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")


@app.route('/viewuser')
def viewuser():
    qry = "SELECT * FROM users"
    s = select(qry)
    return render_template("viewuser.html",val=s)

@app.route('/reply')
def reply():
    return render_template("reply.html")


@app.route('/viewcomplaint')
def viewcomplaint():
    return render_template("viewcomplaint.html")


@app.route('/viewfeedback')
def viewfeedback():
    qry="SELECT `users`.`fname`,`users`.`lname`,`feedback`.* FROM `feedback` JOIN `users` ON `users`.`lid`=`feedback`.`user_lid`"
    s = select(qry)
    return render_template("viewfeedback.html",val=s)

@app.route('/homepage')
def homepage():
    return render_template("homepage.html")






@app.route('/login2',methods=['post'])
def login2():
    uname=request.form['textfield']
    pword=request.form['textfield2']
    q="select * from login where username=%s and password=%s"
    val=(uname,pword)
    s=selectonecond(q,val)
    if s  is None:
        return '''<script>alert('Invalid user name or password');window.location='/'</script>'''
    elif s[3]=='admin':
        return '''<script>alert('login successfully');window.location='/homepage'</script>'''










app.run(debug=True)
