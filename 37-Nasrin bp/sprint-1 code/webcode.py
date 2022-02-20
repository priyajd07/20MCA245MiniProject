from flask import *
app=Flask(__name__)
from dbconn import *

@app.route('/')
def login():

    return render_template('login.html')


@app.route('/logincode',methods=['post'])
def logincode():
    uname=request.form['textfield']
    pwd=request.form['textfield2']
    qry="SELECT * FROM login WHERE username=%s AND PASSWORD=%s"
    val=(uname,pwd)
    print(val)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert('invalid');window.location="/"</script>'''
    else:
        if res[3]=='admin':
            return redirect('/adminhome')
        elif res[3] == 'user':
            return redirect('/userhome')
        else:
            return '''<script>alert('invalid');window.location="/"</script>'''





@app.route('/addtips',methods=['post'])
def addtips():
    return render_template('addtips.html')

@app.route('/addingtips',methods=['post'])
def addingtips():
    tip=request.form['textarea']
    qry="insert into tips values(NULL,%s,CURDATE())"
    iud(qry,tip)
    return '''<script>alert('tip added');window.location="/tips"</script>'''


@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/sendfeedback')
def sendfeedback():
    return render_template('sendfeedback.html')

@app.route('/tips')
def tips():
    qry="select * from tips"
    res=selectall(qry)
    return render_template('tips.html',val=res)

@app.route('/updateprofile')
def updateprofile():
    return render_template('updateprofile.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/upload_history')
def upload_history():
    return render_template('upload_history.html')


@app.route('/view_tip')
def view_tip():
    return render_template('view_tip.html')


@app.route('/viewfeedback')
def viewfeedback():
    return render_template('viewfeedback.html')

@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')


@app.route('/userhome')
def userhome():
    return render_template('userhome.html')

@app.route('/signingup',methods=['post'])
def signingup():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    phone=request.form['textfield6']
    email=request.form['textfield7']
    username=request.form['textfield8']
    password=request.form['textfield9']
    query="INSERT INTO login VALUES(NULL,%s,%s,'user')"
    val=(username,password)
    id=iud(query,val)
    query="INSERT INTO registration VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),fname,lname,gender,place,post,pin,phone,email)
    iud(query,val)
    return '''<script> alert('Registration Success!');window.location='/';</script>'''


@app.route('/viewuser')
def viewuser():
    return render_template('viewuser.html')













app.run(debug=True)