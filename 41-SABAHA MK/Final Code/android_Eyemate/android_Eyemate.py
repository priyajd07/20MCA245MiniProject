import face_recognition
from flask import Flask, render_template, request, jsonify, session
from DBConnection import Db

app = Flask(__name__)

app.secret_key="hiiii"



@app.route('/')
def login():
    return render_template('login.html')


@app.route('/forget')
def forget():
    return render_template('forgetpassword.html')


@app.route('/adminhome')
def home():
    return render_template('admin/home.html')


@app.route('/login_post',methods=['post'])
def login_post():
    uname=request.form["textfield"]
    password=request.form["textfield2"]
    qry="SELECT * FROM `login` WHERE `username`='"+uname+"' AND `password`='"+password+"'"
    d = Db()
    res = d.selectOne(qry)
    if res is not None:
        session['l_id']=res['lid']
        type=res['type']

        if res["type"]=="admin":
            return home()
        else:
            return '''<script>alert("This user not allowed to login"); window.location='/'</script>'''
    else:
        return '''<script>alert("Invalid username and password"); window.location='/'</script>'''


@app.route('/caretaker')
def caretaker():
    qry="SELECT * FROM`caretaker`"
    d=Db()
    res=d.select(qry)
    return render_template('admin/caretaker.html',data=res)



@app.route('/view_blindinfo/<cid>')
def view_blindinfo(cid):
    qry="SELECT * FROM `blind` where caretaker_lid='"+cid+"' "
    d = Db()
    res = d.select(qry)
    return render_template('admin/view blind info.html',data=res)




@app.route('/view review',)
def view_review():
   qry="SELECT `review`.*,`caretaker`.name,`caretaker`.email FROM `review` INNER JOIN `caretaker` ON`review`.car_lid=`caretaker`.lid"
   d = Db()
   res = d.select(qry)
   return render_template('admin/view review.html',data=res)




@app.route('/view review',methods=['post'])
def view_review_post():
    datefrom = request.form["textfield"]
    to = request.form["textfield2"]
    qry="SELECT `review`.*,`caretaker`.name,`caretaker`.email FROM `review` INNER JOIN `caretaker` ON`review`.car_lid=`caretaker`.lid where date between '"+datefrom+"' and '"+to+"'"
    d = Db()
    res = d.select(qry)
    return render_template('admin/view review.html',data=res)


@app.route('/caretaker_post',methods=['post'])
def caretaker_post56():
    to=request.form["textfield"]
    qry = "SELECT * FROM`caretaker` where name like '%"+to+"%'"
    d = Db()
    res = d.select(qry)
    return render_template('admin/caretaker.html', data=res)

@app.route('/change_password')
def change_password():
    return render_template('change_password.html')

@app.route('/change_password_post',methods=['post'])
def change_password_post():
    current_password=request.form['textfield']
    new_password = request.form['textfield2']
    confirm_password = request.form['textfield3']
    d=Db()
    qry="SELECT * FROM `login` WHERE PASSWORD='"+current_password+"' and lid='"+str(session['l_id'])+"'"
    res=d.selectOne(qry)
    if res is not None:
        if(new_password==confirm_password):
            qry2="UPDATE `login` SET `password`='"+new_password+"' where lid='"+str(session['l_id'])+"'"
            res2=d.update(qry2)
            return '''<script>alert('password changed successfully');window.location='/'</script>'''
        else:
            return '''<script>alert('password not matched');window.location='/change_password'</script>'''
    else:
        return '''<script>alert('password not matched');window.location='/change_password'</script>'''







#######android portion

@app.route('/andlogin_post',methods=['post'])
def andlogin_post():
    uname = request.form["uname"]
    password = request.form["password"]

    print(uname,password)

    qry = "SELECT * FROM `login` WHERE `username`='" + uname + "' AND `password`='" + password + "' and type='caretaker'"
    d = Db()
    res = d.selectOne(qry)
    if res is not None:
        return jsonify(status="ok",lid=res['lid'])
    else:
        return jsonify(status="no")
''
@app.route('/signup_post', methods=['post'])
def signup_post():
    name = request.form["name"]
    mobilenumber= request.form["mobilenumber"]
    place = request.form["place"]
    district = request.form["district"]
    email = request.form["email"]
    password = request.form["password"]
    qry="INSERT INTO login(username,PASSWORD,TYPE) VALUE('"+name+"','"+password+"','caretaker')"
    db=Db()
    lid=db.insert(qry)
    qry="INSERT INTO caretaker(NAME,place,mobileno,district,email,lid) VALUE ('"+name+"','"+place+"','"+mobilenumber+"','"+district+"','"+email+"','"+str(lid)+"')"
    db.insert(qry)
    return jsonify(status="ok")

@app.route('/add_blind_post', methods=['post'])
def add_blind_post():
    name = request.form["name"]
    place= request.form["place"]
    mobileno = request.form["mobile"]
    district = request.form["district"]
    pin = request.form["pin"]
    caretaker_lid = request.form["lid"]

    image = request.form["image"]
    import time
    import base64

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(image)
    fh = open("C:\\Users\\HP\\PycharmProjects\\android_Eyemate\\static\\blind_img\\" + timestr + ".jpg", "wb")
    path = "/static/blind_img/" + timestr + ".jpg"
    fh.write(a)
    fh.close()


    qry="INSERT INTO blind(NAME,place,mobileno,district,pin,caretaker_lid,image) VALUE  ('"+name+"','"+place+"','"+mobileno+"','"+district+"','"+pin+"','"+str(caretaker_lid)+"','"+path+"')"
    db=Db()
    db.insert(qry)
    return jsonify(status="ok")



@app.route('/view_blind_post', methods=['post'])
def view_blind_post():
    caretaker_lid = request.form["caretaker_lid"]
    qry="SELECT * FROM blind WHERE caretaker_lid ` = '"+caretaker_lid+"'"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/add_familiar_person', methods=['post'])
def add_familiar_person():
    image= request.form["image"]
    import time
    import base64

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(image)
    fh = open("C:\\Users\\HP\\PycharmProjects\\android_Eyemate\\static\\f_person\\" + timestr + ".jpg", "wb")
    path = "/static/f_person/" + timestr + ".jpg"
    fh.write(a)
    fh.close()
    name = request.form["name"]
    place = request.form["place"]
    mobileno = request.form["mobileno"]
    district= request.form["district"]
    pin= request.form["pin"]
    blindid= request.form["blindid"]
    qry="INSERT into `familiar person`(image,NAME,place,mobileno,district,pin,blindid) VALUE ('"+path+"','"+name+"','"+place+"','"+mobileno+"','"+district+"','"+pin+"','"+blindid+"')"
    db=Db()
    db.insert(qry)
    return jsonify(status="ok")

@app.route('/send_review_post', methods=['post'])
def send_review_post():
    car_lid = request.form["car_lid"]
    feedback = request.form["feedback"]

    qry="INSERT INTO `review`(car_lid,review,DATE) VALUE ('"+car_lid+"','"+feedback+"',curdate())"
    db=Db()
    res=db.insert(qry)
    return jsonify(status="ok")


@app.route('/caretaker_view_blind_post', methods=['post'])
def caretaker_view_blind_post():
    caretaker_id = request.form["caretaker_id"]

    qry="SELECT*FROM `blind` WHERE `caretaker_lid`='"+caretaker_id+"'"
    print(qry)

    db = Db()
    res = db.select(qry)
    print(res)
    return jsonify(status="ok",data=res)


@app.route('/delete_blind_post', methods=['post'])
def delete_blind_post():
    blindid = request.form["blindid"]
    db=Db()
    qry="DELETE FROM`blind`WHERE `blindid`='"+blindid+"'"
    db.delete(qry)
    return jsonify(status="ok")

@app.route('/delete_familiar_person_post', methods=['post'])
def delete_familiar_person_post():
    fmid = request.form["fmid"]
    db=Db()
    qry="DELETE FROM`familiar person` WHERE`fmid`='"+fmid+"'"
    db.delete(qry)
    return jsonify(status="ok")


@app.route('/familiar_person_post', methods=['post'])
def familiar_person_post():
    blind_id = request.form["blindid"]

    qry="SELECT *FROM`familiar person` WHERE`blindid`='"+blind_id+"'"
    print(qry)
    db = Db()
    res = db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/emergency_help_post', methods=['post'])
def emergency_help_post():
    car_lid = request.form["car_lid"]

    qry="SELECT `help`.*,`blind`.`name` FROM `help` INNER JOIN `blind` ON `help`.`blindid`=`blind`.`blindid` WHERE `blind`.`caretaker_lid`='"+car_lid+"'"
    print(qry)
    db = Db()
    res = db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/emergency_addhelp_post', methods=['post'])
def emergency_addhelp_post():
    blindid= request.form["blindid"]
    lattitude= request.form["lattitude"]
    longitude= request.form["longitude"]


    a="INSERT INTO`help`(blindid,lattitude,longitude,DATE,TIME) VALUES ('"+blindid+"','"+lattitude+"','"+longitude+"',CURDATE(),CURTIME())"
    db = Db()
    res = db.insert(a)
    return jsonify(status="ok")

@app.route('/location_post', methods=['post'])
def location_post():
    blindid = request.form["blindid"]
    lattitude = request.form["lattitude"]
    longitude = request.form["longitude"]

    b="INSERT INTO`location`(`blind id`,lattitude,longitude,DATE)VALUES('"+blindid+"','"+lattitude+"','"+longitude+"',CURDATE())"
    db = Db()
    res = db.insert(b)
    return jsonify(status="ok")


@app.route('/face_recognition_post', methods=['post'])
def face_recognition_post():
    blind_pic_path= "C:\\Users\\HP\\PycharmProjects\\android_Eyemate\\static\\a.jpg"


    bid = request.form["bid"]
    # bid="2"
    photo = request.files["pic"]
    photo.save(blind_pic_path)
    qry = "SELECT * FROM `familiar person` WHERE blindid='"+bid+"'"
    print(qry)
    db = Db()
    res = db.select(qry)
    known_faces = []
    userids = []
    person_name = []

    identified = ""
    if res is not None:
        for result in res:
            img = "C:\\Users\\HP\\PycharmProjects\\android_Eyemate" + result["image"]
            print(img)
            b_img = face_recognition.load_image_file(img)
            b_imgs = face_recognition.face_encodings(b_img)[0]
            known_faces.append(b_imgs)
            userids.append(result["fmid"])
            person_name.append(result["name"])
            print(img + "done")

        unknown_image = face_recognition.load_image_file(blind_pic_path)
        unkonownpersons = face_recognition.face_encodings(unknown_image)

        if len(unkonownpersons) > 0:

            for i in range(0, len(unkonownpersons)):
                h = unkonownpersons[i]

                red = face_recognition.compare_faces(known_faces, h, tolerance=0.45)  # true,false,false,false]

                for i in range(0, len(red)):
                    if red[i] == True:
                        identified = identified + person_name[i]

            print("1")

            return jsonify(status="ok", result=identified)
        else:

            print("2")
            return jsonify(status="no", result="Person not found")








#######android portion ends


@app.route('/blank')
def blank():
    return  render_template('blank.html')







if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
