import math
from tkinter import Tk, Label, Entry

import numpy as np
# import pandas as pd
import random
from collections import Counter
# from sklearn import preprocessing
import time

#for plotting

class CKNN:

    def __init__(self):
        self.accurate_predictions = 0
        self.total_predictions = 0
        self.accuracy = 0.0
        ##########
        # with open('labels.dat') as f:
        #     lines = f.readlines()
        # lines=[s.strip('\n') for s in lines]
        # training_data=np.loadtxt("sample.data",dtype=float,delimiter=" ")

        import pandas as pd
        a = pd.read_csv('static/dataset/covid_19_result.csv')
        a.head()
        training_data1 = a.iloc[:, 0:15].values
        training_data=[]
        for i in training_data1:

            ii=str(i).replace('[','').replace(']','')
            iii=ii.split(' ')

            jj=[]
            for j in iii:
                jj.append(int(j))
            training_data.append(jj)


        liness = a.iloc[:, 15].values
        lines=[]
        for i in liness:
            ii = str(i).replace('[', '').replace(']', '')

            lines.append(ii)



        self.training_set= {'0':[], '1':[]}


        #Split data into training and test for cross validation
        #training_data = lbls[: len(lbls)]
        test_data = []#[-int(test_size * len(dataset)):]

        #Insert data into the training set
        cnt=0

        for record in training_data:
            st=lines[cnt][0]
            cnt+=1


            self.training_set[st[-1]].append( record[:])

    #########

    def predict(self,  to_predict, k = 1):


        distributions = []
        for group in self.training_set:
            i=0
            # print(group,'group')
            for features in self.training_set[group]:

                euclidean_distance = np.linalg.norm(np.array(features)- np.array(to_predict))
                if  group=='6':
                    # print('hi',euclidean_distance,training_data[group],len(training_data[group]),len(to_predict),i)
                    i+=1
                distributions.append([euclidean_distance, group])

        # print(distributions)
        results = [i[1] for i in sorted(distributions)[:k]]
        result = Counter(results).most_common(1)[0][0]
        # print("rs",results,self.training_set.keys())
        confidence = Counter(results).most_common(1)[0][1]/k

        return result, confidence



def prep(filename):
    knn = CKNN()
    res=knn.predict(filename)
    print(res,"==============================res")
    return res
