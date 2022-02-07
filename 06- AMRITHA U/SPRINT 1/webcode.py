from flask import *
app=Flask(__name__)
from dbconnection import *

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
    if res is None:
        return '''<script>alert("invalid");window.location="/"</script>'''
    else:
        if res[3]=='admin':
            return redirect('/adminhome')

        else:
            return '''<script>alert("invalid");window.location="/"</script>'''




@app.route('/addfertilizer')
def addfertilizer():
    return render_template('addfertilizer.html')

@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/chatwithfarmers')
def chatwithfarmers():
    return render_template('chatwithfarmers.html')

@app.route('/fertilizer')
def fertilizer():
    return render_template('fertilizer.html')

@app.route('/sendnotification')
def sendnotification():

    return render_template('sendnotification.html')

@app.route('/sendingnotification',methods=['post'])
def sendingnotification():
    noti=request.form['textarea']
    qry="insert into notification values(null,%s,curdate())"
    iud(qry,noti)
    return '''<script>alert("notification sent");window.location="/adminhome"</script>'''


@app.route('/viewfarmer')
def viewfarmer():
    qry="select * from farmer"
    res=selectall(qry)
    return render_template('viewfarmer.html',val=res)

@app.route('/viewfeedback')
def viewfeedback():
    return render_template('viewfeedback.html')







app.run(debug=True)