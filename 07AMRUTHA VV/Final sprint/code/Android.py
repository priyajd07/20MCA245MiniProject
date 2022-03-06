from flask import*
from src.dbconn import *
app=Flask(__name__)
import os
from werkzeug.utils import secure_filename

@app.route('/login',methods=['post'])
def login():
    uname = request.form['uname']
    pswd = request.form['pass']
    qry="select * from login where username=%s and password=%s and type='user' "
    val=(uname,pswd)
    # print(val)
    res=selectone(qry,val)
    if res is None:
        return jsonify({'task': "invalid"})

    else:
        return jsonify({'task': "valid",'id': res[0]})


@app.route('/reg', methods=['post'])
def reg():
    try:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        post=request.form['post']
        pin=request.form['pin']
        gender=request.form['gender']
        phone=request.form['phone']
        email=request.form['email']
        uname=request.form['uname']
        pswd=request.form['pswd']
        qry="insert into login values(NULL,%s,%s,'user')"
        val=(uname,pswd)
        id=iud(qry,val)
        qry1="insert into registration values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val1=(str(id),fname,lname,gender,place,post,pin,phone,email)
        iud(qry1,val1)
        return jsonify({'task':'success'})
    except Exception as e:
        return jsonify({'task': 'already exist'})


@app.route('/sndfeedback', methods=['post'])
def sndfeedback():
    lid=request.form['lid']
    feedback=request.form['feedback']
    qry="insert into feedback values(NULL,%s,curdate(),%s)"
    val=(feedback,lid)
    iud(qry,val)
    return jsonify({'task':'success'})
@app.route('/viewtips', methods=['post'])
def viewtips():
    qry="select*from tips"
    res=androidselectallnew(qry)
    return jsonify(res)

@app.route('/viewtreatments', methods=['post'])
def viewtreatments():
    qry="select*from treatment"
    res=androidselectallnew(qry)
    return jsonify(res)


@app.route('/uploadimage',methods=['post'])
def uploadimage():

    image=request.files['file']
    im= secure_filename(image.filename)
    image.save(os.path.join("static/uploads", im))
    lid=request.form['lid']
    from src.newcnn import predictcnn
    res = predictcnn(os.path.join("static/uploads",im))
    print("resssssssssssss",res)
    qry="select * from dataset where `dateset_id`=%s"
    reslt=selectone(qry,res)
    if reslt is None:
        result="invalid"
    else:
        result=reslt[1]+"-"+reslt[2]
    qry="INSERT INTO `upload` VALUES(NULL,%s,%s,%s,curdate())"
    val=(lid,result,im)
    iud(qry,val)
    return jsonify({"task":result,'img':im})



app.run(host="0.0.0.0",port="5000")
