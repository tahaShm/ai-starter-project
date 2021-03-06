# ~/.local/bin/jupyter-notebook

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def printDataFrameInfo(df) : 
    print("\n\nhead: first 5 rows\n")
    print(df.head())
    print("\n\ntail: last 5 rows\n")
    print(df.tail())
    print("\n\ndescribe: columns' value info\n")
    print(df.describe())
    print("\n\ninfo: columns' non Null and data type info\n")
    print(df.info())    

def showNanInColumns(df) : 
    countNan = len(df) - df.count()
    print("Nan in columns : ")
    print(countNan)

def changeNanWithAverage(df) : 
    for i, col in enumerate(df):
        if (col != "Chance of Admit") :
            df.iloc[:, i] = df.iloc[:, i].fillna(df[col].mean()) # cast to same dtype remains
    # showNanInColumns(df)
    return df
            
inp = pd.read_csv('AdmissionPredict.csv')
df = pd.DataFrame(inp)
# printDataFrameInfo(df) #p1
# showNanInColumns(df) #p2
df = changeNanWithAverage(df) #p3
printDataFrameInfo(df) #p1


#-------------------------------------------------------------part2

