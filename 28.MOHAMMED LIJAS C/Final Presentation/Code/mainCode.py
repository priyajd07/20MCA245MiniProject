import os
from sklearn.feature_extraction.text import TfidfVectorizer
import datetime
from flask import *
import pymysql
from werkzeug.utils import secure_filename
from predict import *
app=Flask(__name__)
con=pymysql.connect(host="localhost",port=3306,user="root",password="root",db="cyberbullying")
cmd=con.cursor()
app.secret_key="asdf"
@app.route('/')
def main():
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")
@app.route('/login',methods=['post','get'])
def login():
    uname=request.form['textfield']
    pwd=request.form['textfield2']
    cmd.execute("select * from login where user_name='"+uname+"' and password='"+pwd+"'")
    s=cmd.fetchone()
    if s is None:
        return '''<script>alert("invalid username or password");window.location='/'</script>'''
    elif s[3]=='admin':
        session['lid']=s[0]
        return '''<script>alert("successfull");window.location='/homeadmin'</script>'''
    elif s[3] == 'user':
        session['lid']=s[0]
        return '''<script>alert("successfull");window.location='/userhome'</script>'''
    else:
        return '''<script>alert("ivalid");window.location='/userhome'</script>'''

@app.route('/homeadmin')
def homeadmin():
    if 'lid' in session:
        return render_template("homeadmin.html")
    else:
        return redirect('/logout')
@app.route('/adaddbullyindwrds')
def adaddbullyindwrds():
    if 'lid' in session:
        return render_template("adaddbullyindwrds.html")
    else:
        return redirect('/logout')
@app.route('/adaddgoodwrds')
def adaddgoodwrds():
    if 'lid' in session:
        return render_template("adaddgoodwrds.html")
    else:
        return redirect('/logout')




@app.route('/adaddbullyindwrdssubmit',methods=['get','post'])
def adaddbullyindwrdssubmit():
    if 'lid' in session:
        word = request.form['textfield']
        idd = session['lid']
        cmd.execute("insert into bullying values('" + str(idd) + "',null,'" + word + "',curdate())")
        con.commit()
        return '''<script>alert("Success");window.location='/homeadmin'</script>'''

    else:
        return redirect('/logout')
@app.route('/adaddgoodwrdssubmit',methods=['get','post'])
def adaddgoodwrdssubmit():
    if 'lid' in session:
        word = request.form['textfield']
        idd = session['lid']
        cmd.execute("insert into good values(null,'" + str(idd) + "','" + word + "',curdate())")
        con.commit()
        return '''<script>alert("Success");window.location='/homeadmin'</script>'''

    else:
        return redirect('/logout')


@app.route('/Addbio1',methods=['post','get'])
def Addbio1():
    if 'lid' in session:
        lid = session['lid']
        cmd.execute("SELECT * FROM `user` WHERE `user`.`l_id`='" + str(lid) + "'")
        s = cmd.fetchone()
        return render_template("Addbio.html", val=s)
    else:
        return redirect('/logout')
@app.route("/choose_pic",methods=['get','post'])
def choose_pic():
    if 'lid' in session:
        return render_template("choose_pic.html")
    else:
        return redirect('/logout')


@app.route("/update_choose_pic",methods=['get','post'])
def update_choose_pic():
    if 'lid' in session:
        idd = session['lid']
        image = request.files['file']
        files = secure_filename(image.filename)
        image.save(os.path.join("static/user_pic", files))
        cmd.execute("update user set photo='" + files + "' where `user`.`l_id`='" + str(idd) + "'")
        con.commit()
        return '''<script>alert("Image Updated Successfully");window.location='/Addbio1'</script>'''

    else:
        return redirect('/logout')



@app.route('/updateAddbio1',methods=['post','get'])
def updateAddbio1():
    if 'lid' in session:
        id = session['lid']
        fname = request.form['textfield']
        lname = request.form['textfield2']
        gender = request.form['radiobutton']
        dob = request.form['date']
        phone = request.form['textfield3']
        bio = request.form['textfield5']
        cmd.execute(
            "update user set f_name='" + fname + "',l_name='" + lname + "',gender='" + gender + "',d_o_b='" + dob + "',phone_number='" + phone + "',bio='" + bio + "' where l_id='" + str(
                id) + "'")
        con.commit()
        return '''<script>alert("Successfully Updated");window.location='/Addbio1'</script>'''

    else:
        return redirect('/logout')



@app.route('/Addbio',methods=['post','get'])
def Addbio():
    try:

        photo = request.files['file']
        files = secure_filename(photo.filename)
        photo.save(os.path.join("static/user_pic", files))
        firstname = request.form['textfield5']
        lname = request.form['textfield6']
        Gender = request.form['radiobutton']
        dob = request.form['textfield']
        PhoneNumber = request.form['textfield2']
        bio = request.form['textarea']
        username = request.form['textfield3']
        password = request.form['textfield4']
        cmd.execute("insert into login values(null,'" + username + "','" + password + "','user')")
        lid = con.insert_id()
        cmd.execute("insert into user values('" + str(
            lid) + "',null,'" + firstname + "','" + lname + "','" + Gender + "','" + dob + "','" + PhoneNumber + "','" + files + "','" + bio + "')")
        con.commit()
        return '''<script>alert("Success");window.location='/'</script>'''
    except Exception as e:
        return '''<script>alert("Duplicate entry plz try again...");window.location='/'</script>'''


@app.route('/view_and_edit_words')
def view_and_edit_words():
    if 'lid' in session:
        cmd.execute("SELECT * FROM `bullying`")
        s = cmd.fetchall()
        return render_template("view_and_edit_words.html", val=s)
    else:
        return redirect('/logout')
@app.route('/viewgoodwords')
def viewgoodwords():
    if 'lid' in session:
        cmd.execute("SELECT * FROM good")
        s = cmd.fetchall()
        return render_template("viewgoodwords.html", val=s)
    else:
        return redirect('/logout')



@app.route('/edit_word',methods=['get','post'])
def edit_word():
    if 'lid' in session:
        id = request.args.get('id')
        session['id'] = id
        cmd.execute("SELECT * FROM `bullying` WHERE `bullying`.`bull_id`='" + str(id) + "'")
        s = cmd.fetchone()
        return render_template("edit_word.html", val1=s)
    else:
        return redirect('/logout')
@app.route('/edit_word1',methods=['get','post'])
def edit_word1():
    if 'lid' in session:
        id = request.args.get('id')
        session['id'] = id
        cmd.execute("SELECT * FROM `good` WHERE `id`='" + str(id) + "'")
        s = cmd.fetchone()
        return render_template("edit_word1.html", val1=s)
    else:
        return redirect('/logout')

@app.route('/update_word',methods=['get','post'])
def update_word():
    if 'lid' in session:
        id = session['id']
        word = request.form['textfield']
        cmd.execute("update bullying set bull_word='" + word + "' where bull_id='" + str(id) + "'")
        con.commit()
        return '''<script>alert("Success");window.location='/view_and_edit_words'</script>'''
    else:
        return redirect('/logout')
@app.route('/update_word1',methods=['get','post'])
def update_word1():
    if 'lid' in session:
        id = session['id']
        word = request.form['textfield']
        cmd.execute("update good set word='" + word + "' where id='" + str(id) + "'")
        con.commit()
        return '''<script>alert("Success");window.location='/viewgoodwords'</script>'''
    else:
        return redirect('/logout')

@app.route('/delete_word',methods=['get','post'])
def delete_word():
    if 'lid' in session:
        id = request.args.get('id')
        cmd.execute("DELETE FROM `bullying` WHERE `bullying`.`bull_id`='" + str(id) + "'")
        con.commit()
        return '''<script>alert("Deleted");window.location='/homeadmin'</script>'''
    else:
        return redirect('/logout')
@app.route('/delete_word1',methods=['get','post'])
def delete_word1():
    if 'lid' in session:
        id = request.args.get('id')
        cmd.execute("DELETE FROM good WHERE id='" + str(id) + "'")
        con.commit()
        return '''<script>alert("Deleted");window.location='/homeadmin'</script>'''
    else:
        return redirect('/logout')


@app.route('/addcomment',methods=['get','post'])
def addcomment():
    if 'lid' in session:
        postid = request.args.get('id')
        session['pid'] = postid

        return render_template("addcomment.html")
    else:
        return redirect('/logout')
@app.route('/addcommentsubmit',methods=['get','post'])
def addcommentsubmit():
    if 'lid' in session:
        userid = session['lid']
        comment = request.form['textfield']
        cmm=predictfn(comment)
        print(cmm)







# ______sentence_analysis______
        cmd.execute("select * from bullying")
        s = cmd.fetchall()
        bull = ""
        for i in s:
            bull = bull + " " + str(i[2])
        print(bull)

        documents = [comment, bull]
        tfidf = TfidfVectorizer().fit_transform(documents)
        # no need to normalize, since Vectorizer will return normalized tf-idf
        pairwise_similarity = tfidf * tfidf.T

        marks = str(pairwise_similarity).split('\n')
        per = 0.0
        print(pairwise_similarity)
        if (len(marks) >= 4):
            print('iffffff')
            pp = marks[0].split('\t')[1]
            per = float(pp)
        print("per",per)
        if ((per!=0)or(cmm=='Negative')):
            print("bully",cmm)
            cmd.execute("insert into report values(null,'" + str(session['lid']) + "','" + str(
                session['pid']) + "','" + comment + "',curdate(),'Comment')")
            con.commit()

            return '''<script>alert("Bullying Detected!!!");window.location='/userhome'</script>'''

        else:
            cmd.execute("insert into comment values(null,'" + str(session['pid']) + "','" + str(
                userid) + "','" + comment + "',curdate(),'pending')")
            con.commit()
            return '''<script>alert("successfull");window.location='/userhome'</script>'''


    else:
        return redirect('/logout')




@app.route('/addlike',methods=['get','post'])
def addlike():
    if 'lid' in session:
        postid = request.args.get('id')
        session['pid'] = postid
        lid = session['lid']
        cmd.execute("insert into likke values(null,'" + str(postid) + "','1',curdate(),'" + str(lid) + "')")
        con.commit()
        return '''<script>alert("successfull");window.location='/userhome'</script>'''

    else:
        return redirect('/logout')


@app.route('/adddislike',methods=['get','post'])
def adddislike():
    if 'lid' in session:
        postid = request.args.get('id')
        session['pid'] = postid
        cmd.execute("delete from likke where  `lid`='" + str(postid) + "'")
        return '''<script>alert("successfull");window.location='/userhome'</script>'''
    else:
        return redirect('/logout')
@app.route('/addpost')
def addpost():
    if 'lid' in session:
        return render_template("addpost.html")
    else:
        return redirect('/logout')


@app.route('/addposttttt',methods=['get','post'])
def addposttttt():
    if 'lid' in session:
        id = session['lid']
        caption = request.form['textfield']
        post = request.files['file']

        cmm = predictfn(caption)
        print(cmm)

        # ______sentence_analysis______
        cmd.execute("select * from bullying")
        s = cmd.fetchall()
        bull = ""
        for i in s:
            bull = bull + " " + str(i[2])
        print(bull)

        documents = [caption, bull]
        tfidf = TfidfVectorizer().fit_transform(documents)
        # no need to normalize, since Vectorizer will return normalized tf-idf
        pairwise_similarity = tfidf * tfidf.T

        marks = str(pairwise_similarity).split('\n')
        per = 0.0
        print(pairwise_similarity)
        if (len(marks) >= 4):
            print('iffffff')
            pp = marks[0].split('\t')[1]
            per = float(pp)
        print("per", per)
        if ((per != 0) or (cmm == 'Negative')):
            print("bully", cmm)
            cmd.execute("insert into report values(null,'" + str(session['lid']) + "','post','" + caption + "',curdate(),'Post')")
            con.commit()

            return '''<script>alert("Bullying Detected!!!");window.location='/userhome'</script>'''

        else:
            files = secure_filename(post.filename)
            post.save(os.path.join("static/post", files))
            cmd.execute("insert into post values(null,'" + str(id) + "','" + files + "','" + caption + "',curdate())")
            con.commit()
            return '''<script>alert("Success");window.location='/viewfrndpost'</script>'''



    else:
        return redirect('/logout')



@app.route('/admnreport')
def admnreport():
    if 'lid' in session:
        return render_template("admnreport.html")
    else:
        return redirect('/logout')

@app.route('/adviewuser')
def adviewuser():
    if 'lid' in session:
        cmd.execute("SELECT * FROM `user` ")
        s = cmd.fetchall()

        return render_template("adviewuser.html", val=s)

    else:
        return redirect('/logout')

@app.route('/editpost')
def editpost():
    if 'lid' in session:
        return render_template("editpost.html")
    else:
        return redirect('/logout')

@app.route('/frndrequest')
def frndrequest():
    if 'lid' in session:
        return render_template("frndrequest.html")
    else:
        return redirect('/logout')


@app.route('/searchfrnd')
def searchfrnd():
    if 'lid' in session:
        return render_template("searchfrnd.html")
    else:
        return redirect('/logout')



@app.route('/searachhh',methods=['get','post'])
def searachhh():
    if 'lid' in session:

        name = request.form['textfield']
        cmd.execute("SELECT * FROM `user` WHERE `user`.`f_name` like '" + name + "%' AND `user`.`l_id`!='" + str(
            session['lid']) + "'")
        # cmd.execute("SELECT * FROM `user` WHERE `user`.`f_name`='"+name+"' AND `user`.`l_id`!='"+str(session['lid'])+"' AND `user`.`user_id` NOT IN (SELECT `to_id` FROM `request`)")
        s = cmd.fetchall()
        return render_template("searchfrnd.html", val=s)

    else:
        return redirect('/logout')


@app.route('/send_request',methods=['get','post'])
def send_request():
    if 'lid' in session:

        toid = request.args.get('id')
        fromid = session['lid']
        cmd.execute("SELECT * FROM request WHERE (from_id='"+str(fromid)+"' AND to_id='"+str(toid)+"') OR (from_id='"+str(toid)+"' AND to_id='"+str(fromid)+"')")
        s=cmd.fetchone()
        if s is None:
            cmd.execute("insert into request values(null,'" + str(fromid) + "','" + str(toid) + "',curdate(),'pending')")
            con.commit()
            return '''<script>alert("Request Sended Successfully");window.location='/userhome'</script>'''
        else:
            if s[4]=="Accepted":
                return '''<script>alert("Alreday Friends!");window.location='/userhome'</script>'''
            elif s[4] == "pending":
                return '''<script>alert("Request in Pending!!");window.location='/userhome'</script>'''
            else:
                cmd.execute(
                    "insert into request values(null,'" + str(fromid) + "','" + str(toid) + "',curdate(),'pending')")
                con.commit()
                return '''<script>alert("Request Sended Successfully");window.location='/userhome'</script>'''

    else:
        return redirect('/logout')



@app.route('/signupuser')
def signupuser():
   return render_template("signupuser.html")
@app.route('/userhome')
def userhome():
    if 'lid' in session:
        return render_template("userhome.html")
    else:
        return redirect('/logout')

@app.route('/viewbullyingwors')
def viewbullyingwords():
    if 'lid' in session:
        return render_template("viewbullyingwords.html")
    else:
        return redirect('/logout')

@app.route('/viewfrndpost')
def viewfrndpost():
    if 'lid' in session:
        lid = session['lid']
        cmd.execute(
            "SELECT * FROM `post`  LEFT JOIN `likke` ON `likke`.`postid`=`post`.`post_id` WHERE `post`.`l_id`!='" + str(
                lid) + "'")
        s = cmd.fetchall()
        print(s)
        return render_template("viewfrndpost.html", vall=s)

    else:
        return redirect('/logout')


@app.route('/viewpost')
def viewpost():
    if 'lid' in session:
        id = session['lid']
        cmd.execute("SELECT * FROM `post` WHERE `post`.`l_id`='" + str(id) + "'")
        s = cmd.fetchall()

        return render_template("viewpost.html", val=s)
    else:
        return redirect('/logout')
@app.route('/likecmmnt')
def likecmmnt():
    if 'lid' in session:
        id = request.args.get('id')
        cmd.execute(
            "SELECT comment.*,`user`.`f_name`,`l_name` FROM `comment`JOIN`user`ON`comment`.`user_id`=`user`.`l_id` WHERE`comment`.`post_id`= '" + str(
                id) + "'")
        c = cmd.fetchall()
        print(c)
        cmd.execute("SELECT COUNT(`lid`) FROM likke WHERE postid='" + str(id) + "'")
        l = cmd.fetchone()
        return render_template('viewlc.html', c=c, l=l)
    else:
        return redirect('/logout')
@app.route('/usereditpost',methods=['get','post'])
def usereditpost():
    if 'lid' in session:
        pid = request.args.get('id')
        session['pid'] = pid
        cmd.execute("SELECT * FROM `post` WHERE `post`.`post_id`='" + str(pid) + "'")
        s = cmd.fetchone()
        print(s)
        return render_template("user_edit_post.html", val=s)
    else:
        return redirect('/logout')

@app.route('/deletepost',methods=['get','post'])
def deletepost():
    if 'lid' in session:
        id = request.args.get('id')
        cmd.execute("delete from likke where postid='" + str(id) + "'")
        con.commit()
        return '''<script>alert("Success");window.location='/userhome'</script>'''
    else:
        return redirect('/logout')
@app.route('/deletepost1',methods=['get','post'])
def deletepost1():
    if 'lid' in session:
        id = request.args.get('id')
        cmd.execute("delete from post where post_id='" + str(id) + "'")
        con.commit()
        return '''<script>alert("Success");window.location='/userhome'</script>'''
    else:
        return redirect('/logout')

@app.route('/userupdatepost',methods=['get','post'])
def userupdatepost():
    if 'lid' in session:
        id = session['pid']
        caption = request.form['textfield']
        post = request.files['file']
        files = secure_filename(post.filename)
        post.save(os.path.join("static/post", files))
        cmd.execute(
            "update post set post='" + files + "',caption='" + caption + "' where `post`.`post_id`='" + str(id) + "'")
        con.commit()
        return '''<script>alert("Successfully Updated");window.location='/viewpost'</script>'''
    else:
        return redirect('/logout')


@app.route('/viewprofileuser')
def viewprofileuser():
    if 'lid' in session:

        return render_template("viewprofileuser.html")
    else:
        return redirect('/logout')
@app.route('/viewreport')
def viewreport():
    if 'lid' in session:

        return render_template("viewreport.html")
    else:
        return redirect('/logout')

@app.route('/viewrequest')
def viewrequest():
    if 'lid' in session:

        cmd.execute(
            "SELECT `request`.*,`user`.* FROM `user` JOIN `request` ON `request`.`from_id`=`user`.`l_id` WHERE `request`.`to_id`='" + str(
                session['lid']) + "'  AND `request`.`status`='pending'")
        s = cmd.fetchall()
        return render_template("viewreport.html", val=s)

    else:
        return redirect('/logout')

@app.route('/accept_request',methods=['get','post'])
def accept_request():
    if 'lid' in session:

        id = request.args.get('id')
        cmd.execute("update request set status='Accepted' where request_id='" + str(id) + "'")
        con.commit()

        return '''<script>alert("Request Accepted");window.location='/userhome'</script>'''
    else:
        return redirect('/logout')


@app.route('/reject_request',methods=['get','post'])
def reject_request():
    if 'lid' in session:
        id = request.args.get('id')
        cmd.execute("update request set status='Rejected' where request_id='" + str(id) + "'")
        con.commit()

        return '''<script>alert("Request Rejected");window.location='/userhome'</script>'''

    else:
        return redirect('/logout')

@app.route('/useraddbullwords',methods=['get','post'])
def useraddbullwords():
    if 'lid' in session:
        return render_template("useradaddbullyindwrds.html")
    else:
        return redirect('/logout')



@app.route('/useradaddbullyindwrdssubmit',methods=['get','post'])
def useradaddbullyindwrdssubmit():
    if 'lid' in session:
        word = request.form['textfield']
        idd = session['lid']
        cmd.execute("insert into bullying values('" + str(idd) + "',null,'" + word + "',curdate())")
        con.commit()
        return '''<script>alert("Success");window.location='/userhome'</script>'''

    else:
        return redirect('/logout')
@app.route('/viewadminreport',methods=['get','post'])
def viewadminreport():
    if 'lid' in session:
        cmd.execute(
            "SELECT `report`.*,`user`.`f_name`,`l_name` FROM `report`JOIN `user`ON `report`.l_id=`user`.`l_id` ")
        s = cmd.fetchall()
        return render_template("viewreportad.html", val=s)
    else:
        return redirect('/logout')
@app.route('/chatuser')
def chatuser():
    if 'lid' in session:
        cmd.execute(
            "SELECT `user`.* FROM `user` JOIN `request` ON (`request`.to_id=`user`.`l_id` AND `request`.`from_id`='"+str(session['lid'])+"') OR (`request`.`from_id`=`user`.`l_id` AND `request`.`to_id`='"+str(session['lid'])+"') WHERE `request`.`status`='Accepted'")
        s = cmd.fetchall()
        return render_template("chatlist.html", val=s)
    else:
        return redirect('/logout')


@app.route('/block',methods=['GET','POST'])
def block():
    id=request.args.get("id")
    qry="update login set usertype='blocked' where l_id="+str(id)
    cmd.execute(qry)
    con.commit()
    return '''<script>alert("Successfully Blocked");window.location='/viewadminreport'</script>'''

@app.route('/chat1',methods=['GET','POST'])
def chat1():
    uid=request.args.get('id')
    session['uidd']=uid
    cmd.execute("select f_name,l_name from user where l_id="+str(uid))
    s1 = cmd.fetchone()
    fid=session['lid']
    session['idd'] = uid
    cmd.execute("select * from chat where (f_id='"+str(uid)+"' and t_id='"+str(fid)+"') or (f_id='"+str(fid)+"' and t_id='"+str(uid)+"') order by date asc")
    s = cmd.fetchall()
    return render_template('chat.html',data=s,fname=s1,fr=str(uid))
@app.route('/chat2',methods=['GET','POST'])
def councilorchat2():
    uid = session['uidd']
    cmd.execute("select f_name,l_name from user where l_id="+str(uid))
    s1 = cmd.fetchone()
    fid=session['lid']
    session['idd'] = uid
    cmd.execute("select * from chat where (f_id='"+str(uid)+"' and t_id='"+str(fid)+"') or (f_id='"+str(fid)+"' and t_id='"+str(uid)+"') order by date asc")
    s = cmd.fetchall()
    return render_template('chat.html',data=s,fname=s1,fr=str(uid))
@app.route('/chat_send',methods=['GET','POST'])
def councilor_send():
    btn=request.form['button']
    if (btn=="send"):
        fid=session["lid"]
        print(fid)
        tid=session['idd']
        session['uidd']=tid
        print(tid)
        msg=request.form['textarea']
        cmd.execute("insert into chat values(null,'"+str(fid)+"','"+str(tid)+"','"+msg+"',curdate())")
        con.commit()
        return '''<script>window.location='/chat2#services'</script>'''
    else:
        return '''<script>window.location='/chat2#services'</script>'''

@app.route('/recometation',methods=['GET','POST'])
def recometation():
    id=str(session['lid'])
    qry="SELECT `request`.`from_id` FROM `request` WHERE `to_id`="+id+" AND `status`='Accepted' UNION SELECT `request`.`to_id` FROM `request` WHERE `from_id`="+id+" AND `status`='Accepted'"
    cmd.execute(qry)
    res=cmd.fetchall()
    ress=["0"]
    for i in res:
        ress.append(str(i[0]))
    ress=",".join(ress)

    ressflist=ress
    print(res,"11111111111111111111")
    print(ress,"2222222222222222222222")
    qry="SELECT `request`.`from_id` FROM `request` WHERE `to_id` IN("+ress+") AND `status`='Accepted' AND `from_id`!="+id+" UNION SELECT `request`.`to_id` FROM `request` WHERE `from_id`  IN("+ress+") AND `status`='Accepted' AND `to_id`!="+id+""
    cmd.execute(qry)

    res=cmd.fetchall()

    ress = ["0"]
    for i in res:
        ress.append(str(i[0]))
    ress = ",".join(ress)

    print(res, "333333333333333333")
    print(ress, "44444444444444444444444444444")
    print(ressflist, "77777777777777777777777")

    qry="SELECT * FROM `user` WHERE `l_id` IN("+ress+") and l_id not in("+ressflist+")"
    print(qry,"8888888888888888888888")
    cmd.execute(qry)
    res=cmd.fetchall()

    print(res,"5555555555555555555555555555555555555")
    return render_template("view_friend_suggestion.html",val=res)

def cleardata():
    qry="delete from login where l_id in(select l_id from user)"
    cmd.execute(qry)
    qry="delete from user"
    cmd.execute(qry)
# cleardata()
app.run(debug=True)