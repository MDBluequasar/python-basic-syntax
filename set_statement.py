# set은 (수학)집합이라고 부르기도 한다.
# set의 특성은 dictionary 와 마차가지로, index가 없고, 중복이 없다.
s1 = {'이름', '나이', '성별'}
# list의 중복을 제거하기 위해 list를 가지고 set으로 형변환 시키는 방식도 많이 사용
s1 = set(['이름', '나이', '성별'])
print(s1)
# 집합의 갯수 구하는 함수 : len
print(len(s1))
s2 = set('test')  # s2 = set(list("test")) 로 작성하여 test가 온전히 나올 수 있다.
print(s2) # 중복이 제거 된다.

# index 로 접근은 불가
# print(s1[0]) -> 출력 안됌

# 예제1
# 리스트의 혈액형의 종류의 갯수를 출력하라.
lista = ['A', 'A', "A", "B", "B", 'AB', "o"]
s1 = set(lista)
print(len(s1))

# s1(set로 변환된 변수)의 값을 하나씩 출력하려면? 
for a in s1:
    print(a)

# 합집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8])
s3 = s1 | s2 # 'shift + \ = |' 프로그래밍에서 '|' 기호는 or 를 의미 # set 에서는 합집합
s4 = s1.union(s2) # 합집합 방법2
print(s3)
print(s4) 

# 교집합
s3 = s1 & s2 # programming 에서 ' & ' 는 and를 의미, 엠퍼샌드 라고 부른다.
s4 = s1.intersection(s2)
print(s3)
print(s4)

#차집합
s3 = s1 - s2
s4 = s1.difference(s2)
print(s3)
print(s4)

# 집합에서 값 추가 : add (list는 append, dicrionary는 key : value 의 차이 확인)
s1 = set({1,2,3,4,5,6})
# 7의 값을 출력하여 s1 출력
s1.add(7)
print(s1)

# 집합에 값 여러 개 추가 update 함수 (dictionary와 동일)
s1 = set({1,2,3,4,5,6})
s2 = set({10,100,1000})
s1.update(s2) # s3 = s1.update(s2) 는 안됨
print(s1)

# set 값 삭제 시 remove 함수 사용
s1 = set({1,2,3,4,5,6})
# discard : remove와의 차이점은 삭제할 값이 존배하지 않아도 error가 발생하지 않음.
s1.remove(4) # 방법1
s1.discard(6) # 방법2
print(s1)

# boolean(불형) type
# in (또는 not in) 뒤에 iterable한 자료형이 나온다.
# a in list, a not in list, a in dictionary, a in set

# 비어있는 값들은 거짓, 값이 들어있으면 참 






