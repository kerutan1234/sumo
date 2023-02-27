import requests
from bs4 import BeautifulSoup

# スクレイピング対象のURL
url = "https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}"

# ページ数を指定
page = 1

while True:
    # URLを設定
    target_url = url.format(page)
    
    # リクエストを送信
    res = requests.get(target_url)
    
    # ステータスコードが200でない場合は終了
    if res.status_code != 200:
        break
    
    # HTMLをパース
    soup = BeautifulSoup(res.content, "html.parser")
    
    # 物件情報のタグを取得
    house_elements = soup.find_all("div", class_="cassetteitem")
    
    for house_element in house_elements:
        # 物件情報を取得
        house_name = house_element.find("div", class_="cassetteitem_content-title").text.strip()
        house_address = house_element.find("li", class_="cassetteitem_detail-col1").text.strip()
        house_age = house_element.find("li", class_="cassetteitem_detail-col2").text.strip()
        house_rent = house_element.find("span", class_="cassetteitem_other-emphasis").text.strip()
        
        # 取得した物件情報を表示
        print(house_name)
        print(house_address)
        print(house_age)
        print(house_rent)
    
    # ページ数を増やす
    page += 1