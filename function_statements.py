a = 100
# 특정한 input 값이 있을때
# 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자.
# 그런데 해당 연산은 매우 빈번하게 사용이 된다고 가정하자.

result = ((a + 10) * 20) / 10 ** 2
print(result)
# 복잡한 로직의 연산을 함수화 시켜서 재사용할 수 있게 해보자.
# input 값이 있어도 되고, 없어도 된다.
# return 값이 있어도 되고, 없어도 된다.
# def myFunc(myInput):
#     calc = ((myInput + 10) * 20) / 10) ** 2
#     return calc
# print()
# 정의된 함수를 호출할 때는 함수명(input)의 형태로 호출하게 된다.


# 함수 직접 구현해보기
# 함수명은 myPlusFunc
# 함수의 로직은 사용자의 input을 받아 input 값의 누적합을 더하는 함수 
# 예를 들어 100을 입력하면 1+2+3+...+100


def myPlusFunc(my):
    sum = 0
    for i in range(1,my+1):
        sum += i
    return sum
result1 = myPlusFunc(100)
result2 = myPlusFunc(10)
print(result1)
print(result2)

# input 값을 2개를 받아 두 값을 더한 뒤
# *2 만큼 하여 return 하는 함수를 만들어보자
# 그리고 해당 함수를 호출하여 호출된 결과값을 result에 담아 출력해보자

def mcu(a,b):
    result = (a + b)*2
    return result
result1 = mcu(1,2)
print(result1)

# list의 index 함수를 쓰지 않고 
# for 문 또는 while문을 통해 숫자 9가 몇번째 인덱스에 있는지 값인지
# print 해보자.

lista = [1,4,6,9,10]

for i in range(len(lista)):
    if lista[i] == 9:
        print(i)
        break # 첫 번째 9 숫자만 출력하기 위해서 break를 해준다.

# 위의 for 문을 활용하여 myIndex 라는 이름의 함수를 만들고자 한다.
# input 값이 2개 필요, print는 함수 내에서 하지 않고 return의 값을 적용한다.

def myIndex(lista, num): #Return이 있는 함수는 가장 일반적인 함수 형태이다.
    result = -1  # 초기화를 해주는 것 잊지 말자.
    for i in range(len(lista)):
        if lista[i] == num:
            result = i
            break
    return result        #return 은 for 열에 맞쳐서 써준다.

lista = [1,4,3,8,56,5,7,3,8,4]
result1 = myIndex(lista, 3)
print(result1)


# 함수에서 프린트 하기
def myIndex(lista, num):
    result = -1  # 초기화를 해주는 것 잊지 말자.
    for i in range(len(lista)):
        if lista[i] == num:
            print(i)
            break
lista = [1,4,3,8,56,5,7,3,8,4]
myIndex(lista, 3)
