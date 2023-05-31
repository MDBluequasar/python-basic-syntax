# Class의 사용
# 1) 같은 기능의 함수의 집합
# 2) 객체를 만들기 위해 사용

# 사칙연산 함수가 있을때, 같은 기능을 하므로
# Calculator라는 Class에 모아둘 수 있다.
# 명명 규칙 : 일반적으로 클래스는 대문자 알파벳으로 시작
# 변수명, 함수명은 소문자로 시작 -> camalcase
# myImportantList # my_important_list 이건 식으로 쓴다.
# 험수의 집합으로서의 클래스 -> 일반적이지 않다.
class Calculator:
    result = 0
    # 클랴스 변수 접근 가능 방법1 : 클래스명, 변수
    # 방법2 : classmethod 데코레이터 사용
    # class 내에 선언된 함수는 method라 부른다.
    @classmethod            
    def plus(cls, a):          # 위 코딩과 아래 코딩으로 쓸 수 있다
        cls.result += a         
    def minus(a):
        Calculator.result -= a
    def multiply(a):
        Calculator.result *= a
    def divide(a):
        Calculator.result /= a        
print(Calculator.result)
Calculator.plus(10)
print(Calculator.result)
Calculator.minus(5)
print(Calculator.result)
Calculator.multiply(10)
print(Calculator.result)
Calculator.divide(10)
# 위 클래스의 문제점은 클래스 내에서 누적된 값을 변수로 갖고 있지 않다.


# 객체의 사용이유
# 클래스의 중복제거 : 변수와 함수의 재활용의 어려움 해결
# 객체 형식의 클ㄹ래스의 기본구조

class Calculator:
    # 객체가 생성될 때 init(생성자)은 가장 먼저 실행
    # 생성자는 객체 생성 될 때 객체 변수를 초기화.
    # result와 self.reult는 다른 값이다.
    def __init__(self): # 언더 바 두 개씩 
        self.result = 0 # 셀프에 각 객체=인스턴스(aCompany) 값이 들어가서 각각의 결과값을 도출해낼 수 있다.
    # 객체를 만들 때 첫번째 매개 변수(self)는 객체를 의미한다.

    def plus(self, a):
        self.result += a
    def minus(self, a):
        self.result -= a
    def multiply(self, a):
        self.result *= a
    def divide(self, a):
        self.result /= a

aCompany = Calculator()
aCompany.plus(100)
bCompany = Calculator()
bCompany.plus(100)
print(aCompany.result) # print(aCompony.plus(100)) => 100
print(bCompany.result) # print(aCompony.plus(100)) => 200 위의 값에서 중복 덧셈되어 결과값 출력


# 클래스 생성 시 매개변수를 통해 초기값 세팅 가능
aCompany = Calculator()
print(aCompany.result)
bCompany = Calculator()
print(bCompany.result)

# 생성자로 이름(name), 나이(age), 성별(gender), email이라는 매개변수 받아, 각각의 객채변수를 만든다.
# register 이라는 method를 만들어서, 해당 method에서는 myInfo라는 객체변수에 이름,나이,성별,email 정보를 문자열로 담는다.
# 2auddml person을 만든다.

class Person:
   
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        
    def register(self): # def registor(self, name, age, gender, email)
        self.myInfo = self.name +" "+ self.age +" "+ self.gender +" "+ self.email
        # self.myInfo = name +" "+ age +" "+ gender +" "+ email
    

p1 = Person('홍길동', '181312', '남', 'hodsos@nssma.com')
p2 = Person('걍걍', '50001', '여', 'asdwa2@dedaasd.com')
p1.register()
p2.register()
print(p1.myInfo)
print(p2.myInfo)

# 클래스의 상속
# 부모클래스에서의 기능을 자식클래스에서 물려받는것
# class 자식클랙스명(부모클래스명) 이런 형식으로 선언
class Calculator: 
    def __init__(self):  
        self.result = 0 
    def plus(self, a):
        self.result += a
    def minus(self, a):
        self.result -= a
    def multiply(self, a):
        self.result *= a

class CalculatorChild(Calculator):  # 괄호 안은 상속 받고자 하는 class명을 적는다.
    def divide(self, a):
        self.result /= a
    
    # 부모한테 있는 기능을 재선언하게 되면, 부모의 기능보다
    # 자식의 기능이 우선하게 되고, 이를 overriding이라 한다.
    def multiply(self, a):
        self.result *= (a+1)
    def printCalObject(self):
        return self.result
cc1 = CalculatorChild()
cc1.plus(100)
cc1.divide(10)
cc1.multiply(10)
print(cc1.result)
print(cc1.printCalObject)
# print 함수가 속해있는 클래스는 objct클래스를 상속 받고 있다.

