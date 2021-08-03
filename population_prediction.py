import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import seaborn as sns
import pickle
import os

page = requests.get("https://www.worldometers.info/world-population/india-population/")
soup = BeautifulSoup(page.text,'lxml')

file = open('indian_population.csv', 'wb')
writer = csv.writer(file)

table = soup.find('div',{'class':'table-responsive'})

headers=[]
for i in table.find_all('th'):
    title = i.text
    headers.append(title)



df = pd.DataFrame(columns=headers)
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text for td in data]
    length = len(df)
    df = df.reset_index(drop=True)
    df.loc[length] = row_data
   # df = df.reset_index(drop=True)
    #df = df.append(row_data,ignore_index=True)
print(df.columns)
#df1 = pd.read_csv("D:\Capegemini Hacathon\population.csv",encoding_errors='ignore')

data_ = df.replace('[^\d.]','',regex=True).astype(float)
X = data_[['Year','Yearly %  Change', 'Yearly Change',
       'Migrants (net)', 'Median Age', 'Fertility Rate', 'Density (P/Km²)',
       'Urban Pop %', 'Urban Population', 'Country\'s Share of World Pop',
       'World Population', 'IndiaGlobal Rank']]
y = data_[['Population']]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=101)

ln = LinearRegression()
ln.fit(X_train,y_train)
predictions = ln.predict(X_test)

plt.scatter(y_test,predictions)
plt.plot(y_test,predictions,c='red',linewidth=2)
plt.show()

print(r2_score(y_test,predictions))

