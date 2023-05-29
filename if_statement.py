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
'''if문 한 줄로 작성 조건부표현식(상한연산자)'''
# a = 0
# if a < 1: print("a는 1보다 작다"); print(";은 줄 구분을 위해 사용")

'''삼항연산자 1'''
'''실행문을 실행하기 위해보다 참인 경우, 
거짓인 경우의 값을 쉽게 result에 담기위해 사용'''
# a = 10
# (print("\'a\'는 10보다 크다")) if a>10 else print("\'a\'는 10보다 작다")

'''삼항연산자 2'''
# a = 10
# print('\'a\'는 10보다 크다') if a>10 else print("\'a\'는 10보다 작다")

# a = 10
# result = '\'a\'는 10보다 크다' if a>10 else "\'a\'는 10보다 작다"
# print(result)

'''삼항연산자 예시'''
# lista = list(range(1,11))
# print(lista)
# num = int(input("숫자 입력 : "))
# print("입력한 숫자 존재") if num in lista else print("입력한 숫자가 없음")

'''if 연습문제 1'''
# suitcase = int(input("짐의 무게 : "))
# if suitcase >= 10:
#     money = (suitcase//10)*10000
#     print(f"짐의 무게는 {suitcase}kg, 수수료는 {money}원입니다.")
#     print("짐의 무게는 {%d}kg, 수수료는 {%d}원입니다."%(suitcase, money))
# else:
#     print("수수료 무료입니다.")

'''if 연습문제 2'''
# money = int(input("가진 돈 : "))
# hunger = str(input("yes/no : "))
# result = "밥을 사 먹으시오" if money > 5000 and hunger == 'yes' \
# else '집에 가시오'
# print(result)

'''비교연산자 is(==)'''
# 숫자, 문자, bool의 경우 데이터 pool에서 만들어서 재활용
# 그래서 값 비교 시 메모리 주소가 아니라 데이터 pool에서 값을 비교


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

