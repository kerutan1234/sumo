
import requests
from bs4 import BeautifulSoup
import pprint
import json
import pandas as pd
import urllib
from tqdm import tqdm

url = "https://suumo.jp/jj/common/ichiran/JJ901FC004/?initFlg=1&seniFlg=1&ar=030&ta=14&scTmp=14132&ct=9999999&cb=0.0&kt=9999999&xt=9999999&et=9999999&cn=9999999&newflg=0&km=1&sc=14132&bs=040&pc=100"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
house_list = []
elements = soup.find_all("li", class_='cassette js-bukkenCassette')
for i in elements:
    temp1 = []
    temp2 = []
    dictemp = {}
    detail_titles = i.find_all("div", class_='infodatabox-box-title')
    detail_contents = i.find_all("div", class_='infodatabox-box-txt')
    #bcid=物件タグの取得
    bc_id_tag = i.find('input', class_="js-ikkatsuCB")
    bcid = bc_id_tag['value']
    #print(bcid)
    for detail_title in detail_titles:
        temp1.append(detail_title.get_text())

    for detail_content in detail_contents:
        ii = detail_content.get_text().replace('　', '').replace(
            '\t', '').replace('\n', '').replace('\r', '')
        temp2.append(ii)
    for title, result in zip(temp1, temp2):
        dictemp[title] = result
    dictemp['bcid'] = bcid
    house_list.append(dictemp)

#jsonに保存している
with open("data.json", "w") as f:
    json.dump(house_list, f, sort_keys=True, indent=4)
pprint.pprint(house_list)
#保存したJSONをデータフレームにしている
df=pd.read_json("data.json",encoding='utf-8')
#print(df)
df.to_excel('output.xlsx')


#間取り図
#https://img01.suumo.com/front/gazo/fr/bukken/437/100291162437/100291162437_co.jpg
#https://img01.suumo.com/front/gazo/fr/bukken/525/100311986525/100311986525_co.jpg"


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)
for i in tqdm(house_list):
    src="https://img01.suumo.com/front/gazo/fr/bukken/"+i["bcid"][-3:]+"/"+i["bcid"]+"/"+i["bcid"]+"_co.jpg"#ダブル掲載がある場合は、BCIDを流用している場合があるため、取得できないことがある。
    #print(src)
    download_file(src, "./drawing/"+i["bcid"]+".jpg")