#2021.11.04 Progrmmers Python Basic <module 사용하기>
# module : 모듈, 다른 기능을 가져다가 쓸 수 있는 방법

"""
import math : math 문법을 가져다 쓰겠다는 의미
예를 들어 반지름이 10인 원의 둘레를 구하겠다 
-> r(반지름) = 10
2 * math.pi * r = 반지름이 10인 원의 둘레 공식
"""
import math
math.ceil(2.5) # == 올림
# -> 값은 3 출력
math.floor(2.5) #== 내림
# -> 값은 2 출력


"""
import random : 무작위에 관련된 모듈
random.choice() : 후보로 받은 list 중 하나를 무작위로 골라주는 함수 
"""
import random
candidates = ['가위', '바위', '보']
selected = random.choice(candidates)
print(selected)
