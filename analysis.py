#Analysing Iris Data Set
#A program that:
#1.Outputs a summary of each variable to a single text file,
#2. Saves a histogram of each variable to png files, and
#3. Outputs a scatter plot of each pair of variables.
#4. Performs any other analysis you think is appropriate

#Author: Andrea Stanicic

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset into pandas dataframe
data = pd.read_csv('iris.csv')

#to get basic statistics about the data
basicstat = (data.describe())

#to get basic info on the data
info = data.info ()

#to see number of samples for each species

samples = data ['species'].value_counts()

# to display histogram 

data['sepallength'].hist()



