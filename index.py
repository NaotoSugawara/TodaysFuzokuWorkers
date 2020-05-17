# ウェブアプリケーションフレームワーク
from flask import Flask, render_template
# スクレイピング用
import requests
from bs4 import BeautifulSoup
# import json

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

todayGirlListFromWeb = soup.find_all(class_='girlDetailArea')

todayGirlList = []
for oneGirl in todayGirlListFromWeb:
    name = oneGirl.find(class_='name').text
    age = oneGirl.find(class_='age').text
    measurements = oneGirl.find(class_='measurements').text
    shopGuide = oneGirl.find(class_='shopGuide').text
    girlInfo = "\n・" + name + age + measurements + " \n　店舗:" + shopGuide
    todayGirlList.append(girlInfo)
message = ''.join(todayGirlList)
LINE_notify(message)



# for oneGirl in todayGirlList:
#     name = oneGirl.find(class_='name').text
#     age = oneGirl.find(class_='age').text
#     measurements = oneGirl.find(class_='measurements').text
#     starBox = oneGirl.find(class_='starBox').text
#     catName = oneGirl.find(class_='catName').text
#     shopGuide = oneGirl.find(class_='shopGuide').text
#     print("name:" + name + ",age:" + age + ",measurements:" + measurements + ",starBox:" + starBox + ",catName:" + catName + ",shopGuide:" + shopGuide)

# announcer_name = soup.find_all('p', {'class': 'name-ja'})
# announcer_img = soup.find_all('img', {'class': ''})
# woman = announcer_name[0].text


########## 画面作成処理 ##########
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     name = len(todayGirlList)
#     return render_template('hello.html', title='flask test', name=name)

# ## おまじない
# if __name__ == "__main__":
#     app.run(debug=True)