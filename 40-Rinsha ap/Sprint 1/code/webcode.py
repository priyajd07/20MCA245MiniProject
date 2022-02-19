from  flask import *

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
        elif res[3] == 'manager':
            session['ln']=res[0]
            return '''<script>alert('welcome');window.location="/managerhome"</script>'''
        else:
            return '''<script>alert('invalid entry');window.location="/"</script>'''

@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')
@app.route('/manageprojects')
def manageprojects():
    return render_template('adminmanageprojects.html')

@app.route('/managestockholders')
def managestockholders():
    qry = "SELECT `stockholder`.* FROM `stockholder` JOIN `login` ON `stockholder`.`loginid`=`login`.`id` WHERE `login`.type='pending'"
    s = select(qry)
    return render_template('managestockholhers.html',v=s)



@app.route('/managemanagers')
def managemanagers():
    qry="SELECT `manager`.* FROM `manager` JOIN `login` ON `manager`.`loginid`=`login`.`id` WHERE `login`.type='pending'"
    s=select(qry)
    return render_template('managemanagers.html',v=s)




@app.route('/acceptmanagers')
def acceptmanagers():
    id=request.args.get('id')
    q="update `login` set type='manager' WHERE `id`=%s"
    v=str(id)
    iud(q,v)
    # qry="DELETE FROM `manager` WHERE `loginid`=%s"
    # iud(qry,v)
    return '''<script>alert('Accepted');window.location="/managemanagers"</script>'''


@app.route('/rjctmanagers')
def rjctmanagers():
    id=request.args.get('id')
    q="update `login` set type='reject' WHERE `id`=%s"
    v=str(id)
    iud(q,v)
    return '''<script>alert('Rejected');window.location="/managemanagers"</script>'''

@app.route('/acceptsh')
def acceptsh():
    id=request.args.get('id')
    q="update `login` set type='stakeholder' WHERE `id`=%s"
    v=str(id)
    iud(q,v)
    return '''<script>alert('Accepted');window.location="/managestockholders"</script>'''


































app.run(debug=True)