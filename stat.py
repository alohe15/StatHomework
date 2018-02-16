#This will hopefully do my stats homework for me
#Find range, mean, mode, median, variance, standard deviation, and calculate Chebychev inequalities
import numpy as np
import pandas as pd
n = int(input("Enter number of data points: "))
data_sort = sorted([float(input("Enter Data Points: ")) for _ in range(n)])
#data = sorted([74, 72, 67, 79, 81, 82, 73, 80, 70, 78, 75, 66, 45, 90, 92, 56, 70, 78, 74, 89, 78, 61, 90, 81, 53, 74, 78, 77, 65, 86, 78, 67, 82, 82, 82, 61, 78, 69, 85, 64])
#replace all lists data in this program with data_sort once done
#data)

def datarange():
    low = data_sort[0]
    large = data_sort[-1]
    range_ = large - low
    return range_
def createdf(): #returns dataframe with class bounds and frequencies
    classnum = int(input("Enter desired number of classes: "))
    df = pd.DataFrame(index = range(classnum), columns = ["Lower Class Bounds", "Upper Class Bounds", "Frequency"])
    classwidth = int((datarange())/classnum)
    low = data_sort[0]
    classboundslower = []
    classboundsupper = []
    classboundslower.append(low)
    for i in range(classnum):
        low += classwidth
        classboundsupper.append(low)
        low += 1
        classboundslower.append(low)
    if len(classboundslower) > len(classboundsupper):
        del classboundslower[-1]
    df["Lower Class Bounds"] = classboundslower
    df["Upper Class Bounds"] = classboundsupper
    df = df.fillna(0)
    for i in range(classnum):
        for number in data_sort:
            if classboundslower[i] <= number <= classboundsupper[i]:
                df["Frequency"][i] += 1
    return df
def samplemean():
    df = createdf()
    df["XF"] = (df["Lower Class Bounds"] + df["Upper Class Bounds"])/2 * df["Frequency"]
    sum_ = sum(df["XF"])
    mean = sum_/len(data_sort)
    return round(mean, 1)
def mean():
    mean = (sum(data_sort))/(len(data_sort))
    return mean
def mode():
    dataset = set(data_sort)
    datadict = dict.fromkeys(dataset, 0)
    for number in data_sort:
        if number in dataset:
            datadict[number] += 1
    def keywithmaxval(d):
        v=list(d.values())
        k=list(d.keys())
        return k[v.index(max(v))]
    return keywithmaxval(datadict)
def var():
    df = createdf()
    df["X"] = (df["Lower Class Bounds"] + df["Upper Class Bounds"])/2
    df["XX"] = df["X"] ** 2
    n = len(df.index)
    B = (sum(df["X"])) ** 2
    A = sum(df["XX"]) * n
    diff = A - B
    var = diff/(n*(n-1))
    return round(var, 1)
def stdev():
    variance = var()
    stdev = variance**0.5
    return stdev
def classes():
    df = createdf()
    classes = [[df["Lower Class Bounds"][i], df["Upper Class Bounds"][i]] for i in range(len(df.index))]
    print(classes)
def median():
    median = data_sort[int(len(data_sort)/2)]
    return median

i = 0
lst = ['median', 'mode', 'mean', 'classesmean', 'range', 'variance', 'stdev', 'classes']
while type(i) == int:
    command = str(input("Enter 'median' 'mode' 'mean' 'samplemean' 'range' 'variance' 'stdev' 'classes' for the value you would like to obtain: "))
    if command == 'median':
        print("The median of your data is %f" %median())
    if command == 'mode':
        print("The mode of your data is %f" %mode())
    if command == 'mean':
        print("The mean of your data is %f" %mean())
    if command == 'samplemean':
        print("The sample mean of your data from using classes is %f" %samplemean())
    if command == 'range':
        print("The range of your data is %f" %datarange())
    if command == 'variance':
        print("The variance of your data is %f" %var())
    if command == 'stdev':
        print("The standard deviation of your data is %f" %stdev())
    if command == 'classes':
        print("Your data has been divided into the following classes: ")
        print('\n')
        classes()

    i += 1
