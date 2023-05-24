# list는 변수마다 값을 할당해서 사용하기에, 관리의 어려움이 있으므로
# 한 변수에 값을 집합시켜놓은 것
# 하나의 변수로 여러개의 대이터를 관리
# list의 경우에 []대괄호를 사용하여 데이터를 집합
lista = ["김돌쇠", "김갑돌", "김갑순"]

# list 안의 각각의 값에 접근할 때에는 index를 사용
print(lista[0])
print(lista[1])
print(lista[2])

# 여러개의 데이터를 범위를 지정해서 가져오고 싶을 때는 slicing 사용
# slicing의 결과값은 값은 list로 출력
# 0~5번째까지 출력
print(lista[0:5])

# 0~5번째까지 출력한 결과물의 type 출력
print(type(lista[:5]))

# 예제 1
# list_ex = ['a','b','c',[1,2,3]] 
# 변수 number에 [1,2,3]을 담아 출력하라
# nember에 담은 값 중 1과 3을 더해 4를 출력하라

list_ex = ['a','b','c',[1,2,3]]
print(list_ex[3][:3])
print(list_ex[3][0] + list_ex[3][2])

# 리스트 더하기 또는 곱하기
lista = ['a', 'b', 'c']
listb = [1, 2, 3]
listc = lista + listb
listd = lista * 2
print(listc)
print(listd)

# 리스트 길이 구하기 : len
print(len(lista))

# 리스트 값 수정하기 -> 1개의 값만 바꿀 땐 1개의 값으로
# 여러 값으로 바꿀 땐 다른 리스트로 대체
lista = [1,3,5,7,9]
lista[1] = 4
print(lista)
lista[2] = [6,8,10]
print(lista)

# 리스트 요수 개수 세기(count)
lista = ["1","2","3","4","1","1","1"]
print(lista.count("1")) # counta = lista.count("1") -> print(counta)

# 리스트 값 삭제하기 (del)
#a = [1, 2, 3, 5, 7, 9, 10]
# 위리스트에서 3번째 값을 삭제하라
a = [1, 2, 3, 5, 7, 9, 10]
del a[2]
print(a)

# 위 리스트에서 2번째 ~ 5번째 값을 삭제하라
a = [1, 2, 3, 5, 7, 9, 10]
del a[1:5]
print(a)

# 리스트 값 삭제하기 (remove)
a = [1, 2, 3, 5, 7, 9, 10]
a.remove(3)
print(a)

# 예제 2 (del, remove, for range)
# 모든 특정한 값을 모두 삭제하는 법
# 9 값을 제거 하여라
# 방법1
count = 0
lista = [1, 3, 9, 3, 5, 6, 9, 9]
for a in range(0, len(lista)):
    if lista[a-count] == 9:
        del lista[a-count]
        count =  count + 1
print(lista)

# 방법2
lista = [1, 3, 9, 3, 5, 6, 9, 9]
listb = []
for a in range(0, len(lista)):
    if lista[a] != 9:
        listb = listb + [lista[a]] # listb.append(lista[a])
print(listb)

# 방법3
lista = [1, 3, 9, 3, 5, 6, 9, 9]
for a in range(0, len(lista)):
    if 9 in lista:
        lista.remove(9)
    else:
        break
print(lista)

# list append : 리스트 맨 뒤로 추가
# 9,10을 추가해서 출력
lista =  [1,3,4,7]
lista.append(9)
lista.append(10)
print(lista)

# kist insert : index를 지정하여 추가 기능
# list. index(2,"adc") 추가 후 출력
lista.insert(2,"abc") # 2는 문자열 3번째 자리에 삽입하는 것이다.
print(lista)

# list extend : iterable 객체를 list에 추가할 때 사용
#extend는 각 요소를 꺼내어 맨 뒤에 추가
listb = [10, 20, 30]
lista.extend(listb) #lista.append(listb)
print(lista)

# list의 정렬은 sort() 함수 이용
# sort()는 오름차순 정렬
numa = [5, 3, 18, 4, 2, 1]
numa.sort() #내림차순 sort(reverse=True)
print(numa)

chlist = ['brad', 'john', 'abc', 'jack', 'peter']
chlist.sort()
print(chlist)

# list 뒤집기 : reverse()
chlist.reverse()
print(chlist)

# list 위치 변환(index)
#list.index(값)
# 리스트 중 "김철수"는 몇 번째 문자인가?
listc = ["김돌쇠", '김갑돌', "김갑순", "김철수"]
print(listc.index('김철수'))

# list 마지막 요소 끄집어 내기 : pop()
# listc.pop()
# remove and return last value

listc.pop()
lastvalue = listc.pop()
print(lastvalue) # 최종적으로 print(listc.pop()) 으로 쓸 수 있다.

# 문자 리스트를 문자열로 만들기
listv = ['hello', 'python', 'world']
sta = "hello python world"
st1 = ""
st2 = st1.join(listv)
print(st2)

listv = ['hello', 'python', 'world']
st1 = ""
for a in listv:
    t = st1 + a
print(t)

# 문자열을 문자 리스트로 만들기
sta = "hello python world"
mysta1 = list[sta]
mysta2 = sta.split()
print(mysta1)
print(mysta2)