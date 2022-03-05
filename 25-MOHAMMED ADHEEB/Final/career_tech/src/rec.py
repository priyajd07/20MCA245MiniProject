from scipy import spatial

import pymysql
from sklearn.feature_extraction.text import TfidfVectorizer





vect = TfidfVectorizer(min_df=1, stop_words="english")
from nltk import word_tokenize
from nltk. corpus import stopwords
def recommendor(id):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='career_tech')
    cmd = con.cursor()

    stuentid=id
    # q="select * from course "
    # rescrs=selectall(q)
    cmd.execute("SELECT * FROM `job_post`")
    rescrs=cmd.fetchall()
    # q2="select * from student where `loginid`!="+str(stuentid)
    # resusers=selectall(q2)
    cmd.execute("SELECT `education` FROM `education_qualification` WHERE `candidate_id`="+str(stuentid))
    resusers=cmd.fetchall()


    crslist=[]
    for i in resusers:
        crslist.append(str(str(i[0])))
    quali=' '.join(crslist)



    dataset=[]
    result = ['0']
    for i in rescrs:
        row=[i[0],i[6]]
        corpus = [quali, i[6]]
        tfidf = vect.fit_transform(corpus)
        pairwise_similarity = tfidf * tfidf.T

        res = str(pairwise_similarity).split('\n')

        if len(res) > 2:

            res = res[0].split('\t')[1]
            print(res,"%%%%%%%%%%%%%%%%%%%%%%%%")
            if float(res) > .5:
                result.append(str(i[0]))



    # for i in resusers:
    #     row=[]
    #     crsrow=[]
    #     # qry="SELECT `courseid` FROM `course_apply` WHERE `studentid`="+str(i[1])
    #     cmd.execute("SELECT `job_id` FROM `apply` WHERE `candidate_id`="+str(i[5]))
    #     # crssele=selectall(qry)
    #     crssele =cmd.fetchall()
    #     for ii in crssele:
    #         crsrow.append(str(ii[0]))
    #     for ii in crslist:
    #         if ii in crsrow:
    #             row.append(1)
    #         else:
    #             row.append(0)
    #
    #     dataset.append(row)
    #
    # # qry = "SELECT `courseid` FROM `course_apply` WHERE `studentid`=" + str(id)
    # cmd.execute("SELECT `job_id` FROM `apply` WHERE `candidate_id`="+ str(id))
    # # crssele = selectall(qry)
    # crssele=cmd.fetchall()
    # crsrow=[]
    # row=[]
    # for ii in crssele:
    #     crsrow.append(str(ii[0]))
    # for ii in crslist:
    #     if ii in crsrow:
    #         row.append(1)
    #     else:
    #         row.append(0)
    #
    #
    # print(row)
    # # dataset.append(row)
    # print(dataset)
    # distributions = []
    # for i in range(0,len(dataset)):
    #     sd=spatial.distance.euclidean(row,dataset[i])
    #     # print(sd)
    #     # print(i,resusers[i])
    #     distributions.append([sd, resusers[i][5]])
    # results = [i[1] for i in sorted(distributions)[:3]]
    # print(distributions)
    # print(results)
    # lis=[]
    # for i in results:
    #     lis.append(str(i))
    # result=','.join(lis)
    # print(result)
    return result

# res=recommendor()



def stop(text):

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import numpy as np
    import nltk

    def process(file):
        raw = open(file).read()
        tokens = word_tokenize(raw)
        words = [w.lower() for w in tokens]
        porter = nltk.PorterStemmer()
        stemmed_tokens = [porter.stem(t) for t in words]
        # Removing stop words
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [w for w in stemmed_tokens if not w in stop_words]
        # count words
        count = nltk.defaultdict(int)
        for word in filtered_tokens:
            count[word] += 1
        return count;

    def cos_sim(a, b):
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        return dot_product / (norm_a * norm_b)

    def getsimilarity(dictl, dict2):
        all_words_list = []
        for key in dictl:
            all_words_list.append(key)
        for key in dict2:
            all_words_list.append(key)
        all_words_list_size = len(all_words_list)

        v1 = np.zeros(all_words_list_size, dtype=np.int)
        v2 = np.zeros(all_words_list_size, dtype=np.int)
        i = 0
        for (key) in all_words_list:
            v1[i] = dictl.get(key, 0)
            v2[i] = dict2.get(key, 0)
            i = i + 1
        return cos_sim(v1, v2)

    example_sent = text.lower()
    example_sent=str(example_sent).replace('-',' ')
    example_sent = str(example_sent).replace('_', ' ')
    stop_words= set(stopwords.words('english'))
    word_tokens= word_tokenize(example_sent)

    filtered_sentence= [w for w in word_tokens if not w in stop_words]

    filtered_sentence=[]

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)


    return filtered_sentence
def process(file):
    raw =file
    tokens = word_tokenize(raw)
    words = [w. lower() for w in tokens]
    porter = nltk.PorterStemmer()
    stemmed_tokens = [porter. stem(t) for t in words]
    # Removing stop words
    stop_words = set(stopwords.words( 'english' ) )
    filtered_tokens = [w for w in stemmed_tokens if not w in stop_words]
    # count words
    count = nltk.defaultdict(int)
    for word in filtered_tokens:
        count [word] += 1
    return count;
def cos_sim(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a  * norm_b)


