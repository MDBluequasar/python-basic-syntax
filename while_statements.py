# while 문의 기본구조
# while 조건식: #조건식이 참인 경우 반복 => 무한반복이 기본전제
#     실행문

# a = 10
# while a>5:
#     print("참입니다.") #무한 반복한다.

a = 0
while a < 5:
    print(str(a)+"번 반복")
    a += 1
# 조건을 체크 후 True 이면 실행문 1회 실행시키고
# 다시 조건을 체크하러 돌아온다. 그리고 True 이면 또 다시 실행.
# 그러다 조건이 False 되면 while문 종료

# 예제
# 1~1000까지만 프린트 되도록 출력.

# r = 1
# while r <= 1000:
#     print(r)
#     r += 1
    

# # 1~1000까지 모두 더한 값을 출력
# a = 1
# sum = 0
# while a <= 1000:
#     sum += a
#     a += 1
# print(sum)

# 1~1000까지 모두 더한 값의 평균값
# print(int(sum/r))

# while 문에서 조건이 참이면 반복을 진행하다가 break를 만나면, 반복문 종료.
# if 문을 써서 XXX한 조건에 break

a = 0
while a >= 0:
    a += 1
    if a == 5:
        break
print(a)

# continue : 이 구문을 만나면 다시 반복문 조건으로 이동
# 하단에 불필요한 로직을 수행하지 않고 다시 조건으로 이동할 수 있게 한다.
# 아래와 같이 코딩하면 hello가 무한 출력 된다.
# a = 0
# while a < 1000:
#     print("hello")
#     continue
#     a += 1

# 올바른 예시
a = 0
sum = 0
while a < 1000:
    a += 1
    if a % 2 == 0:
        continue    
    sum += a
print(sum)

# 연습문제
# 리스트의 크기를 키보드로 입력받아 그 크기만큼 임의 숫자를 리스트에 추가하고, 리스트의 크기와 값 전체를 출력하라.
# 모든 값은 키보드로 입력을 받고, list의 크기는 함수를 통해 구하라. 단, 리스트의 크기는 10 이하로 입력하라.

# k = 0
# lista = []
# while k <= 10:
#     k = int(input("숫자를 입력하세요.: "))
#     lista.append(k)
# print(lista) #내가 풀이한 과정

# 해설
# while True:
#     listsize = int(input("리스크의 크기를 입력해주세요.: "))
#     if listsize > 10:
#         print("다시 입력해주세요.")
#         continue
#     a = 0
#     lista = []
#     while a < listsize:
#         listValue = input("리스트의 값을 입력해주세요.: ")
#         lista.append(listValue)
#         a += 1
#     print(lista)

# 로또 번호 생성기
# 랜덤 값을 추출하는 파이썬 라이브러리 : random
# import random
# print(random.randint(1,45))
# 리스트의 크기가 6개인 리스트를 만들어서, 오늘의 로또번호를 만들어보자.
import random
a = 0
lista = []
while a < 6:
    rotto = random.randint(1,45)
    lista.append(rotto)
    a += 1
print(lista)


'''답(중복 숫자 배제)'''
# import random
# a = 0
# lista = []
# while a < 6:
#     randnum = random.randint(1,45)
#     if randnum not in lista:
#         lista.append(randnum)
# print(lista)