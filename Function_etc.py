# 람다함수 : 
# 1) 함수를 간편하게 표현하기 위한 방식
# 2) 함수를 변수에 담기 위한 방식
# lambda 매개변수 : 실행문

def add(a,b):
    return a+b
print(add(1,2))

add_lambda = lambda a, b : a + b
print(add_lambda(1,2))
# 매개 변수 a를 입력했을 때, a의 제곱이 출려되는 lambda 함수 생성

st = lambda a : pow(a, 2)
print(st(2))

# list에 lambda 함수를 담아서 사용 가능.
cal_list = [lambda a,b: a+b, lambda a,b: a-b, lambda a,b: a*b]
print(cal_list[0](1,2), cal_list[1](1,2), cal_list[2](1,2))

# Dictionary 이용한 lambda
cal_dict = {'plus':lambda a,b: a+b, 'minus':lambda a,b: a-b, 'multiple':lambda a,b: a*b}
print(cal_dict['plus'](1,2),cal_dict['minus'](1,2),cal_dict['multiple'](1,2))

# lambda 로 입력한 매개변수가 짝수면 Truem 홀수이면 False
oddOrNot = lambda x : True if x % 2 == 0 else False

# Map 함수 : 특정 함수와 반복가능한 자료형을 입력받아, 특정함수가 수행가능한 결과값을 return
# Map의 역할 : 함수를 적용하여 대상이 되는 리스트를 가지고, 새로운 리스트를 만들어내는 역할
# 사용예시 : map(함수, 리스트 or (튜플))

def two_times(x):
    return x*2
print(list(map(two_times, [1,2,3,4,]))) # lst = list(map(two_times, [1,2,3,4,])) => print(lst) 도 가능

# map 함수와 lambda 함수를 사용해서 입력한 list의 제곱값을 담은 list를 출력하도록 하자.

ls = list(map(lambda x : pow(x ,2), [1,2,3,4,5]))
print(ls) # print(list(map(lambda x : pow(x ,2), [1,2,3,4,5])))

# Filter
# filter의 역할 : 함수를 적용하여 참/거짓 대상이 되는 리스트에서 득정한 조건으로 값을 걸러내는 것
def TrueOrNot(x):
    if x > 0:
        return True
    else:
        return False
lst = list(filter(TrueOrNot, [-1,0,3,-2,5]))
print(lst)

# 위 로직을 lambda를 써서 바꾸어보자(삼항연산자)
lst = list(filter(lambda x : True if x > 0 else False, [-1, 0, 3, -2,5]))
print(lst) 

# 위 로직을 map을 썼을 때
lst = list(map(lambda x : True if x > 0 else False, [-1, 0, 3, -2,5]))
print(lst) # [False, False, True, False, True]

# 연습문제
# 함수형 프로그래밍을 사용하여, 주어진 list에서 홀수만 추출하도록 하여라.
# Filter와 lambda 사용
lista = [4,7,1,2,5,6,8]
ans = list(filter(lambda a: True if a % 2 != 0 else False, lista))
print(ans)

# 위 코드의 총합
print(sum(ans))  # sum_value = sum(ans)
                 # print(sum_value)

# sum : 주어진 자료들의 총합
print(sum([1,2,3]))

# 문자를 아스키코드 변환 : ord()
print(ord('a'))
# 숫자 107이 의미하는 아스키코드상의 문자는 뭘까? : chr()
print(chr(97))
# 예를 문자열이 주어질 때 숫자를 제외하고 문자값만 새로운 문자열로 만들어보아라
str1 = '123asdf512kjlk'
print(ord('z')) #소문자 a~z : 97~122
print(ord('z')) # 소문자 a~z : 65~90
new_str = ''
for a in str1:
    if (122 >= ord(a) >= 97) or (65 >= ord(a) >= 90):
        new_str += a
print(new_str)

# 절대값 : abs()
print(abs(-3))
# map을 사용해서 주어진 리스트를 절대값으로 변환한 리스트를 출력해보자.
lista = [1, -5, -7, 12, -5]
fun = list(map(abs, lista))
print(fun)

# 재귀함수
# Factorial 예제
# 변수 n 을 넣었을 때 n!가 나오도록 함수를 만들어보자.

def facto(n):
    total = 1
    for a in range(1, n+1):
        total *= a
    return total
result = facto(5)
print(result)

# 재귀함수를 통한 factorial 예제
# 재귀함수란 함수내에서 함수자기자신을 호출하는 함수
# 재귀함수에서는 반드시 재귀함수를 종료시키는 조건이 필요하다.

#예시1 덧셈
def test(n):
    if n == 1:
        return 1
    return n + test(n-1)
result = test(10)
print(result)

#예시2 factorial
def test2(n):
    if n == 1:
        return 1
    return n * test2(n-1)
result = test2(10)
print(result)


# 재귀함수를 반드시 써야만 하는 상황
# 반복의 획수를 알 수 없을 때

#예제
# 다섯 개의 숫자 중에 2개씩 숫자를 추출하는 경우의 수를 구하고자 한다.
# 2개씩 숫자를 추출하여 list에 담아 마지막에 모든 텍스트를 추력하도록 하여라.
lista = [34,15,7,7,1]

lst = []
for a in range(len(lista)):
    for b in range(a+1, len(lista)):
        lst.append([lista[a], lista[b]])

print(lst)


