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
listb = []
for a in range(10):
    if a % 2 != 0:
        a = a * 2
        listb.append(a)
print(listb)