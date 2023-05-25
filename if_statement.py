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

Q = int(input("얼마를 가지고 있습니까?"))
if Q >= 30000:
    print("택시를 타고 가시오.")
else:
    print("걸어 가시오")

# for 문의 기본 구조
# for 변수 in 반복 가능한 자료형 (iterable)
#     실행문
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #lista는 대괄호를 쓰며, 변수를 한 곳에 모은다. (집합 같은 의미)
for a in lista:
    print(a)

# range 문법 : range(x, y) x이상 y미만
for a in range(1,101): # for a in [1부터 100까지]
    print(a)
