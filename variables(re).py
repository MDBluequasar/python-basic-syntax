# 샵 표시는 프로그래밍에서 주석이라 말한다.
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
# "쌍따옴표(")는 파이썬에서 문자를 의미한다" 라는 문구를 출력해보자.

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

# python 에서 인덱스란, 기본적으로 특정위치를 가르키는 용도로 사용
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

# 문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)를 삽입하는 방식
#  %s : 문자열, %d : 정수, %f : 실수
a = "I studied %s %d" % ("python", 2)
print(a)

# 포맷팅을 왜 쓰는가?
# 1)문자열을 직접 삽입하면 1회성으로 coding 할 수 밖에 없지만 포맷팅은 변수값을 삽입할 수 있다.
# 2)따옴표를 여러번 안닫아도 된다.
language = input("좋아하는 언어를 입력하세요.")
times = input("그 언어를 몇번이나 공부하셨나요.")
a = "I studied %s very hard %d times" % (language, int(times)) # %d는 %s로 변경하면 int 함수를 사용하지 않아도 된다.
print(a) # 실행 중지는 ctrl + C

# 아래와 같이 코딩하면 따옴료로 열고 닫고를 반복하게 된다. 
times = 2
a = "I studied python " + str(times) + " times"
print(a)

# 예제 3
# my age is XX, and weight is XX kg의 문장에서 "나이가 몇살이신가요?" "뭄무게가 몇킬로그햄이신가요?" 를 입력한 후
# 결과값을 출력하시오.

age = int(input("나이가 몇살이신가요?"))
weight = float(input("몸무게가 몇킬로그램이신가요?"))
q = "my age is %d, and weight is %f kg" % (age, weight) 
print(q) 

# 문자열 관련 주요 함수
# count : 대상 문자열에 지정한 문자가 몇개가 있는 출력하는 함수
a = "python"
print(a.count('o'))

# find : 대상 문자열에 지정한 문자가 몇번 index에 있는 찾는 함수
print(a.find('o'))
print(a.index('o'))

# 없는 문자를 찾을 때는 -1 return
print(a.find('x'))

# 예시
whatyouwant = input("문자를 입력해주세요")
search = input("찾고자 하는 문자 1개만 입력해주세요")
result = whatyouwant.find(search)
if result == -1:
    print("찾고자 하는 값이 없습니다.")
else:
   print("요청하신 문자는 %d 번째에 있습니다. " % result)

# 대소문자 변경 : upper() / lower()
# 대문자 변경
a = "hello"
print(a.upper())

# 소문자 변경
b = "HELLO"
print(b.lower())

# 문자열 양쪽 공백을 없는 함수 : strip()
a = "   hello word   "
print(a.strip())

# 문자열 대체 : replace()
a = 'I studied python'
print(a.replace('python', 'java'))

# 공백을 기준으로 문자를 자르는 함수 : spilt()
a = 'i    studied    python'
b = a.split()
c = a.split(" ")
print(b) # 결과값 ['i', 'studied', 'python']
print(c) # 결과값 ['i', '', '', '', 'studied', '', '', '', 'python']

a = 'i:studied:python'
c = a.split(":")
print(c)

# 예제 4
# 3개의 단어를 키보드로 입력 받아 각 단어의 첫글자를 추출 후 단어의 약자를 출력하라.
# <조건1> 각 단어 변수 (word1, word2, word3)
# <조건2> 입력과 출력 구분선 : 문자열 연산
# <조건3> 각 변수의 첫 단어만 추출하여 변수(abbr) 저장

first =  input("첫번째 단어를 입력해주세요")
second = input("두번째 단어를 입력해주세요")
third = input("세번째 단어를 입력해주세요")
addr = first[0] + second[0] + third[0]
print(addr)