# 예외처리 : Try except 구문
# 예외처리를 하는 이유는 프로그램 실행 중간에 예외가 발생하더라도
# 프로그램이 강제 종료되지 않도록 하기 위해

# while True:
#     # 분자를 입력해주세요 first
#     # 분모를 입력해주세요 second
    
#     # 사용자가 0으로 숫자를 나누게 되면 division by zero error 발생
#     try: # error 발생 예상 구간에 try 삽입
#         first = int(input('분자를 입력해주세요: ')) # 문자 혹은 다른 에러가 생길 변수를 생각하여 try 아래에 삽입한다.
#         second = int(input('분모를 입력해주세요: '))
#         print(first/second)
#     except ZeroDivisionError as zd: # 문제가 발생했을 때 이후의 action except
#         print(f'{zd}오류입니다.')
#     except ValueError as ve: 
#         print(f'{ve}오류입니다.')
#     except Exception: 
#         print(f'{Exception}오류입니다.')
#     finally : # 문제가 있든 없든 무조건 실행
#         print('결과를 확인해주세요')
#     break

# Error 강제의 예시
# 부모클래스 raise Excpeption(에러 강제)를 통해
# 자식클래스로 하여금 overriding(재정의) 유도
while True:
    raise Exception

class Bird:
    def fly(self):
        raise Exception

class Eagle(Bird):
    def fly(self):
        print('fly fly')
    pass

eagle1 = Eagle()
eagle1.fly()


