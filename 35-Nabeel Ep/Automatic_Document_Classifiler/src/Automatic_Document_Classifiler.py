from flask import Flask,render_template,request,session,redirect

import re, math
import os
import  functools

from werkzeug.utils import secure_filename

from src.DBConnection import Db
from src.ss import *
from src.dbconnector import *

app = Flask(__name__)
app.secret_key="aaa"

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "session_id" not in session:
            return redirect("/")
        return func()
    return secure_function

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

#LOGIN
@app.route('/')
def Login():
    return render_template('Login.html')
# def Login(func):
#     @functools.wraps(func)
#     def secure_function():
#         if "lid" not in session:
#             return redirect("/")
#         return secure_function



@app.route('/Login_Action',methods=['post'])
def Login_Action():

    username=request.form['textfield']
    password = request.form['textfield2']
    # db=Db()
    res=selectone1("select * from login where username='"+username+"' and password='"+password+"'")
    # res=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
    if res is not None:
        session['session_id']=res[0]
        if res[3]=='User':
            session['line'] = 'session_id'
            return redirect('/User_Home')
        elif res[3]=='Admin':
            return redirect('/admin_home')



    else:
        return '<script>alert("INCORRECT USERNAME OR PASSWORD");window.location="/"</script>'


# User home

@app.route('/User_Home')
@login_required
def User_Home():

    return render_template('/USER/User_home.html')

#USER REGISTERATION


@app.route('/User_Registeration')
def User_Registeration():

        return render_template('USER/User_Registration.html')



@app.route('/User_Registeration_Action',methods=['post'])
def User_Registeration_Action():
    try:


        db=Db()
        name = request.form['name']
        gender = request.form['gender']
        address = request.form['address']
        district = request.form['district']

        number = request.form['number']
        email = request.form['email']
        passwrd = request.form['passwrd']
        cpasswrd = request.form['cpasswrd']

        if passwrd==cpasswrd:

            i=db.selectOne("select *from login where username='"+email+"'")
            if i:
                return '<script>alert("email already exists");window.location="/User_Registeration"</script>'

            else:

                query1 = "insert into login VALUES('','" + email + "','" + passwrd + "','pending')"
                result=db.insert(query1)
                print(str(result))

                query="insert into user_details VALUES('"+str(result)+"','"+name+"','"+gender+"','"+address+"','"+district+"','"+email+"','"+number+"','pending')"
                db.insert(query)
                return '<script>alert("USER REGISTERED SUCESSFULLY..");window.location="/User_Registeration"</script>'


        else:
            return '<script>alert("PASSWORD MISMATCHED");window.location="/User_Registeration"</script>'

    except Exception as e:
        return '<script>alert("duplicate entry for phone number");window.location="/User_Registeration"</script>'


#SEND MESSAGES

@app.route('/Send_Message')
# @login_required
def Send_Message():

        db = Db()
        if session['line'] == 'session_id':
            query = "select * from user_details WHERE id='"+str(session['session_id'])+"'"
            result = db.selectOne(query)
            return render_template('USER/send_message.html', view=result)
        else:
            return redirect('/')



@app.route('/Send_Message_Action',methods=['post'])
# @login_required

def Send_Message_Action():

    db=Db()
    user_id = session['session_id']
    message = request.form['message']
    query = "insert into messages VALUES('','" + str(user_id) + "','" + message + "','Not Replied','pending')"
    db.insert(query)
    return '<script>alert("MESSAGE ADDED SUCESSFULLY..");window.location="/Send_Message"</script>'






#ADMIN

#VERIFY USER
@app.route('/verify_user')
# @login_required

def verify_user():
    db = Db()
    query = "select * from user_details WHERE status='pending'"
    result = db.select(query)
    return render_template('ADMIN/verify_user.html', view=result)


@app.route('/update_user/<id>')
# @login_required
def update_user(id):
    db = Db()
    query = "update user_details set status='approved' where id='" + id + "' "
    db.update(query)
    query1 = "update login set type='User' where id='" + id + "' "
    db.update(query1)


    return '<script>alert("UPDATED SUCESSFULLY..");window.location="/verify_user"</script>'

@app.route('/reject_user/<id>')
# @login_required
def reject_user(id):
    db = Db()
    query = "update user_details set status='rejected' where id='" + id + "' "
    db.update(query)
    return '<script>alert("USER REJECTED SUCESSFULLY");window.location="/verify_user"</script>'



#VIEW MESSAGES
@app.route('/view_messages')

@login_required
def view_messages():
    db = Db()
    query = "select * from messages,user_details  WHERE messages.user_id=user_details.id and messages.status='pending'"
    result = db.select(query)
    return render_template('ADMIN/view_messages.html', view=result)



@app.route('/reply_message/<id>')
# @login_required

def reply_message(id):
    db = Db()
    query = "select * from messages WHERE m_id='"+id+"'"
    result = db.selectOne(query)
    return render_template('ADMIN/reply_message.html', view=result)


@app.route('/reply_message_action',methods=['post'])
# @login_required

def reply_message_action():
    db = Db()
    reply = request.form['reply']
    msg_id = request.form['msg_id']
    query = "update messages set reply='"+reply+"' where m_id='" + msg_id + "' "
    db.update(query)
    return '<script>alert("REPLY ADDED SUCESSFULLY");window.location="/view_messages"</script>'


@app.route('/admin_home')
@login_required

def admin_home():
    return render_template('ADMIN/Admin_home.html')



@app.route('/view_user_replies')
@login_required

def view_user_replies():
    if session['line'] == 'session_id':
        db = Db()
        query = "select * from messages  WHERE user_id ='"+str(session['session_id'])+"'"
        result = db.select(query)
        return render_template('USER/view_reply.html', view=result)
    else:
        return redirect('/')



@app.route('/upload_documents')
@login_required

def upload_documents():
    if session['line'] == 'session_id':
        return render_template('USER/upload_documents.html')
    else:
        return redirect('/')

@app.route('/upload_documents_action',methods=['post'])
def upload_documents_action():
      keywords = []
      hash=''
      files = request.files['files']
      fn=secure_filename(files.filename)
      import datetime
      date=datetime.datetime.now().strftime('%y%m%d-%H%M%S')
      fn=date+fn
      path = r"C:\Users\Hp\Desktop\project\Automatic_Document_Classifiler\src\static\documents\\"+fn
      files.save(path)
      wrds = []
      try:
          with open(path, 'r') as file11:
              for line in file11:
                  wrds.append(line)

          wrdsting = ' '.join(wrds)

          if len(wrds) == 0:
              return ''' <script> alert('Document is Empty!!!');window.location='/upload_documents'</script> '''
          print("wwwwwwww", wrdsting)
          import hashlib

          # initializing string

          # then sending to SHA1()
          result = hashlib.sha1(wrdsting.encode())

          # printing the equivalent hexadecimal value.

          hash=result.hexdigest()

          qry="SELECT * FROM `document` WHERE `hash`=%s AND `user_id`=%s"
          val=(hash,str(session['session_id']))
          re=selectone(qry,val)
          if re is not None:
              return render_template("result.html", out=re[3]+" - It is a similar document ")

          query = "SELECT DISTINCT words_type FROM dataset"
          result = select(query)
          for i in result:
              keywords.append(i[0])
              print(i[0])

          # keyword_string = ' '.join(keywords)
          # print("THE KEYWORD STRINGS ARE :  ", keyword_string)
          RR=[]
          max=100000
          out=''
          flag = 0
          db=Db()
          for j in keywords:
              query2 = "SELECT keyword  FROM dataset where words_type='" + j + "'"
              result2 = db.select(query2)
              word_types = []
              for k in result2:
                  word_types.append(k['keyword'])

              word_type_string = ' '.join(word_types)
              print(word_type_string, "++++++++++++++++++", j)
              print(len(word_type_string), len(wrdsting))
              # for i in range(len(word_type_string), len(wrdsting)):
              #     word_type_string+="x"
              res, ratio = predict(wrdsting, word_type_string)
              print(ratio, "@@@@@@@@")
              if ratio == 1:
                  flag = 1

              RR.append(res)
              if res < max:
                  max = res
                  out = j

          if flag == 0:

              import smtplib
              from email.mime.text import MIMEText

              try:
                  gmail = smtplib.SMTP('smtp.gmail.com', 587)
                  gmail.ehlo()
                  gmail.starttls()
                  gmail.login('autodocclassi@gmail.com', 'classiier@1')
              except Exception as e:
                  print("Couldn't setup email!!" + str(e))
              msg = MIMEText("Entered text : " + wrdsting)

              msg['Subject'] = 'New File Category'
              msg['To'] = 'adithyakprabhu@gmail.com'
              msg['From'] = 'autodocclassi@gmail.com'
              try:
                  gmail.send_message(msg)
              except Exception as e:
                  print("COULDN'T SEND EMAIL", str(e))

              # return ''' <script> alert('No Category Available');window.location='/upload_documents'</script> '''
          qry = "insert into document values(null,%s,%s,%s,%s)"
          val = (fn,str(session['session_id']),out, hash)
          iud(qry, val)
          print(out)
          return render_template("result.html", out=out)

      except:
          import PyPDF2

          # creating a pdf file object
          pdfFileObj = open(path, 'rb')

          # creating a pdf reader object
          pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

          # printing number of pages in pdf file
          print(pdfReader.numPages)

          # creating a page object
          pageObj = pdfReader.getPage(0)

          # extracting text from page
          print()

          wrdsting = pageObj.extractText()
          print ("============================")
          print (wrdsting)
          # closing the pdf file object
          pdfFileObj.close()


          if len(wrds) == 0:
              return ''' <script> alert('Document is Empty!!!');window.location='/upload_documents'</script> '''
          print("wwwwwwww", wrdsting)
          import hashlib

          # initializing string

          # then sending to SHA1()
          result = hashlib.sha1(wrdsting.encode())

          # printing the equivalent hexadecimal value.

          hash = result.hexdigest()

          qry = "SELECT * FROM `document` WHERE `hash`=%s AND `user_id`=%s"
          val = (hash, str(session['session_id']))
          re = selectone(qry, val)
          if re is not None:
              return render_template("result.html", out=re[3] + " - It is a similar document ")

          query = "SELECT DISTINCT words_type FROM dataset"
          result = select(query)
          for i in result:
              keywords.append(i[0])
              print(i[0])

          # keyword_string = ' '.join(keywords)
          # print("THE KEYWORD STRINGS ARE :  ", keyword_string)
          RR = []
          max = 100000
          out = ''
          flag = 0
          db = Db()
          for j in keywords:
              query2 = "SELECT keyword  FROM dataset where words_type='" + j + "'"
              result2 = db.select(query2)
              word_types = []
              for k in result2:
                  word_types.append(k['keyword'])

              word_type_string = ' '.join(word_types)
              print(word_type_string, "++++++++++++++++++", j)
              print(len(word_type_string), len(wrdsting))
              # for i in range(len(word_type_string), len(wrdsting)):
              #     word_type_string+="x"
              res, ratio = predict(wrdsting, word_type_string)
              print(ratio, "@@@@@@@@")
              if ratio == 1:
                  flag = 1

              RR.append(res)
              if res < max:
                  max = res
                  out = j

          if flag == 0:

              import smtplib
              from email.mime.text import MIMEText

              try:
                  gmail = smtplib.SMTP('smtp.gmail.com', 587)
                  gmail.ehlo()
                  gmail.starttls()
                  gmail.login('autodocclassi@gmail.com', 'classiier@1')
              except Exception as e:
                  print("Couldn't setup email!!" + str(e))
              msg = MIMEText("Entered text : " + wrdsting)

              msg['Subject'] = 'New File Category'
              msg['To'] = 'adithyakprabhu@gmail.com'
              msg['From'] = 'autodocclassi@gmail.com'
              try:
                  gmail.send_message(msg)
              except Exception as e:
                  print("COULDN'T SEND EMAIL", str(e))

                  # return ''' <script> alert('No Category Available');window.location='/upload_documents'</script> '''
          qry = "insert into document values(null,%s,%s,%s,%s)"
          val = (fn, str(session['session_id']), out, hash)
          iud(qry, val)
          print(out)
          return render_template("result.html", out=out)


@app.route('/viewcat')
@login_required

def viewcat():
    qry="SELECT DISTINCT `words_type` FROM `dataset`"


    res=select(qry)

    return render_template('viewcatergory.html',val=res)
@app.route('/History')
@login_required

def History():
    qry="SELECT * FROM `document` WHERE `user_id`=%s"
    print (session['session_id'])
    val=(str(session['session_id']),)
    res=selectall(qry,val)

    return render_template('History.html',val=res)



@app.route('/Add_dataset')
@login_required

def Add_dataset():
    return render_template('ADMIN/add_dataset.html')


@app.route('/Add_dataset_action',methods=['post'])
@login_required

def Add_dataset_action():
    db=Db()
    type = request.form['type']
    keyword = request.form['keyword']
    query = "insert into dataset VALUES('','" + type + "','" + keyword + "')"
    db.insert(query)
    return '<script>alert("DATASET ADDED SUCESSFULLY..");window.location="/Add_dataset"</script>'



@app.route('/search',methods=['post'])
@login_required

def search():
    db=Db()
    qry1 = "SELECT DISTINCT `words_type` FROM `dataset`"

    res1 = select(qry1)
    type = request.form['select']
    qry="SELECT * FROM `document` WHERE `type`=%s"
    val=type
    res=selectall(qry,val)
    return render_template("viewcatergory.html",val1=res,val=res1)


def similarity_check(message, msg1):

        # cosine similarity
    from collections import Counter
    WORD = re.compile(r'\w+')

    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
                  return float(numerator) / denominator


    def text_to_vector(text):
        words = WORD.findall(text)
        return Counter(words)


    print()
        # message= "PLUSTWO,SCIENCE,2010-2012,0,40 TO 90,0-1"

    vector1 = text_to_vector(str(message))

    vector2 = text_to_vector(str(msg1))
    cosine = get_cosine(vector1, vector2)
    print("cosine", cosine)

    return cosine









@app.route('/Logout')
def logout():
        session.clear()
        return render_template("Login.html")



if __name__ == '__main__':
    app.run(debug=True)