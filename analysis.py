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

#getting dataset info from a csv file
data = pd.read_csv('iris.csv')
print (data)
#to get basic statistics about the data
basicstat = (data.describe())
print (basicstat)

#to get basic info on the data
info = data.info ()
print (info)
#to see number of samples for each species
samples = data ['species'].value_counts()
print (samples)

#visualisation/showing the graph using the function plot
data.plot()


# to display the plot based on x and y 
data.plot(kind = "scatter",x="sepallength",y="sepalwidth",color = "green")
 
#to show the difference between the scatter based on species using seaborn function
sns.FacetGrid(data,hue="species",size=5).map(plt.scatter,"sepallength","sepalwidth").add_legend()

#if petal lenght/width is taken into account we can easly distinguish the difference in between versicolor and virginica from setosa
sns.FacetGrid(data,hue="species",size=5).map(plt.scatter,"petallength","petalwidth").add_legend

plt.show ()

