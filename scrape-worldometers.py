from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://www.worldometers.info/coronavirus/'

response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll(["th","td"]):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
    
df = pd.DataFrame(list_of_rows, columns=["Country,Other","TotalCases","NewCases",\
                                         "TotalDeaths","NewDeaths","TotalRecovered",\
                                         "ActiveCases","Serious,Critical","Tot Cases/1M pop",\
                                         "Tot Deaths/1M pop"])
