# dictionary에서 key 목록만을 뽑아낼 때
# iterable한 형태로 data가 뽑아져 나오므로 

#dic1 = {'이름' : '홍길동', '나이' : 25, '몸무게' : 25, '성별' : '남', '성별' : '여'}
# key:value 추가
# dic1['신분'] = '학생'
# print(dic1)


# dictionary에서 key 를 이영한 key:value 삭제
# del dic1['성별']
# print(dic1)


# dictionary의 확장 : update 함수
# dic1 = {"a" : 1, "b" : 2, "c" : 3}
# dic2 = {"a" : 2, "b" : 4, "c" : 5}
# dic1.update(dic2)
# print(dic1)

#dicthionary 로 변환해서 출력해보자.
# 'A' : 2, 'B' : 1, 'O': 2, 'AB' : 2 로 출력되도록 초딩해보자.
# Hint : a in dicta.key() 을 통해 a key가 dicta에 있는지 검사.
lista = ['A', 'A', 'B', 'O', 'O', 'AB', 'AB']
dicta = {}

# 방법1
for a in lista:
    if a not in dicta.keys():
        dicta[a] = 1
    else:
        dicta[a] = dicta[a] +1
print(dicta)

# 방법2
for a in lista:
    if a not in dicta.keys():
        dicta[a] = lista.count(a)
print(dicta)

# programmers 완주하지 못한 선수 다시 풀어 보기