'''복습'''
list = ['피카츄', '파이리', '꼬부기', '버터풀']
print(list)
list.append('라이츄')
print(list)
list.insert(1, '거북이')
print(list)
element = list.pop()
print(element)

'''tuple은 변경 불가능한 자료형, ()로 표현'''
t1 = (1,2,'a','b')
print(t1)
print(t1[0])
del t1[0]
t1.remove(1)
# 튜플 사용 이유 : 개발자가 해당 자료를 수정하지 못 하게 강제적으로 지정하려고