from flask import *

from src.dbconnection import *
app=Flask(__name__)
app.secret_key="aaa"

@app.route('/')
def main():
    return render_template('login.html')

@app.route("/loginnew",methods=['post'])
def loginnew():
    uname=request.form['textfield']
    passwd=request.form['textfield2']

    qry="select * from login where username=%s and password=%s"
    val = (uname,passwd)
    res=selectone(qry,val)
    print(res)
    if res is None :

        return '''<script>alert("invalid username or password");window.location="/"</script>'''
    else:
        if res[3]=='admin':

            return '''<script>alert("welcome");window.location="/adminhome"</script>'''


@app.route('/adminhome')
def adminhome():
    return render_template('admin/adminhome.html')
@app.route('/addpolice',methods=['post'])
def addpolice():
    return render_template('admin/addpolice.html')

@app.route('/addpolice1',methods=['post'])
def addpolice1():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    age=request.form['textfield3']
    gender=request.form['radiobutton']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    phone=request.form['textfield7']
    email=request.form['textfield8']
    uname=request.form['textfield9']
    pswd=request.form['textfield10']
    qry = "insert into login values (null,%s,%s,'vo')"
    val = (uname,pswd)
    id=iud(qry,val)
    qry1 = "insert into police values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 =(str(id),fname, lname, age,gender,  place, post, pin, phone, email)
    iud(qry1, val1)
    return '<script>alert("Added successfully");window.location="/mngpolice"</script>'''




@app.route('/mngpolice')
def mngpolice():
    qry="select*from police "
    res=selectallnew(qry)
    return render_template('admin/manage police.html',val=res)
@app.route('/editpolice')
def editpolice():
    id=request.args.get('id')
    session['id']=id
    qry="select*from police where lid=%s"
    val=str(id)
    res=selectone(qry,val)
    return render_template('admin/editpolice.html',val=res)
@app.route('/dltpolice')
def dltpolice():
    id = request.args.get('id')
    q="delete from police where lid=%s"
    iud(q,str(id))
    q1="delete from login where lid=%s"
    iud(q1,str(id))

    return '<script>alert("delete successfully");window.location="/mngpolice"</script>'''
@app.route('/updatepolice',methods=['post'])
def updatepolice():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    age = request.form['textfield3']
    gender = request.form['radiobutton']
    place = request.form['textfield4']
    post = request.form['textfield5']
    pin = request.form['textfield6']
    phone = request.form['textfield7']
    email = request.form['textfield8']
    id=session['id']
    qry="UPDATE `police` SET `fname`=%s,`lname`=%s,`age`=%s,`gender`=%s,`place`=%s,`post`=%s,`pin`=%s,`phone`=%s,`email`=%s WHERE `lid`=%s"
    val=(fname,lname,age,gender,place,post,pin,phone,email,str(id))
    iud(qry,val)
    return '<script>alert("update successfully");window.location="/mngpolice"</script>'''
@app.route('/dltcase')
def dltcase():
    id = request.args.get('id')
    q = "delete from crime_report where reportid=%s"
    iud(q, str(id))

    return '<script>alert("delete successfully");window.location="/viewcrimereport"</script>'''




@app.route('/assignwrk')
def assignwrk():
    return render_template('admin/assign work to police.html')

@app.route('/viewcrimereport')
def viewcrimereport():
    qry="SELECT `case`.*,`crime_report`.* FROM `case` JOIN `crime_report` WHERE`case`.`caseid`=`crime_report`.`caseid`"
    res=selectallnew(qry)
    return render_template('admin/view crime report.html',val=res)

@app.route('/viewfeedback')
def viewfeedback():
    return render_template('admin/view feedback.html')

@app.route('/viewcasestatus')
def viewcasestatus():
    return render_template('admin/view_case_status.html')




























app.run(debug=True)