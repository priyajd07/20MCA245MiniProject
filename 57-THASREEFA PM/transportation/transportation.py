

from flask import Flask, render_template, request, redirect,jsonify,session
from DBConnection import Db

staticpath = "C:\\Users\\THOUFEEQ PM\\PycharmProjects\\transportation\\static\\"

app = Flask(__name__)
app.secret_key="222"


@app.route('/')
def hello_world():
    return render_template('logindex.html')


@app.route('/adindex')
def adindex():
    return render_template('adindex.html')


@app.route('/login_post', methods=['POST'])
def login_post():
    username = request.form["textfield"]
    password = request.form["textfield2"]
    db = Db()
    qry = "select * from login where username='" + username + "' and password='" + password + "'"
    res = db.selectOne(qry)
    if res is not None:
        if res["type"] == "admin":
            return '''<script>alert('Successfully logged in');window.location='/adindex'</script>'''
        else:
            return '''<script>alert('Invalid username or password');window.location='/'</script>'''
    else:
        return '''<script>alert('Invalid username or password');window.location='/'</script>'''


@app.route('/admin_add_advertisement')
def admin_add_advertisement():
    return render_template('admin/add advertisement.html')


@app.route('/admin_add_advertisement_post', methods=["post"])
def admin_add_advertisement_post():
    pic = request.files["file"]
    lat = request.form["lat"]
    lon = request.form["lon"]
    pic.save(staticpath + "advertisement\\" + pic.filename)
    url = "/static/advertisement/" + pic.filename
    qry = "insert into advertisement(photo,date,latitude,longitude)values('" + url + "',curdate(),'" + lat + "','" + lon + "')"
    d = Db()
    d.insert(qry)
    return '''<script>alert('Successfully Added');window.location='/admin_add_advertisement'</script>'''



@app.route('/admin_add_bus')
def admin_add_bus():
    qry = "select * from route"
    d = Db()
    res = d.select(qry)
    return render_template('admin/add bus.html', route=res)


@app.route('/admin_add_bus_post', methods=["post"])
def admin_add_bus_post():
    bname = request.form["textfield"]
    ml = request.form["textfield2"]
    rgno = request.form["textfield3"]
    clr = request.form["textfield5"]
    rid = request.form["select"]
    img = request.files["image"]
    img.save(staticpath +"bus\\"+ img.filename)
    url = "/static/bus/" + img.filename
    qry = "insert into bus(busname,regno,color,model,photo,routeid)values('" + bname + "','" + rgno + "','" + clr + "','" + ml + "','" + url + "','" +rid+ "')"

    d = Db()
    res= d.insert(qry)
    return '''<script>alert('Successfully Added');window.location='/admin_add_bus'</script>'''


@app.route('/admin_add_notification')
def admin_add_notification():
    return render_template('admin/add notification.html')


@app.route('/admin_add_notification_post', methods=["post"])
def admin_add_notification_post():
    dname = request.form["textarea"]
    qry = "insert into notification(notification,date)values('" + dname + "',curdate())"
    d = Db()
    d.insert(qry)
    return '''<script>alert('Successfully Added');window.location='/admin_add_notification'</script>'''


@app.route('/admin_add_route')
def admin_add_route():
    return render_template('admin/add route.html')


@app.route('/admin_add_route_post', methods=["post"])
def admin_add_route_post():
    rname = request.form["textfield"]
    qry = "insert into route(routename)values('" + rname + "')"
    d = Db()
    d.insert(qry)
    return '''<script>alert('Successfully Added');window.location='/admin_add_route'</script>'''




@app.route('/admin_add_stop')
def admin_add_stop():
    qry = "select * from route"
    d = Db()
    res = d.select(qry)

    return render_template('admin/add stop.html', route=res)


@app.route('/admin_add_stop_post', methods=["post"])
def admin_add_stop_post():
    sname = request.form["textfield"]
    rt = request.form["select"]
    pstn = request.form["plc"]
    lat = request.form["lat"]
    lon = request.form["lon"]
    qry = "insert into stop(routeid,stopname,place,latitude,longitude) values('" + rt + "','" + sname + "','" + pstn + "','" + lat + "','" + lon + "')"
    d = Db()
    d.insert(qry)
    return '''<script>alert('Successfully Added');window.location='/admin_add_stop'</script>'''


@app.route('/admin_delete_advertisement/<id>')
def admin_delete_advertisement(id):
    qry = "delete from advertisement where `advertisementid`='" + id + "'"
    db = Db()
    res = db.delete(qry)
    return '''<script>alert('Successfully Removed');window.location='/admin_view_advertisement'</script>'''


@app.route('/admin_delete_stop/<id>')
def admin_delete_stop(id):
    qry = "delete from stop where `stopid`='" + id + "'"
    db = Db()
    res = db.delete(qry)
    return '''<script>alert('Successfully Removed');window.location='/admin_view_stop'</script>'''


@app.route('/admin_edit_stop/<id>')
def admin_edit_stop(id):
    qry = "select stop.*,route.* from stop inner join route on stop.routeid=route.routeid where stopid='" + id + "'"
    db = Db()
    res = db.selectOne(qry)
    qry1 = "select * from route"

    rt = db.select(qry1)
    return render_template('admin/edit stop.html', data=res, route=rt)


@app.route('/admin_edit_stop_post', methods=["post"])
def admin_edit_stop_post():
    stname = request.form["textfield"]
    id = request.form["id"]
    lt = request.form["textfield3"]
    lon = request.form["textfield4"]
    pl = request.form["textfield5"]
    qry = "update stop set stopname='" + stname + "',latitude='" + lt + "',longitude='" + lon + "',place='" + pl + "' where stopid='" + id + "'"
    d = Db()
    d.update(qry)
    return '''<script>alert('Successfully Updated');window.location='/admin_view_stop'</script>'''


@app.route('/admin_edit_notification/<id>')
def admin_edit_notification(id):
    qry = "select * from notification WHERE notid='" + id + "'"
    db = Db()
    res = db.selectOne(qry)
    return render_template('admin/edit notification.html', data=res)


@app.route('/admin_edit_notification_post', methods=['POST'])
def admin_edit_notification_post():
    notfctn = request.form["notification"]
    id = request.form["notid"]
    qry = "update notification set notification= '" + notfctn + "' WHERE notid='" + id + "'"
    d = Db()
    d.update(qry)
    return '''<script>alert('Successfully Updated');window.location='/admin_view_notification'</script>'''


@app.route('/admin_delete_notification/<id>')
def admin_delete_notification(id):
    qry = "delete from notification WHERE notid='" + id + "'"
    db = Db()
    res = db.delete(qry)
    return '''<script>alert('Successfully Deleted');window.location='/admin_view_notification'</script>'''


@app.route('/admin_view_notification_post', methods=['POST'])
def admin_view_notification_post():
    d1 = request.form["d1"]
    qry = "select * from notification WHERE date '" + d1 + "'"
    db = Db()
    res = db.select(qry)
    return render_template('admin/view notification.html', data=res)


@app.route('/admin_view_notification')
def admin_view_notification():
    qry = "select * from notification"
    db = Db()
    res = db.select(qry)
    return render_template('admin/view notification.html', data=res)


@app.route('/search_notification', methods=["post"])
def search_notification():
    dname = request.form["d1"]
    qry = "select * from notification where date like'%" + dname + "%'"
    db = Db()
    res = db.select(qry)
    return render_template('admin/view notification.html', data=res)


@app.route('/admin_view_advertisement_post', methods=['POST'])
def admin_view_advertisement_post():
    d1 = request.form["d1"]
    d2 = request.form["d2"]
    qry = "select * from advertisement WHERE date BETWEEN '" + d1 + "' and '" + d2 + "'"
    db = Db()
    res = db.select(qry)
    return render_template('admin/view advertisement.html', data=res)


@app.route('/admin_view_advertisement')
def admin_view_advertisement():
    qry = "select * from advertisement"
    db = Db()
    res = db.select(qry)
    return render_template('admin/view advertisement.html', data=res)


@app.route('/admin_edit_advertisement/<id>')
def admin_edit_advertisement(id):
    qry = "select * from advertisement WHERE advertisementid='" + id + "'"
    db = Db()
    res = db.selectOne(qry)
    return render_template('admin/edit advertisement.html', data=res)


@app.route('/admin_edit_advertisement_post', methods=["post"])
def admin_edit_advertisement_post():
    lat = request.form["lat"]
    lon = request.form["lon"]
    id = request.form["id"]
    if 'file' in request.files:
        pic = request.files["file"]
        if pic.filename != '':
            pic.save(staticpath + "advertisement\\" + pic.filename)
            url = "/static/advertisement/" + pic.filename
            qry = "update advertisement set photo='" + url + "',latitude='" + lat + "',longitude='" + lon + "' where advertisementid='" + id + "'"
        else:
            qry = "update advertisement set latitude='" + lat + "',longitude='" + lon + "' where advertisementid='" + id + "'"
    else:
        qry = "update advertisement set latitude='" + lat + "',longitude='" + lon + "' where advertisementid='" + id + "'"

    d = Db()
    d.update(qry)
    return '''<script>alert('Successfully Updated');window.location='/admin_view_advertisement'</script>'''


@app.route('/admin_view_bus')
def admin_view_bus():
    qry = "select bus.*,route.* from bus inner join route on bus.routeid=route.routeid"
    db = Db()
    res = db.select(qry)

    qry1 = "select * from route"
    db = Db()
    res2 = db.select(qry1)
    return render_template('admin/view bus.html', data=res, r=res2)


@app.route('/admin_search_bus_post',methods=['post'])
def admin_search_bus_post():
    search=request.form['textfield9']
    db=Db()
    qry="select * from bus where busname like '%"+search+"%'"
    res=db.select(qry)
    return render_template('admin/view bus.html',data=res)






@app.route('/admin_edit_bus/<id>')
def admin_edit_bus(id):
    qry = "select bus.*,route.* from bus inner join route on bus.routeid=route.routeid where busid='" + id + "'"
    db = Db()
    res = db.selectOne(qry)
    qry1 = "select * from route"
    rt = db.select(qry1)
    return render_template('admin/edit bus.html', data=res,data1=rt)


@app.route('/admin_edit_bus_post', methods=["post"])
def admin_edit_bus_post():
    bid = request.form["bus_id"]
    bsname = request.form["textfield"]
    rgno = request.form["textfield2"]
    clr = request.form["textfield3"]
    mdl = request.form["textfield4"]
    rtname = request.form["select"]


    if 'file' in request.files:
        pic = request.files["file"]
        if pic.filename != '':
            pic.save(staticpath + "bus\\" + pic.filename)
            url = "/static/bus/" + pic.filename

            d = Db()
            q="update bus set busname='"+bsname+"',regno='"+rgno+"',color='"+clr+"',model='"+mdl+"',photo='"+url+"',routeid='"+rtname+"' where busid='"+bid+"'"
            res=d.update(q)
            print("11111111111111111111")
            print(res)
            return '''<script>alert('Successfully Updated');window.location='/admin_view_bus'</script>'''
        else:
            d = Db()
            q1 = "update bus set busname='" + bsname + "',regno='" + rgno + "',color='" + clr + "',model='" + mdl + "',routeid='" +rtname+ "' where busid='" +bid+ "'"
            res1 = d.update(q1)
            print("2222222222222222222222")
            return '''<script>alert('Successfully Updated');window.location='/admin_view_bus'</script>'''
    else:
        d = Db()
        q2 = "update bus set busname='" + bsname + "',regno='" + rgno + "',color='" + clr + "',model='" + mdl + "',routeid='" +rtname+ "' where busid='" +bid+ "'"
        res2 = d.update(q2)
        print("3333333333333333333333")
        return '''<script>alert('Successfully Updated');window.location='/admin_view_bus'</script>'''


@app.route('/admin_delete_bus/<id>')
def admin_delete_bus(id):
    qry = "delete from bus where `busid`='" + id + "'"
    db = Db()
    res = db.delete(qry)
    return '''<script>alert('Successfully Removed');window.location='/admin_view_bus'</script>'''


@app.route('/admin_track_bus/<id>')
def admin_track_bus(id):
    qry = "select * from location where `bus id`='" + id + "' order by `location id` DESC"
    print(qry)
    db = Db()
    res = db.select(qry)
    if len(res)>0:
        a=res[0]
        location=a['latitude']+","+a['longitude']
        print(location)
        # return  "<script> window.location='http://www.maps.google.com?q="+location+"'</script>"
        return  "<script> window.location='https://www.google.com/maps/?q=-"+location+"'</script>"
    else:
        return "No location updated"


@app.route('/admin_add_emergency')
def admin_add_emergency():
    return render_template('admin/add emergency.html')


@app.route('/admin_add_emergency_post', methods=["post"])
def admin_add_emergency_post():
    mname = request.form["textarea"]
    # print(mname)
    qry = "insert into emergency(message,date,time)values('" + mname + "',curdate(),curtime())"
    d = Db()
    d.insert(qry)
    return '''<script>alert('Successfully Added');window.location='/admin_add_emergency'</script>'''

@app.route('/admin_edit_emergency/<id>')
def admin_edit_emergency(id):
    qry = "select * from emergency WHERE emergency_id='" + id + "'"
    db = Db()
    res = db.selectOne(qry)
    return render_template('admin/edit emergency.html', data=res)


@app.route('/admin_edit_emergency_post', methods=['POST'])
def admin_edit_emergency_post():
    msg = request.form["message"]
    id = request.form["emergency_id"]
    qry = "update emergency  set message= '" + msg + "' WHERE emergency_id='" + id + "'"
    d = Db()
    d.update(qry)
    return '''<script>alert('Successfully Updated');window.location='/admin_view_emergency'</script>'''


@app.route('/admin_delete_emergency/<id>')
def admin_delete_emergency(id):
    qry = "delete from emergency WHERE emergency_id='" + id + "'"
    db = Db()
    res = db.delete(qry)
    return '''<script>alert('Successfully Deleted');window.location='/admin_view_emergency'</script>'''


@app.route('/admin_view_emergency_post', methods=['POST'])
def admin_view_emergency_post():
    d1 = request.form["d1"]
    qry = "select * from emergency WHERE date '" + d1 + "'"
    db = Db()
    res = db.select(qry)
    return render_template('admin/view emergency.html', data=res)


@app.route('/admin_view_emergency')
def admin_view_emergency():
    qry = "select * from emergency"
    db = Db()
    res = db.select(qry)
    return render_template('admin/view emergency.html', data=res)


@app.route('/search_emergency', methods=["post"])
def search_emergency():
    mname = request.form["d1"]
    qry = "select * from emergency where date like'%" + mname + "%'"
    db = Db()
    res = db.select(qry)
    return render_template('admin/view emergency.html', data=res)



@app.route('/admin_view_route')
def admin_view_route():
    qry = "select * from route"
    db = Db()
    res = db.select(qry)
    return render_template('admin/view route.html', data=res)


@app.route('/admin_view_stop')
def admin_view_stop():
    qry = "select stop.*,route.* from stop inner join route on stop.routeid=route.routeid"
    db = Db()
    res = db.select(qry)

    qry1 = "select * from route"
    db = Db()
    res2 = db.select(qry1)
    return render_template('admin/view stop.html', data=res, r=res2)


@app.route('/search_post', methods=["post"])
def search_post():
    name = request.form["select"]
    qry = "select stop.*,route.* from stop inner join route on stop.routeid=route.routeid where route.routeid='" + name + "'"
    db = Db()
    res = db.select(qry)

    qry1 = "select * from route"
    db = Db()
    res2 = db.select(qry1)
    return render_template('admin/view stop.html', data=res, r=res2)


@app.route('/search_route', methods=["post"])
def search_route():
    shname = request.form["search"]
    qry = "select * from route where routename like '%" + shname + "%'"
    db = Db()
    res = db.select(qry)

    return render_template('admin/view route.html', data=res)

#
# @app.route('/admin_edit_stop/<id>')
# def admin_edit_stop(id):
#     qry = "select stop.*,route.* from stop inner join route on stop.routeid=route.routeid where stopid='" + id + "'"
#     db = Db()
#     res = db.selectOne(qry)
#     qry1 = "select * from route"
#     rt = db.select(qry1)
#     return render_template('admin/edit stop.html', data=res, route=rt)


# @app.route('/admin_edit_stop_post', methods=["post"])
# def admin_edit_stop_post():
#     stname = request.form["textfield"]
#     id = request.form["id"]
#     lt = request.form["textfield3"]
#     lon = request.form["textfield4"]
#     pl = request.form["textfield5"]
#     qry = "update stop set stopname='" + stname + "',latitude='" + lt + "',longitude='" + lon + "',place='" + pl + "' where stopid='" + id + "'"
#     d = Db()
#     d.update(qry)
#     return '''<script>alert('Successfully Updated');window.location='/admin_view_stop'</script>'''


@app.route('/admin_delete_route/<id>')
def admin_delete_route(id):
    qry = "delete from route where `routeid`='" + id + "'"
    db = Db()
    res = db.delete(qry)
    return '''<script>alert('Successfully Removed');window.location='/admin_view_route'</script>'''


@app.route('/admin_edit_route/<id>')
def admin_edit_route(id):
    qry = "select * from route where `routeid`='" + id + "'"
    db = Db()
    res = db.selectOne(qry)
    return render_template('admin/edit route.html', data=res)


@app.route('/admin_edit_route_post', methods=["post"])
def admin_edit_route_post():
    rtname = request.form["textfield"]
    id = request.form["id"]
    qry = "update route set routename='" + rtname + "' where routeid='" + id + "'"
    d = Db()
    d.update(qry)
    return '''<script>alert('Successfully Updated');window.location='/admin_view_route'</script>'''


@app.route('/admin_home')
def admin_home():
    return render_template('admin/adminhome.html')


@app.route('/signup_index')
def signup_index():
    return render_template('signupindex.html')


@app.route('/blank_page')
def blank_page():
    return render_template('blank-page.html')

@app.route('/busallocation')
def busallocation():
    c=Db()
    qry="select * from bus"
    res=c.select(qry)
    qry2 = "select * from stop"
    res2 = c.select(qry2)
    return render_template('admin/buslocation.html',data=res,data2=res2)



@app.route('/busallocationview')
def busallocationview():
    c=Db()
    qry2 = "select bus.*,bus_locations.*,stop.* from bus_locations,bus,stop,route where bus.busid=bus_locations.busid and stop.routeid=route.routeid and route.routeid=bus.routeid and bus_locations.stopid=stop.stopid"
    res = c.select(qry2)
    print(res)
    return render_template('viewbuslocation.html',data=res)



@app.route('/busallocationviewed/<f>')
def busallocationviewed(f):
    c=Db()
    qry2 = "select bus.*,bus_locations.*,stop.* from bus_locations,bus,stop,route where bus.busid=bus_locations.busid and stop.routeid=route.routeid and route.routeid=bus.routeid and bus_locations.stopid=stop.stopid and bus_locations.locid='"+f+"'"
    res = c.selectOne(qry2)
    print(res)
    session['uu']=f
    return render_template('admin/editbuslocation.html',data=res)


@app.route('/editbusallocationpost',methods=['post'])
def editbusallocationpost():
    uu=session['uu']
    f=request.form["lat"]
    g=request.form["lon"]
    d=request.form.get("plaa")
    s=request.form["date"]
    j=request.form.get("ty")
    qry="update bus_locations set latitude='"+f+"',longitude='"+g+"',place='"+d+"',Date='"+s+"',Time='"+j+"' where locid='"+str(uu)+"'"
    c=Db()
    res=c.update(qry)
    return busallocationview()

@app.route('/busallocationpost',methods=['post'])
def busallocationpost():
    v=request.form["buses"]
    f=request.form["lat"]
    g=request.form["lon"]
    d=request.form.get("plaa")
    s=request.form["date"]
    j=request.form.get("ty")
    print("hh",j)
    x=j.split(":")
    hours=x[0]
    minu=x[1]
    bb=int(hours)*60+int(minu)
    print(bb)
    qry="insert into bus_locations(busid,latitude,longitude,place,DATE,TIME)values('"+str(v)+"','"+str(f)+"','"+str(g)+"','"+str(d)+"','"+str(s)+"','"+str(bb)+"')"
    c=Db()
    res=c.insert(qry)
    return render_template('admin/buslocation.html')



#------------------------------------Android----------------------------
@app.route('/and_user_registration',methods=["post"])
def user_registration():
    name=request.form["name"]
    photo=request.form["img"]
    place=request.form["place"]
    post=request.form["post"]
    pin=request.form["pin2"]
    district=request.form["dist"]
    email=request.form["email"]
    contact=request.form["phone"]
    d = Db()
    import base64
    import datetime
    a = base64.b64decode(photo)
    dt = datetime.datetime.now()
    dd = str(dt).replace(" ", "_").replace(":", "_").replace("-", "_")
    fh = open("C:\\Users\\THOUFEEQ PM\\PycharmProjects\\transportation\\static\\userpics\\" + dd + ".jpg", "wb")
    path = "/static/userpics/" + dd + ".jpg"
    fh.write(a)
    fh.close()
    qry="insert into login(username,password,type)values('" +email+ "','" +contact+ "','user')"
    lid=d.insert(qry)
    qry1 = "insert into user (name,photo,place,post,pin,district,email,contact,lid) values('" + name + "','" + path + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + email + "','" +contact+ "','" +str(lid)+ "')"
    res1 = d.insert(qry1)
    return jsonify(status="ok")




@app.route('/locinsertion',methods=["post"])
def locationn():
    db = Db()
    lid=request.form['lid']
    lati=request.form['latitude']
    longi=request.form['longitude']
    place=request.form['place']
    qqq="select * from location where busid='"+str(lid)+"'"
    rrr=db.selectOne(qqq)
    if rrr is not None:
        ss="update location set latitude='"+lati+"',longitude='"+longi+"',Date=curdate(),time=curtime() where busid='"+str(lid)+"'"
        oo=db.update(ss)
    else:
        qq = "insert into location(busid,latitude,longitude,Date,status,time)values('"+lid+"','"+lati+"','"+longi+"',curdate(),'user',curtime())"
        res = db.insert(qq)
    return jsonify(status="ok")



@app.route('/locinsertion2',methods=["post"])
def locinsertion2():
    db = Db()
    lati=request.form['lati']
    longi=request.form['longi']
    qqq="select * from advertisement where latitude='"+lati+"' and longitude='"+longi+"'"
    rrr=db.select(qqq)
    return jsonify(status="ok",data=rrr)


@app.route('/and_login_post', methods=['POST'])
def and_login_post():
    username = request.form["username"]
    password = request.form["password"]
    db = Db()
    qry = "select * from login where username='" + username + "' and password='" + password + "'"
    res = db.selectOne(qry)
    if res is not None:
        return jsonify(status="ok",lid=res["lid"],type=res['type'])
    else:
        return jsonify(status="no")

@app.route('/and_user_view_notification',methods=['POST'])
def and_user_view_notification():
    qry = "select * from notification"
    db = Db()
    res = db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_user_view_emergency',methods=['POST'])
def and_user_view_emergency():
    qry = "select * from emergency"
    db = Db()
    res = db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/viewcurrentstop',methods=['POST'])
def viewcurrentstop():
    qry = "select * from emergency"
    db = Db()
    res = db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/viewmybus',methods=['POST'])
def viewmybus():
    rr=request.form['routeid']
    qry = "select bus.* from bus,route where route.routeid=bus.routeid and route.routeid='"+rr+"'"
    db = Db()
    res = db.select(qry)
    return jsonify(status="ok",data=res)



@app.route('/viewmyroutes',methods=['POST'])
def viewmyroutes():
    qry = "select * from route"
    db = Db()
    res = db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/currentstop',methods=['POST'])
def viewmybus_current():

    busid=request.form['busid']
    rr=request.form['rid']
    qry = "select stop.*,bus.busname,bus_locations.* from stop,route,bus,bus_locations where bus.routeid=route.routeid and stop.routeid=route.routeid and bus_locations.busid=bus.busid and bus_locations.latitude=stop.latitude and bus_locations.longitude=stop.longitude and bus.busid='"+busid+"'"
    db = Db()
    res = db.selectOne(qry)

    qry666="select * from bus_locations where busid='"+busid+"' and date='2022-02-23'  order by locid desc "
    res666=db.selectOne(qry666)

    todayreach=res666['locid']


    qry22="select DISTINCT stop.* from bus,stop,route where route.routeid=bus.routeid and route.routeid=stop.routeid  and route.routeid='"+rr+"' order by stop.stopid"
    res2=db.select(qry22)

    stopids=[]
    stopnames=[]

    for i in res2:

        stopids.append(i['stopid'])
        stopnames.append(i['stopname'])


    dateares=[]

    qry333="select distinct date from bus_locations where busid='"+busid+"' and date!='2022-02-23'"
    res333=db.select(qry333)
    for i in res333:
        dateare=i['date']
        dateares.append(dateare)
    lst=[]

    mlabel = []
    for k in dateares:
        print("m",k)
        m=[]

        tdys=[]
        for j in stopids:
            print("jj=",j,"todayreach=",todayreach)
            if j==todayreach:
                break
            qry777 = "select * from bus_locations where stopid='" + str(j) + "' and Date='2022-02-23'"
            res777 = db.selectOne(qry777)
            print(qry777)
            if res777 is not  None:
                tdys.append(res777['Time'])
                qry444="select * from bus_locations where stopid='"+str(j)+"' and Date='"+str(k)+"'"
                res444=db.selectOne(qry444)
                m.append(res444['Time'])


            else:
                qry444 = "select * from bus_locations where stopid='" + str(j) + "' and Date='" + str(k) + "'"
                res444 = db.selectOne(qry444)
                mlabel.append(res444['Time'])






        lst.append(m)

    print("jjjjjjjjjjjjjjjjjjjjjjjjj")

    print(lst)

    print(mlabel)

    from sklearn.tree import  DecisionTreeClassifier
    a=DecisionTreeClassifier()


    print("aaaaaaaaaaaaaaaaaaaaaaaa")
    print(lst)

    print("kdjhkjfdhgkjdfhgjkdfhgkjfd")

    print(mlabel)



    a.fit(lst,mlabel)

    c=a.predict([tdys])
    print(c)


    print("lst==",lst)
    print("tdy==",tdys)
    return jsonify(status="ok",date=res['Date'],time=res['Time'],stop=res['stopname'])


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
