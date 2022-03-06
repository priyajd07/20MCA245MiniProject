import math
from tkinter import Tk, Label, Entry

import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import style
# import pandas as pd
import random
from collections import Counter
# from sklearn import preprocessing
import time

#for plotting
from src.featureextract import glcm_feat


class CKNN:

    def __init__(self):
        self.accurate_predictions = 0
        self.total_predictions = 0
        self.accuracy = 0.0
        ##########
        with open('labels.dat') as f:
            lines = f.readlines()
        lines=[s.strip('\n') for s in lines]
        training_data=np.loadtxt("sample.data",dtype=float,delimiter=" ")




        self.training_set= {'0':[], '1':[],'2':[],'3':[],'4':[]}

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

                distributions.append([euclidean_distance, group])

        # print(distributions)
        results = [i[1] for i in sorted(distributions)[:k]]
        result = Counter(results).most_common(1)[0][0]
        # print("rs",results,self.training_set.keys())
        confidence = Counter(results).most_common(1)[0][1]/k

        return result, confidence



def prep(filename):



    feat=glcm_feat(filename)
    knn = CKNN()
    res=knn.predict(feat)
    print("result",res)

    return res

# prep(r"C:\Users\ahmed\PycharmProject\pythonProject\leaf disease\static\dataset\Alternaria Alternata\1.jpg")
