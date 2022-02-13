from flask import *

app=Flask(__name__)
from dbconn import *

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
        elif res[3]=='broker':
            return redirect('/bhome')
        else:
            return '''<script>alert("invalid");window.location="/"</script>'''


@app.route('/accept_or_reject_broker')
def accept_or_reject_broker():
    return render_template('Acceptorrejectbroker.html')

@app.route('/addcomplaints')
def addcomplaints():
    return render_template('addcomplaints.html')

@app.route('/addplot')
def addplot():
    return render_template('addplot.html')


@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@app.route('/blockorunblockbroker')
def blockorunblockbroker():
    return render_template('blockorunblockbroker.html')

@app.route('/chatwithuser')
def chatwithuser():
    return render_template('chatwithuser.html')

@app.route('/enquiries')
def enquiries():
    return render_template('enquiries.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/manageplot')
def manageplot():
    return render_template('manageplot.html')

@app.route('/registeration')
def registeration():
    return render_template('registeration.html')

@app.route('/userreg',methods=['post'])
def userreg():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    phone=request.form['textfield6']
    email=request.form['textfield7']
    uname=request.form['textfield8']
    pwd=request.form['textfield9']
    qry1="INSERT INTO login VALUES(NULL,%s,%s,'broker')"
    val1=(uname,pwd)
    id=iud(qry1,val1)
    qry2="INSERT INTO `broker` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),fname,lname,place,post,pin,phone,email)
    iud(qry2,val)
    return '''<script>alert("Registration successfull");window.location="/"</script>'''


@app.route('/replytocomplaint')
def replytocomplaint():
    return render_template('replytocomplaint.html')

@app.route('/sendreplytoenquiry')
def sendreplytoenquiry():
    return render_template('sendreplytoenquiry.html')


@app.route('/bhome')
def bhome():
    return render_template('bhome.html')

@app.route('/viewbooking')
def viewbooking():
    return render_template('viewbooking.html')


@app.route('/viewcomplaint')
def viewcomplaint():
    return render_template('viewcomplaint.html')


@app.route('/viewfeedback')
def viewfeedback():
    return render_template('viewfeedback.html')

@app.route('/viewuserreviews')
def viewuserreviews():
    query="SELECT `user`.`fname`,`user`.`lname`,`user`.`phone`,`user`.`email`,`reviews`.* FROM `user` JOIN `reviews` ON `reviews`.`lid`=`user`.`lid`"
    res=selectall(query)
    return render_template('viewuserreviews.html',val=res)




























app.run(debug=True)