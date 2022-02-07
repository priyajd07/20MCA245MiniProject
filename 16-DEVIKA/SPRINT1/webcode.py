from flask import *
from src.dbconnect import *
app=Flask(__name__)
@app.route('/')
def login():
    return render_template("login.html")


@app.route('/addandmanagebook')
def addandmanagebook():
    qry = "SELECT * FROM books"
    s = select(qry)
    return render_template("addandmanagebook.html",val=s)

@app.route('/issuebook')
def issuebook():
    return render_template("issuebook.html")


@app.route('/returnbook')
def returnbook():
    return render_template("returnbook.html")


@app.route('/verifyuser')
def verifyuser():
    qry = "SELECT `user_registration`.*,`login`.`type` FROM `login` JOIN `user_registration` ON `user_registration`.`lid`=`login`.`id` "
    s = select(qry)
    return render_template("verifyuser.html",val=s)

@app.route('/viewbookreservation')
def viewbookreservation():
    return render_template("viewbookreservation.html")




@app.route('/homepage')
def homepage():
    return render_template("homepage.html")


@app.route('/addbook',methods=['post'])
def addbook():
    return render_template("add book.html")



@app.route('/login2',methods=['post'])
def login2():
    uname=request.form['textfield']
    pword=request.form['textfield2']
    q="select * from login where username=%s and password=%s"
    val=(uname,pword)
    s=selectonecond(q,val)
    if s  is None:
        return '''<script>alert('Invalid user name or password');window.location='/'</script>'''
    elif s[3]=='admin':
        return '''<script>alert('login successfully');window.location='/homepage'</script>'''



@app.route('/addbooks',methods=['post','get'])
def addbooks():
    bookname=request.form['textfield']
    author =request.form['textfield2']
    publisg_date =request.form['textfield3']
    price=request.form['textfield4']
    qry2 = "insert into books values(null,%s,%s,%s,%s)"
    values = (bookname, author, publisg_date, price)
    iud(qry2, values)
    return '''<script>alert('BOOK ADDED');window.location='/addandmanagebook'</script>'''



@app.route('/deletebook')
def deletebook():
    id=request.args.get('id')
    print(id)
    q="delete from books where id=%s"
    val=(id)
    iud(q,val)
    return '''<script>alert('deleted');window.location='/addandmanagebook'</script>'''




@app.route('/approveuser')
def approveuser():
    id=request.args.get('id')
    print(id)
    q="update login set type='user' where id=%s"
    val=(id)
    iud(q,val)
    return '''<script>alert('user approved');window.location='/verifyuser'</script>'''

@app.route('/rejectuser')
def rejectuser():
    id=request.args.get('id')
    print(id)
    q="update login set type='reject' where id=%s"
    val=(id)
    iud(q,val)
    return '''<script>alert('user rejectd');window.location='/verifyuser'</script>'''








app.run(debug=True)
