from flask import *
from src.dbconnection import *
app=Flask(__name__)
app.secret_key="aaa"
@app.route("/")
def login():
    return render_template('login.html')

@app.route('/login1', methods=['post'])
def login1():
    uname = request.form['textfield']
    pwd = request.form['textfield2']
    qry = "select * from login where user_name = %s and password= %s"
    val = (uname, pwd)
    res = select1(qry, val)

    if res is None:
        return '''<script>alert("invalid");window.location='/'</script>'''

    else:

        if res[3] == 'admin':
            session['lid']=res[0]
            return redirect('/adminhome')

@app.route("/adminhome")
def adminhome():
    return render_template('homeadmin.html')


@app.route("/viewuser")
def viewuser():
    qry="select*from user"
    res=selectalla(qry)
    return render_template('adviewuser.html',val=res)


@app.route("/addbullyingwords")
def addbullyingwords():
    return render_template('adaddbullyindwrds.html')


@app.route("/addbullyingwords1",methods=['post'])
def addbullyingwords1():
    word=request.form['textfield']
    qry="insert into bullying values(%s,NULL,%s,curdate())"
    val=(str(session['lid']),word)
    iud(qry,val)
    return '''<script>alert("added");window.location='/adminhome'</script>'''

app.run(debug=True)