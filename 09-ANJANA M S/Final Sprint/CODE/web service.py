from flask import *
from werkzeug.utils import secure_filename

from src.dbconnection import *
from src.recognize_face import *
from src.encode_faces import *
app=Flask(__name__)

@app.route('/login',methods=['post'])
def login():
    username=request.form['username']
    password=request.form['password']
    qry='select * from login where username=%s and password=%s'
    val=(username,password)
    res=selectone (qry,val)
    if res is None:
        return jsonify({'task':'invalid'})
    else:
        return jsonify({'task':'success','id':str(res[0])})

@app.route('/view_time_schedule',methods=['post'])
def view_time_schedule():
    lid=request.form['lid']
    q="SELECT `subject_table`.`subject`,`subject_table`.`semester`,`timetable`.* FROM `timetable` JOIN `subject_table` ON `subject_table`.`id`=`timetable`.`sid` JOIN student_table ON `student_table`.`course`=`subject_table`.`course_id` AND `subject_table`.`semester`=`student_table`.`semester` WHERE `student_table`.login_id=%s"
    res=androidselectall(q,lid)
    return jsonify(res)

@app.route('/view_video_classes',methods=['post'])
def view_video_classes():
    q="SELECT `subject_table`.`subject`,`video`.* FROM `video` JOIN `subject_table` ON `subject_table`.`id`=`video`.`sub_id`"
    res = androidselectallnew(q)
    return jsonify(res)

@app.route('/view_study_material',methods=['post'])
def view_study_material():
    q="SELECT `subject_table`.`subject`,`study_material`.*FROM `study_material` JOIN `subject_table` ON `subject_table`.`id`=`study_material`.`id`"
    res = androidselectallnew(q)
    return jsonify(res)

@app.route('/view_exam_notification',methods=['post'])
def view_exam_notification():
    q="SELECT `subject_table`.`subject`,`exam`.* FROM `exam` JOIN `subject_table` ON `subject_table`.`id`=`exam`.`sid`"
    res = androidselectallnew(q)
    print(res)
    return jsonify(res)


@app.route('/upload_answer_paper',methods=['post'])
def upload_answer_paper():
    print(request.form)
    studid=request.form['lid']
    exmid=request.form['eid']
    anspaper=request.files['file']
    answerpaper= secure_filename(anspaper.filename)
    print("artyujk========",answerpaper)
    anspaper.save("static/anspaper/"+answerpaper)
    qry="SELECT HOUR(TIMEDIFF(CURTIME(),`time`)),MINUTE(TIMEDIFF(CURTIME(),`time`) ),`duration` FROM `exam` WHERE `id`=%s"
    val=(exmid)
    res=selectone(qry,val)
    dur=float(res[2])*60
    print(dur)
    ttime=str(res[0])+"."+str(res[1])
    ttime=float(ttime)
    print(ttime)
    if ttime<=dur:
        q="INSERT INTO`answer` VALUES (NULL,%s,%s,%s,CURDATE(),curtime())"
        val=(studid,exmid,answerpaper)
        iud(q,val)
        return jsonify({'task': 'success'})
    else:
        return jsonify({'task': 'time out'})

@app.route('/view_staff')
def view_staff():
    q="SELECT*FROM `staff_table`"
    res = androidselectallnew(q)
    return jsonify(res)

@app.route('/view_sub',methods=['post'])
def view_sub():
    lid=request.form['lid']
    q="SELECT `subject_table`.* FROM `subject_table` JOIN `student_table` ON `subject_table`.`course_id`=`student_table`.`course` WHERE `student_table`.`login_id`=%s "
    res = androidselectall(q,lid)
    return jsonify(res)

@app.route('/viewstaff',methods=['post'])
def viewstaff():
    print(request.form)
    lid=request.form['lid']
    qry="SELECT * FROM `staff_table`"

    res = androidselectallnew(qry)
    res11=[]
    for i in res:
        print(i)
        sid=i['login_id']
        qry="SELECT SUM(`status`) FROM `chat` WHERE `from_id`=%s AND `to_id`=%s"
        val=(sid,lid)
        res1=selectone(qry,val)
        re=str(res1[0])
        print(str(res1[0]))
        if re=="None":
            re="0"
        i["list"]=re
        res11.append(i)
    print(res11)
    print(res,"===============================")
    return jsonify(res)

#############################################################
@app.route('/addimg',methods=['post','get'])
def addimg():
    img=request.files['files']
    import time
    fn=time.strftime("%Y%m%d_%H%M%S")+".jpg"
    img.save("static/pic/"+fn)
    q="SELECT `student_table`.`login_id`,`student_table`.`first_name`,`pics`.`pic` FROM `student_table` JOIN `pics` ON `student_table`.`login_id`=`pics`.`stud_id`"
    s=selectall(q)
    enf("static/pic/"+fn)
    for r in s:
        res=rec_face_image("static/pic/"+r[2])
        if len(res)>0:
            return jsonify({"result":r[1]+"#"+str(r[0])})
    return jsonify({"result": "na" + "#" + fn})


app.run(host='0.0.0.0',port=5000)




