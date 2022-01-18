from flask import *

from src.dbconnection import *
app=Flask(__name__)
app.secret_key="aaa"

@app.route('/')
def main():
    return render_template('login.html')

@app.route("/loginnew",methods=['post'])
def loginnew():
    uname=request.form['textfield']
    passwd=request.form['textfield2']

    qry="select * from login where username=%s and password=%s"
    val = (uname,passwd)
    res=select1(qry,val)
    print(res)
    if res is None :

        return '''<script>alert("invalid username or password");window.location="/"</script>'''
    else:
        if res[3]=='admin':

            return '''<script>alert("welcome");window.location="/adminhome"</script>'''


@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')
@app.route('/studmng')
def studmng():
    qry="select * from student_registration "
    res=selectalla(qry)
    return render_template('viewstud.html',val=res)
@app.route('/studreg',methods=['post'])
def studreg():
    qry="select * from subject"
    res=selectalla(qry)
    return render_template('studreg.html',val=res)
@app.route('/studreg1',methods=['post'])
def studreg1():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    dob = request.form['textfield7']
    phone = request.form['textfield4']
    email = request.form['textfield3']
    course=request.form['select']
    uname=request.form['textfield5']
    pswd=request.form['textfield6']
    qry = "insert into login values (null,%s,%s,'student')"
    val = (uname, pswd)

    id = iud(qry, val)

    qry1 = "insert into student_registration values(null,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id), fname, lname, gender, dob, course,email, phone,)
    iud(qry1, val1)
    return '''<script>alert("Added successfully");window.location='/studmng'</script>'''

@app.route('/editstud')
def editstud():
    id=request.args.get('id')
    session['id']=id
    q="select * from student_registration where lid=%s"
    res=select1(q,str(id))
    return render_template('editstud.html',val=res)
@app.route('/viewexam')
def viewexam():
    return render_template('viewexam.html')
@app.route('/viewqn')
def viewqn():
    return render_template('viewqn&answer.html')
@app.route('/viewstudy')
def viewstudy():
    return render_template('viewstudy.html')

@app.route('/updatstud',methods=['post'])
def updatstud():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    dob = request.form['textfield7']
    phone = request.form['textfield4']
    email = request.form['textfield3']
    course = request.form['select']
    id=session['id']
    qry="UPDATE `student_registration` SET `fname`=%s,`lname`=%s,`gender`=%s,`dob`=%s,`course`=%s,`email`=%s,`phoneno`=%s WHERE `lid`=%s"
    val=(fname,lname,gender,dob,course,email,phone,str(id))
    iud(qry,val)
    return '<script>alert("update successfully");window.location="/studmng"</script>'''

@app.route('/dltstud')
def dltstud():
    id=request.args.get('id')
    q="delete from student_registration where lid=%s"
    v=str(id)
    iud(q,v)
    q1="delete from login where id=%s"
    iud(q1,str(id))
    return '''<script>alert("delete successfully");window.location='/studmng'</script>'''
@app.route('/viewsub')
def viewsub():
    q="select*from subject"
    res=selectalla(q)
    return render_template('viewsub.html',val=res)
@app.route('/addsub',methods=['post'])
def addsub():
    return render_template('addsubject.html')
@app.route('/addsub1',methods=['post'])
def addsub1():
    sub=request.form['textfield']
    course=request.form['select']
    des=request.form['textarea']
    qry="insert into subject values(NULL,%s,%s,%s)"
    val=(sub,course,des)
    iud(qry,val)
    return redirect('/viewsub')
@app.route('/editsub')
def editsub():
    id=request.args.get('id')
    session['id']=id
    q="select * from subject where sid=%s"
    res=select1(q,str(id))
    return render_template('editsubject.html',val=res)
@app.route('/updatsub',methods=['post'])
def updatsub():
    sub = request.form['textfield']
    course = request.form['select']
    des = request.form['textarea']
    id=session['id']
    qry="UPDATE subject SET `subject`=%s,`course`=%s,`description`=%s WHERE `sid`=%s"
    val=(sub,course,des,str(id))
    iud(qry,val)
    return '<script>alert("update successfully");window.location="/viewsub"</script>'''
@app.route('/dltsub')
def dltsub():
    id=request.args.get('id')
    q="delete from subject where sid=%s"
    v=str(id)
    iud(q,v)

    return '<script>alert("delete successfully");window.location="/viewsub"</script>'''





app.run(debug=True