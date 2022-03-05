from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def predictfn(fn,comp):
    fulllist=[]

    p_list = fn.split(" ")
    df_pos = []
    for r in p_list:
        if r not in df_pos:
            df_pos.append(r)
        if r not in fulllist:
            fulllist.append(r)




    i = 0
    corp = []
    tcorp=[]
    f_t_label = []
    tlabel=[]
    listcount = []
    count = 0
    for rr in df_pos:

    #giving label as 0 for positive
        if str(rr) != 'nan':
            corp.append(rr)
            f_t_label.append(0)
            count = count + 1
            if count==10:
                count=0
                tcorp.append(rr)
                tlabel.append(0)

        listcount.append(count)
        i = i + 1


    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corp)
    print(len(vectorizer.get_feature_names()))
    print(vectorizer.get_feature_names())

    print(X.toarray())


    # Load the dataset
    # data = fetch_20newsgroups()# Get the text categories
    text_categories = [0,1]#data.target_names# define the training set
    train_data =corp


    train_data1=[]
    for i in range(0,len(train_data)):
        train_data1.append([i,i])



    model = make_pipeline(TfidfVectorizer(), MultinomialNB())# Train the model using the training data
    model.fit(train_data, f_t_label)# Predict the categories of the test data
    predicted_categories = model.predict(tcorp)


    import nltk
    import re
    nltk.download('punkt')
    import collections
    import string
    from nltk.tokenize import sent_tokenize,word_tokenize
    str = comp
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|`'''
    sentences=[str] #sent_tokenize(str)
    new_words = []
    freq_table = {}
    score = {}
    #tokenized_word=[]
    with open("input_data.txt","w+",encoding="UTF-8") as f:
        for sent in sentences:
            new_words = []
            freq_table = {}
            sent = ''.join([i for i in sent if not i.isdigit()])
            for x in sent:
                if x in punctuations:
                    sent = sent.replace(x, "")
            print(sent)
            tokenized_word=word_tokenize(sent)
            print(tokenized_word)
            f.write('\n'.join(tokenized_word)+'\n')



    sent=open("input_data.txt","r+",encoding="UTF-8")

    file=sent.read()

    negative_list = file.split(" ")
    df_neg=[]
    for r in negative_list:
        if r not in df_neg:
            if r!='':
                if r in fulllist:
                    df_neg.append(r)

    if len(df_neg)>0:

        lis=[]
        for r in df_neg:
            ind = train_data.index(r)
            lis.append([ind,ind])


        predicted_categories = model.predict(lis)


        res=((len(predicted_categories)-sum(predicted_categories))/len(predicted_categories))*100
        return 100-res

    else:
        return 100
