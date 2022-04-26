#Analysing Iris Data Set
#Writing a program that:
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
sns.FacetGrid(data,hue="species").map(plt.scatter,"sepallength","sepalwidth").add_legend()

#if petal lenght/width is taken into account we can easly distinguish the difference in between versicolor and virginica from setosa
sns.FacetGrid(data,hue="species").map(plt.scatter,"petallength","petalwidth").add_legend

#if we try do compare other two variables:
sns.FacetGrid(data,hue="species").map(plt.scatter,"sepallength","petalwidth").add_legend
sns.FacetGrid(data,hue="species").map(plt.scatter,"petallength","sepalwidth").add_legend
plt.show ()

#to show histogram for sepal lenght
plt.figure(figsize = (10, 7))
x = data["sepallength"]
plt.hist(x, bins = 20, color = "blue")
plt.title("sepal length in cm")
plt.xlabel("sepal length in cm")
plt.ylabel("Count")
plt.savefig("sepallenght.png")

#to show histogram for sepal width
plt.figure(figsize = (10, 7))
x = data.sepalwidth
plt.hist(x, bins = 20, color = "pink")
plt.title("sepal width in cm")
plt.xlabel("sepal width in cm")
plt.ylabel("Count") 
plt.savefig("sepalwidth.png")

#to show histogram for petallength
plt.figure(figsize = (10, 7))
x = data.petallength
plt.hist(x, bins = 20, color = "red")
plt.title("Petal length in cm")
plt.xlabel("petal length in cm")
plt.ylabel("Count")
plt.savefig("petallength.png")

#to show histogram for petalwidth

plt.figure(figsize = (10, 7))
x = data.petalwidth 
plt.hist(x, bins = 20, color = "purple")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width in cm")
plt.ylabel("Count") 
plt.savefig("petalwidth.png")

