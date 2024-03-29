
import requests
from bs4 import BeautifulSoup
import pprint
import json
import pandas as pd

url = "https://suumo.jp/jj/common/ichiran/JJ901FC004/?initFlg=1&seniFlg=1&ar=030&ta=14&scTmp=14132&ct=9999999&cb=0.0&kt=9999999&xt=9999999&et=9999999&cn=9999999&newflg=0&km=1&sc=14132&bs=040&pc=100"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

# print(soup.select("h1"))

# print(soup.select("p"))
house_list = []
elements = soup.find_all("li", class_='cassette js-bukkenCassette')
for i in elements:
    temp1 = []
    temp2 = []
    dictemp = {}
    detail_titles = i.find_all("div", class_='infodatabox-box-title')
    detail_contents = i.find_all("div", class_='infodatabox-box-txt')
    bc_id = i.find("div", class_='ui-media-object infodatabox-object')

    print(bc_id)
    for detail_title in detail_titles:
        temp1.append(detail_title.get_text())

    for detail_content in detail_contents:
        ii = detail_content.get_text().replace('　', '').replace(
            '\t', '').replace('\n', '').replace('\r', '')
        temp2.append(ii)
    for title, result in zip(temp1, temp2):
        dictemp[title] = result
    house_list.append(dictemp)

#jsonに保存している
with open("data.json", "w") as f:
    json.dump(house_list, f, sort_keys=True, indent=4)
print(house_list)
#保存したJSONをデータフレームにしている
df=pd.read_json("data.json",encoding='utf-8')
#print(df)
df.to_excel('output.xlsx')


#間取り図
#https://img01.suumo.com/front/gazo/fr/bukken/437/100291162437/100291162437_co.jpg
#https://img01.suumo.com/front/gazo/fr/bukken/525/100311986525/100311986525_co.jpg"