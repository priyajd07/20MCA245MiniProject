from flask import *

from src.dbconnection import selectone, iud, selectall

app=Flask(__name__)
app.secret_key="aaaa"

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/log',methods=['post'])
def log():
    uname=request.form['textfield']
    pswrd=request.form['textfield2']
    print(uname,pswrd)
    qry="select * from login where username=%s and password=%s"
    val=(uname,pswrd)
    res=selectone(qry,val)
    print(res)
    if res is None:
        return '''<script>alert("invalid username or password");window.location="/"</script>'''
    elif(res[3]=='blood bank'):
        session['lid'] = res[0]
        return '''<script>alert("welcome blood bank");window.location="/bloodbankhome"</script>'''

    else:

        return '''<script>alert("not valid");window.location="/"</script>'''


@app.route('/bloodbankhome')
def bloodbankhome():
    return render_template("blood bank home.html")


@app.route('/add_blood_requirement')
def add_blood_requirement():
    return render_template("Add blood reqirement.html")



@app.route('/add_blood_requirement2',methods=['post'])
def add_blood_requirement2():
    blood=request.form['textfield']
    qry="INSERT INTO `blood_requirement` VALUES(NULL,%s,'required',CURDATE())"
    val=blood
    iud(qry,val)
    return '''<script>alert("requirement added succefully");window.location="/bloodbankhome"</script>'''



@app.route('/update_donation_status')
def update_donation_status():
    return render_template("update donation status.html")


@app.route('/view_request_status')
def view_request_status():
    qry="SELECT * FROM `blood_requirement`"
    res=selectall(qry)
    return render_template("view request status.html",val=res)


app.run(debug=True)