import bs4
import urllib.request
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup as soup
import csv

filename = 'population.csv'
f = open(filename,'w',newline = '')
pop = csv.writer(f)

#html = urlopen('https://www.worldometers.info/world-population/india-population/')
html = requests.get("https://www.worldometers.info/world-population/india-population/")
bsobj = bs4.BeautifulSoup(html.text, 'lxml')
#bsobj = soup(html.read())
tbody = bsobj('div',{'class':'table-responsive'})[0].findAll('tr')
xl = []
for row in tbody:
    cols = row.findChildren(recursive = False)
    cols = [element.text.strip() for element in cols]
    pop.writerow(cols) #Writing to CSV
    xl.append(cols)
print('Population.csv file created successfully')
