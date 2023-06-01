a = 3
b = 4
# 덧셈 : +, 뺄셈 : -, 곱하기 : *, 나누기 : /, 몫 : //, 나머지 : %
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

# 제곱, 제곱근
# 2의 10 제곱을 출력하라
# print(2**10)
# print(pow(2,10)) <- #python 내장함수

# 1024의 제곱근을 구하라
import math # python에 내장되지 않은 함수
print(math.pow(2,10))

# 제곱근은 math라는 라이브러리를 import해줘야한다.
print(math.sqrt(1024))

# 예제 1
# 아래와 같은 2차 방정식을 파이썬 수식으로 코딩하고 y의 결과를 출력하라.
x = int(input("x의 값을 입력해주세요"))
y = 2.5 * pow(x,2) + 3.3 * x + 6
print("y의 값은 %f 입니다." % (y))