
from flask import Flask, jsonify,render_template,request
from flask.globals import session
from itsdangerous import json
from scipy.fft import idstn
from scipy.fftpack import ss_diff
from DBConnection import  Db
import time
import datetime
import random

app = Flask(__name__)
app.secret_key="4fdfdfij4d"
staticpath="C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\"


@app.route('/')
def login():
    return render_template("Login/Login.html")

@app.route('/login_post',methods=['post'])
def login_post():
    username=request.form["textfield"]
    password=request.form["textfield2"]
    db=Db()
    qry="SELECT * FROM login WHERE username='"+username+"' AND PASSWORD='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:


        if res["type"]=="admin":
            return '''<script>alert('Login Success');window.location='/admin_add_puzzles'</script>'''
        elif res["type"]=="doctor":
            qry="select * from doctor where lid='"+str(res["lid"])+"'"
            rr=db.selectOne(qry)
            session["lid"] = res["lid"]
            session["photo"]=rr["image"]
            session["name"]=rr["name"]
            return doc_view_profile()
        else:
            return '''<script>alert('Invalid username or password');window.location='/'</script>'''
    else:
        return '''<script>alert('Invalid username or password');window.location='/'</script>'''


@app.route('/home')
def home():
    return render_template('admin/HOME.html')
@app.route('/Change_passwrd')
def change_password():
    return render_template("admin/Change_passwrd.html")

@app.route('/Change_passwrd_post',methods=['post'])
def change_passwrd_post():
    cupasswrd=request.form["textfield"]
    newpasswrd=request.form["textfield2"]
    conpasswrd=request.form["textfield3"]
    if(cupasswrd==session["pass"]):
        if newpasswrd==conpasswrd:
            qry="UPDATE login SET PASSWORD='"+conpasswrd+"' WHERE `lid`='"+str(session["lid"])+"'"
            c=Db()
            res=c.update(qry)
            return '''<script>alert("success");window.location='/'</script>'''

        else:
            return '''<script>alert("Incorrect Confirm Password");window.location='/Change_passwrd'</script>'''
    else:
        return '''<script>alert("Incorrect Password");window.location='/Change_passwrd'</script>'''

@app.route('/admin_add_doctor')
def admin_add_doctor():
    return render_template("admin/Add_Doctor.html")
@app.route('/doc_add_post',methods=['post'])
def doc_add_post():
    name=request.form["textfield"]
    gender=request.form["radiobutton"]
    place=request.form["textfield3"]
    pin=request.form["textfield4"]
    post=request.form["textfield2"]
    phone=request.form["textfield5"]
    image=request.files["file"]
    image.save("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\Doctor\\"+image.filename)
    path="/static/Doctor/"+image.filename
    email=request.form["textfield6"]
    qual=request.form["textfield7"]
    expe=request.form["textfield8"]
    prev=request.form["textfield9"]
    acheiv=request.form["textfield10"]
    password= random.randint(1000,9999)
    db=Db()

    qry="INSERT INTO login(`username`,`password`,`type`)VALUES('"+email+"','"+str(password)+"','doctor')"
    lid=db.insert(qry)
    qry1="INSERT INTO doctor(`name`,`place`,`pin`,`post`,`phone`,`image`,`email`,`lid`,`gender`,qualification,experience,previous_work,acheivement)VALUES('"+name+"','"+place+"','"+pin+"','"+post+"','"+phone+"','"+path+"','"+email+"','"+str(lid)+"','"+gender+"','"+qual+"','"+expe+"','"+prev+"','"+acheiv+"')"
    db.insert(qry1)
    return admin_add_doctor()

@app.route('/adm_view_doctor')
def adm_view_doctor():
    qry="select * from doctor"
    db=Db()
    res=db.select(qry)
    return render_template("admin/Admin view doctor.html",data=res)

@app.route('/adm_view_doctor_post',methods=['post'])
def adm_view_doctor_post ():
    name=request.form["textfield"]
    qry = "select * from doctor where name like '%"+name+"%'"
    db = Db()
    res = db.select(qry)
    return render_template("admin/Admin view doctor.html", data=res)

@app.route('/admin_delete_doctor/<id>')
def admin_delete_doctor(id):
    qry="DELETE FROM doctor WHERE lid='"+id+"'"
    db = Db()
    res = db.delete(qry)
    return "<script>alert('succescc');window.location='/adm_view_doctor'</script>"

@app.route('/admin_edit_doctor/<id>')
def admin_edit_doctor(id):
    qry="select *  FROM doctor WHERE lid='"+id+"'"
    db = Db()
    res = db.selectOne(qry)
    return  render_template("admin/Edit_Doctor.html",data=res)


@app.route('/doc_edit_post',methods=['post'])
def doc_edit_post():
    name=request.form["textfield"]
    gender=request.form["radiobutton"]
    place=request.form["textfield3"]
    pin=request.form["textfield4"]
    post=request.form["textfield2"]
    phone=request.form["textfield5"]
    id=request.form["idd"]
    email=request.form["textfield6"]

    db=Db()
    if 'file' in request.files:
        image=request.files["file"]
        if image.filename!="":
            image.save("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\Doctor\\"+image.filename)
            path="/static/Doctor/"+image.filename
            qry="update doctor set name='"+name+"',place='"+place+"',pin='"+pin+"',post='"+post+"',phone='"+phone+"',image='"+path+"',email='"+email+"',gender='"+gender+"' where id='"+id+"'"
        else:
            qry="update doctor set name='"+name+"',place='"+place+"',pin='"+pin+"',post='"+post+"',phone='"+phone+"',email='"+email+"',gender='"+gender+"' where id='"+id+"'"

    else:
        qry="update doctor set name='"+name+"',place='"+place+"',pin='"+pin+"',post='"+post+"',phone='"+phone+"',email='"+email+"',gender='"+gender+"' where id='"+id+"'"
    db.update(qry)
    return "<script>alert('succes');window.location='/adm_view_doctor'</script>"

@app.route('/view_complaints')
def view_complaints():

    db=Db()
    qry = "SELECT `complaint`.*, `doctor`.`name`, `caretaker`.`name`,  `caretaker`.`email` FROM `doctor` INNER JOIN `complaint` ON `complaint`.`doctor_id`=`doctor`.`lid` INNER JOIN `caretaker` ON `caretaker`.`lid`=`complaint`.`from_id`"
    res = db.select(qry)
    return render_template("admin/View Compaint.html", data=res)



@app.route('/view_complaint_search',methods=['post'])
def view_complaint_earch_post():
    frm_date = request.form['textfield']
    to_date = request.form['textfield2']
    db = Db()
    qry = "SELECT `complaint`.*, `doctor`.`name`, `caretaker`.`name`,`caretaker`.`email` FROM `doctor` INNER JOIN `complaint` ON `complaint`.`doctor_id`=`doctor`.`id` INNER JOIN `caretaker` ON `caretaker`.`id`=`complaint`.`from_id` WHERE `date` BETWEEN '"+frm_date+"' AND '"+to_date+"'"
    res = db.select(qry)
    return render_template("admin/View Compaint.html", data=res)



@app.route('/send_complaint_reply/<id>')
def send_complaint_reply(id):

    db = Db()
    qry = "SELECT * FROM complaint WHERE `complaint_id`='"+id+"'"
    res = db.selectOne(qry)
    return render_template("admin/Admin Send Reply.html", data=res)




@app.route('/adm_sent_reply_post',methods=['post'])
def adm_sent_reply_post():
    compl_id = request.form['com_id']
    reply = request.form['textarea']
    db = Db()
    qry = "UPDATE complaint SET `reply`='"+reply+"' ,status='replied'WHERE `complaint_id`='"+compl_id+"'"
    res = db.update(qry)
    return '''<script>alert('send');window.location='/view_complaints'</script>'''


@app.route('/adm_view_patients')
def adm_view_patients():
    qry="select * from patient"
    db = Db()
    res=db.select(qry)
    return render_template("admin/Admin View patients.html",data=res)

@app.route('/adm_view_patients_post',methods=['post'])
def adm_view_patients_post():
    name=request.form["textfield"]
    qry="select * from patient where name like '%"+name+"%'"
    db = Db()
    res=db.select(qry)
    return render_template("admin/Admin View patients.html",data=res)

@app.route('/adm_view_progress/<id>')
def adm_view_progress(id):
    qry="select * from progress where patient_id='"+id+"'"
    db = Db()
    res=db.select(qry)
    return render_template("admin/Admin View progress.html",res=res)



@app.route('/admin')
def admin():
    return render_template("admin/Admin.html")
@app.route('/admin_add_puzzles')
def admin_add_puzzles():
    return render_template("admin/addpuzzle.html")
@app.route('/admin_add_puzzles_post',methods=['POST'])
def admin_add_puzzles_post():
    name=request.form["name"]
    file=request.files["file"]
    fname = str(file.filename).split(".")
    fname.pop()
    fname = ".".join(fname)
    file.save(staticpath+"puzzles\\"+file.filename)
    # file.save(staticpath+"puzzles\\"+fname+".jpg")
    path="/static/puzzles/"+file.filename
    # path="/static/puzzles/"+fname+".jpg"
    from PIL import Image
    import cv2
    # img = Image.open("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\puzzles\\"+fname+".jpg")
    img = Image.open("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\puzzles\\"+file.filename)
    baseWidth = 800
    baseheight = 800
    img = img.resize((baseWidth, baseheight), Image.ANTIALIAS)

    # img.save('C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\puzzles\\1' + fname+".jpg")
    img.save('C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\puzzles\\1' + file.filename)




    # img = cv2.imread('C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\puzzles\\1'+ fname+".jpg")
    img = cv2.imread('C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\puzzles\\1'+ file.filename)

    k = 1

    for i in range(0, 800, 200): # height wise
        for j in range(0, 800, 200): # width wise
            crop_img = img[i:i + 200, j:j + 200]
            cv2.imshow('img', crop_img)
            # cv2.imwrite('C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\puzzles\\resized\\' + str(k) + "" + file.filename, crop_img)
            cv2.imwrite('C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\puzzles\\resized\\' + str(k) + "" + fname+".jpg", crop_img)
            k = k + 1


    qry="insert  into `puzzle`(`name`,`filename`,`imagename`) values ('"+name+"','"+path+"','"+file.filename+"')"
    db=Db()
    db.insert(qry)
    return '''<script>alert('Added');window.location='/admin_add_puzzles'</script>'''

@app.route('/admin_view_puzzles')
def admin_view_puzzles():
    qry="select * from puzzle"
    db = Db()
    res=db.select(qry)
    return render_template("admin/viewpuzzle.html",data=res)

@app.route('/admin_delete_puzzles/<i>')
def admin_delete_puzzles(i):
    qry="delete from puzzle where id='"+i+"'"
    db = Db()
    res=db.delete(qry)
    return admin_view_puzzles()
#------------------------------------------doctor----------------
@app.route('/doc_add_patinet')
def doc_add_patinet():
    return render_template("Doctor/Add Patient.html")

@app.route('/doc_add_patinet_post',methods=['post'])
def doc_add_patinet_post():
    name=request.form["textfield"]
    gender=request.form["radiobutton"]
    dob=request.form["textfield20"]
    place=request.form["textfield2"]
    pin=request.form["textfield3"]
    post=request.form["textfield4"]
    district=request.form["textfield5"]
    adharno=request.form["textfield6"]
    phone=request.form["textfield7"]
    image=request.files["file"]
    email=request.form["textfield8"]
    import datetime
    dt=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    image.save(staticpath+"patient\\"+dt+".jpg")
    path="/static/patient/"+dt+".jpg"
    db=Db()
    import random
    password=random.randint(1000,100000)
    qry1="INSERT INTO login(username,PASSWORD,TYPE)VALUES('"+email+"','"+str(password)+"','patient')"
    res1=db.insert(qry1)
    qry="INSERT INTO patient(NAME,place,pin,post,district,adhar_no,image,email,phone,lid,gender,dob)VALUES('"+name+"','"+place+"','"+pin+"','"+post+"','"+district+"','"+adharno+"','"+path+"','"+email+"','"+phone+"','"+str(res1)+"','"+gender+"','"+dob+"')"
    res=db.insert(qry)
    return render_template("Doctor/Add Patient.html")


@app.route('/doc_viewpatient')
def doc_viewpatient():
    db=Db()
    qry="select * from patient "
    res=db.select(qry)
    return render_template("Doctor/View Patients.html",data=res)


@app.route('/doc_add_caretaker')
def doc_add_add_caretaker():
    return render_template("Doctor/Caretaker Add.html")

@app.route('/doc_add_caretaker_post',methods=['post'])
def doc_add_caretaker_post():
    name=request.form["textfield"]
    gender=request.form["radiobutton"]
    qual=request.form["textfield7"]
    place=request.form["textfield2"]
    pin=request.form["textfield3"]
    post=request.form["textfield4"]

    adharno=request.form["textfield5"]
    phone=request.form["textfield6"]
    image=request.files["file"]
    email=request.form["textfield8"]
    import datetime
    dt=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    image.save(staticpath+"caretaker\\"+dt+".jpg")
    path="/static/caretaker/"+dt+".jpg"
    db=Db()
    import random
    password=random.randint(1000,100000)
    qry1="INSERT INTO login(username,PASSWORD,TYPE)VALUES('"+email+"','"+str(password)+"','caretaker')"
    res1=db.insert(qry1)
    qry="INSERT INTO caretaker (NAME,place,pin,post,adhar_no,photo,email,phone,lid,gender,qualification,doctor_lid)VALUES('"+name+"','"+place+"','"+pin+"','"+post+"','"+adharno+"','"+path+"','"+email+"','"+phone+"','"+str(res1)+"','"+gender+"','"+qual+"','"+str(session["lid"])+"')"
    res=db.insert(qry)
    return render_template("Doctor/Caretaker Add.html")


@app.route('/doc_assign_patient_to_caretaker')
def doc_assign_patient_to_caretaker():
    qry1="select * from patient"
    qry2="select * from caretaker"
    db=Db()
    res=db.select(qry1)
    res2=db.select(qry2)
    return render_template("Doctor/Assign Patient To Caretaker.html",pat=res,care=res2)

@app.route('/doc_assign_patient_to_caretaker_post',methods=['post'])
def doc_assign_patient_to_caretaker_post():
    caretaker=request.form["care"]
    pat=request.form["pat"]
    qry="insert into allocation(caretaker_id,patient_id,status,date)values('"+caretaker+"','"+pat+"','Active',curdate())"
    db=Db()
    db.insert(qry)
    return doc_assign_patient_to_caretaker()

@app.route('/doc_view_caretaker_complaint')
def doc_view_caretaker_complaint():
    db=Db()
    qry = "select * from complaint,caretaker where caretaker.lid=complaint.from_id and complaint.doctor_id='"+str(session["lid"])+"'"
    res = db.select(qry)
    return render_template("Doctor/Doctor View Caretaker Complaint.html",data=res)

@app.route('/doc_view_caretaker_complaint_post',methods=['post'])
def doc_view_caretaker_complaint_post():
    datefrom=request.form["textfield"]
    to=request.form["textfield2"]
    qry = "select * from complaint,caretaker where caretaker.lid=complaint.from_id and complaint.doctor_id='"+str(session["lid"])+"' and date between '"+datefrom+"' and '"+to+"'"

    db=Db()
    res = db.select(qry)
    return render_template("Doctor/Doctor View Caretaker Complaint.html",data=res)
@app.route('/send_complaint_replydoc/<id>')
def send_complaint_replydoc(id):

    db = Db()
    qry = "SELECT * FROM complaint WHERE `complaint_id`='"+id+"'"
    res = db.selectOne(qry)
    return render_template("Doctor/Send Reply.html", data=res)




@app.route('/doc_sent_reply_post',methods=['post'])
def doc_sent_reply_post():
    compl_id = request.form['com_id']
    reply = request.form['textarea']
    db = Db()
    qry = "UPDATE complaint SET `reply`='"+reply+"' ,status='replied'WHERE `complaint_id`='"+compl_id+"'"
    res = db.update(qry)
    return '''<script>alert('send');window.location='/doc_view_caretaker_complaint'</script>'''
@app.route('/doc_view_profile')
def doc_view_profile():
    qry="select * from doctor where lid='"+str(session["lid"])+"'"
    db=Db()
    res=db.selectOne(qry)
    return render_template("Doctor/doctor view profile.html",d=res)

@app.route('/doc_change_password')
def doc_change_password():
    return render_template("Doctor/Doctor-Change Password.html")

@app.route('/doc_change_password_post',methods=['post'])
def doc_change_password_post():
    current = request.form['textfield']
    new = request.form['textfield2']
    confirm = request.form['textfield3']
    a = Db()
    qry = "SELECT * FROM login WHERE `password`='"+current+"' and login_id='"+str(session['lid'])+"'"
    res = a.selectOne(qry)
    if res!=None:
        if new==confirm:
            qry ="update login set password ='"+confirm+"' where login_id='"+str(session['lid'])+"'"
            res = a.update(qry)
            return '''<script>alert('Password created');window.location='/'</script>'''
        else:
            return '''<script>alert('Password mismatch');window.location='/doc_change_password'</script>'''
    else:
        return '''<script>alert('Current password must be valid');window.location='/doc_change_password'</script>'''

    return render_template("Doctor/Doctor-Change Password.html")

# @app.route('/doc_view_patient_imotion')
# def doc_view_patient_imotion():
#     return render_template("Doctor/Doctors View Patient Imotion.html")

# @app.route('/doc_view_patient_imotion_post',methods=['post'])
# def doc_view_patient_imotion_post():
#     datefrom=request.form["textfield"]
#     to=request.form["textfield2"]
#     return render_template("Doctor/Doctors View Patient Imotion.html")





@app.route('/doc_edit_caretaker/<id>')
def doc_edit_caretaker(id):
    qry="select * from caretaker where id='"+id+"'"
    db=Db()
    res=db.selectOne(qry)
    print(res)
    return render_template("Doctor/Edit Caretaker.html",d=res)

@app.route('/doc_delete_caretaker/<id>')
def doc_delete_caretaker(id):
    qry="delete from caretaker where id='"+id+"'"
    db=Db()
    db.delete(qry)
    return doc_view_caretaker()

@app.route('/doc_edit_caretaker_post',methods=['post'])
def doc_edit_caretaker_post():
    name=request.form["textfield"]
    place=request.form["textfield2"]
    pin=request.form["textfield3"]
    post=request.form["textfield4"]
    gender=request.form["radiobutton"]
    adhar=request.form["textfield5"]
    phone=request.form["textfield6"]
    id=request.form["id"]
    qual=request.form["textfield7"]
    email=request.form["textfield8"]

    if 'file' in request.files:
        image=request.files["file"]
        if image.filename!="":
            image.save("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\caretaker\\"+image.filename)
            path="/static/caretaker/"+image.filename
            qry="update caretaker set name='"+name+"',place='"+place+"',pin='"+pin+"',post='"+post+"',adhar_no='"+adhar+"',email='"+email+"',phone='"+phone+"',photo='"+path+"',qualification='"+qual+"',gender='"+gender+"' where id='"+id+"'"
        else:
            qry="update caretaker set name='"+name+"',place='"+place+"',pin='"+pin+"',post='"+post+"',adhar_no='"+adhar+"',email='"+email+"',phone='"+phone+"',qualification='"+qual+"',gender='"+gender+"' where id='"+id+"'"

    else:
        qry="update caretaker set name='"+name+"',place='"+place+"',pin='"+pin+"',post='"+post+"',adhar_no='"+adhar+"',email='"+email+"',phone='"+phone+"',qualification='"+qual+"',gender='"+gender+"' where id='"+id+"'"
    db=Db()
    db.update(qry)
    return "<script>alert('succes');window.location='/doc_view_caretaker'</script>"


@app.route('/doc_delete_patient/<id>')
def doc_delete_patient(id):
    db=Db()
    db.delete("delete from patient where id='"+id+"'")
    return doc_viewpatient()

@app.route('/doc_edit_patient/<id>')
def doc_edit_patient(id):
    db=Db()
    qry=db.selectOne("select *  from patient where id='"+id+"'")
    return render_template("Doctor/Edit-Ptient.html",d=qry)

@app.route('/doc_edit_patient_post',methods=['post'])
def doc_edit_patient_post():
    name=request.form["textfield"]
    gender=request.form["radiobutton"]
    dob=request.form["select"]
    place=request.form["textfield2"]
    pin=request.form["textfield3"]
    post=request.form["textfield4"]
    district=request.form["textfield5"]
    adharno=request.form["textfield6"]
    phone=request.form["textfield7"]

    email=request.form["textfield8"]
    id=request.form["id"]
    if 'file' in request.files:
        image=request.files["file"]
        if image.filename!="":
            image.save("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\patient\\"+image.filename)
            path="/static/patient/"+image.filename
            qry="update patient set name='"+name+"',place='"+place+"',pin='"+pin+"',post='"+post+"',district='"+district+"',adhar_no='"+adharno+"',image='"+path+"',email='"+email+"',phone='"+phone+"',gender='"+gender+"',dob='"+dob+"' where id='"+id+"'"
        else:
            qry="update patient set name='"+name+"',place='"+place+"',pin='"+pin+"',post='"+post+"',district='"+district+"',adhar_no='"+adharno+"',email='"+email+"',phone='"+phone+"',gender='"+gender+"',dob='"+dob+"' where id='"+id+"'"

    else:
        qry="update patient set name='"+name+"',place='"+place+"',pin='"+pin+"',post='"+post+"',district='"+district+"',adhar_no='"+adharno+"',email='"+email+"',phone='"+phone+"',gender='"+gender+"',dob='"+dob+"' where id='"+id+"'"
    db=Db()
    db.update(qry)
    return "<script>alert('succes');window.location='/doc_viewpatient'</script>"

@app.route('/doc_send_notification_to_caretaker')
def doc_send_notification_to_caretaker():
    qry="select * from caretaker where doctor_lid='"+str(session["lid"])+"'"
    db=Db()
    res=db.select(qry)
    return render_template("Doctor/Send Notification To Cretaker.html",data=res)

@app.route('/doc_send_notification_to_caretaker_post',methods=['post'])
def doc_send_notification_to_caretaker_post():
    caretaker=request.form["select"]
    notification=request.form["textarea"]
    qry="insert into notification (doctor_lid,caretaker_lid,description,date)values('"+str(session["lid"])+"','"+caretaker+"','"+notification+"',curdate())"
    db=Db()
    db.insert(qry)
    return "<script>alert('succes');window.location='/doc_send_notification_to_caretaker'</script>"



@app.route('/doc_view_caretaker')
def doc_view_caretaker():
    db=Db()
    qry="select * from caretaker where doctor_lid='"+str(session["lid"])+"'"
    res=db.select(qry)
    print(qry)
    print(res)
    return render_template("Doctor/View Caretaker.html",data=res)

@app.route('/doc_view_caretaker_post',methods=['post'])
def doc_view_caretaker_post():
    name=request.form["dtextfiel"]
    db=Db()
    qry="select * from caretaker where name like '%"+name+"%' and doctor_lid='"+str(session["lid"])+"'"
    res=db.select(qry)
    return render_template("Doctor/View Caretaker.html",data=res)

@app.route('/doc_view_progress/<id>')
def doc_view_progress(id):
    qry="select * from progress where patient_id='"+id+"'"
    db = Db()
    res=db.select(qry)
    return render_template("Doctor/Doctors View Patient-Progress.html",res=res)

@app.route('/doc_view_patient_post',methods=['post'])
def doc_view_patient_post():
    name=request.form["textfield"]
    db=Db()
    qry="select * from patient where name like '%"+name+"%'"
    res=db.select(qry)
    return render_template("Doctor/View Patients.html",data=res)



@app.route('/doc_view_patient_assigned_caretaker')
def doc_view_patient_assigned_caretaker():
    qry="select patient.*,caretaker.* ,patient.name as pname,allocation.*, caretaker.name as cname from patient inner join allocation on allocation.patient_id=patient.lid inner join caretaker on caretaker.lid=allocation.caretaker_id"
    db=Db()
    res=db.select(qry)
    return render_template("Doctor/View Ptient Assigned Caretaker.html",data=res)

@app.route('/doc_view_patient_assigned_caretaker_post',methods=['post'])
def doc_view_patient_assigned_caretaker_post():
    carename=request.form["textfield"]
    qry="select patient.*,caretaker.* ,patient.name as pname,allocation.*,  caretaker.name as cname from patient inner join allocation on allocation.patient_id=patient.lid inner join caretaker on caretaker.lid=allocation.caretaker_id where patient.name like '%"+carename+"%' or caretaker.name like '%"+carename+"%'"
    db=Db()
    res=db.select(qry)
    return render_template("Doctor/View Ptient Assigned Caretaker.html",data=res)

@app.route('/doc_delete_assigned_caretaker/<id>')
def doc_delete_assigned_caretaker(id):
    qry="delete from allocation where alloc_id ='"+id+"'"
    db=Db()
    res=db.delete(qry)
    return doc_view_patient_assigned_caretaker()

@app.route('/doc_view_send_notification')
def doc_view_send_notification():
    db=Db()
    qry="select * from notification inner join caretaker on notification.caretaker_lid=caretaker.lid where notification.doctor_lid='"+str(session["lid"])+"'"
    res=db.select(qry)
    return render_template("Doctor/View Send Notification.html",data=res)

@app.route('/delete_notification/<id>')
def delete_notification(id):
    db=Db()
    qry="delete from notification where id='"+id+"'"
    res=db.delete(qry)
    return doc_view_send_notification()

@app.route('/doc_view_send_notification_post',methods=['post'])
def doc_view_send_notification_post():
    datefrom=request.form["textfield"]
    to=request.form["textfield2"]
    db=Db()
    qry="select * from notification inner join caretaker on notification.caretaker_lid=caretaker.lid where notification.doctor_lid='"+str(session["lid"])+"' and date between '"+datefrom+"' and '"+to+"'"
    res=db.select(qry)
    return render_template("Doctor/View Send Notification.html",data=res)

@app.route('/doc_HOME')
def doc_HOME():
    return render_template("Doctor/HOME.html")




# --------------------------Android methods------------------

@app.route("/and_login",methods=['post'])
def and_login():
    username=request.form["username"]
    password=request.form["password"]
    db=Db()
    qry="SELECT * FROM login WHERE username='"+username+"' AND PASSWORD='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:

        if res["type"]=="caretaker":

            return jsonify(status="ok",lid=res["lid"],type="caretaker")
        if res["type"]=="patient":
            return jsonify(status="ok",lid=res["lid"],type="patient")
        else:
            return jsonify(status="no")
    else:
        return jsonify(status="no")

@app.route("/and_viewcomplaint",methods=['POST'])
def and_viewcomplaint():
    id=request.form["lid"]

    qry="select * from complaint where from_id='"+id+"'"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route("/and_complaint_add",methods=['POST'])
def and_complaint_add():
    id=request.form["lid"]
    comp=request.form["comp"]
    qq="select doctor_lid from caretaker where lid='"+id+"'"
    db=Db()
    rr=db.selectOne(qq)
    ddid=str(rr["doctor_lid"])
    qry="insert into complaint(date,doctor_id,from_id,reply,complaint,status)values(curdate(),'"+ddid+"','"+id+"','pending','"+comp+"','pending')"

    db=Db()
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route("/and_caretaker_viewpatient",methods=['POST'])
def and_caretaker_viewpatient():
    id=request.form["lid"]

    qry="select * from allocation inner join patient on patient.lid=allocation.patient_id where caretaker_id='"+id+"'"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route("/and_caretaker_viewpatientsearch",methods=['POST'])
def and_caretaker_viewpatientsearch():
    id=request.form["lid"]
    name=request.form["name"]
    qry="select * from allocation inner join patient on patient.lid=allocation.patient_id where caretaker_id='"+id+"' and patient.name like '%"+name+"%'"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route("/and_notification",methods=['POST'])
def and_notification():
    id=request.form["lid"]

    qry="select * from notification where caretaker_lid='"+id+"'"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route("/and_add_care_person",methods=['POST'])
def and_person():
    lid=request.form["pid"]
    pname=request.form["name"]
    phone=request.form["phone"]
    pic=request.files["pic"]
    pic.save("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\person\\"+pname+".jpg")
    path="/static/person/"+pname+".jpg"
    qry="insert into imp_person(patient_id,pname,image,phone) values('"+lid+"','"+pname+"','"+path+"','"+phone+"')"
    db=Db()
    db.insert(qry)
    return jsonify(status="ok")


@app.route("/and_care_updateimpdate",methods=['POST'])
def and_care_updateimpdate():
    event=request.form["event"]
    lid=request.form["pid"]
    date=request.form["date"]
    description=request.form["description"]
    id =request.form["id"]
    if 'image' in request.files:
        pic=request.files["image"]
        pic.save("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\event\\"+event+".jpg")
        path="/static/event/"+event+".jpg"
        qry="update reminder set patient_id='"+lid+"',event='"+event+"',description='"+description+"',event_date='"+date+"',photo='"+path+"' where id='"+id+"'"
    else:
        qry="update reminder set patient_id='"+lid+"',event='"+event+"',description='"+description+"',event_date='"+date+"' where id='"+id+"'"

    print(qry)
    db=Db()
    res=db.insert(qry)
    return jsonify(status="ok")
@app.route("/and_view_person",methods=['POST'])
def and_viewperson():
    lid=request.form["lid"]
    qry="select * from  imp_person where patient_id='"+lid+"'"
    print(qry)
    db=Db()
    res=db.select(qry)

    return jsonify(status="ok",data=res)

@app.route("/deleteperson",methods=['POST'])
def deleteperson():
    lid=request.form["id"]
    qry="delete from  imp_person where id='"+lid+"'"
    print(qry)
    db=Db()
    res=db.delete(qry)

    return jsonify(status="ok")
@app.route("/and_view_personsearch",methods=['POST'])
def and_view_personsearch():
    lid=request.form["lid"]
    name=request.form["name"]
    qry="select * from  imp_person where patient_id='"+lid+"'and pname like '%"+name+"%'"
    db=Db()
    res=db.select(qry)

    return jsonify(status="ok",data=res)

@app.route("/and_care_addimpdate",methods=['POST'])
def and_care_addimpdate():
    event=request.form["event"]
    lid=request.form["pid"]
    date=request.form["date"]
    description=request.form["description"]
    pic=request.files["image"]
    pic.save("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\event\\"+event+".jpg")
    path="/static/event/"+event+".jpg"
    qry="insert into reminder(patient_id,event,description,event_date,photo)values('"+lid+"','"+event+"','"+description+"','"+date+"','"+path+"')"
    print(qry)
    db=Db()
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route("/and_viewimpdate",methods=['POST'])
def and_viewimpdate():
    lid=request.form["lid"]
    qry="select * from reminder where patient_id='"+lid+"'"
    print(qry)
    db=Db()
    res=db.select(qry)

    return jsonify(status="ok",data=res)
@app.route("/and_viewimpdate",methods=['POST'])
def and_adddates():
    lid=request.form["lid"]
    qry="select * from reminder where patient_id='"+lid+"'"
    print(qry)
    db=Db()
    res=db.select(qry)

    return jsonify(status="ok",data=res)

@app.route("/caretakerprofile",methods=['POST'])
def caretakerprofile():
    id=request.form["lid"]


    qry="select * from allocation inner join caretaker on caretaker.lid=allocation.caretaker_id where allocation.patient_id='"+id+"'"
    db=Db()
    res=db.selectOne(qry)
    return jsonify(status="ok",name=res["name"],place=res["place"],pincode=res["pin"],post=res["post"],district=res["adhar_no"],email=res["email"],phone=res["phone"],photo=res["photo"],qualification=res["qualification"],gender=res["gender"])
@app.route("/and_progress_insert",methods=['POST'])
def and_progress_insert():
    lid=request.form["lid"]
    type=request.form["type"]
    resul=request.form["result"]
    qry="insert into progress (date,type,status,patient_id) values(curdate(),'"+type+"','"+resul+"','"+lid+"')"
    d=Db()
    d.insert(qry)
    return jsonify(status="ok")

@app.route("/pat_person",methods=['POST'])
def pat_person():
    id=request.form["lid"]


    qry="select * from imp_person where patient_id='"+id+"'"
    db=Db()
    res=db.select(qry)
    if len(res)>0:
        aa=len(res)
        import random

        s=random.randint(0,aa-1)
        if s< aa:
            b=res[s]
            return jsonify(status="ok",name=b["pname"],image=b["image"])
        else:
            return jsonify(status="no")
    return jsonify(status="no")




@app.route("/emotions",methods=['POST'])
def emotions():
    import numpy as np
    a=request.files["pic"]
    aid=request.form["plid"]
    import random
    ss=str(random.randint(1,1200))
    from keras import Sequential
    from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
    a.save("C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\emotion_image\\"+ss_diff+".jpg")
    path="/static/emotion_image/"+ss+".jpg"

    urlpath="C:\\Users\\LENOVO\\Desktop\\project_backup\\try_to_remenber\\static\\emotion_image\\"+ss_diff+".jpg"
    import cv2
    model = Sequential()

    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation='softmax'))

    model.load_weights(r'C:\Users\LENOVO\Desktop\project_backup\try_to_remenber\static\emotionmodel\model.h5')

    # prevents openCL usage and unnecessary logging messages
    cv2.ocl.setUseOpenCL(False)

    # dictionary which assigns each label an emotion (alphabetical order)
    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}




    frame=cv2.imread(urlpath)



    facecasc = cv2.CascadeClassifier(r'C:\Users\\LENOVO\Desktop\project_backup\try_to_remenber\static\emotionmodel\haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        prediction = model.predict(cropped_img)
        # print(prediction)
        maxindex = int(np.argmax(prediction))
        print(emotion_dict[maxindex])


        print(aid,"aaaaaaaaaaaaaaa")

    qry="insert into emotion(patient_lid,image,emotion,date,time) values('"+aid+"','"+path+"','"+str(emotion_dict[maxindex])+"',curdate(),curtime())"
    db=Db()
    db.insert(qry)
    return jsonify(status='ok')

@app.route("/and_puzzle",methods=['POST'])
def and_puzzle():


    qry="select * from puzzle"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",res=res)

@app.route("/edt_fed_viw",methods=['POST'])
def ed_f_v():

    import random
    list = []
    for i in range(1000):
        r = random.randint(1, 16)
        if r not in list:
            list.append(r)
    abc = ""
    for ii in list:
        abc = abc + str(ii) + ","

    # print(abc)

    res = abc
    if res is not None:
        return jsonify(status='ok',fname=res)
    else:
        return jsonify(status='no')

@app.route("/andviewprogress",methods=['POST'])
def andviewprogress():
    lid=request.form["pid"]

    qry="select * from progress where patient_id='"+lid+"'"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",data=res)
@app.route("/and_chnagepassword",methods=['POST'])
def and_chnagepassword():
    lid=request.form["lid"]
    old=request.form["oldpassword"]
    nn=request.form["newpassword"]
    qry="update login set password='"+nn+"' where lid='"+lid+"' and password='"+old+"'"
    db=Db()
    res=db.update(qry)
    return jsonify(status="ok")
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
