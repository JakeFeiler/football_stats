from bs4 import BeautifulSoup
import pandas as pd
import requests
import sys




for i in range(1962, 2023):
    url = "https://www.pro-football-reference.com/years/" + str(i) + "/passing.htm"

    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    #print(soup.prettify())

    #rows = soup.select('tr data-row=')
    #print(rows)
    table  = soup.find(lambda tag: tag.name == 'table' and tag['id'] == "passing")
    #rows =  table.findAll(lambda tag: tag.name == 'tr')
    rows =  table.findAll('tr', class_=None)


    #Getting the headers for pandas
    row0 = rows[0]
    headers = []
    for chil in row0.children:
        try:
            headers.append(chil['aria-label'])
        except:
            pass


    rows = rows[1:]
    row1 = rows[0]


    df = pd.DataFrame(columns = headers)
    #print(df)
    #for chil in row1.children:
       #print(chil.string)


    #for chil in row1.children:
    #    print(type(chil))
        #print(chil['data-stat'])


    for row in rows:
        stats = [chil.string for chil in row.children]
        df.loc[len(df)] = stats
        

    file_name = str(i) + "_season_stats.csv"
    #print(file_name)

    #print(df)
    df.to_csv('/Users/jacobfeiler/Desktop/cs_projects/football/' + file_name)
    print("Made stats for " + str(i))
  
