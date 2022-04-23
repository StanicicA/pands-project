#Analysing Iris Data Set
#Write a program that:

#1.Outputs a summary of each variable to a single text file,
#2. Saves a histogram of each variable to png files, and
#3. Outputs a scatter plot of each pair of variables.
#4. Performs any other analysis you think is appropriate

#Author: Andrea Stanicic

#filename = 'irisdata.text'
#with open (filename, 'r') as f:
    #read_data = f.read ()
    #f = open ('irisdata.text')
    #f.close ()
    #print (filename)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Load Dataset
iris = pd.read_csv('irisdata.csv')
filename = 'irisdata.csv'
infile = open (filename, 'r') 
#data = infile.read ()

print (filename)
infile.close ()