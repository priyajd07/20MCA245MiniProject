import email

from flask import *
import smtplib
from email.mime.text import MIMEText

import pymysql
app=Flask(__name__)
con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='career_tech')
cmd=con.cursor()

app.secret_key="qwertyu"

#login
@app.route('/')
def main():
    return render_template('login.html')
@app.route('/login',methods=['post'])
def login():
    uname=request.form['textfield']
    pword=request.form['textfield2']
    cmd.execute("SELECT * FROM login WHERE user_name='"+uname+"' AND PASSWORD='"+pword+"'")
    s=cmd.fetchone()
    if s is None:
        return '''<script>alert("invalid login!");window.location='/'</script>'''
    else:
        if s[3]=='admin':
            session['lid']=1
            return '''<script>alert("Login successful");window.location='/addf'</script>'''
        elif s[3]=='company':
            session['lid']=str(s[0])
            return '''<script>alert("Login successful");window.location='/comhome'</script>'''
        else:
            return '''<script>alert("invalid login!");window.location='/'</script>'''



#admin home
@app.route('/addf')
def addf():
    if 'lid'in session:
        return render_template('Admin/admin front.html')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


#admin verification




@app.route('/view_feedback')
def view_feedback():
    cmd.execute("SELECT `feedbacks`.*,`candidate`.`candidate_name` FROM `candidate` JOIN `feedbacks` ON `feedbacks`.`uid`=`candidate`.`login_id` UNIOn SELECt`feedbacks`.*,`company_details`.`company_name` FROM `company_details` JOIN `feedbacks` ON `feedbacks`.`uid`=`company_details`.`login_id`")
    s=cmd.fetchall()
    return render_template("Admin/view_feedback.html",val=s)






@app.route('/addv')

def addv():
    if 'lid'in session:
        cmd.execute("SELECT company_details.* FROM company_details JOIN login  ON company_details.login_id=login.login_id WHERE login.user_type='pending'")
        s=cmd.fetchall()
        return render_template('Admin/verification.html',s=s)

    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


#accept
@app.route('/AcceptC')
def AcceptC():
    if 'lid'in session:
        lid=request.args.get('id')
        cmd.execute("UPDATE `login` SET `user_type`='company' WHERE `login_id`="+str(lid))
        con.commit()
        return redirect('/addv')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''




#decline
@app.route('/DeclineC')
def DeclineC():
    if 'lid'in session:
        lid=request.args.get('id')
        cmd.execute("delete from  `login`  WHERE `login_id`="+str(lid))
        cmd.execute("DELETE FROM `company_details` WHERE `login_id`="+str(lid))
        con.commit()
        return redirect('/addv')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''




#admin add questions
@app.route('/addq')
def addq():
    if 'lid'in session:
        cmd.execute("SELECT * FROM questions_and_answers")
        q=cmd.fetchall()
        return render_template('Admin/add spe que.html',q=q)
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''

#admin home--
@app.route('/adhome')
def adhome():
    if 'lid'in session:
        return render_template('Admin/admin front.html')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''
@app.route('/viewstud')
def viewstud():
    if 'lid'in session:
        cmd.execute("SELECT * FROM `candidate`")
        s=cmd.fetchall()
        return render_template('Admin/view candidates.html',s=s)
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''
#add specific question
@app.route('/add1',methods=['post'])
def add1():
    if'lid'in session:
        comid=request.form['select2']
        postid=request.form['select3']
        opt1=request.form['textfield2']
        opt2=request.form['textfield3']
        ques=request.form['textfield']
        type=request.form['select']
        opt3=request.form['textfield4']
        opt4=request.form['textfield5']
        crtans=request.form['textarea']
        cmd.execute("INSERT INTO questions_and_answers VALUES(NULL,'" + ques + "','" + opt1 + "','" + opt2 + "','" + opt3 + "','" + opt4 + "','" + type + "','" + crtans + "','"+str(session['lid'])+"','"+str(comid)+"','"+str(postid)+"','pending')")
        con.commit()
        return '''<script>alert("Successful");window.location='/addq'</script>'''
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


#add new question
@app.route('/addnq')
def addnq():
    if 'lid'in session:
        cmd.execute("SELECT * FROM `company_details`")
        s=cmd.fetchall()
        cmd.execute("SELECT * FROM `job_post`")
        ss=cmd.fetchall()
        return render_template('Admin/add new que.html',com=s,post=ss)
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''



#delete
@app.route('/DeleteC')
def DeleteC():
    if 'lid'in session:
        qid=request.args.get('id')
        cmd.execute("delete from  `questions_and_answers`  WHERE `qstn_no`="+str(qid))
        #cmd.execute("DELETE FROM `company_details` WHERE `login_id`="+str(qid))
        con.commit()
        return redirect('/addq')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''








#notification
@app.route('/addnt')
def addnt():
    if'lid'in session:
        cmd.execute("SELECT `notification_table`.*,`company_details`.`company_name` FROM `company_details` JOIN `notification_table` ON `notification_table`.`company_id`=`company_details`.`login_id`")
        n=cmd.fetchall()
        return render_template('Admin/notification.html',n=n)
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


@app.route('/addnt1',methods=['post'])
def addnt1():
    if'lid'in session:
        msg=request.form['n']
        cid=request.form['c']
        cmd.execute("INSERT INTO notification_table VALUES(NULL,"+cid+",'"+msg+"',curdate())")
        con.commit()
        return '''<script>alert("Message has been sent");window.location='/addnt'</script>'''
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''

@app.route('/addnoti')
def addnoti():
    if'lid'in session:
        cmd.execute("SELECT `login_id`,`company_name` FROM `company_details`")
        s=cmd.fetchall()
        return render_template('Admin/addnoti.html',val=s)
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''








#company home
@app.route('/comhome')
def comhome():
    if'lid'in session:
        return render_template('Company/home.html')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''




#company registration
@app.route('/reg')
def reg():
    return render_template('register.html')



@app.route('/reg1',methods=['post'])
def reg1():
    compname = request.form['textfield']
    cmpplc = request.form['textfield2']
    cmppost = request.form['textfield3']
    cmppin = request.form['textfield4']
    cmpdes = request.form['textfield5']
    cmpestdt = request.form['textfield6']
    cmpnp = request.form['textfield7']
    cmpcp = request.form['textfield8']
    cmpem = request.form['textfield9']
    cmpcon = request.form['textfield10']
    if (cmpnp == cmpcp):
        cmd.execute("INSERT INTO login VALUES(NULL,'" + compname + "','" + cmpcp + "','pending')")
        k = con.insert_id()
        cmd.execute(
            "INSERT INTO company_details VALUES(NULL,'" + compname + "','" + cmpplc + "','" + cmppost + "','" + cmppin + "','" + cmpem + "','" + cmpcon + "','" + cmpdes + "','" + cmpestdt + "','" + str(
                k) + "')")
        con.commit()
        return '''<script>alert("Successful");window.location='/'</script>'''
    else:
        return '''<script>alert("Password mismatch");window.location='/'</script>'''


#company add vacancy
@app.route('/comvac',methods=['post','get'])
def comvac():
    if'lid'in session:
        cmd.execute("SELECT `job_post`.*,opeclose.* FROM `job_post` JOIN `opeclose` ON `opeclose`.`id`=`job_post`.`job_id` where job_post.company_id='"+str(session['lid'])+"'")
        q = cmd.fetchall()
        print(q)
        return render_template('Company/add vacancy.html',q=q)
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''

@app.route('/viewvacc',methods=['post','get'])
def viewvacc():
    if'lid'in session:
        # cmd.execute("SELECT `job_post`.*,opeclose.* FROM `job_post` JOIN `opeclose` ON `opeclose`.`id`=`job_post`.`job_id` WHERE `opeclose`.`closedate`>=CURDATE()")
        cmd.execute("SELECT * FROM `job_post`")
        q = cmd.fetchall()
        return render_template('Admin/add vacancy.html',q=q)
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


@app.route('/comvac1',methods=['post'])
def comvac1():
    if'lid'in session:
        jobname=request.form['textfield']
        date=request.form['textfield2']
        date1=request.form['textfield21']

        skills=request.form['textfield3']
        desc=request.form['textfield4']
        qualification=request.form['textfield5']
        experience=request.form['textfield6']

        cmd.execute("INSERT INTO job_post VALUES(NULL,'"+jobname+"','"+str(session['lid'])+"','"+date+"','"+skills+"','"+desc+"','"+qualification+"','"+experience+"')")
        id=con.insert_id()
        con.commit()
        cmd.execute("INSERT INTO opeclose VALUES('" + str(id)+"','" + date + "','" + date1 + "')")
        con.commit()
        return '''<script>alert("Successful");window.location='/comvac'</script>'''
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


#add new vacancy details
@app.route('/comvacde',methods=['post'])
def comvacde():
    if 'lid'in session:
        return render_template('Company/add vac det.html')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


#delete vacancy
@app.route('/DelC')
def DelC():
    if'lid'in session:
        qid=request.args.get('id')
        cmd.execute("delete from  `job_post`  WHERE `job_id`="+str(qid))
        con.commit()
        return redirect('/comvac')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


#view notification

@app.route('/comnotf')
def comnotf():
    if'lid'in session:
        cmd.execute("SELECT * FROM `notification_table` WHERE `company_id`="+str(session['lid']))
        s=cmd.fetchall()
        print(s)
        return render_template('Company/view_notf.html',s=s)
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''




#Company manage complaints
@app.route('/comcmp')
def comcmp():
    if'lid'in session:
        cmd.execute("SELECT `complaints`.*,`candidate`.`candidate_name` FROM `candidate` JOIN `complaints` ON `complaints`.`candidate_id`=`candidate`.`login_id` WHERE `complaints`.`reply`='pending'")
        s=cmd.fetchall()
        return render_template('Company/manage complaints.html',s=s)
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


#company reply page
@app.route('/comcmpre',methods=['post','get'])
def comcmpre():
    if 'lid'in session:
        reply=request.form['textarea']
        cmpid=session['cmpid']
        print("khkhkhk"+cmpid)
        cmd.execute("update `complaints` set `reply`='"+reply+"' where `complaint_id`="+str(cmpid))
        con.commit()
        return '''<script>alert("Message sent");window.location='/comcmp'</script>'''
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''

#add new vacancy details
@app.route('/comcmprepl')
def comcmprepl():
    if'lid'in session:
        session['cmpid']=request.args.get('id')
        return render_template('Company/complaint reply.html')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''


#logout
@app.route('/lgout')
def lgout():
    if'lid'in session:
        session.clear()
        return render_template('login.html')
    else:
        return '''<script>alert("plz login!");window.location='/'</script>'''







@app.route('/forgt_password')
def forgt_password():
    return render_template("forgot_password.html")

@app.route('/forgt_password2',methods=['post'])
def forgt_password2():
    username=request.form['textfield1']
    print(username)
    email=request.form['textfield']
    print(email)
    cmd.execute("SELECT * FROM `login` WHERE `login`.`user_name`='"+username+"'")
    s=cmd.fetchone()
    try:

        gmail = smtplib.SMTP('smtp.gmail.com',587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('adheeb836@gmail.com','Adheeb@2000')
    except Exception as e:
        print("Couldn't setup email!!" +str(e))

    msg=MIMEText("Your password is"+"  " + s[2])
    msg['Subject']='Personality prediction Through CV Analysis'
    msg['To']=email
    msg['From']='adheeb836@gmail.com'

    try:
        gmail.send_message(msg)
        print("see")

    except Exception as e:
        print ("COULDN'T SEND EMAIL",str(e))


    return '''<script>alert("plz Check your Email!");window.location='/'</script>'''



@app.route('/deletefbk',methods=['post','get'])
def deletefbk():
    id=request.args.get("id")
    qry="DELETE FROM `feedbacks` WHERE `id`="+str(id)
    cmd.execute(qry)
    con.commit()
    return redirect("/viewfbc")


@app.route('/viewfbc',methods=['post','get'])
def viewfbc():
    qry="SELECT * FROM `feedbacks` WHERE `uid`="+str(session['lid'])
    cmd.execute(qry)
    res=cmd.fetchall()
    return render_template("Company/feedback.html",val=res)

@app.route('/insertfb',methods=['post','get'])
def insertfb():
    fb=request.form['fb']
    qry="INSERT INTO `feedbacks` VALUES(NULL,%s,%s,CURDATE())"
    val=(session['lid'],fb)
    cmd.execute(qry,val)
    con.commit()
    return redirect("/viewfbc")

@app.route('/company_add_new_qstn',methods=['post','get'])
def company_add_new_qstn():
    lid = session['lid']
    cmd.execute("SELECT * FROM job_post WHERE `job_post`.company_id='"+str(lid)+"'")
    s=cmd.fetchall()
    return render_template("Company/company_add new que.html",val=s)

@app.route('/add_com_qstn',methods=['post','get'])
def add_com_qstn():
    login_id=session['lid']
    post_id=request.form['select']
    qstn=request.form['textfield']
    op1=request.form['textfield2']
    op2=request.form['textfield3']
    op3=request.form['textfield4']
    op4=request.form['textfield5']
    correct_ansr=request.form['textfield6']
    cmd.execute("insert into company_question values(null,'"+str(post_id)+"','"+qstn+"','"+op1+"','"+op2+"','"+op3+"','"+op4+"','"+correct_ansr+"','"+str(login_id)+"')")
    con.commit()
    return '''<script>alert("success");window.location='/company_view_qstn'</script>'''







@app.route('/company_view_qstn')
def company_view_qstn():
    id=request.args.get('id')
    cmd.execute("SELECT `company_question`.*,`job_post`.`job_name` FROM `job_post` JOIN `company_question` ON `company_question`.`post_id`=`job_post`.`job_id`")
    s=cmd.fetchall()


    return render_template("Company/company_view_question.html",val=s)

@app.route("/delete_qstn",methods=['get','post'])
def delete_qstn():
    id=request.args.get('id')
    cmd.execute("delete from company_question where qid='"+str(id)+"'")
    con.commit()

    return '''<script>alert("deleted");window.location='/company_view_qstn'</script>'''


@app.route("/test_result")
def test_result():

    cmd.execute("SELECT `candidate`.`candidate_name`,`candidate`.`contact_01`,`job_post`.`job_name`,`result`.`marks` FROM `result` INNER JOIN `job_post` ON `job_post`.`job_id`=`result`.`post_id` INNER JOIN `candidate` ON `candidate`.`login_id`=`result`.`candidate_id` WHERE `result`.`com_id`='"+str(session['lid'])+"'")
    s=cmd.fetchall()
    return render_template("Company/Comany_View_test_result.html",val=s)




@app.route("/test_result1")
def test_result1():

    print("SELECT distinct `candidate`.`candidate_name`,`candidate`.`contact_01`,`job_post`.`job_name`,`result`.`candidate_id`,`result`.`post_id` FROM `result` INNER JOIN `job_post` ON `job_post`.`job_id`=`result`.`post_id` INNER JOIN `candidate` ON `candidate`.`login_id`=`result`.`candidate_id` WHERE `result`.`com_id`='"+str(session['lid'])+"' order by candidate_id")
    cmd.execute("SELECT distinct `candidate`.`candidate_name`,`candidate`.`contact_01`,`job_post`.`job_name`,`result`.`candidate_id`,`result`.`post_id` FROM `result` INNER JOIN `job_post` ON `job_post`.`job_id`=`result`.`post_id` INNER JOIN `candidate` ON `candidate`.`login_id`=`result`.`candidate_id` WHERE `result`.`com_id`='"+str(session['lid'])+"' order by candidate_id")
    s=cmd.fetchall()
    print(s,"---------------------------------")
    res=[]
    for i in s:
        cid=i[3]
        pid=i[4]

        cmd.execute("SELECT `marks` FROM `result` WHERE `candidate_id`='"+str(cid)+"' AND `post_id`='"+str(pid)+"'")
        ss=cmd.fetchall()
        if(len(ss)>=2):
            row=[]
            row.append(i[0])
            row.append(i[1])
            row.append(i[2])
            row.append(ss[0][0])
            row.append(ss[1][0])

            res.append(row)

    return render_template("Company/view result.html",val=res)






@app.route("/company_view_shortlst")
def company_view_shortlst():
    cmd.execute("SELECT * FROM `job_post` WHERE `job_post`.`company_id`='"+str(session['lid'])+"'")
    ss=cmd.fetchall()
    return render_template("Company/view_short_list.html",name=ss)







@app.route("/com_view_admin_qstn")
def com_view_admin_qstn():
    cmd.execute("SELECT * FROM `questions_and_answers` WHERE `comid`='"+str(session['lid'])+"' AND STATUS='pending'")
    s=cmd.fetchall()
    for i in s:
        comid=i[9]
        session['cid']=comid
        postid=i[10]
        session['pid']=postid
    return render_template("Company/company_vew_admin_qstn.html",qstn=s)




@app.route("/acceptqqq",methods=['get','post'])
def acceptqqq():
    qid=request.args.get('id')
    session['qid']=qid
    cmd.execute("SELECT * FROM `questions_and_answers` WHERE`qstn_no`='"+str(qid)+"'")
    s=cmd.fetchone()
    qstnid=s[0]
    session['qid']=qstnid
    return render_template("Company/addtoquestionbank.html",val=s)


@app.route("/acceptqqqupdate",methods=['get','post'])
def acceptqqqupdate():
    id=session['qid']
    queston=request.form['textarea']
    optnone=request.form['textfield']
    optiontwo=request.form['textfield2']
    optionthree=request.form['textfield3']
    optionfour=request.form['textfield4']
    anser=request.form['textfield5']
    cmd.execute("insert into company_question values(null,'"+str(session['pid'])+"','"+str(queston)+"','"+str(optnone)+"','"+str(optiontwo)+"','"+str(optionthree)+"','"+str(optionfour)+"','"+str(anser)+"','"+str(session['cid'])+"')")
    cmd.execute("update `questions_and_answers` set status='accepted' where qstn_no='"+str(id)+"'")
    con.commit()
    return '''<script>alert("Success");window.location='/comhome'</script>'''
@app.route("/acceptqssstn",methods=['get','post'])
def acceptqssstn():
    qid=request.args.get('id')
    cmd.execute("update questions_and_answers set status='accepted' where qstn_no='"+str(qid)+"'")

    con.commit()
    return '''<script>alert("success");window.location='/comhome'</script>'''





@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html")

@app.route("/admin_view_shortlst")
def admin_view_shortlst():
    cmd.execute("SELECT * FROM `candidate`")
    ss=cmd.fetchall()
    cmd.execute("SELECT * FROM `company_details`")
    dd=cmd.fetchall()
    return render_template("Admin/admin_view_short_list.html",name=ss,com=dd)



@app.route("/admin_view_shortlst1",methods=['get','post'])
def admin_view_shortlst1():
    cid = request.form['select']
    session['lidd']=cid
    comid= request.form['select2']

    cmd.execute("SELECT `result`.*,SUM(`totalqstn`) AS totalqstn,SUM(`marks`) AS totalmark,(SUM(`marks`)/SUM(`result`.`totalqstn`))*100 AS percentage FROM `result`  where  `result`.`com_id`='"+str(comid)+"'  AND `result`.`candidate_id`='"+str(cid)+"' HAVING percentage>60")
    s = cmd.fetchall()

    return render_template("Admin/admin_view_short_list.html",list=s)



@app.route('/admin_view_more_detailsof_shortlist_candidate')
def admin_view_more_detailsof_shortlist_candidate():
    cmd.execute("SELECT `candidate`.*,`resume`.* FROM `resume` JOIN `candidate` ON `candidate`.`login_id`=`resume`.`canid` WHERE `resume`.`canid`='"+str(session['lidd'])+"'")
    s=cmd.fetchone()
    return render_template("Admin/admin_view_more_detailsof_shortlist_candidate.html",val=s)


@app.route("/company_view_shortlst1",methods=['get','post'])
def company_view_shortlst1():
    cid = request.form['select']
    session['lidd'] = cid


    cmd.execute("SELECT `result`.*,SUM(`totalqstn`) AS totalqstn,SUM(`marks`) AS totalmark,(SUM(`marks`)/SUM(`result`.`totalqstn`))*100 AS percentage FROM `result` WHERE `result`.`post_id`='"+str(cid)+"'  HAVING percentage>60")
    s = cmd.fetchall()

    return render_template("Company/view_short_list.html",list=s)





@app.route('/company_view_more_detailsof_shortlist_candidate')
def company_view_more_detailsof_shortlist_candidate():
    id=request.args.get('id')
    cmd.execute("SELECT `candidate`.*,`resume`.* FROM `resume` JOIN `candidate` ON `candidate`.`login_id`=`resume`.`canid` WHERE `resume`.`canid`='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("Company/company_view_more_detailsof_shortlist_candidate.html",val=s)


@app.route('/admindelete',methods=['get','post'])
def admindelete():
    cmd.execute("SELECT `company_details`.*,`login`.`user_type` FROM `company_details` JOIN `login` ON `company_details`.`login_id`=`login`.`login_id` WHERE `login`.`user_type`!='pending'")
    s=cmd.fetchall()
    return render_template("Admin/admin_view_company_and_delete.html",val=s)
@app.route('/adminblock',methods=['get','post'])
def adminblock():
    id=request.args.get('id')
    cmd.execute("UPDATE `login` SET `user_type`='block' WHERE `login_id`='"+str(id)+"'")
    con.commit()
    return '''<script>alert("blocked");window.location='/admindelete'</script>'''
@app.route('/adminunblock',methods=['get','post'])
def adminunblock():
    id=request.args.get('id')
    cmd.execute("UPDATE `login` SET `user_type`='company' WHERE `login_id`='"+str(id)+"'")
    con.commit()
    return '''<script>alert("unblocked");window.location='/admindelete'</script>'''



# @app.route('/admindelete2',methods=['get','post'])
# def admindelete2():
#     id=request.args.get('id')
#     cmd.execute("delete from `company_details` where `company_details`.`login_id`='"+str(id)+"'")
#     con.commit()
#     return '''<script>alert("success");window.location='/addf'</script>'''
@app.route('/compsheduleexam',methods=['get','post'])
def compsheduleexam():
    id=session['lid']
    cmd.execute("SELECT `apply`.*,`candidate`.*,`job_post`.* FROM `candidate` INNER JOIN `apply` ON `apply`.`candidate_id`=`candidate`.`login_id` INNER JOIN `job_post` ON `job_post`.`job_id`=`apply`.`job_id` WHERE `job_post`.`company_id`='"+str(id)+"' AND `apply`.`status`='pending'")
    ss=cmd.fetchall()


    return render_template("Company/company_schedule_exam.html",val=ss)


@app.route('/cscheduleexam',methods=['get','post'])
def cscheduleexam():
    cid=session['lid']
    id=request.args.get('id')

    cmd.execute("SELECT `apply`.*,`candidate`.*,`job_post`.* FROM `candidate` INNER JOIN `apply` ON `apply`.`candidate_id`=`candidate`.`login_id` INNER JOIN `job_post` ON `job_post`.`job_id`=`apply`.`job_id` WHERE `job_post`.`company_id`='"+str(cid)+"' AND `apply`.`apply_id`='"+str(id)+"'")
    sc=cmd.fetchall()

    for i in sc:
        session['cdid'] = i[1]
        email = i[7]
        session['email'] = email
    cmd.execute("UPDATE `apply` SET `apply`.`status`='scheduled' WHERE `apply`.`apply_id`='"+str(id)+"'")
    con.commit()
    return render_template("Company/company_assign_time.html")

@app.route('/cscheduleexamsubmit',methods=['get','post'])
def cscheduleexamsubmit():
    idd=session['cdid']
    date=request.form['textfield']
    time=request.form['textfield2']
    password=request.form['textfield3']
    email= session['email']

    cmd.execute("insert into exam_shedule values(null,'"+str(date)+"','"+str(time)+"','"+str(idd)+"','"+str(password)+"')")

    con.commit()

    try:

        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('regionalmails@gmail.com', 'mails2020')
    except Exception as e:
        print("Couldn't setup email!!" + str(e))

    msg = MIMEText("Your exam date,time and password is" + "  " + date +" "+ time  +" " +password )
    msg['Subject'] = 'Personality prediction Through CV Analysis'
    msg['To'] = email
    msg['From'] = 'careertechgroup4@gmail.com'

    try:
        gmail.send_message(msg)
        print("see")

    except Exception as e:
        print("COULDN'T SEND EMAIL", str(e))

    return '''<script>alert("success");window.location='/comhome'</script>'''






@app.route("/view_application_and_updatestatus")
def view_application_and_updatestatus():
    lid=session['lid']
    cmd.execute("SELECT `education_qualification`.*,`candidate`.*,`apply`.*,`job_post`.* FROM `job_post` JOIN `apply` ON `apply`.`job_id`=`job_post`.`job_id` JOIN `candidate` ON `candidate`.`login_id`=`apply`.`candidate_id`  INNER JOIN `education_qualification` ON `education_qualification`.`candidate_id`=`candidate`.`login_id` WHERE `job_post`.`company_id`='"+str(lid)+"' AND `apply`.`status`='pending'")
    s=cmd.fetchall()
    return render_template("Company/view_application_and-update_status.html",val=s)

@app.route("/aaccept_application")
def aaccept_application():
    id=request.args.get('id')
    cmd.execute("UPDATE `apply` SET `status`='accepted' WHERE `apply_id`='"+str(id)+"'")
    con.commit()
    return '''<script>alert("accepted");window.location='/view_application_and_updatestatus'</script>'''

@app.route("/rejecct_application")
def accept_application():
    id = request.args.get('id')
    cmd.execute("UPDATE `apply` SET `status`='rejected' WHERE `apply_id`='" + str(id) + "'")
    con.commit()
    return '''<script>alert("rejected");window.location='/view_application_and_updatestatus'</script>'''


app.run(debug=True)
