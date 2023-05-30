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
            break        # break를 할 필요는 없이 return을 해도 된다.
    return result        # return 은 for 열에 맞쳐서 써준다.
                         # 함수에서 return을 만나면 함수가 종료된다. 

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

# 연습문제1 (사용자 정의 함수)
# 키보드로 반지름의 길이를 입력받고
# 원의 넓이를 구하는 함수를 만들어 결과를 출력하라.
# 원의 넓이 = 반지름 * 반지름 * 3.14


def circlesize(n):
    size = n**2*3.14
    return size
n = int(input("반지름의 길이를 입력하세요.: "))
size = circlesize(n)
print('원의 넓이 :' + str(size))

# 연습문제2 (입력값이 없는 함수)
# hello 출력하기

def hello1():
    print('hello1 python')
def hello2():
    result = "hello2 python"
    return result

print(hello1())
print(hello2())


# 입력 값의 갯수가 정해져 있지 않고 multiple한 함수
def sum(*inputs):
    total = 0
    for a in inputs:
        total += a
    return total
totalvalue = sum(1,2,3,4,5)
print(totalvalue)

# 2개 이상의 리턴값이 있는 경우
def cal(a, b):
    result1 = a + b
    result2 = a - b
    result3 = a * b
    return result1, result2, result3
calvalue = cal(1,2)
print(f'계산한 첫번째 결과값 {result1}, 두번째 결과값 {result2}, 세번째 결과값 {result3}')

# 함수에서 default값 미리 세팅
def cal (a, b, c):
    if c == 'plus':
        result = a + b
    elif c == 'minus':
        result = a - b
    elif c == 'multiple':
        result = a * b
    return result

# 더하기한 값 출력
print(cal(1, 3, 'plus'))
# 마이너스한 값 출력
print(cal(1, 3, 'minus'))
# 곱하기한 값 출력
print(cal(1, 3, 'multiple'))

# 매개변수의 순서를 안맞추고도 원하다 매개변수의 자리에 값을 넣어 함수를 호출하는 방법
def whoareyou(name, age, gender):
    print(f'제 이름은 {name}이고, 나이는 {age}, 성별은 {gender}입니다.')

whoareyou(age = 19, name = '홍길동', gender = '남자')

# print 2개를 사용해서 줄바꿈 없이 hello wirld 라고 출력이 되도록 만들어보자.
print('hello', end ='')
print('world')

# 지역변수와 전역변수
# 지역변수 : 함수내에서의 변수, 함수 내에서만 유효
# 전역변수 : 함수 밖에서의 변수, 함수 내에서도 인식가능 

a = 100 # 전역 변수
def sum(a,b):
    # 여기서 a는 100 인가? 10인가?
    # 전역 변수인 100보다 지역변수인 10을 먼저 인식             
    result =  a + b + 200    # 지역변수
    return result
result = sum(10, 20)
print(result)
print(a)

# for 문마다 같은 변수를 사용하는 것은 전역변수이기는 하지만
# 재할당을 해서 사용하는 것이므로 어차피 reset되서 문제되지 않는다
lista = [10, 20, 30, 40]
for a in range(len(lista)):
    print(a)
for a in range(len(lista)):
    print(a)
print(a)

# 이중 for 문을 사용할 때 문제가 될 여지가 있다.
for a in range(len(lista)):
    for b in range(len(lista)):
        print(a)
        print(b)


# 함수 내에서 전역변수에 영향을 미치는 방법 : global
# 기본적으로 저장되는 메모리 위치가 다르기 때문에 함수 내에서 함수 밖의 전역변수를 변경할 수 없다.
result = 0
def sum(a):
    global result
    result += a
    return result
result = sum (10)
print(result)

# 객체는 힙메모리 영역에 저장되는데, 함수 내에서도 접근하여 추가/수정이 가능하다.
# 스택영역에 있는 지역변수는 함수가 끝나면 휘발되지만, 힙메모리는 휘발되지 않는다.

lista = [2,3,4]
def appendTest(input1, input2):
    input.append(input2)

appendTest(lista, 5)
print(lista)

# 만약에 지역변수가 함수호출이 끝난 뒤에도 남아있다면 어떻게 될까?
# 함수에서 사용하는 지역변수가 계속 메모리에 남아 있으면
# 메모리 낭비 뿐만 아니라 다른 함수
# def test1(result):
#     result += 10
#     return result
# def test2():
#     result += 100
#     return result
# a = test1(20)
# b = test2()


# 아래 선택 정렬을 함수화 시켜서 활용해보기
# def mySort 정의하고
# lista = [~~~~~~~~] 호출할 때
# mySort(lista)
# print(lista)
# for a in range(len(lista)-1):
#     for b in range(a+1, len(lista)):
#         if lista[a] > lista[b]:
#             temp = lista[a] 
#             lista[a] = lista[b]
#             lista[b] = temp


def mySort(lista):
    for a in range(len(lista)-1):
        for b in range(a+1, len(lista)):
            if lista[a] > lista[b]:
                temp = lista[a] 
                lista[a] = lista[b]
                lista[b] = temp
    # return lista 없어도 로직 가동 됨, return은 원본을 변형해줄 수 있으며 아래서 재정의를 해줘야 한다.
lst = [5,1,1,23,6,7,8,1,2,3]
mySort(lst) #return 값 사용 할 때 a = mySort(lst)로 변경
print(lst) # return 값 사용 할 때 print(a)로 변경

# lista 에 listb를 담으면, 객체의 주소가 복사가 되게 된다.
# 그래서 listb가 lista와 동일한 주소, 동일한 데이터를 갖게 된다.
lista = [5,1,2] # 1,5,2
listb = lista
# 주소를 출력하는 함수 : id
print(id(lista))
print(id(listb))
# lista 와 값은 갖되, 동일한 메모리 주소가 아니게 할당하고 싶으면 copy 함수 사용

import copy
# 얕은 복사 즉, 객체만의 객체의 값은 (메모리)주소로 복사가 된다.
# 깊은 복사는 copy.deepcopy를 사용하여 객체의 객체도 모두 value로 복사.
listb = copy.copy(lista)
print(id(listb))
print(listb)

