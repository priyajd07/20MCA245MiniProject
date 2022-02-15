from flask import *
app=Flask(__name__)
from src.dbconnection import *

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/logincode',methods=['post'])
def logincode():
    uname=request.form['textfield']
    pwd=request.form['textfield2']
    qry="SELECT * FROM login WHERE username=%s AND PASSWORD=%s"
    val=(uname,pwd)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location='/'</script>'''
    else:
        if res[3]=='admin':
            return redirect('/admin_home')
        else:
            return '''<script>alert("invalid");window.location='/'</script>'''


@app.route('/add_camera')
def add_camera():
    return render_template('add camera.html')

@app.route('/add_staff',methods=['post'])
def add_staff():
    return render_template('add staff.html')

@app.route('/adding_staff',methods=['post'])
def adding_staff():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    dob=request.form['textfield6']
    phone=request.form['textfield7']
    email=request.form['textfield8']
    uname=request.form['textfield9']
    pwd=request.form['textfield10']
    qry="INSERT INTO login VALUES(NULL,%s,%s,'staff')"
    val=(uname,pwd)
    id=iud(qry,val)
    qry1="INSERT INTO `staff` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),fname,lname,gender,place,post,pin,dob,phone,email)
    iud(qry1,val1)
    return '''<script>alert("success");window.location='/manage_staff'</script>'''



@app.route('/admin_home')
def admin_home():
    return render_template('admin home.html')

@app.route('/assign_work_to_staff')
def assign_work_to_staff():
    return render_template('assign work to staff.html')


@app.route('/manage_camera')
def manage_camera():
    return render_template('manage camera.html')

@app.route('/manage_staff')
def manage_staff():
    qry="select * from staff"
    res=selectall(qry)
    return render_template('manage staff.html',val=res)

@app.route('/send_notification')
def send_notification():
    return render_template('send notification.html')

@app.route('/view_work_status')
def view_work_status():
    return render_template('view work status.html')


@app.route('/viewnotification')
def viewnotification():
    return render_template('view notification.html')


















app.run(debug=True)