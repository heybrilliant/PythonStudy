#2021.10.25 Progrmmers Python Basic <함수의 값>
# return의 기능 : return을 이용해 값을 돌려줄 수 있다
#  = 함수가 실행 결과로 값을 갖도록 하는 것

def add_10(value): 
    """ value에 10을 더한 값을 돌려주는 함수"""
    result = value + 10
    return result

n = add_10(42)
print(n)

n = round(1.5)
print(n)

# 만약 한 함수에 return값이 2개라면?

def add_10(value): 
    return 10
    result = value + 10
    return result
# 결과값은 10이 나옴 
# return은 실행 즉시 함수를 끝내버림 = 첫 return 뒤의 코드는 모두 실행되지 않는다 
# -> if문을 이용해서 원할 때 return을 사용해서 끝낼 수도 있음

def add_10(value): 
    if value < 10 :
        return 10
    else : 
        result = value + 10
    return result

n = add_10(5)
print(n)
n = add_10(42)
print(n)