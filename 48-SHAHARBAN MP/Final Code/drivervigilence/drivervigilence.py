import base64
from logging import log

from flask import Flask, json, render_template, request,jsonify
from DBConnection import Db
app = Flask(__name__)
static_path="C:\\Users\\MUHAMMED ASLAM\\Desktop\\New folder\\drivervigilence\\static\\"



@app.route('/')
def admin():
    return render_template("index.html")

@app.route('/logout')
def logout():
    return render_template("index.html")




@app.route('/adm_addnotification')
def adm_addnotification():
    return render_template("admin/addnotification.html")

@app.route('/adm_addnotification_post',methods=['post'])
def adm_addnotification_post():
    subject = request.form['textfield']
    content = request.form['textarea2']
    db = Db()
    qry2 = "insert into notification(subject,content,date) values('"+subject+"','"+content+"',curdate())"
    res2 = db.insert(qry2)
    return '''<script>alert("success");window.location="/adm_addnotification"</script>'''

@app.route('/adm_viewnotification')
def adm_viewnotification():
    db=Db()
    qry="select * from notification "
    res=db.select(qry)
    return render_template("admin/viewnotification.html", data=res)

@app.route('/adm_viewnotification_post',methods=['post'])
def adm_viewnotification_post():
    db = Db()
    f = request.form['textfield']
    t=request.form['textfield2']
    qry = "select * from notification WHERE date Between '"+f+"'and'"+t+"'"
    res = db.select(qry)
    return render_template("admin/viewnotification.html", data=res)

@app.route('/adm_deletenotification/<id>')
def adm_deletenotification(id):
    db=Db()
    qry="delete from notification where not_id='"+id+"'"
    print(qry)
    res=db.delete(qry)
    return '''<script>alert("deleted");window.location="/adm_viewnotification"</script>'''



@app.route('/adm_editnotification/<id>')
def adm_editnotification(id):
    db=Db()
    qry="select * from notification where not_id='"+id+"'"
    print(qry)
    res=db.selectOne(qry)
    return render_template("admin/editnotification.html", data=res)

@app.route('/adm_editnotification_post',methods=['post'])
def adm_editnotification_post():
    db=Db()
    noti_id=request.form['notification_id']
    subject=request.form['textfield']
    content=request.form['textarea2']

    qry="update notification set subject='"+subject+"',content='"+content+"', date=curdate() where not_id='"+noti_id+"'"
    print(qry)
    res=db.update(qry)
    return '''<script>alert("success");window.location="/adm_viewnotification"</script>'''


@app.route('/adm_changepassword')
def adm_changepassword():
    return render_template("admin/changepassword.html")

@app.route('/adm_changepassword_post',methods=['post'])
def adm_changepassword_post():
    oldpassword=request.form['textfield']
    newpassword=request.form['textfield2']
    conformpassword=request.form['textfield3']
    db = Db()
    qry = "select * from login WHERE password='" +oldpassword+"' and user_type='admin'"
    res = db.selectOne(qry)

    if res==None:
        return '''<script>alert("old password not match");window.location="/adm_login"</script>'''

    else:
        if newpassword==conformpassword:
            qry1 = "update login set  password='"+newpassword+"' where user_type='admin'"
            res1 = db.update(qry1)
            return '''<script>alert("successs");window.location="/adm_login"</script>'''

            return render_template('login.html')
        else:
            return '''<script>alert("error");window.location="/adm_changepassword"</script>'''



@app.route('/adm_cmplntrply/<id>')
def adm_cmplntrply(id):
    db=Db()
    qry="select * from complaints WHERE complaint_id='"+id+"'"
    print(qry)
    res=db.selectOne(qry)
    return render_template('admin/cmplntrply.html', data=res)

@app.route('/adm_cmplntrply_post',methods=['post'])
def adm_cmplntrply_post():
  db=Db()
  replay=request.form['textfield']
  id = request.form['textfield2']
  qry="update complaints set replay='"+replay+"'where complaint_id='"+id+"'"
  res=db.update(qry)
  return '''<script>alert("successs");window.location="/adm_viewcompsndrply"</script>'''


@app.route('/adm_login')
def adm_login():
    return render_template("index.html")

@app.route('/ahome')
def ahome():
    return render_template("admin/home.html")

@app.route('/adm_login_post',methods=['post'])
def adm_login_post():
    username = request.form['textfield']
    password = request.form['textfield2']
    db = Db()
    qry = "select * from login WHERE user_name='"+username+"' and password='"+password+"'"
    res = db.selectOne(qry)
    if res == None:
        return '''<script>alert("invalid username & password");window.location="/adm_login"</script>'''

    else:
        if res['user_type']=='admin':
            return render_template('admin/home.html')
        else:
            return 'hi'


@app.route('/adm_viewcompsndrply')
def adm_viewcompsndrply():
    db = Db()
    qry = "select driver.name,driver.place,driver.contact_no,driver.email,complaints.*from driver inner join complaints on driver.driverlogin_id=complaints.driverlogin_id"
    res = db.select(qry)
    return render_template("admin/viewcomp&sndrply.html", data=res)

@app.route('/adm_viewcompsndrply_post',methods=['post'])
def adm_viewcompsndrply_post():
  db=Db()
  f=request.form['textfield']
  t=request.form['textfield2']
  qry="select driver.name,driver.place,driver.contact_no,driver.email,complaints.*from driver inner join complaints on driver.driverlogin_id=complaints.driverlogin_id where date Between '"+f+"'and '"+t+"'"
  print(qry)
  res=db.select(qry)
  return render_template("admin/viewcomp&sndrply.html", data=res)


@app.route('/adm_viewdrivers')
def adm_viewdrivers():
    db = Db()
    qry = "select * from driver"
    res = db.select(qry)
    return render_template("admin/viewdrivers.html", data=res)

@app.route('/adm_viewdrivers_post',methods=['post'])
def adm_viewdrivers_post():
    db=Db()
    search=request.form['textfield']
    qry="select * from driver WHERE name like '%"+search+"%'"
    res=db.select(qry)
    return render_template('admin/viewdrivers.html', data=res)


@app.route('/adm_viewfdbckfrmdrvr')
def adm_viewfdbckfrmdrvr():
    db = Db()
    qry = "select driver.name,driver.place,driver.contact_no,driver.email,feedback.*from driver inner join feedback on driver.driverlogin_id=feedback.driverlogin_id"
    res = db.select(qry)
    return render_template("admin/viewfdbckfrmdrvr.html", data=res)

@app.route('/adm_viewfdbckfrmdrvr_post',methods=['post'])
def adm_viewfdbckfrmdrvr_post():
    db = Db()
    f = request.form['textfield']
    t = request.form['textfield2']
    qry="select driver.*,feedback.*from driver inner join feedback on driver.driverlogin_id=feedback.driverlogin_id where feedback.date between '"+f+"'and '"+t+"'"
    res = db.select(qry)
    return render_template("admin/viewfdbckfrmdrvr.html", data=res)


# ''''''''''''''templates''''''''''''''''#



@app.route('/and_login',methods=['post'])
def and_login():
    username = request.form['user']
    password = request.form['pass']
    db = Db()
    qry = "select * from login WHERE user_name='"+username+"' and password='"+password+"'"
    res = db.selectOne(qry)
    if res is None:
        return jsonify(status="no")
    elif res['user_type'] == "admin":
        return jsonify(status="no")
    else:
        return jsonify(status="ok",lid=res['login_id'],type=res['user_type'])



@app.route('/and_signup',methods=['post'])
def and_signup():
    name = request.form['name']
    houseno = request.form['hsno']
    place = request.form['place']
    post = request.form['post']
    pin= request.form['pin']
    contactno = request.form['cntctno']
    email = request.form['email']
    image = request.form['image']
    reg_type = request.form['reg_type']
    password=request.form['pass']
    db = Db()
    qry1="insert into login(user_name,password,user_type) values('"+email+"','"+password+"','"+reg_type+"')"
    lid=db.insert(qry1)
    import time
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(image)
    if reg_type=="driver":
        fh = open(static_path+"driver_image\\" + timestr + ".jpg", "wb")
        path = "/static/driver_image/" + timestr + ".jpg"
        fh.write(a)
        fh.close()
        qry = "insert into driver(driverlogin_id,name,house_no,place,post,pin,contact_no,email,photo) values('"+str(lid)+"','"+name+"','"+houseno+"','"+place+"','"+post+"','"+pin+"','"+contactno+"','"+email+"','"+path+"')"
        res = db.insert(qry)
        db.insert("insert into location(driverlogin_id, date, time) values('"+str(lid)+"', curdate(), curtime())")
        return jsonify(status="ok")
    else:
        fh = open(static_path+"user_image\\" + timestr + ".jpg", "wb")
        path = "/static/user_image/" + timestr + ".jpg"
        fh.write(a)
        fh.close()
        qry = "insert into partner(partnerlogin_id,name,house_no,place,post,pin,contact_no,email,photo)VALUES('"+str(lid)+"','"+name+"', '"+houseno+"','"+place+"','"+post+"','"+pin+"','"+contactno+"','"+email+"','"+path+"')"
        res = db.insert(qry)
        return  jsonify(status="ok")

@app.route('/and_changepassword', methods=['post'])
def and_changepassword():
        lid = request.form['lid']
        oldpassword = request.form['oldpass']
        newpassword = request.form['newpass']
        db = Db()
        qry = "select * from login WHERE password='" + oldpassword + "' and login_id='"+str(lid)+"'"
        res = db.selectOne(qry)
        if res is None:
            return jsonify(status="no")
        else:
                qry1 = "update login set  password='" + newpassword + "' where login_id='"+str(lid)+"'"
                res1 = db.update(qry1)
                return jsonify(status="ok")



@app.route('/and_view_profile_driver', methods=['post'])
def and_view_profile_driver():
    lid=request.form['lid']
    db = Db()
    qry = "select * from driver where driverlogin_id='"+lid+"'"
    res = db.selectOne(qry) 
    return jsonify(status="ok", name=res['name'], phone=res['contact_no'], email=res['email'], photo=res['photo'],
            house=res['house_no'], place= res['place'] , post=res['post'] , pin=res['pin'])

@app.route('/and_edit_profile_driver', methods=['post'])
def and_edit_profile_driver():
    db=Db()
    lid = request.form['lid']
    name = request.form['name']
    houseno = request.form['hsno']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    contactno = request.form['cntctno']
    image = request.form['image']
    if len(image)!=0:
        import time
        timestr = time.strftime("%Y%m%d-%H%M%S")
        print(timestr)
        a = base64.b64decode(image)
        fh = open(static_path+"driver_image\\" + timestr + ".jpg", "wb")
        path = "/static/driver_image/" + timestr + ".jpg"
        fh.write(a)
        fh.close()
        qry="update driver set name='"+name+"', house_no='"+houseno+"', place='"+place+"', post='"+post+"', pin='"+pin+"', contact_no='"+contactno+"', photo='"+path+"' where driverlogin_id='"+lid+"'"
    else:
        qry="update driver set name='"+name+"', house_no='"+houseno+"', place='"+place+"', post='"+post+"', pin='"+pin+"', contact_no='"+contactno+"' where driverlogin_id='"+lid+"'"
    
    db=Db()
    db.update(qry)
    return  jsonify(status="ok")

@app.route('/and_view_notification', methods=['post'])
def and_view_notification():
    db = Db()
    qry = "select * from notification order by not_id desc"
    res = db.select(qry)
    return jsonify(status="ok", data=res)

@app.route('/insertintodriverlogs', methods=['post'])
def insertintodriverlogs():
    lati = request.form['lati']
    longi = request.form['longi']
    lid = request.form['lid']
    angle = request.form['angle']
    speed= request.form['speed']
    place= request.form['place']
    db = Db()
    db.update("update location set location='"+place+"', latitude='"+lati+"', longitude='"+longi+"', date=curdate(), time=curtime() where driverlogin_id='"+lid+"'")
    qry = "insert into driver_logs(driverlogin_id,speed,angle,date,time, latitude, longitude) values('"+lid+"','"+speed+"','"+angle+"',curdate(), curtime(), '"+lati+"','"+longi+"')"
    db.insert(qry)

    asss = ""
    if speed=='':
        speed="0"
    if float(speed) < 40:
        asss = "0-40"
    elif float(speed) < 60:
        asss = "40-60"
    else:
        asss = ">60"

    distrupt="no"

    qry = "SELECT *, SQRT( POW(69.1 * (`latitude` - '" + lati + "'), 2) +POW(69.1 * ('" + longi + "' - `longitude`) * COS(`latitude` / 57.3), 2)) AS distance FROM distraction  HAVING distance < 25 ORDER BY distance;"
    distruptions = db.selectOne(qry)
    if distruptions is not None:
        distrupt = distruptions['placename']
    else:
        distrupt="no"
    print(distruptions)


    
    fs = "SELECT `mode`,`brightness`,`touch`,`callblock`,auto_msg,`msg_type`,`message` from `speed_settings` where `driver_lid`='" + str(
        lid) + "' and `speed`='" + asss + "'"
    ds = db.selectOne(fs)
    print('------------------',ds)

    if ds is not None:
        return jsonify(status='ok', mode=ds['mode'], bri=ds['brightness'], tch=ds['touch'], blk=ds['callblock'], typ=ds['auto_msg'], msg=ds['message'], distrupt=distrupt)
    else:
        print("QQQQQ")
        return jsonify(status='no', distrupt=distrupt)


@app.route("/and_check_disrupt", methods=['post'])
def and_check_disrupt():
    lati=request.form['lati']
    logi=request.form['longi']
    db=Db()
    qry = "SELECT *, SQRT( POW(69.1 * (`latitude` - '" + lati + "'), 2) +POW(69.1 * ('" + logi + "' - `longitude`) * COS(`latitude` / 57.3), 2)) AS distance FROM distraction  HAVING distance < 25 ORDER BY distance;"
    distruptions = db.selectOne(qry)
    if distruptions is not None:
        distrupt=distruptions['placename']
        return jsonify(status="ok", dist=distrupt )
    else:
        return  jsonify(status="no")

@app.route("/driverspeedsetting_view", methods=['post'])
def driverspeedsetting_view():
    did=request.form['driverid']
    speed=request.form['speed']
    db=Db()
    qry="select * from speed_settings where driver_lid='"+did+"' and speed='"+speed+"'"
    print(qry)
    res=db.selectOne(qry)
    if res is not None:
        return jsonify(status="ok", mode=res['mode'], bright=res['brightness'], touch=res['touch'], callblock=res['callblock'],
                       automessage=res['auto_msg'], messagetype=res['msg_type'], message=res['message'])
    else:
        return jsonify(status='no')

@app.route("/driverspeed_settings", methods=['post'])
def driverspeed_settings():
    did=request.form['driverid']
    speed=request.form['speed']
    mode=request.form['mode']
    brightness=request.form['brightness']
    touch=request.form['touch']
    callblock=request.form['callblock']
    automessage=request.form['automessage']
    message=request.form['message']
    messagetype=request.form['messagetype']
    db = Db()
    qry = "select * from speed_settings where driver_lid='" + did + "' and speed='" + speed + "'"
    res = db.selectOne(qry)
    if res is None:
        qry="insert into speed_settings(driver_lid,speed,mode,brightness,touch,callblock,auto_msg,msg_type,message)" \
            " values('"+did+"','"+speed+"','"+mode+"','"+brightness+"','"+touch+"','"+callblock+"','"+automessage+"','"+messagetype+"','"+message+"')"
        db.insert(qry)
    else:
        qry="update speed_settings set mode='"+mode+"', brightness='"+brightness+"', touch='"+touch+"', callblock='"+callblock+"', auto_msg='"+automessage+"', msg_type='"+messagetype+"', message='"+message+"' where driver_lid='"+did+"' and speed='"+speed+"'"
        db.update(qry)
    return jsonify(status="ok")

@app.route('/and_driver_send_feedback', methods=['post'])
def and_driver_send_feedback():
    feedback = request.form['feed']
    lid = request.form['lid']
    db = Db()
    res=db.selectOne("select * from feedback where driverlogin_id='"+lid+"'")
    if res is not None:
        qry1 = "update feedback set feedback='" + feedback + "', date=curdate() where driverlogin_id='" + lid + "'"
    else:
        qry1="insert into feedback(driverlogin_id, feedback, date)  values('"+lid+"','"+feedback+"',curdate())"
    db.update(qry1)
    return jsonify(status="ok")



@app.route('/and_driver_view_reply', methods=['post'])
def and_driver_view_reply():
    lid=request.form['lid']
    db = Db()
    qry = "select * from complaints where driverlogin_id='"+lid+"'"
    res = db.select(qry)
    if len(res)==0:
        return jsonify(status='no')
    else:
        return jsonify(status="ok", data=res)

@app.route('/and_driver_delete_complaint', methods=['post'])
def and_driver_delete_complaint():
    cid=request.form['cid']
    db = Db()
    qry = "delete from complaints where complaint_id='"+cid+"'"
    db.delete(qry)
    return jsonify(status="ok")

@app.route('/and_driver_send_complaint', methods=['post'])
def and_driver_send_complaint():
    comp = request.form['comp']
    lid = request.form['lid']
    db = Db()
    qry = "insert into complaints(driverlogin_id, complaint, replay, status, date) values('"+lid+"', '"+comp+"', 'pending', 'pending', curdate())"
    db.insert(qry)
    return jsonify(status="ok")









@app.route('/and_driver_view_partners', methods=['post'])
def and_driver_view_partners():
    lid=request.form['lid']
    db = Db()
    qry = "select partner.*, driver_add_partner.date, driver_add_partner.dap_id from driver_add_partner inner join partner on partner.partnerlogin_id=driver_add_partner.partnerlogin_id where driver_add_partner.driverlogin_id='"+lid+"'"
    res = db.select(qry)
    return jsonify(status="ok", data=res)

@app.route('/and_driver_delete_partner', methods=['post'])
def and_driver_delete_partner():
    pid=request.form['pid']
    db = Db()
    qry = "delete from driver_add_partner where dap_id='"+pid+"'"
    db.delete(qry)
    return jsonify(status="ok")


@app.route('/and_driver_view_users', methods=['post'])
def and_driver_view_users():
    lid=request.form['lid']
    db = Db()
    qry = "select * from partner where partnerlogin_id not in (select partnerlogin_id from driver_add_partner where driverlogin_id='"+lid+"')"
    res=db.select(qry)
    if res is None:
        return jsonify(status='no')
    else:
        return jsonify(status="ok", data=res)

@app.route('/and_driver_search_users', methods=['post'])
def and_driver_search_users():
    lid=request.form['lid']
    name=request.form['name']
    db = Db()
    qry = "select * from partner where name like '%"+name+"%' and partnerlogin_id not in (select driver_add_partner.partnerlogin_id from driver_add_partner inner join partner on partner.partnerlogin_id=driver_add_partner.partnerlogin_id where driver_add_partner.driverlogin_id='"+lid+"')"
    res=db.select(qry)
    if res is None:
        return jsonify(status='no')
    else:
        return jsonify(status="ok", data=res)

@app.route("/and_driver_add_partner", methods=['post'])
def and_driver_add_partner():
    lid=request.form['lid']
    p_lid=request.form['p_lid']
    db=Db()
    qry="insert into driver_add_partner(driverlogin_id, partnerlogin_id, date) values('"+lid+"', '"+p_lid+"', curdate())"
    db.insert(qry)
    return jsonify(status='ok')

@app.route('/and_driver_view_msg', methods=['post'])
def and_insertintodriverlogsdriver_view_msg():
    lid = request.form['lid']
    p_lid = request.form['p_lid']
    db = Db()
    qry="select  driver_add_partner.*,message.message,message.date from driver_add_partner inner join partner on partner.partnerlogin_id=driver_add_partner.partnerlogin_id inner join message on message.driverlogin_id=driver_add_partner.driverlogin_id where driver_add_partner.driverlogin_id='"+str(lid)+"'"
    res = db.select(qry)
    return jsonify(status="ok", data=res)


@app.route("/and_insert_distraction", methods=['post'])
def and_insert_distraction():
    lid=request.form['lid']
    lati=request.form['lati']
    logi=request.form['logi']
    plc=request.form['place']
    db=Db()
    qry="insert into distraction(driverlogin_id,placename,latitude,longitude, date) values('"+lid+"','"+plc+"','"+lati+"','"+logi+"',curdate())"
    db.insert(qry)
    return jsonify(status='ok')









@app.route("/and_view_profile_partner", methods=['post'])
def and_view_profile_partner():
    lid=request.form['lid']
    db=Db()
    qry="select * from partner where partnerlogin_id='"+lid+"'"
    res=db.selectOne(qry)
    return jsonify(status="ok", name=res['name'], phone=res['contact_no'], email=res['email'], photo=res['photo'],
            house=res['house_no'], place= res['place'] , post=res['post'] , pin=res['pin'])


@app.route('/and_edit_profile_partner', methods=['post'])
def and_edit_profile_partner():
    name = request.form['name']
    houseno = request.form['hsno']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    contactno = request.form['cntctno']
    image = request.form['image']
    lid = request.form['lid']
    if len(image)!=0:
        import time
        timestr = time.strftime("%Y%m%d-%H%M%S")
        print(timestr)
        a = base64.b64decode(image)
        fh = open(static_path+"user_image\\" + timestr + ".jpg", "wb")
        path = "/static/user_image/" + timestr + ".jpg"
        fh.write(a)
        fh.close()
        qry="update partner set name='"+name+"', house_no='"+houseno+"', place='"+place+"', post='"+post+"', pin='"+pin+"', contact_no='"+contactno+"', photo='"+path+"' where partnerlogin_id='"+lid+"'"
    else:
        qry="update partner set name='"+name+"', house_no='"+houseno+"', place='"+place+"', post='"+post+"', pin='"+pin+"', contact_no='"+contactno+"' where partnerlogin_id='"+lid+"'"
    
    db=Db()
    db.update(qry)
    return  jsonify(status="ok")


@app.route("/and_partner_view_drivers", methods=['post'])
def and_partner_view_drivers():
    lid=request.form['lid']
    db=Db()
    qry="select driver.*, location.latitude, location.longitude from driver inner join driver_add_partner on driver_add_partner.driverlogin_id=driver.driverlogin_id inner join location on driver.driverlogin_id=location.driverlogin_id where driver_add_partner.partnerlogin_id='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok", data =res)

@app.route('/and_partner_insert_msg', methods=['post'])
def and_partner_insert_msg():
    msg = request.form['msg']
    lid = request.form['lid']
    d_lid = request.form['d_lid']
    db = Db()
    qry = "insert into message(message, driverlogin_id, partnerlogin_id, type, date) values('"+msg+"','"+d_lid+"','"+lid+"','partner',curdate())"
    db.insert(qry)
    return jsonify(status="ok")


@app.route('/and_partner_view_msg', methods=['post'])
def and_partner_view_msg():
    lid = request.form['lid']
    d_lid = request.form['d_lid']
    db = Db()
    qry = "select message, date from message where driverlogin_id='"+d_lid+"' and partnerlogin_id='"+lid+"' order by message_id desc"
    res = db.select(qry)
    return jsonify(status="ok", data=res)


@app.route('/and_partner_view_driver_logs', methods=['post'])
def and_partner_view_driver_logs():
    d_lid=request.form['d_lid']
    db = Db()
    qry = "select * from driver_logs where driverlogin_id='" + d_lid + "' order by date desc, time desc"
    res = db.select(qry)
    return jsonify(status="ok", data=res)


@app.route('/getmsg', methods=["post"])
def getmsg():
    db = Db()
    msgid = request.form["msgid"]
    driverid = request.form["driverid"]
    qry="select message,message_id from message where driverlogin_id='"+driverid+"' and type='partner' and message_id>'"+msgid+"' ORDER by message_id"
    ps=db.selectOne(qry)
    print(ps)
    if ps is not None :
        return jsonify(status='ok',msgid=ps['message_id'],message=ps['message'])
    else:
        return jsonify(status='no')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')