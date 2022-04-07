from flask import *
app=Flask(__name__)
from src.dbconnection import *

@app.route('/login',methods=['post'])
def login():
    uname=request.form['username']
    pwd=request.form['password']
    qry="SELECT * FROM login WHERE username=%s AND PASSWORD=%s and type='staff'"
    val=(uname,pwd)
    res=selectone(qry,val)
    if res is None:
        return jsonify({'task':'invalid'})
    else:
        if res[3]=='staff':
            return jsonify({'task': 'valid','id':res[0]})







@app.route('/viewwork',methods=['post'])
def viewwrk():
    staffid=request.form['lid']
    qry="select* from work where staff_lid=%s and status='pending'"
    res=androidselectall(qry,staffid)
    return jsonify(res)

@app.route('/camnoti',methods=['post'])
def camnoti():

    qry="SELECT `camnoti`.*,`camera`.`cameranumber` FROM `camera` JOIN `camnoti` ON `camera`.`id`=`camnoti`.`camid`  WHERE `status`='pending'"
    res=androidselectallnew(qry)
    qry="UPDATE `camnoti` SET `status`='viewed' WHERE `status`=%s"
    val=('pending')
    iud(qry,val)

    return jsonify(res)

@app.route('/updatestts',methods=['post'])
def updatestts():
    wid=request.form['wid']
    status=request.form['status']
    print(status)
    qry="update work set status=%s where id=%s"
    val=(status,wid)
    print(val)
    iud(qry,val)
    return jsonify({'task':'success'})

@app.route('/viewnoti',methods=['post'])
def viewnoti():
    staffid=request.form['lid']
    # print(staffid)
    qry="select * from notification where staffid=%s"
    res=androidselectall(qry,staffid)
    # print(res)
    return jsonify(res)

@app.route('/viewcamnoti',methods=['post'])
def viewcamnoti():
    qry="select*from camnoti"
    res=androidselectallnew(qry)
    return jsonify(res)



app.run(host='0.0.0.0',port=5000)