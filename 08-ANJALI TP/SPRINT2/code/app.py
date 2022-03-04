from flask import *
app=Flask(__name__)
from src.dbconnection import *
app.secret_key="aaaaa"

import functools
def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect('/')
        return func()
    return secure_function

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
            session['lid']=res[0]
            return redirect('/admin_home')
        else:
            return '''<script>alert("invalid");window.location='/'</script>'''


@app.route('/add_camera',methods=['post'])
@login_required

def add_camera():
    return render_template('add camera.html')

@app.route('/add_camera1',methods=['post'])
@login_required

def add_camera1():
    cnumb=request.form['textfield']
    qry="insert into camera values(NULL,%s)"
    val=cnumb
    iud(qry,val)


    return '''<script>alert("added");window.location='/manage_camera'</script>'''


@app.route('/add_staff',methods=['post'])
@login_required

def add_staff():
    return render_template('add staff.html')

@app.route('/adding_staff',methods=['post'])
@login_required

def adding_staff():
    try:
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
    except Exception as e:
        return '''<script>alert("duplicate entry!!!");window.location='/manage_staff'</script>'''


@app.route('/edit_staff')
@login_required

def edit_staff():
    id=request.args.get('id')
    session['id']=id
    qry="select*from staff where lid=%s"
    res=selectone(qry,str(id))
    return render_template('editstaff.html',val=res)
@app.route('/update_staff',methods=['post'])
@login_required

def update_staff():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    place = request.form['textfield3']
    post = request.form['textfield4']
    pin = request.form['textfield5']
    dob = request.form['textfield6']
    phone = request.form['textfield7']
    email = request.form['textfield8']
    qry="update staff set fname=%s,lname=%s,gender=%s,place=%s,post=%s,pin=%s,dob=%s,phone=%s,email=%s where lid=%s"
    val=(fname,lname,gender,place,post,pin,dob,phone,email,session['id'])
    iud(qry,val)
    return '''<script>alert("updated");window.location='/manage_staff'</script>'''

@app.route('/dlt_staff')
@login_required

def dlt_staff():
    id=request.args.get('id')
    qry="delete from login where id=%s"
    iud(qry,str(id))
    qry1 = "delete from staff where lid=%s"
    iud(qry1, str(id))

    return '''<script>alert("deleted");window.location='/manage_staff'</script>'''


@app.route('/update_cam',methods=['post'])
def update_cam():
    camno=request.form['textfield']
    qry="update camera set cameranumber=%s where id=%s"
    val=(camno,session['cid'])
    iud(qry,val)
    return '''<script>alert("updated");window.location='/manage_camera'</script>'''


@app.route('/admin_home')
@login_required

def admin_home():
    return render_template('admin home.html')

@app.route('/assign_work_to_staff')
@login_required

def assign_work_to_staff():
    qry = "select*from staff"
    res = selectall(qry)
    return render_template('assign work to staff.html',val=res)

@app.route('/assign_work_to_staff1',methods=['post'])
@login_required

def assign_work_to_staff1():
    staff=request.form['select']
    work=request.form['textarea']
    qry="insert into work values(NULL,%s,%s,curdate(),'pending')"
    val=(work,staff)
    iud(qry,val)
    return '''<script>alert("assigned ");window.location='/assign_work_to_staff'</script>'''



@app.route('/editcam')
@login_required

def editcam():
    id=request.args.get('id')
    session['cid']=id
    qry="select*from camera where id=%s"
    res=selectone(qry,str(id))
    return render_template('editcamera.html',val=res)


@app.route('/manage_camera')
@login_required

def manage_camera():
    qry="select*from camera"
    res=selectall(qry)
    return render_template('manage camera.html',val=res)

@app.route('/dltcam')
@login_required

def dltcam():
    id=request.args.get('id')
    qry="delete from camera where id=%s"
    iud(qry,str(id))

    return '''<script>alert("deleted");window.location='/manage_camera'</script>'''

@app.route('/manage_staff')
@login_required

def manage_staff():
    qry="select * from staff"
    res=selectall(qry)
    return render_template('manage staff.html',val=res)

@app.route('/send_notification')
@login_required

def send_notification():
    qry="select*from staff"
    res=selectall(qry)
    return render_template('send notification.html',val=res)

@app.route('/send_notification1',methods=['post'])
@login_required

def send_notification1():
    staff=request.form['select']
    noti=request.form['textarea']
    qry="insert into notification values(NULL,%s,curdate(),%s)"
    val=(noti,staff)
    iud(qry,val)
    return '''<script>alert("sent ");window.location='/send_notification'</script>'''


@app.route('/view_work_status')
@login_required

def view_work_status():
    qry="SELECT `work`.*,`staff`.`fname`,`staff`.`lname`,`staff`.`phone` FROM `staff` JOIN `work` ON `staff`.`lid`=`work`.`staff_lid`"
    res=selectall(qry)
    return render_template('view work status.html',val=res)


@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")

















app.run(debug=True)