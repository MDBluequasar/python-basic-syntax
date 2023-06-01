# 아래 모듈은 외장 라이브러리 이므로, 별도 설치 필요
# 설치 할 때, pip 라는 패키지 tool을 이용
# import requests
# from bs4 import BeautifulSoup


# 터미널에서
# 1) python --version 
# 2) python -m pip --version
# 3) python -m pip install requests
# 4) python.exe -m pip install --upgrade pip
# 안될 때
# 파이썬 실행 프로그램을 모두 제거하고 후
# 파이썬 재설치 시 add PATH 체크 후 설치 그리고 다시 명령어 입력

import requests
from bs4 import BeautifulSoup

url = 'https://ko.wikipedia.org/wiki/%EC%95%84%EB%B0%94%ED%83%80:_%EB%AC%BC%EC%9D%98_%EA%B8%B8'

# 웹으로 주고받는 통신 프로토콜(약속)을 http통신이라 한다.
# http 통신을 하기 위해 : http 통신 규격에 맞게 request를 서버로 전달해야한다.
# requst는 header와 body로 이루어져 있다.
# 마찬가지로 응답(response)도 header와 body로 이루어져있다.
header = {'User-Agent' : 'Mozillla/5.0' }
response = requests.get(url, headers = header)
html_response = BeautifulSoup(response.text, 'html.parser')

# for sup in html_response.find_all('sup'):
#     sup.decompose()


# 감독정보, 제작비 정보
# tag 정보를 가지고 html_response
director_info = html_response.select_one('table.infobox > tbody > tr:nth-of-type(3) > td').get_text()
budget_info = html_response.select_one('table.infobox > tbody > tr:nth-of-type(16) > td').get_text()
print(director_info)
print(budget_info)

print(f'아바타 감독 {director_info}이고 제작비는 {budget_info}이다.')

# json
# 코인 시세정보 API url
import json
url = "https://api.binance.com/api/v3/ticker/24hr"
response = requests.get(url)
data_json = json.loads(response.text)
# print(data_json)

# 출력 결과
# 'symbol' : 'BTCUSDT', 'lastPrice' : xxxxx(가격)
# print(f'{}코인의 price는 {}입니다.')
for a in data_json:
    if a['symbol'] == 'BTCUSDT':
        print(f'{a["symbol"]}코인의 price는 {a["lastPrice"]} 입니다.')

# CSV 파일 parsing
import seaborn # 밑줄이나 실행 안될 시 pip install seaborn 터미널로 실행
from matplotlib import pyplot
import pandas

file_path = 'C:\Users\User\Desktop\궁둥박사'
csv_data = pandas.read_csv(file_path)

# 성별에 따라 tip이 어떻게 달라지는가.
# Day에 따라 tip이 어떻게 달라지는가
tip_by_gender = csv_data.groupby('gendet')['tip'].agg(['mean', 'std']).reset_index()
tip_bt_day = csv_data.groupby('day')['tip'].agg(['mean', 'std']).reset_index()

seaborn.barplot(x = 'gender', y = 'mean', data = tip_by_gender['mean'], capsize = 0.1)
seaborn.despine() #테두리 없애주는 함수
pyplot.title('average tip per gender')
pyplot.xlabel('gender')
pyplot.ylabel('average tip')

