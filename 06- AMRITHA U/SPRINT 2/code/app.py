from flask import *

from src.dbconnection import *

app=Flask(__name__)
import functools

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect("/")
        return func()

    return secure_function
app.secret_key="qwe"
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/logincode',methods=['post'])
def logincode():
    uname=request.form['textfield']
    pwd=request.form['textfield2']
    qry="SELECT * FROM login WHERE `username`=%s AND `password`=%s"
    val=(uname,pwd)
    res=selectone(qry,val)
    print(res[0])
    if res is None:
        return '''<script>alert("invalid");window.location="/"</script>'''
    else:
        if res[3]=='admin':
            session['lid']=res[0]
            return redirect('/adminhome')

        else:
            return '''<script>alert("invalid");window.location="/"</script>'''




@app.route('/addfertilizer',methods=['post'])
@login_required
def addfertilizer():
    return render_template('addfertilizer.html')


@app.route('/addfertilizers',methods=['post'])
@login_required

def addfertilizers():
    name=request.form['textfield']
    des=request.form['textarea']
    uses=request.form['textarea2']

    qry="insert into fertilizer values(null,%s,%s,%s)"
    val=(name,des,uses)
    iud(qry,val)
    return '''<script>alert("fertilizer added");window.location="/fertilizer"</script>'''

@app.route('/adminhome')
@login_required

def adminhome():
    return render_template('adminhome.html')

@app.route('/chat')
@login_required

def chat():
    return render_template('chat.html')

@app.route('/chatwithfarmers')
@login_required

def chatwithfarmers():
    qry = "select * from farmer"
    res = selectall(qry)
    return render_template('chatwithfarmers.html',val=res)



@app.route('/chat1',methods=['GET','POST'])
@login_required

def chat1():
    uid=request.args.get('uid')
    session['uidd']=uid
    qry=("select fname from farmer where lid=%s")
    val=str(uid)
    s1 = selectone(qry,val)
    fid=session['lid']
    session['idd'] = uid
    qry=("select * from chat where (fid=%s and tid=%s) or (fid=%s and tid=%s) order by date asc")
    val=(str(uid),str(fid),str(fid),str(uid))
    print(val)
    s = selectall2(qry,val)
    print(s)
    return render_template('chat.html',data=s,fname=s1[0],fr=str(uid))

@app.route('/chat11',methods=['GET','POST'])
@login_required

def chat11():
    uid = session['uidd']
    qry=("select fname from farmer where lid=%s")
    val=str(uid)
    s1 = selectone(qry,val)
    fid=session['lid']
    session['idd'] = uid
    qry=("select * from chat where (fid=%s and tid=%s) or (fid=%s and tid=%s) order by date asc")
    val=(str(uid),str(fid),str(fid),str(uid))
    print(val)
    s = selectall2(qry,val)
    print(s)
    return render_template('chat.html',data=s,fname=s1[0],fr=str(uid))
@app.route('/send',methods=['GET','POST'])
@login_required

def send():

        fid=session["lid"]
        print(fid)
        tid=session['idd']
        session['uidd']=tid
        print(tid)
        msg=request.form['textarea']
        qry=("insert into chat values(null,%s,%s,%s,curdate())")
        val=str(fid),str(tid),msg
        iud(qry,val)
        return '''<script>window.location='/chat11'</script>'''



@app.route('/fertilizer')
@login_required

def fertilizer():
    qry="SELECT * FROM `fertilizer`"
    res=selectall(qry)

    return render_template('fertilizer.html',val=res)

@app.route('/sendnotification')
@login_required

def sendnotification():

    return render_template('sendnotification.html')

@app.route('/sendingnotification',methods=['post'])
@login_required

def sendingnotification():
    noti=request.form['textarea']
    qry="insert into notification values(null,%s,curdate())"
    iud(qry,noti)
    return '''<script>alert("notification sent");window.location="/adminhome"</script>'''


@app.route('/viewfarmer')
@login_required

def viewfarmer():
    qry="select * from farmer"
    res=selectall(qry)
    return render_template('viewfarmer.html',val=res)

@app.route('/viewfeedback')
@login_required

def viewfeedback():
    qry="SELECT `feedback`.*,`farmer`.* FROM `farmer` JOIN `feedback` ON `feedback`.`lid`=`farmer`.`lid`"
    res=selectall(qry)
    return render_template('viewfeedback.html',val=res)

@app.route('/deleteferti',methods=['get'])
@login_required

def deleteferti():
    id=request.args.get('id')
    qry="delete from fertilizer where fertid=%s"

    iud(qry,id)
    return '''<script>alert("deleted");window.location="/fertilizer"</script>'''



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)