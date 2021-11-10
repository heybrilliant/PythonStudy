#2021.11.10 Progrmmers Python Basic <예외처리 try, except>


"""
파이썬에서 발생할 수 있는 오류들 
1. IndexError : 색인오류 index out of range
2. ValueError : invalid literal or number

-> 이러한 에러이름을 활용하면 에러를 코드 내에서 처리할 수 있음
"""

text = '100%'
try : 
    number = int(text)
except ValueError:
    print('{}는 숫자가 아니네요.'.format(text))
# 오류가 발생할 것 같은 코드를 try아래에 넣고 except 뒤에서 발생할 수 있는 에러의 이름을 입력해두면 에러가 발생할 경우 별도로 처리해줄 수 있음

"""
try:
    # 에러가 발생할 가능성이 있는 코드
except Exception: # 에러 종류
    #에러가 발생 했을 경우 처리할 코드
"""

def safe_pop_print(list, index) :
    try : 
        print(list.pop(index))
    except IndexError :
        print('{} index의 값을 가져올 수 없습니다'.format(index))
safe_pop_print([1,2,3], 5)

# if - else문으로도 처리가 가능함
def safe_pop_print(list, index) :
    if index <len(list):
        print(list.pop(index))
    else :
        print('{} index의 값을 가져올 수 없습니다'.format(index))
safe_pop_print([1,2,3], 5)
# 같은 결과를 가져옴 -> 코드가 간결하고 읽기 쉬운편으로 선택해주면 됨


try :
    import my_module
except ImportError: 
    print('모듈이 없습니다.')