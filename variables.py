# 샵 표시는 프로그래밍에서 주서깅라 말한다.
# 주석은 파이썬의 인터프리터가 인식하지 못하도록 하는 기호
# 단축키는 ctrl 슬래시

# 아래 a = 1의 의미는 a와 1이 같다라는 의미가 아니라,
# a라는 이름의 변수에 1을 담겠다는 뜻.
a = 1
b = "1"

#print는 실행 후 결과값을 가시적으로 보여주기 위해 터미널차에 출력하는 것 
print(a)
print(b)

a = a + 1
print(a)

# 변수명명규칙
# 변수명을 지을 떄는 숫자가 먼저 나와서는 안된다.
# 변수명 중간에 띄어쓰기, 득수기호등을 일반적으로 쓰지 않는다.
# 특수부호는 일반적으로 사용하지는 않지만 '_' 언더바는 빈번히 사용한다.

# 변수 자료형 출력해보기
# int = integer 정수
print(type(a))

# str = string 문자열

print(type(b))

# Float = 실수
c = 2.1
print(type(c))

# 사칙연산
# 덧셈: +, 뺄셈: -, 곱셈: *(asteris or all 모든 것을 의미하기도 함), 나눗셈: /

# 자료의 형변환
# 숫자 -> 문자
c = 10
d = 20
# 결과값이 1020이 나오도록 덧셈을 하여라
answer = str(c) + str(d)
print(answer)

# 실수 -> 정수
e = 23333.3333
# e를 정수로 바뀌어라
print(int(e))

# 문자 자료형
# 문자는 ""쌍따옴표 또는 ''홀따옴표로 표현 한다.

# 'a' 라는 문자를 변수에 저장하게 되면, 메모리상에 어떤 숫자값을 저장될까?
X = 'a'
print(ord(X)) # ord = ordinal 내장 함수

y = 'Y'
print(ord(y))

# multi line으로 문자열을 표현 = 쌍따옴표 3개를 사용 or 홀따옴표 3개를 사용
g = """hello 
world"""
print(g)

# 이스케이프문을 활요한 줄바꿈
# 이스케이프문이란 \n or \t 등의 특수기호를 말한다.
# \n : 줄바꿈, \t : tap

h = "hello \nworld"
print(h)

i = "hello \tworld"
print(i)

# 역슬래쉬의 또다른 활용 : 특수문자를 있는 그대로 표현하는 역할
# "쌍따옴표(")는 파이썬에서 문자를 의미한다" 라는 문굴를 출력해보자.

w = "쌍따옴표(\")는 파이썬에서 문자를 의미한다"
print(w)

# 에제. python is easy 라는 문구를 출력해보자.
r = "python's easy"
print(r)

# 문자열 더하기, 곱하기
# a 라는 변수에 python이라는 문자열을 담고, b변수에는 is fun이라는 문자열을 담는다.
# 그리고 c라는 변수에 두 문자열을 더한 값을 넣어 출력

a = "python "
b = " is fun"
c = a + b
print(c)

# python python is fun 이라는 문자열을 c에 담아 출력
c = a*2 + b
print(c)

# python 에서 인덱스란, 기복적으로 특정위치를 가르키는 용도로 사용
# 인덱스의 사용방법은 원하는 대상[숫자값]
# 프로그래밍에서는 '0' 부터 시작한다. *공백도 포함된다.
u = "pyt hon's fun python's fun python's fun"
print(u[4])

# 문자열의 마지막문자를 출력
print(u[-1])

# 문자열의 길이를 구하는 함수 len()
print(len(u)) # 0부터 시작하는게 아니다.
print(u[38]) # 마지막 숫자는 39가 아니라 38번째이다.
print(u[len(u)-1])

# 문자열의 슬라이싱
# 문자열을 잘라내는 것을 의미
# 대상이되는값[x:y] x 이상 y 미만의 index를 가진 문자열을 잘라낸다.

i = "python is fun"
# python만 잘라내서 p 에 담아 출력하세요
p = i[0:6]
print(p)

# x,y 자리에 값이 없으면 처음부터 또는 끝까지 의미
# 6번째 문자부터 끝까지 잘라내서 변수 q에 출력
q = i[6:]
print(q)

# a[x:y:z] 여가에서 z는 z-1 개씩 건너뛰고
# 2번째 이상 5번째 이하 문자열 중 1개씩 건너뛰고  v에 출력
v = i[2:5:2]
print(v)

# 예제 2
# a = "20220505children's_day" 를 date 라는 변수에 날짜, day 라는 변수에 children's day를 담아서 각각 출력하시오
a = "20220505children's day"
date = a[0:8]
day = a[8:]
print(date)
print(day)