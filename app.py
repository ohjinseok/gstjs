from flask import Flask, render_template,request
import requests
import os
import sys

app = Flask(__name__)

@app.route("/") # 주문 받을(요청 받을) 서비스 / : home 정의
def index(): # 해당하는 주문/요청에 대한 결과
    return render_template('index.html')
    
@app.route("/show") # index에서 날려준 단어를 받아 그대로 출력한다.
def show():
    client_id = os.getenv('NAVER_ID')
    client_secret = os.getenv('NAVER_SECRET')
    
    url = "https://openapi.naver.com/v1/papago/n2mt" 

    word = request.args.get('word')
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }

    data = {
        "source":"en",
        "target":"ko",
        "text":word
    }
    
    res = requests.post(url, headers=headers, data=data)
    res_dict = res.json()
    res_word = res_dict.get('message').get('result').get('translatedText')
    
    # if(rescode==200):
    #     response_body = response.read()
    #     print(response_body.decode('utf-8'))
    # else:
    #     print("Error Code:" + rescode)
    
    return render_template('show.html', word = res_word)