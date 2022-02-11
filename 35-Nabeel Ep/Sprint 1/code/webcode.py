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
        # elif res[3] == 'user':
        #     session['ln']=res[0]
        #     return '''<script>alert('welcome');window.location="/userhome"</script>'''
        else:
            return '''<script>alert('invalid entry');window.location="/"</script>'''



@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')


@app.route('/viewuser')
def viewuser():
    qry="SELECT `user_details`.* from user_details join login on login.id=user_details.lid where login.type='pending' "
    res=select(qry)
    return render_template('viewuser.html',val=res)
@app.route('/verifyuser')
def verifyuser():
    id=request.args.get('id')
    qry="UPDATE `login` SET `type`='user' WHERE `id`=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("verified");window.location="viewuser"</script>'''

@app.route('/rejectuser')
def rejectuser():
    id=request.args.get('id')
    qry="UPDATE `login` SET `type`='rejected' WHERE `id`=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("rejected");window.location="viewuser"</script>'''


@app.route('/reply_massage')
def reply_massage():
    return render_template('reply_message.html')


























app.run(debug=True)