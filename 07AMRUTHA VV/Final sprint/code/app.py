from flask import *
import functools
app=Flask(__name__)
from dbconn import *
app.secret_key="hjvghvf"

@app.route('/')
def login():
    return render_template('/login.html')

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect ("/")
        return func()
    return secure_function


@app.route('/logincode',methods=['post'])
def logincode():
    uname=request.form['textfield']
    pwd=request.form['textfield2']
    qry="SELECT * FROM login WHERE username=%s AND PASSWORD=%s"
    val=(uname,pwd)
    print(val)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert('invalid');window.location="/"</script>'''
    else:
        if res[3]=='expert':
            session['lid']=res[0]
            return redirect('/experthome')
        else:
            return '''<script>alert('invalid');window.location="/"</script>'''


@app.route('/add_and_manage_treatment')
@login_required
def add_and_manage_treatment():

    qry="select* from treatment"
    res=selectall(qry)
    return render_template('add_and_manage_treatments.html',val=res)
@app.route('/dlttrtmnt')
@login_required

def dlttrtmnt():
    id=request.args.get('id')
    qry="delete from treatment where tid=%s"
    iud(qry,str(id))
    return '''<script>alert(' deleted');window.location="/add_and_manage_treatment#about"</script>'''


@app.route('/add_treatment',methods=['post'])
@login_required

def add_treatment():
    return render_template('add_treatment.html')

@app.route('/add_treatment1',methods=['post'])
@login_required

def add_treatment1():
    disease=request.form['textfield']
    trtmnt=request.form['textfield2']
    details=request.form['textarea']
    qry="insert into treatment values(NULL,%s,%s,%s,curdate())"
    val=(disease,trtmnt,details)
    iud(qry,val)

    return '''<script>alert('added');window.location="/add_and_manage_treatment#about"</script>'''

@app.route('/addtips',methods=['post'])
@login_required

def addtips():
    return render_template('addtips.html')

@app.route('/addingtips',methods=['post'])
@login_required

def addingtips():
    tips=request.form['textarea']
    qry="INSERT INTO tips VALUES(NULL,%s,CURDATE())"
    iud(qry,tips)
    return '''<script>alert('tip added');window.location="/tips#about"</script>'''


@app.route('/experthome')
@login_required

def experthome():
    return render_template('experthome.html')


@app.route('/tips')
@login_required

def tips():
    qry="SELECT * FROM `tips`"
    res=selectall(qry)
    return render_template('tips.html',val=res)

@app.route('/dlttips')
@login_required

def dlttips():
    id=request.args.get('id')
    qry="delete FROM `tips` where tip_id=%s"
    iud(qry,str(id))
    return '''<script>alert('tip deleted');window.location="/tips#about"</script>'''


@app.route('/viewfeedback')
@login_required

def viewfeedback():
    qry="SELECT `registration`.`fname`,`registration`.`lname`,`registration`.`email`,`feedback`.* FROM `registration` JOIN `feedback` ON `registration`.`lid`=`feedback`.`lid`"
    res=selectall(qry)
    return render_template('viewfeedback.html',val=res)

@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')
app.run(debug=True)