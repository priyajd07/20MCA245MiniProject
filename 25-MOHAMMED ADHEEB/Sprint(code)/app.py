from flask import *

from src.dbconnection import selectone, selectall, iud

app=Flask(__name__)
app.secret_key="aaaa"

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/log',methods=['post'])
def log():
    uname=request.form['textfield']
    pswrd=request.form['textfield2']
    qry="select * from login where user_name=%s and password=%s"
    val=(uname,pswrd)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid username or password");window.location="/"</script>'''
    elif(res[3]=='admin'):
        session['lid'] = res[0]
        return '''<script>alert("welcome admin");window.location="/adminhome"</script>'''
    elif (res[3] == 'company'):
        session['lid'] = res[0]
        return '''<script>alert("welcome company");window.location="/companyhome"</script>'''

    else:

        return '''<script>alert("not valid");window.location="/"</script>'''

@app.route('/adminhome')
def adminhome():
    return render_template("admin/admin home.html")


@app.route('/approvecompany')
def approvecompany():
    qry="SELECT `company_details`.*,`login`.`user_type` FROM `company_details` JOIN `login` ON `company_details`.`login_id`=`login`.`login_id` WHERE `login`.`user_type`='pending'"
    res=selectall(qry)
    return render_template("admin/approve company.html",val=res)


@app.route('/acceptcompany')
def acceptcompany():
    id=request.args.get('id')
    qry="update login set user_type='company' where login_id=%s"
    val=str(id)
    iud(qry,val)

    return'''<script>alert("accepted");window.location="/approvecompany"</script>'''

@app.route('/declinecompany')
def declinecompany():
    id=request.args.get('id')
    qry="update login set user_type='declined' where login_id=%s"
    val=str(id)
    iud(qry,val)

    return'''<script>alert("declined");window.location="/approvecompany"</script>'''



@app.route('/blockunblockcompany')
def blockunblockcompany():
    return render_template("admin/block unblock company.html")


@app.route('/viewcandidate')
def viewcandidate():
    return render_template("admin/view candidate.html")


@app.route('/viewcompany')
def viewcompany():
    qry="SELECT `company_details`.*,`login`.`user_type` FROM `company_details` JOIN `login` ON `company_details`.`login_id`=`login`.`login_id` WHERE `login`.`user_type`='company'"

    res=selectall(qry)
    return render_template("admin/view company.html",val=res)


@app.route('/viewfeedback')
def viewfeedback():
    return render_template("admin/view feedback.html")






@app.route('/register')
def register():
    return render_template("company/register.html")

@app.route('/addvaccancy')
def addvaccancy():
    return render_template("company/add vac det.html")


@app.route('/addvaccancydetails')
def addvaccancydetails():
    return render_template("company/add vacancy.html")



@app.route('/companyhome')
def companyhome():
    return render_template("company/company home.html")



@app.route('/feedback')
def feedback():
    return render_template("company/feedback.html")



@app.route('/viewapplication')
def viewapplication():
    return render_template("company/view application.html")







app.run(debug=True)