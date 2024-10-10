import pandas as pd
import matplotlib.pyplot as plt

courselist = ["CCIT", "CCDM", "CCNS"]
courseID = [101, 102, 103]

#TO USE PANDA'S DATAFRAME FUNCTION, CREATE A DICTIONARY
courseDict = {'course': courselist, 'ID':courseID}

#USE FUNCYION
myvariable = pd.DataFrame(courseDict)

#print(myvariable)

#PANDA SERIES
myvariable2 = pd.Series(courseDict)
#print(myvariable2)

#READING CSV FILES
myvariable3 = pd.read_csv('student.csv')
#print(myvariable3)


pulsedata = pd.read_csv('student.csv')
#print(myvariable3)

update1 = pulsedata.dropna()
#print(update1)

#CHANGING DATE FORMAT
update2 = pd.read_csv('Pulse.csv')
update2['Date'] = pd.to_datetime(update2["Date"])
#YYYY-MM-DD
#print(update2)

#CHANGE VALUE
pulsedata.loc[10, 'Pulse']=111
#print(pulsedata)

#USING MATHPLOT AND PANDAS
pulsedata = pd.read_csv('Pulse.csv')
pulsedata.plot(kind='scatter', x='Duration', y= 'Calories')
#plt.show()

#HISTOGRAM GRAPH
pulsedata["Duration"].plot(kind='hist')
#plt.show()

#PIE GRAPH
pulsedata["Duration"].plot(kind='pie')
plt.show()
