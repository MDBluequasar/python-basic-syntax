# # range 문법 : range(x, y) x이상 y미만
# for a in range(1, 101):
#     print(a)


# range의 의미
# range(x,y) : x 이상 y 미만의 숫자를 담은 객체
# # range(y) : 0이상 y미만의 숫자를 담은 객체
# c1 = list(range(1, 10))
# print(c1)

# # for a in 리스트를 써서 v1의 값을 모두 출력
v1 = list(range(10,20)) # 10, 11, ..., 19
for a in v1:
    print(a)
# for a in range 를 써서 v1[index]의 형태로 v1의 값을 모두 출력
for b in range (len(v1)):
    print(v1[b])

# for a in 리스트 구문으로는 원본리스트 데이터를 변경할 수 없다.
# listt = [10,20,30,40,50,60,70]
# for a in listt:
#     a = 100
# 이런 방식으로는 원본의 listt의 값을 변경할 수 없다.

# 해결 방법
# 직접 리스트의 index로 접근해야지 원본을 바꿀 수 있다.
listt = [10,20,30,40,50,60,70]
for a in range(len(listt)):
    listt[a] = 100
print(listt)

# 리스트를 만드는 방법 중에 리스트 컴프리헨션이라는 방법이 있다.
# 리스트에 0~9까지를 담는 방법

# 방법1
lista = [0, 1, 2, 3, 4, 5, 6, 7]

# 방법2
lsita = list(range(10))

# 방법3
lista = []
for a in range(10):
    lista.append(a)

# 방법4 : 리스트 컴프리헨션
# 장점 : 간결하다
lista = [a for a in range(10)]
print(lista)

# 홀수 인 값에 2를 곱한 값만을 list로 만들어라.
# 방법 1
listb = []
for a in range(10):
    if a % 2 != 0:
        a = a * 2
        listb.append(a)
print(listb)

# 방법 2
lista = [a*2 for a in range(10) if a % 2 != 0]
print(lista)

'''for a in 리스트 구문으로는 원본 리스트 데이터 변경 불가'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for a in lista:
#     a = 100 #이런 방식으로는 원본 lista 값 변경 불가

'''원본 바꾸기 1 while'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# lista[0] = 100 #있어도 상관 없음
# indexTemp = 0
# while indexTemp < len(lista):
#     lista[indexTemp] = 100
#     indexTemp += 1
# print(lista)
'''원본 바꾸기 1.5 특정 값만 바꾸기'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# indexTemp = 0
# while indexTemp < len(lista):
#     if indexTemp == 2:
#         lista[indexTemp] = 500
#     indexTemp += 1
# print(lista)

'''원본바꾸기 2 for'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# lista[5] = 100
# for a in lista:
#     a = 100 #이런 방식으로는 원본 lista 값 변경 불가
# print(lista)
# #직접 리스트의 index로 접근해야 원본을 바꿀 수 있다    
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for a in range(len(lista)):
#     lista[a] = 100
# print(lista)

'''원본바꾸기 2.5 특정 값만 바꾸기'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for a in range(len(lista)):
#     if a == 9:
#         lista[a] = lista[a]*10
# print(lista)

'''리스트 내포(comprehension)'''
'''리스트 생성 방법 중 하나'''
# #방법1
# lista = [0,1,2,3,4,5,6,7,8,9]

# #방법2
# lista = list(range(10))

# #방법3
# lista = []
# for a in range(10):
#     lista.append(a)

# #방법4 comprehension
# lista = [a for a in range(10)]
# print(lista)

# 방법4에서 a*2 값 출력
# lista = [a*2 for a in range(10)]
# print(lista)

#방법3에 홀수인 값에 2를 곱한 값만 list화
# lista = []
# for a in range(10):
#     if a % 2!= 0:
#         lista.append(a*2)
# print(lista)

'''응용문제'''
# 1반 수학점수가 60점이 넘으면 합격
# 60점 미만이면 불합격
lista = [30, 25 , 67 , 45 , 80]
# 위 list가 학생 번호 순서대로 있을때, 아래와 같이 출력하도록 코딩하여라.
# 예시
# 1번 학생은 합격입니다
# 2번 학생은 불합격입니다.

# 방법1
# num = 1
# for a in lista:
#     if a >= 60 :
#         print("%d 번 학생은 합격입니다." % num )
#     else:
#         print("%d 번 학생은 불합격입니다." % num )
#         num += 1 

# # 방법2
# for a in range(len(lista)):
#     if lista[a] >= 60:
#         print("%d 번 학생은 합격입니다." % (a+1))
#     else:
#         print("%d 번 학생은 불합격입니다." % (a+1))

# For 문과 break : for ansdptj break문을 받으시 써야 하는 이유
# 혈액형이 a형인 고객 선착순 1명만 찾는 상황
lista = ['b', 'b', 'ab', 'a','b','a']
# 출력 결과 : 4번째 고객이 이벤트에 당첨되었습니다.
answer = 0
for a in range(len(lista)):
    if lista[a] == 'a':
        answer = a + 1
        break
print(str(answer) + "번째 고객이 이벤트에 당첨되었습니다.")


# 구구단 5단을 출력해보자
for a in range(1, 10):
    print(f"5 X {a} = {5*a}")


# 구구단 몇 단을 계산해드릴까요?
# 방법 1
# num =  int(input("구구단 몇 단을 계산해드릴까요?"))
# for i in range(1, 10):
#     print(f"{num} X {a} = {num*i}")

# 이중 for 문 문제
# 구구단을 5단 ~ 9단까지 한꺼번에 출력
# 5 X 1 = 5 형식으로

# 방법 1
for a in range(5, 10):
    for b in range(1, 10):
        print(f"{a} X {b} = {a*b}")

# 방법 2 (while 문 사용)
num = 5
while num < 10:
    for i in range(1, 10):
        print(f"{num} X {a} = {num*i}")
    num += 1    


# 데이버 맞바꾸기
lista = [10,20,30,40]
# lista[0] 와 lista[1]의 자리를 바꾸려면? lista = [20, 10, 30, 40]
temp = lista[0] # 0 번째 데이터를 살려두고 서로 변경한다.
lista[0] = lista[1]
lista[1] =  temp
# 파이썬에서 지원하는 문법
lista[0], lista[1] = lista[1], lista[0]

# for 문을 이용한 정렬 
lista = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# 위 리스트를 어떻게 오름차순 정렬 할 것인가?
# lista.sort()
# print(lista)

# 선택 정렬: 0번째 index부터 가장 작은 값을 채워나가는 방식
for a in range(len(lista) - 1): # 첫번째 for문은 채워나가야할 index를 의미
                                # '-1' 은 마지막 index는 비교할 필요가 없기 때문에 써준다.
    for b in range(a + 1, len(lista)): # 두번째 for문은 비교의 대상이 되는 index를 의미
                                   # for b in range(len(lista))는 내림차순으로 정렬된다.
        if lista[a] > lista[b]: # 자리 change, 큰 값이 오른쪽으로 간다.
             temp = lista[a] #lista[a], lista[b] = lista[b], lista[a]
             lista[a] = lista[b]
             lista[b] = temp
print(lista)


# 버블정렬

#programmers 문제
# 출력 예시
# [[4,6], [7,9]]
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
answer = []
for a in range(len(arr1)):
    temp = []
    for b in range(len(arr1[0])):
        temp.append(arr1[a][b] + arr2[a][b])
    answer.append(temp)
print(answer)