import requests
from bs4 import BeautifulSoup

########## LINEへの送信処理 ##########
def LINE_notify(message):
    def LineNotify(message):
        line_notify_token = "ekHn1eW0wLzLcobprromHYlT7wNXQ6aKT8hY8e6hD9P"
        line_notify_api = "https://notify-api.line.me/api/notify"
        payload = {"message": message}
        headers = {"Authorization": "Bearer " + line_notify_token}
        requests.post(line_notify_api, data=payload, headers=headers)
    LineNotify(message)
    return

########## スクレイピング処理 ##########

# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get('https://www.fuzoku-watch.com/yoshiwara/today.html')

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(res.text, 'html.parser')

# HTMLから今日の出勤情報を取得
todayGirlListFromWeb = soup.find_all(class_='girlDetailArea')

todayGirlList = []
# 一人ずつ情報を抽出する
for oneGirl in todayGirlListFromWeb:
    name = oneGirl.find(class_='name').text
    age = oneGirl.find(class_='age').text
    measurements = oneGirl.find(class_='measurements').text
    shopGuide = oneGirl.find(class_='shopGuide').text
    girlInfo = "\n・" + name + age + measurements + " \n　店舗:" + shopGuide
    # 嬢の情報をListに追加する
    todayGirlList.append(girlInfo)

# Listを一つのStringにまとめる
message = ''.join(todayGirlList)
LINE_notify(message)