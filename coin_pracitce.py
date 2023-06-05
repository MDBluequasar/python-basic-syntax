import time
import json
import requests
import mysql.connector
while True:
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data_json = json.loads(response.text)
    for a in data_json:
        if a['symbol'] == "BTCUSDT":
            try:
                connector = mysql.connector.connect(
                host="localhost", 
                port="3406", 
                user="root", 
                password="1234", 
                database="practice")
            except mysql.connector.Error as err:
                print(err)

# 커서객체는 데이터베이스에서 쿼리의 결과를 
# 검색하고 순회하는데 사용되는 객체
            try:
                cursor = connector.cursor()
                add_data = "INSERT INTO coin_practice(coin_name, last_price) VALUES(%s, %s)"
                data = ("BTCUSDT",a['last_price'])
                cursor.execute(add_data, data)
                connector.commit()
                cursor.close()
                connector.close()
            except mysql.connector.Error as err:
                print(err)

# 코인 시세 10초에 한 번식 업로드

