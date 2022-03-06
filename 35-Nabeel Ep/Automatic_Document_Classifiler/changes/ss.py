
# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import random

# Number of individuals in each generation


POPULATION_SIZE = 2
from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.secret_key="aaa"

import re, math
import os

from werkzeug.utils import secure_filename


# Valid genes
#
# GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
# QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
#
# # Target string to be generated
# TARGET = "I love GeeksforGeeks"
keywords = []
wrdsting=[]

# keyword_string = '''the proposal of a knowledge-based genetic
#      algorithm is a viable approach to solve the classification problem.'''
# # print("THE KEYWORD STRINGS ARE :  ", keyword_string)
#
wrdsting = ''' The use of the Web has increased the creation of digital information in an accelerated way and
     about multiple subjects. Text classification is widely used to filter emails, classify Web pages, and organize
     results retrieved by Web browsers. In this paper, we propose to raise the problem of automatic classification
     of scientific texts as an optimization problem, which will allow obtaining groups from a data set. The use
     of evolutionary algorithms to solve classification problems has been a recurrent approach. However, there
     are a few approaches in which classification problems are solved, where the data attributes to be classified
     are text-type. In this way, it is proposed to use the association for computing machinery taxonomy to obtain
     the similarity between documents, where each document consists of a set of keywords. According to the
     results obtained, the algorithm is competitive, which indicates that the proposal of a knowledge-based genetic
     algorithm is a viable approach to solve the classification problem. '''
#

def predict(keyword_string,wrdsting):



    class Individual(object):

        '''
        Class representing individual in population
        '''
        def __init__(self, chromosome):
            self.chromosome = chromosome
            self.fitness = self.cal_fitness()

        @classmethod
        def mutated_genes(self):
            '''
            create random genes for mutation
            '''
            # global keyword_string
            gene = random.choice(keyword_string)
            return gene

        @classmethod
        def create_gnome(self):
            '''
            create chromosome or string of genes
            '''
            global wrdsting
            gnome_len = len(wrdsting)
            return [self.mutated_genes() for _ in range(gnome_len)]

        def mate(self, par2):
            '''
            Perform mating and produce new offspring
            '''

            # chromosome for offspring
            child_chromosome = []
            for gp1, gp2 in zip(self.chromosome, par2.chromosome):

                # random probability
                prob = random.random()

                # if prob is less than 0.45, insert gene
                # from parent 1
                if prob < 0.45:
                    child_chromosome.append(gp1)

                # if prob is between 0.45 and 0.90, insert
                # gene from parent 2
                elif prob < 0.90:
                    child_chromosome.append(gp2)

                # otherwise insert random gene(mutate),
                # for maintaining diversity
                else:
                    child_chromosome.append(self.mutated_genes())

            # create new Individual(offspring) using
            # generated chromosome for offspring
            return Individual(child_chromosome)

        def cal_fitness(self):
            '''
            Calculate fittness score, it is the number of
            characters in string which differ from target
            string.
            '''
            global wrdsting
            fitness = 0
            for gs, gt in zip(self.chromosome, wrdsting):
                if gs != gt: fitness+= 1
            return fitness


    # Driver code
    def upload_documents_action():



        simlist = []
        global POPULATION_SIZE

        # current generation
        generation = 1

        found = False
        population = []


        # create initial population
        for _ in range(POPULATION_SIZE):
            gnome = Individual.create_gnome()
            population.append(Individual(gnome))
            break

        while not found:

            # sort the population in increasing order of fitness score
            population = sorted(population, key=lambda x: x.fitness)

            # if the individual having lowest fitness score ie.
            # 0 then we know that we have reached to the target
            # and break the loop
            if population[0].fitness <= 0:
                found = True
                break

            # Otherwise generate new offsprings for new generation
            new_generation = []

            # Perform Elitism, that mean 10% of fittest population
            # goes to the next generation
            s = int((10 * POPULATION_SIZE) / 100)
            new_generation.extend(population[:s])

            # From 50% of fittest population, Individuals
            # will mate to produce offspring
            s = int((90 * POPULATION_SIZE) / 100)
            for _ in range(s):
                parent1 = random.choice(population[:50])
                parent2 = random.choice(population[:50])
                child = parent1.mate(parent2)
                new_generation.append(child)


            population = new_generation

            # print("Generation: {}\tString: {}\tFitness: {}". \
            #       format(generation,
            #              "".join(population[0].chromosome),
            #              population[0].fitness))

            generation += 1
            break

        # print("Generation: {}\tString: {}\tFitness: {}". \
        #       format(generation,
        #              "".join(population[0].chromosome),
        #              population[0].fitness))

        return population[0].fitness

    from difflib import SequenceMatcher

    ratio = SequenceMatcher(None, keyword_string,wrdsting).ratio()



    res=int(upload_documents_action())*(1-float(ratio))
    return int(res)


from src.dbconnector import *

res=select("SELECT  DISTINCT `words_type` FROM `dataset`")
row=[]
for r in res:
    qry="SELECT `keyword` FROM `dataset` WHERE `words_type`=%s"
    val=(r[0],)
    re=selectall(qry,val)

    rr=[]
    for rrr in re:
        rr.append(rrr[0])
    string=' '.join(rr)
    ress = predict(string, wrdsting)
    row.append(ress)

for i in range(0,len(row)):
    print (row[i],res[i])
