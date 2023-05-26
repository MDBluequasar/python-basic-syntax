# if 문의 기본 문법
# if 참조건:
#     살행문
# else:
#     실행문

a = 1 # a = int(input("숫자를 입력해주세요"))
if a > 10:
    print("a는 10보다 큽니다.")
else:
    print("a는 10보다 작습니다.")
print("a는 10보다 작습니다.")

# 예제 1
# 얼마를 가지고 있습니까? 를 변수에 담고
# 만약 30,000 이상이면 택시를 타고 가시오를 출력
# 그렇지 않으면 걸어가시오를 출력

# Q = int(input("얼마를 가지고 있습니까?"))
# if Q >= 30000:
#     print("택시를 타고 가시오.")
# else:
#     print("걸어 가시오")

# for 문의 기본 구조
# for 변수 in 반복 가능한 자료형 (iterable)
#     실행문
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #lista는 대괄호를 쓰며, 변수를 한 곳에 모은다. (집합 같은 의미)
for a in lista:
    print(a)

# range 문법 : range(x, y) x이상 y미만
for a in range(1,101): # for a in [1부터 100까지]
    print(a)


# f formating

# numInput = int(input("짐의 무게를 입력해주세요: "))
# weight = int(input("수수료를 입력해주세요.: "))

# print(f'짐의 무게는 {numInput}이고 수수료는 {weight} 입니다.')
# print("짐의 문게는 이고" + numInput + "수수료는" + weight + "입니다.")

# money = int(input("돈이 얼마가 있나요"))
# hungryOrNot = input("배가 고프신가요 yes or no로 대답해주세요.")
# if money > 10000 and hungryOrNot == 'yes':
#     print("밥을 사먹으세요") 
# else:
#     print("no")





# 조건부표현식(삼항연산자)



# a 와 b 같은지 비교하는 연산자 is
# 객체타입의 경우에는 메모리 주소를 비교하고,
# 숫자, 문자, bool 기본타입의 경우 값을 비교한다.
# 순자, 문자, bool 같은 경우에는 데이터 pool을 만들어서, 재활용한다.
# 그래서 값을 비교할 때 메모리 주소가 아니라 데이터 pool에서 값을 비교한다.
a = [10,20]
b = [10,20]
if a is b:
    print("참입니다.")

a = 10
b = 20
if a == b:
    pass # 통과 시키는 것
else:
    print('두 값이 다릅니다.')

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
