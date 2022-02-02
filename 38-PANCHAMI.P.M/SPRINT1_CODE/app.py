import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask,render_template,request,session
from flask_mail import Mail,Message


from DBConnection import Db
app = Flask(__name__)

app.secret_key="hi"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_DEFAULT_SENDER'] = 'mediclaim2022@gmail.com'
app.config['MAIL_PASSWORD'] = '9946891018'
mail = Mail(app)

staticpath="C:\\Users\\Admin\\PycharmProjects\\flaskProject\\Static\\"
@app.route('/')
def login():
    return render_template("Login.html")

@app.route('/login_post',methods=['post'])
def login_post():
    name=request.form['textfield']
    password=request.form['textfield2']

    qry="select * from login where username='"+name+"' and password='"+password+"'"
    print(qry)
    db=Db()
    res=db.selectOne(qry)
    if res!=None:
        type=res['type']
        session["lid"]=res["lid"]
        if type=='admin':
            return home()
        elif type=='health':
            return render_template("health/home.html")
        elif type=='patient':
            return render_template("patients/patient_home.html")
        elif type=='insurance':
            return render_template("/insurance/insurance_home.html")
        else:
            return 'invalid'
    else:
        return '''<script>alert("user not allowed"); window.location='/'</script>'''

@app.route('/ic_registration')
def ic_registration():
    return render_template("/insurance/ic_registration.html")

@app.route('/ic_registration',methods=['post'])
def ic_registration_post():
    name=request.form['textfield']
    place=request.form['textfield2']
    post=request.form['textfield3']
    pin=request.form['textfield5']
    district=request.form['textfield4']
    state=request.form['textfield6']
    number=request.form['textfield7']
    email=request.form['textfield8']
    website=request.form['textfield9']
    db=Db()
    qry="INSERT INTO insurance_company(name,place,post,pin,district,state,email,number,website,status)value('"+name+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+state+"','"+email+"','"+number+"','"+website+"','pending')"
    print(qry)
    res=db.insert(qry)
    return '''<script>alert("accepted"); window.location='/'</script>'''
@app.route('/viewpending_ic')
def viewpending_ic():
    qry="select * from insurance_company where status='pending'"
    ob=Db()
    res=ob.select(qry)
    return render_template("insurance.html",data=res)
@app.route('/icrequest_accept/<id>')
def icrequest_accept(id):
    ob = Db()
    qry="update insurance_company set status='Approved' where icid='"+str(id)+"'"
    res=ob.update(qry)
    qry1 = "select * from insurance_company where icid='" + str(id) + "'"
    res1 = ob.selectOne(qry1)
    email=res1['email']
    number = res1['number']
    qry2 = "insert into login(username,password,type)values('" + str(res1['email']) + "','" +str(res1['number']) + "','insurance')"
    res2 = ob.insert(qry2)

    qq="update insurance_company set  iclid='"+str(res2)+"' where icid='"+str(id)+"'"
    res3=ob.update(qq)
    # msg = Message(subject="------------------------",
    #               sender=app.config.get("mediclaim2022@gmail.com"),
    #               recipients=[email],
    #               body="Username : " + email + " & " + "Password : " + str(number))
    # mail.send(msg)

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("mediclaim2022@gmail.com", "9946891018")
    msg = MIMEMultipart()  # create a message.........."
    message = "Messege from mediclaim"
    msg['From'] = "mediclaim2022@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Your Password for mediclaim"
    body = "Your Account has been verified by our team. You Can login using your password - " + str(str(number)+"Your username="+str(email))
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)

    return '''<script>alert("accepted"); window.location='/viewpending_ic'</script>'''

@app.route('/icreq_reject/<id>')
def icreq_reject(id):
    qry = "update insurance_company set status='Rejected' where icid='" + str(id) + "'"
    ob = Db()
    res = ob.update(qry)
    return '''<script>alert("rejected"); window.location='/viewpending_ic'</script>'''


@app.route('/signup')
def signup():
    return render_template("/health/signup hp.html")

@app.route('/signup_post',methods=['post'])
def signup_post():
    name=request.form['textfield']
    place = request.form['textfield2']
    post=request.form['textfield3']
    pin = request.form['textfield4']
    district = request.form['textfield5']
    state = request.form['textfield6']
    number = request.form['textfield7']
    email = request.form['textfield8']
    website = request.form['textfield9']
    db=Db()

    qry="insert into health_provider(hp_name,place,post,pin,district,state,number,email,website,status)values('"+name+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+state+"','"+number+"','"+email+"','"+website+"','pending')"
    res=db.insert(qry)
    return '''<script>alert("accepted"); window.location='/'</script>'''

@app.route("/home")
def home():
    return render_template("home.html")



@app.route('/viewhealthpending_request')
def viewhealthpending_request():
    qry="select * from health_provider where status='pending'"
    ob=Db()
    res=ob.select(qry)
    return render_template("view healthp.html",data=res)

@app.route('/healthproviderrequest_accept/<id>')
def healthproviderrequest_accept(id):
    ob = Db()
    qry="update health_provider set status='Approved' where hpid='"+str(id)+"'"
    res=ob.update(qry)
    qry1 = "select * from health_provider where hpid='" + str(id) + "'"
    res1 = ob.selectOne(qry1)
    email=res1['email']
    number = res1['number']
    qry2 = "insert into login(username,password,type)values('" + str(res1['email']) + "','" +str(res1['number']) + "','health')"
    res2 = ob.insert(qry2)

    qq="update health_provider set  hplid='"+str(res2)+"' where hpid='"+str(id)+"'"
    res3=ob.update(qq)
    # msg = Message(subject="------------------------",
    #               sender=app.config.get("mediclaim2022@gmail.com"),
    #               recipients=[email],
    #               body="Username : " + email + " & " + "Password : " + str(number))
    # mail.send(msg)

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("mediclaim2022@gmail.com", "9946891018")
    msg = MIMEMultipart()  # create a message.........."
    message = "Messege from mediclaim"
    msg['From'] = "mediclaim2022@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Your Password for mediclaim"
    body = "Your Account has been verified by our team. You Can login using your password - " + str(str(number))
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)

    return '''<script>alert("accepted"); window.location='/viewhealthpending_request'</script>'''

@app.route('/healthproviderrequest_reject/<id>')
def healthproviderrequest_reject(id):
    qry = "update health_provider set status='Rejected' where hpid='" + str(id) + "'"
    ob = Db()
    res = ob.update(qry)
    return '''<script>alert("rejected"); window.location='/viewhealthpending_request'</script>'''


@app.route('/view_accepted_healthpenders')
def view_accepted_healthpenders():
    qry="select * from health_provider where status='Approved'"
    ob=Db()
    res=ob.select(qry)
    return render_template("view HP.html",data=res)

@app.route('/healthproviderrequest_rejected/<id>')
def healthproviderrequest_rejected(id):
    qry = "update health_provider set status='Rejected' where hplid='" + str(id) + "'"
    ob = Db()
    res = ob.update(qry)
    qry1 = "update login set type='pending' where lid='" + str(id) + "'"
    res1 = ob.update(qry1)
    return '''<script>alert("rejected"); window.location='/view_accepted_healthpenders'</script>'''




@app.route('/view_rejected_healthpenders')
def view_rejected_healthpenders():
    qry="select * from health_provider where status='Rejected'"
    ob=Db()
    res=ob.select(qry)
    return render_template("view rejected hp.html",data=res)

@app.route('/viewhp')
def viewhp():
    return render_template("view HP.html")

@app.route('/viewrejectedhp')
def viewrejectedhp():
    return render_template("/view rejected hp.html")

@app.route('/insurance')
def insurance():
    return render_template("/insurance.html")

@app.route('/viewic')
def viewic():
    qry = "select * from insurance_company where status='Approved'"
    ob = Db()
    res = ob.select(qry)
    return render_template("view ic.html",data=res)

