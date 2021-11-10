#2021.11.10 Progrmmers Python Basic <예외처리 - 예외의 이름을 모를 때>

# list = []
# print(list[0]) #IndexError

# text = 'abc'
# number = int(text) #ValueError

# 그런데 만약 에러의 이름을 모를때는 예외처리를 어떻게 해주어야 할까?
# -> except 뒤에 에러의 이름을 적어주지 않으면 된다

try : 
    list = []
    print(list[0]) 
except:
    print('에러가 발생했습니다.')

"""
try:
    # 에러가 발생할 가능성이 있는 코드
except Exception as ex: # 에러 종류
    print('에러가 발생 했습니다', ex) 
    # ex는 발생한 에러의 이름을 받아오는 변수
"""

try : 
    list = []
    print(list[0]) 

    text = 'abc'
    number = int(text)
except Exception as ex:
    print('에러가 발생했습니다.',ex)
    # 에러가 발생했습니다. list index out of range 에러 출력 