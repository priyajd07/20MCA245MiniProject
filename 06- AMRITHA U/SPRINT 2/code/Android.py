import os
from flask import *
from werkzeug.utils import secure_filename



from src.dbconnection import *
from src.myknn import prep

app=Flask(__name__)


@app.route("/logincode",methods=['post'])
def logincode():
    print(request.form)
    username=request.form['username']
    password=request.form['password']
    q="SELECT * FROM `login`WHERE `username`=%s AND`password`=%s"
    val=username,password
    res=selectone(q,val)
    print(res)
    if res is None:
        return jsonify({'task': 'unsuccessfull'})
    else:
        return jsonify({'task': 'success','lid':res[0],'type':res[3]})





@app.route("/farmer",methods=['post'])
def farmer():
    try:
        print(request.form)

        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['Phone']
        place = request.form['Place']
        pin = request.form['pin']
        post = request.form['post']
        email = request.form['Email']
        uname = request.form['username']
        passd = request.form['password']



        qry="INSERT INTO `login` VALUE(null,%s,%s,'farmer')"
        val=(uname,passd)
        id=iud(qry,val)
        qy="insert into farmer values( null,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(id,fname,lname,phone,place,pin,post,email)
        iud(qy,val)
        return jsonify({'task': 'success','id':id})
    except Exception as e:
        print(e)
        return jsonify({'task':str(e)})



@app.route("/viewnotification",methods=['post'])
def viewnotification():

    qry="SELECT * from `notification` "
    res = androidselectallnew(qry)
    print(res)
    return jsonify(res)







@app.route("/feedback",methods=['post'])
def feedback():
    id = request.form['id']
    fd = request.form['feedback']
    qry="INSERT INTO `feedback` VALUE(null,%s,curdate(),%s)"
    val=(fd,id)
    iud(qry,val)
    return jsonify({'task': 'success'})


@app.route("/viewfertilizer",methods=['post'])
def viewfertilizer():

    qry="SELECT * from fertilizer"
    res = androidselectallnew(qry)
    print(res)
    return jsonify(res)




@app.route('/img',methods=['post','get'])
def img():
    id=request.form['id']

    img=request.files['files']
    fn=secure_filename(img.filename)
    img.save("static/chk/"+fn)
    res=prep("static/chk/"+fn)

    print(res[0])
    qry="insert into upload values(null,%s,%s,%s,curdate())"
    val=(id,str(res[0]),fn)
    iud(qry,val)
    if str(res[0])!='0':
        print("Healthy Leaves")
        qry = "insert into upload values(null,%s,'Healthy Leaves',%s,curdate())"
        val = (id, fn)
        iud(qry, val)
        return jsonify('Healthy Leaves')
    else:
        print("Healthy Leaves")
        qry = "insert into upload values(null,%s,'Black rot detected',%s,curdate())"
        val = (id,fn)
        iud(qry, val)
        print("Black rot detected")
        return jsonify('Black rot detected')





@app.route('/views',methods=['post'])
def views():
    lid=request.form['uid']
    print(lid)
    qry="SELECT * FROM login WHERE `lid` NOT IN (SELECT `lid` FROM `farmer`)"
    value=(lid)
    res = androidselectallnew(qry)
    return jsonify(res)


@app.route('/in_message2',methods=['post'])
def in_message():
    print(request.form)
    fromid = request.form['fid']
    print("fromid",fromid)

    toid = request.form['toid']
    print("toid",toid)

    message=request.form['msg']
    print("msg",message)
    qry = "INSERT INTO `chat` VALUES(NULL,%s,%s,%s,CURDATE())"
    value = (fromid, toid, message)
    print("pppppppppppppppppp")
    print(value)
    iud(qry, value)
    return jsonify(status='send')

@app.route('/view_message2',methods=['post'])
def view_message2():
    print("wwwwwwwwwwwwwwww")
    print(request.form)
    fromid=request.form['fid']
    print(fromid)
    toid=request.form['toid']
    print(toid)
    lmid = request.form['lastmsgid']
    print("msgggggggggggggggggggggg"+lmid)
    sen_res = []
    # qry="SELECT * FROM chat WHERE (fromid=%s AND toid=%s) OR (fromid=%s AND toid=%s) ORDER BY DATE ASC"
    qry="SELECT `fid`,`message`,`date`,`chat_id` FROM `chat` WHERE `chat_id`>%s AND ((`tid`=%s AND  `fid`=%s) OR (`tid`=%s AND `fid`=%s)  )  ORDER BY chat_id ASC"

    val=(str(lmid),str(toid),str(fromid),str(fromid),str(toid))
    print("fffffffffffff",val)
    res = androidselectall(qry,val)
    print("resullllllllllll")
    print(res)
    if res is not None:
        return jsonify(status='ok', res1=res)
    else:
        return jsonify(status='not found')



app.run(port=5000,host="0.0.0.0")