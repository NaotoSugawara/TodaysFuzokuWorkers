# ウェブアプリケーションフレームワーク
from flask import Flask, render_template
# スクレイピング用
import requests
from bs4 import BeautifulSoup

########## スクレイピング処理 ##########

# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get('https://www.tv-tokyo.co.jp/announcer/announcer-profile-list')

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(res.text, 'html.parser')

# class が name-ja の p 要素を全て取得する
quote_elms = soup.find_all('p', {'class': 'name-ja'})
woman = quote_elms[0].text


########## 画面作成処理 ##########
app = Flask(__name__)

@app.route('/')
def hello():
    name = woman
    return render_template('hello.html', title='flask test', name=name)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)