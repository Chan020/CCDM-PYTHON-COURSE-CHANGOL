import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('employees.csv')
#print(data.head())

column_name = 'First Name' 

plt.hist(data[column_name], bins=10, edgecolor='black')

plt.title('Histogram of ' + column_name)
plt.xlabel(column_name)
plt.ylabel('Frequency')

plt.show()