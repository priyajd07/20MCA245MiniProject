from flask import *
app=Flask(__name__)
from src.dbconnector import *

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


@app.route('/viewusers')
def viewusers():
    qry="SELECT * FROM `user_reg`"
    res=select(qry)
    return render_template('view users.html',val=res)

@app.route('/viewfeedback')
def viewfeedback():
    qry="SELECT `feedback`.*,`shop_reg`.`shopname`,`user_reg`.`firstname`,`lastname` FROM `shop_reg` JOIN `feedback` ON `feedback`.`companyid`=`shop_reg`.`lid` JOIN `user_reg` ON `user_reg`.`lid`=`feedback`.`useerid`"
    res=select(qry)
    return render_template('viewfeedback.html',val=res)






































app.run(debug=True)