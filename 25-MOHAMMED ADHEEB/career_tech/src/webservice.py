import os
from flask import  *
import re, math
from datetime import datetime
import pymysql
import xlrd
from scipy import spatial
from werkzeug.utils import secure_filename
from src.neww import predictfn
from src.rec import recommendor
# import xlrd
con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='career_tech')
cmd=con.cursor()
from collections import Counter
WORD = re.compile(r'\w+')
app = Flask(__name__)
#LOGIN CANDIDATE
@app.route('/login',methods=['POST'])
def login():
    try:
        uname=request.form['uname']
        passwd=request.form['pass']
        try:
            cmd.execute("select * from login where user_name='"+uname+"' and password='"+passwd+"'")
            s=cmd.fetchone()
            print(s)
            if s is  not None:
                id=s[0]
                type=s[3]
                print(id)
                return jsonify({'task':str(id)})
            else:
                return jsonify({'task':"invalid"})
        except Exception as e:
            print(str(e))
            return jsonify({'task':"invalid"})
    except Exception as e:
        print(e)
        return jsonify({'task':"success"})




#CANDIDATE REGISTRATION
@app.route('/registration',methods=['POST'])
def registration():
    name=request.form['name']
    email=request.form['email']
    contact1=request.form['contact1']
    contact2=request.form['contact2']
    username=request.form['uname']
    password=request.form['password']
    cmd.execute("insert into login values(null,'"+username+"','"+password+"','user')")
    lid=con.insert_id()
    cmd.execute("insert into candidate values(null,'"+name+"','"+email+"','"+contact1+"','"+contact2+"','"+str(lid)+"')")
    con.commit()
    return jsonify({'task': "success"})





@app.route('/send_complaints',methods=['POST'])
def send_complaints():
    lid=request.form['lid']
    complaints=request.form['complaints']
    cmd.execute("insert into complaints values(null,'"+str(lid)+"',curdate(),'"+complaints+"','pending')")
    con.commit()
    return jsonify({'task': "success"})






#UPLOAD CV
@app.route('/uploadcv',methods=['POST'])
def uploadcv():
    lid=request.form['lid']
    education=request.form['education']
    institution = request.form['institution']
    year = request.form['year']
    regno = request.form['regno']
    percentage = request.form['percentage']
    cmd.execute("insert into education_qualification values(null,'"+str(lid)+"','"+education+"','"+institution+"','"+year+"','"+regno+"','"+percentage+"')")
    con.commit()
    return jsonify({'task': "success"})




@app.route('/company',methods=['POST'])
def company():
    cmd.execute("SELECT * FROM company_details")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


@app.route('/viewcomp_vacancy',methods=['POST'])
def viewcomp_vacancy():
    comid=request.form['cid']
    cmd.execute("SELECT * FROM `job_post` WHERE `company_id`='"+str(comid)+"'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)

# @app.route('/viewcomp_vacancy',methods=['POST'])
# def viewcomp_vacancy():
#     cid=request.form['cid']
#     id1=request.form['id1']
#     print(cid)
#     cmd.execute("SELECT `education_qualification`.*,`qualification_details`.* FROM `qualification_details` JOIN `education_qualification` ON `education_qualification`.`candidate_id`=`qualification_details`.`candidate_id` WHERE `education_qualification`.`candidate_id`='"+str(id1)+"'")
#     sres=cmd.fetchone()
#
#
#
#     print("sres----",sres)
#     cmd.execute("SELECT `company_details`.`company_name`,`job_post`.* FROM `job_post`,`company_details` WHERE `company_details`.`login_id`=`job_post`.`company_id` AND `job_post`.`company_id`='"+str(cid)+"'")
#     row_headers = [x[0] for x in cmd.description]  # this will extract row headers
#     results = cmd.fetchall()
#     json_data = []
#     for result in results:
#         print(result[1])
#         # cmd.execute("SELECT `branch`,`yop`,`backlog`,`percentage`,vacancy_details.`qualification`,`experience` FROM `vacancy_details` JOIN `vaccancy` ON `vaccancy`.v_id=`vacancy_details`.`vid` WHERE `vaccancy`.`v_id`="+str(result[1]))
#         cmd.execute("SELECT  * FROM `job_post` WHERE `job_post`.`job_id`='"+str(result[1])+"'")
#         svac=cmd.fetchone()
#         print("svac----",svac)
#         str1=svac[4]+" "+svac[6]+" "+svac[7]
#         print(svac[4])
#         print(svac[6])
#         print(svac[7])
#         ma = similarity_check(str(sres), str(str1))
#         if ma > 0.4:
#             json_data.append(dict(zip(row_headers, result)))
#     con.commit()
#     print(json_data)
#
#     return jsonify(json_data)
#
#
# def similarity_check(message, msg1):
#
#         # cosine similarity
#
#     def get_cosine(vec1, vec2):
#         intersection = set(vec1.keys()) & set(vec2.keys())
#         numerator = sum([vec1[x] * vec2[x] for x in intersection])
#
#         sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
#         sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
#         denominator = math.sqrt(sum1) * math.sqrt(sum2)
#
#         if not denominator:
#             return 0.0
#         else:
#                   return float(numerator) / denominator
#
#
#
#
#     def text_to_vector(text):
#         words = WORD.findall(text)
#         return Counter(words)
#
#
#     print()
#         # message= "PLUSTWO,SCIENCE,2010-2012,0,40 TO 90,0-1"
#
#     vector1 = text_to_vector(str(message))
#
#     vector2 = text_to_vector(str(msg1))
#     cosine = get_cosine(vector1, vector2)
#     print("cosine", cosine)
#
#     return cosine
#


@app.route('/apply_for_job',methods=['POST'])
def apply_for_job():
    lid=request.form['lid']
    jobid=request.form['jobid']
    cmd.execute("insert into apply values(null,'"+str(lid)+"','"+str(jobid)+"',curdate(),'pending')")
    con.commit()
    return jsonify({'task': "success"})








@app.route('/more_qualification_details',methods=['POST'])
def more_qualification_details():
    lid=request.form['lid']
    skill=request.form['skill']
    exp= request.form['experience']
    cmd.execute("insert into qualification_details values(null,'"+str(lid)+"','"+skill+"','"+exp+"')")
    con.commit()
    return jsonify({'task': "success"})


@app.route('/addmore_personal_details',methods=['POST'])
def addmore_personal_details():
    print(request.files)

    # lid=request.form['lid']
    #
    #
    # dob=request.form['dob']
    #
    # obective=request.form['obective']
    # # print(obective)
    # house = request.form['house']
    # # print(house)
    # place = request.form['place']
    # # print(place)
    # post = request.form['post']
    # # print(post)
    # pin = request.form['pin']
    # # print(pin)
    # father = request.form['father']
    # # print(father)
    # mother = request.form['mother']
    # # print(mother)
    # quardn = request.form['quardn']
    # # print(quardn)
    # relatn = request.form['relatn']
    # # print(relatn)
    # gender = request.form['gender']
    photo = request.files['file']
    print(photo,"00000000000000000")
    # path='./static/candidate_pc'
    file=secure_filename(photo.filename)
    print(file, "00000000000000000")
    file = file.split('.')

    file =datetime.now().strftime("%Y%m%d%H%M%S")+"."+ file[len(file)-1]
    # os.path.join(photo.save("static/candidate_pc"+file))
    photo.save(os.path.join("static/pic",file))

    # cmd.execute("insert into resume values(null,'"+str(file)+"','"+str(dob)+"','"+str(obective)+"','"+str(gender)+"','"+str(house)+"','"+str(place)+"','"+str(post)+"','"+str(pin)+"','"+str(father)+"','"+str(mother)+"','"+str(quardn)+"','"+str(relatn)+"','"+str(lid)+"')")
    # con.commit()
    return jsonify({'task': "success"})
@app.route('/view_question',methods=['POST'])
def view_question():
    postid=request.form['pid']
    comid=request.form['cid']
    cmd.execute("SELECT * FROM `company_question` WHERE `company_question`.`post_id`='"+str(postid)+"' AND `company_question`.`company_loginid`='"+(str(comid))+"'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)

@app.route('/markup',methods=['POST'])
def markup():
    candidate_id=request.form['lid']
    print(candidate_id)
    com_id=request.form['cid']
    print(com_id)
    post_id= request.form['sid']
    print(post_id)
    mark = request.form['mark']
    index = request.form['index']
    print(index)
    cmd.execute("insert into result values(null,'"+str(candidate_id)+"','"+str(com_id)+"','"+post_id+"','"+mark+"','"+str(index)+"')")
    con.commit()
    return jsonify({'task': "success"})


@app.route('/select_companyy',methods=['POST'])
def select_company():
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='career_tech')
    cmd = con.cursor()
    cmd.execute("SELECT * FROM `company_details`")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)




@app.route('/select_companyy1',methods=['POST'])
def select_companyy1():
    print(request.form)
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='career_tech')
    cmd = con.cursor()
    lid=request.form['lid']
    cmd.execute("SELECT `apply`.`apply_id`,`job_post`.`job_name`,`job_post`.`job_id`,`company_details`.`company_name` FROM `apply` JOIN `job_post` ON `apply`.`job_id`=`job_post`.`job_id` JOIN `company_details` ON `company_details`.`login_id`=`job_post`.`company_id` WHERE `apply`.`candidate_id`="+str(lid)+" AND `apply`.`status`='scheduled' ")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    print (json_data)
    return jsonify(json_data)


@app.route('/select_postt',methods=['POST'])
def select_post():
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='career_tech')
    cmd = con.cursor()
    cid=request.form['cid']
    print(cid)
    cmd.execute("SELECT * FROM `job_post` WHERE job_post.company_id='"+str(cid)+"'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


@app.route('/viewcomreply',methods=['POST'])
def viewcomreply():
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='career_tech')
    cmd = con.cursor()
    uid=request.form['uid']

    cmd.execute("SELECT * FROM `complaints` WHERE `complaints`.`candidate_id`='"+str(uid)+"'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)






@app.route("/addques",methods=['POST'])
def addques():
    try:
        comid=request.form['cid']
        postid=request.form['sid']
        cmd.execute("SELECT * FROM `company_question` WHERE `company_question`.`post_id`='"+str(postid)+"' AND `company_question`.`company_loginid`='"+str(comid)+"'")
        row_headers = [x[0] for x in cmd.description]
        s = cmd.fetchall()
        print(s)
        json_data = []
        for d in s:
            json_data.append(dict(zip(row_headers, d)))
        print(json_data)
        return jsonify(json_data)
    except Exception as e:
        print(e)
        return jsonify({'task': "invalid"})


@app.route("/addquesnew",methods=['POST'])
def addquesnew():
    try:
        comid=request.form['cid']
        postid=request.form['sid']
        cmd.execute("SELECT * FROM `questions_and_answers` WHERE  `postid`='"+str(postid)+"' AND STATUS='accepted'")
        row_headers = [x[0] for x in cmd.description]
        s = cmd.fetchall()
        print(s)
        json_data = []
        for d in s:
            json_data.append(dict(zip(row_headers, d)))
        print(json_data)
        return jsonify(json_data)
    except Exception as e:
        print(e)
        return jsonify({'task': "invalid"})

@app.route('/markupnew',methods=['POST'])
def markupnew():
    candidate_id=request.form['lid']
    print(candidate_id)
    com_id=request.form['cid']
    print(com_id)
    post_id= request.form['sid']
    print(post_id)
    mark = request.form['mark']
    index = request.form['index']
    cmd.execute("insert into result values(null,'"+str(candidate_id)+"','"+str(com_id)+"','"+post_id+"','"+mark+"','"+str(index)+"')")
    con.commit()
    return jsonify({'task': "success"})




@app.route('/predtc', methods=['post'])
def predtc():
    lid=request.form['lid']
    print(lid)
    repeatedword(lid)
    cmd.execute(
        "SELECT `job_post`.*,`apply`.* FROM `apply` INNER JOIN `job_post` ON `job_post`.`job_id`=`apply`.`job_id` WHERE `apply`.`candidate_id`!='" + str(
            lid) + "'")
    s = cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


def repeatedword(id):

    con = pymysql.connect(host="localhost", user="root", password="", port=3306, database="career_tech")
    cmd = con.cursor()

    fn2 = []
    n = []
    mat = []
    users=[]
    # cmd.execute("select distinct `Userid` FROM `ordertable`")
    cmd.execute("SELECT DISTINCT `login_id` FROM `candidate`")
    users = cmd.fetchall()
    print(users)
    cmd.execute("SELECT DISTINCT `job_id` FROM `job_post`") # menu id alla product id ane vende===================n
    pdts = cmd.fetchall()
    # print(pdts)
    for i in users:
        m = []
        for j in pdts:
            # cmd.execute("select * from `ordertable` WHERE `Userid`='"+str(i[0])+"' AND `Menuid`='"+str(j[0])+"'")
            cmd.execute("SELECT * FROM `apply` WHERE `apply`.`candidate_id`='"+str(i[0])+"' AND `apply`.`job_id`='"+str(j[0])+"'")
            cnt=cmd.fetchall()
            jj=len(cnt)
            # print(jj)
            m.append(jj)
        mat.append(m)
    print("mat",mat)
    mm=[]
    M1 = []
    mat1 = []

    # print(s)
    # cmd.execute("select distinct `Menuid` FROM `ordertable`")
    # pdts1 = cmd.fetchall()
    # print(pdts1)
    m = []
    for j in pdts:
        # cmd.execute("select * from `ordertable` WHERE `Userid`='" + str(id) + "' AND `Menuid`='" + str(j[0]) + "'")

        # cmd.execute("SELECT * FROM `job_post` WHERE `job_post`.`job_id`='"+str(j[0])+"' and `apply`.`candidate_id`='"+str(id)+"'")
        cmd.execute("SELECT * FROM `apply` WHERE `apply`.`job_id`='"+str(j[0])+"' AND `apply`.`candidate_id`='"+str(id)+"'")
        cnt = cmd.fetchall()
        jj = len(cnt)
        # print(jj)
        m.append(jj)
        mat1.append(m)
    rows = []
    print("mat1",m)
    # idx = ma[place]
    # print(rows[place][3])
    # print(idx)
    sim = []
    print(len(users))
    for i in range(0,len(mat)):
        if users[i][0]!=id:
            simm=predictfn(mat[i],m)
            roww = (i, spatial.distance.euclidean(mat[i],m),simm)
            sim.append(roww)
    print(sim)

    sim_scores = sorted(sim, key=lambda x: x[1], reverse=False)
    sim_scores = sim_scores[0:5]

    menulist = []
    for r in sim_scores:
        print("rrrrrrrr", r)

        menulist.append(users[r[0]])
        print(users[r[0]])
        print(menulist)
        print(menulist)
    return menulist


    # # Return the top 5 most similar places
    # return tr_data['place'].iloc[tr_indices]


@app.route('/conformexam',methods=['POST'])
def conformexam():
    lid=request.form['lid']
    date=request.form['date']
    time=request.form['time']
    password=request.form['password']
    cmd.execute("SELECT * FROM `exam_shedule` WHERE `exam_shedule`.`date`='"+str(date)+"' AND `exam_shedule`.`time`='"+str(time)+"' AND `exam_shedule`.`password`='"+str(password)+"' AND `exam_shedule`.`candiid`='"+str(lid)+"'")
    s=cmd.fetchone()
    if s is None:

        return jsonify({'task': "Your Are Not sheduled For Exam"})
    else:
        return jsonify({'task': "You are eligible"})

@app.route('/uploadskill',methods=['POST'])
def uploadskill():
    # lid=request.form['lid']
    photo = request.files['files']
    file = secure_filename(photo.filename)

    photo.save(os.path.join("static/files", file))

    loc = ("static/files/skilss.xlsx")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        print(sheet.cell_value(i, 0))





    return jsonify({'task': "success"})



@app.route('/uploadqualificationfiles',methods=['POST'])
def uploadqualificationfiles():
    lid=request.form['lid']
    photo = request.files['files']
    file = secure_filename(photo.filename)

    photo.save(os.path.join("static/files", file))

    loc = ("static/files/Book1.xlsx")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        print(sheet.cell_value(i, 0))

    return jsonify({'task': "success"})




@app.route('/viewresult',methods=['POST'])
def viewresult():
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='career_tech')
    cmd = con.cursor()
    pid=request.form['pid']

    cmd.execute("SELECT `candidate`.*,`job_post`.`job_name`,`result`.*,CONVERT(SUM(`totalqstn`),CHAR) AS totalqstn,SUM(`marks`) AS totalmark,(SUM(`marks`)/SUM(`result`.`totalqstn`))*100 AS percentage FROM `result` JOIN `job_post` ON `job_post`.`job_id`=`result`.`post_id` JOIN `candidate` ON `candidate`.`login_id`=`result`.`candidate_id`  WHERE `result`.`post_id`='"+str(pid)+"'  GROUP BY`result`.`candidate_id`  ORDER BY percentage DESC")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
        print(json_data)
    return jsonify(json_data)









@app.route('/viewresult1',methods=['POST'])
def viewresult1():
    id=request.form['lid']
    print(id)

    cmd.execute("SELECT distinct `candidate`.`candidate_name`,`candidate`.`contact_01`,`job_post`.`job_name`,`result`.`candidate_id`,`result`.`post_id` FROM `result` INNER JOIN `job_post` ON `job_post`.`job_id`=`result`.`post_id` INNER JOIN `candidate` ON `candidate`.`login_id`=`result`.`candidate_id` WHERE `result`.`candidate_id`='"+str(id)+"' order by candidate_id")
    s=cmd.fetchall()
    print(s,"---------------------------------")
    res=[]
    for i in s:
        cid=i[3]
        pid=i[4]

        cmd.execute("SELECT `marks` FROM `result` WHERE `candidate_id`='"+str(id)+"' AND `post_id`='"+str(pid)+"'")
        ss=cmd.fetchall()
        if(len(ss)>=2):
            row={}
            row['post']=i[2]
            row['tmark']=ss[0][0]
            row['amark']=ss[1][0]




            res.append(row)
    return jsonify(res)







@app.route('/viewpost',methods=['POST'])
def viewpost():
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='career_tech')
    cmd = con.cursor()

    cmd.execute("SELECT * FROM `job_post`")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)

@app.route('/viewpro',methods=['POST'])
def viewpro():
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='career_tech')
    cmd = con.cursor()
    id=request.form['lid']

    cmd.execute("SELECT * FROM `resume` WHERE `canid`='"+str(id)+"'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)




@app.route('/sendfeed',methods=['POST'])
def sendfeed():
   feed=request.form['feed']
   lid=request.form['lid']
   cmd.execute("insert into feedbacks values(null,'"+str(lid)+"','"+feed+"',curdate())")
   con.commit()
   return jsonify({'task': "success"})



@app.route('/recommendation',methods=['post'])
def recommendation():
    print("-----------------------------------------")
    lid=request.form['lid']
    res=recommendor(lid)
    print(res)
    res=','.join(res)
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='career_tech')
    cmd = con.cursor()
    qry = "SELECT * FROM `job_post` WHERE `job_id` IN(SELECT `job_id` FROM `apply` WHERE `candidate_id` IN("+res+")) AND `job_id` NOT IN(SELECT `job_id` FROM `apply` WHERE `candidate_id`='"+str(lid)+"')"
    print(qry)
    print("SELECT * FROM `job_post` WHERE `job_id` IN("+res+") AND `job_id` NOT IN(SELECT `job_id` FROM `apply` WHERE `candidate_id`='"+str(lid)+"')")
    cmd.execute("SELECT * FROM `job_post` WHERE `job_id` IN("+res+") AND `job_id` NOT IN(SELECT `job_id` FROM `apply` WHERE `candidate_id`='"+str(lid)+"')")
    s = cmd.fetchall()
    print(s,"1234567890")
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)




if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)