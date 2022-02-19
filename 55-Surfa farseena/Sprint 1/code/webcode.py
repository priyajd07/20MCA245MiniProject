from flask import *

from src.dbconnector import *

app=Flask(__name__)

app.secret_key="123"

@app.route('/')
def log():
    return render_template('login.html')

@app.route('/login',methods=['post'])
def login():
    uname=request.form['textfield']
    pword=request.form['textfield2']
    qry="SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val=(uname,pword)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert('invalid enrty');window.location="/"</script>'''
    else:
        if res[3]=='admin':
            session['ln']=res[0]
            return '''<script>alert('welcome');window.location="/adminhome"</script>'''
        # elif res[3] == 'staff':
        #     session['ln']=res[0]
        #     return '''<script>alert('welcome');window.location="/userhome"</script>'''
        else:
            return '''<script>alert('invalid entry');window.location="/"</script>'''



@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@app.route('/staffreg',methods=['post'])
def staffreg():
    return render_template('staffregister.html')
@app.route('/regstaff',methods=['post'])
def regstaff():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    qualif=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    email=request.form['textfield7']
    phno=request.form['textfield8']
    uname=request.form['textfield9']
    password=request.form['textfield10']
    print(request.form)
    qry="INSERT INTO `login` VALUES (NULL,%s,%s,'staff')"
    val=(uname,password)
    res=iud(qry,val)
    q="INSERT INTO `staffreg` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    v=(str(res),fname,lname,gender,qualif,place,post,pin,phno,email)
    iud(q,v)
    return'''<script>alert("added");window.location="/addandmanagestaff"</script>'''


@app.route('/addandmanagestaff')
def addandmanagestaff():
    qry="SELECT * FROM `staffreg`"
    res=select(qry)
    return render_template('addandmanagestaff.html',val=res)

@app.route('/delete_staff')
def delete_staff():
    id=request.args.get('id')
    qry="DELETE FROM `staffreg` WHERE `lid`=%s"
    val=(str(id))
    iud(qry,val)
    q="DELETE FROM `login` WHERE `id`=%s"
    v=(str(id))
    iud(q,v)
    return '''<script>alert("deleted successfully");window.location="/addandmanagestaff"</script>'''



@app.route('/viewattendance')
def viewattendance():
    return render_template('viewattendance.html')

@app.route('/viewperfomance')
def viewperfomance():
    return render_template('viewperfomance.html')


@app.route('/viewreview')
def viewreview():
    return render_template('viewreview.html')


















































app.run(debug=True)