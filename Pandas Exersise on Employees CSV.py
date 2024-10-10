#HANDS-ON EXCERCISE

#COULD NOT FIND THE FILE EMPLOYEE.CSV IF THOUGH I OPENED THE FOLDER

import pandas as pd
import matplotlib.pyplot as plt

#Q1) CREATE A NEW OBJECT CALLED "empData" TO READ employees.csv.

empData = pd.read_csv('employees.csv')
print(empData)

#READING CSV FILES
pulsedata = pd.read_csv('employees.csv')
print(empData)

#Q2) CREATE NEW OBJECT CALLED "NONULL" TO REMOVE EMPTY/ NULL SPACES. USE dropna().
#Question: HOW MANY ROWS WERE DROPPED? 43 ROWS

NONULL = pulsedata.dropna()
print(NONULL)

#Q3) CREATE OBJECT "empStartDate" to format date to YYYY-MM-DD
empStartDate = pd.read_csv('employees.csv.csv')
empStartDate["Date"] = pd.to_datetime(empStartDate["Date"])
print(empStartDate)


#Q4) USING PLOT FUNCTION, COME UP WITH A
#HISTOGRAM CHART BASED ON SALARY TO ANSWER THE FOLLOWING:
#WHAT IS THE RANGE THAT MOST EMPLOYEES ARE PAID WITHIN?
#PROVIDE ANSWER: 

#HISTOGRAM GRAPH

pulsedata = pd.read_csv('employees.csv')
pulsedata["Salary"].plot(kind='hist')
plt.show()






