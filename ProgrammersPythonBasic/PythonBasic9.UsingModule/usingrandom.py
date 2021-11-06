#2021.11.06 Progrmmers Python Basic <module 사용 및 활용하기>

import random
# 파이썬에서 랜덤 관련한 함수들을 모아놓은 모듈

# 1. random.choice()
# choice 함수는 매개변수로 seq 타입을 받습니다. 시퀀스 데이터 타입은 문자열, 튜플, range, 리스트 타입들을 말합니다.
# 시퀀스 함수는 인자로 받은 리스트, 튜플, 문자열, range 에서 무작위로 하나의 원소를 뽑습니다.
# 만약, 비어있는 시퀀스 타입의 객체를 인자로 넣는다면 (ex. 리스트가 비어있다면) indexError 의 예외가 발생합니다.
list = ["빨","주","노","초","파","남","보"]
random_element = random.choice(list)

print(random_element)


# 2. random.randint()
# randint 함수는 인자로 들어온 a, b 사이의 랜덤한 정수(int)를 반환합니다.
# 반환하는 x는  a, b를 포함한 범위 입니다. (a <= N <= b)
random_number = random.randint(2,5)

print(random_number)


# 3. random.shuffle()
# 셔플 함수는 데이터의 순서를 무작위로 랜덤하게 바꾸어 주는 함수 입니다.
# 매개변수 x에는 시퀀스 데이터 타입이 들어가게 됩니다. 하지만 내부의 값을 무작위로 바꿔야 하기 때문에 
# 내부인자를 변경할 수 있는 리스트만 가능하게 됩니다. (문자열, 튜플 및 range(a,b)는 불가능)

list = ["빨","주","노","초","파","남","보"]
random.shuffle(list)

print(list)