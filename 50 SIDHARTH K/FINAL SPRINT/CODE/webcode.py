from flask import *

from src.dbconnection import selectone, iud, selectall,selectall2

app=Flask(__name__)
app.secret_key="aaaa"

import functools
def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect ("/login")
        return func()
    return secure_function

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/log',methods=['post'])
def log():
    uname=request.form['textfield']
    pswrd=request.form['textfield2']
    print(uname,pswrd)
    qry="select * from login where username=%s and password=%s"
    val=(uname,pswrd)
    res=selectone(qry,val)
    print(res)
    if res is None:
        return '''<script>alert("invalid username or password");window.location="/"</script>'''
    elif(res[3]=='blood bank'):
        session['lid'] = res[0]
        return '''<script>alert("welcome blood bank");window.location="/bloodbankhome"</script>'''

    else:

        return '''<script>alert("not valid");window.location="/"</script>'''


@app.route('/bloodbankhome')
@login_required
def bloodbankhome():
    return render_template("blood bank home.html")


@app.route('/add_blood_requirement')
@login_required

def add_blood_requirement():
    return render_template("Add blood reqirement.html")



@app.route('/add_blood_requirement2',methods=['post'])
@login_required

def add_blood_requirement2():
    blood=request.form['select']
    unit=request.form['select2']
    qry="INSERT INTO `blood_requirement` VALUES(NULL,%s,%s,%s,'required',now())"
    val=(session['lid'],blood,unit)

    iud(qry,val)
    return '''<script>alert("requirement added succefully");window.location="/bloodbankhome"</script>'''



@app.route('/update_donation_status')
@login_required

def update_donation_status():
    qry="SELECT `donation`.*,`blood_requirement`.`blood_grp`,`blood_requirement`.`units`,`user`.`fname`,`user`.`lname`,`user`.`gender`,`user`.`phone` FROM `user` JOIN `donation` ON `user`.`ulid`=`donation`.`ulid` JOIN `blood_requirement` ON `blood_requirement`.`id`=`donation`.`bldrequire_id` WHERE donation.donation_status='accepted'"
    res=selectall(qry)
    return render_template("update donation status.html",val=res)

@app.route('/update')
@login_required

def update():
    id=request.args.get('id')
    rid=request.args.get('rid')
    qry="select units FROM `blood_requirement` WHERE `id`=%s"
    val=(rid)
    res=selectone(qry,val)
    units=res[0]
    qry = "update donation set donation_status='donated', date=now() where id=%s "
    iud(qry, str(id))
    qry="SELECT COUNT(*) FROM `donation` WHERE `bldrequire_id`=%s AND `donation_status`='donated'"
    out=selectone(qry,rid)
    getunit=out[0]
    if  getunit ==units:
        qry = "update `blood_requirement` SET STATUS ='finished' WHERE id=%s"
        iud(qry, str(rid))
    return '''<script>alert("donated");window.location="/update_donation_status#about"</script>'''


@app.route('/updatereq')
@login_required

def updatereq():
    id=request.args.get('id')
    qry="update blood_requirement set status='finished' where id=%s "
    iud(qry,str(id))
    return '''<script>alert("finished");window.location="/view_request_status#about"</script>'''


@app.route('/cancel')
@login_required

def cancel():
    id=request.args.get('id')
    qry="update donation set donation_status='cancelled' where id=%s "
    iud(qry,str(id))
    return '''<script>alert("cancelled");window.location="/update_donation_status#about"</script>'''





@app.route('/view_request_status')
@login_required

def view_request_status():
    qry="SELECT * FROM `blood_requirement` where status='required'"
    res=selectall(qry)
    return render_template("view request status.html",val=res)
@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")

@app.route('/prob')
@login_required
def prob():

    return render_template("probability check.html",sg='',val=[])

# @app.route('/prob1',methods=['post'])
# @login_required
# def prob1():
#     bg=request.form['bg']
#     qry = "select user.ulid,user.fname,user.lname,user.phone,count(donation.ulid) as cnt from user left join donation on user.ulid=donation.ulid where user.ulid in(select ulid from user where ulid not in(select ulid from donation where year(curdate())-year(date)=0 and month(curdate())-month(date)<=3) and blood_grp=%s) group by user.ulid,user.fname,user.lname,user.phone order by cnt desc"
#     val =(bg)
#     res=selectall2(qry,val)
#     result=[]
#     for i in res:
#         row=[]
#         row.append(i[1])
#         row.append(i[2])
#         row.append(i[3])
#         qry="select id,month(curdate())-month(date),year(curdate())-year(date) from donation where ulid=%s order by id desc limit 1"
#         val=(str(i[0]))
#         resmnth=selectone(qry,val)
#         if resmnth is None:
#             row.append("NA")
#         else:
#             yr=(int(resmnth[2])*12)+int(resmnth[1])
#             row.append(yr)
#         row.append(i[4])
#         qry = "select id,month(curdate())-month(date),year(curdate())-year(date) from donation where ulid=%s order by id limit 1"
#         val = (str(i[0]))
#         resmnth = selectone(qry, val)
#         if resmnth is None:
#             row.append("NA")
#         else:
#             yr = (int(resmnth[2]) * 12) + int(resmnth[1])
#             row.append(yr)
#         result.append(row)
#
#     return render_template("probability check.html",sg=bg,val=result)
@app.route('/prob1',methods=['post'])
@login_required
def prob1():
    from joblib import  load
    from sklearn.naive_bayes import GaussianNB
    classifier = load('filename.joblib')
    bg=request.form['bg']
    qry = "select user.ulid,user.fname,user.lname,user.phone,count(donation.ulid) as cnt from user left join donation on user.ulid=donation.ulid where user.ulid in(select ulid from user where ulid not in(select ulid from donation where year(curdate())-year(date)=0 and month(curdate())-month(date)<=3) and blood_grp=%s) group by user.ulid,user.fname,user.lname,user.phone order by cnt desc"
    val =(bg)
    res=selectall2(qry,val)
    result=[]
    for i in res:
        row=[]
        row.append(i[1])
        row.append(i[2])
        row.append(i[3])
        qry="select id,month(curdate())-month(date),year(curdate())-year(date) from donation where ulid=%s order by id desc limit 1"
        val=(str(i[0]))
        resmnth=selectone(qry,val)
        if resmnth is None:
            row.append(0)
        else:
            yr=(int(resmnth[2])*12)+int(resmnth[1])
            row.append(yr)
        row.append(int(i[4]))
        qry = "select id,month(curdate())-month(date),year(curdate())-year(date) from donation where ulid=%s order by id limit 1"
        val = (str(i[0]))
        resmnth = selectone(qry, val)
        if resmnth is None:
            row.append(0)
        else:
            yr = (int(resmnth[2]) * 12) + int(resmnth[1])
            row.append(int(yr))
        rr = [row[3], row[4], row[5]]
        res=classifier.predict([rr])

        print(rr,res)
        if(res[0])=='1':
            row.append("More chance")

        else:
            row.append("Less Chance")
        result.append(row)
        print (result,"================")
    return render_template("probability check.html",sg=bg,val=result)


app.run(debug=True)