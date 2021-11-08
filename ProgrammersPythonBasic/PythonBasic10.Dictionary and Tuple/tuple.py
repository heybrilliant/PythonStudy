#2021.11.08 Progrmmers Python Basic <튜플 만들기>

# 리스트는 순서가 정해진 값의 집합 

# 튜플 생성
# 리스트 생성=대괄호, 딕셔너리 생성=중괄호, 튜플 생성=소괄호

tuple1 = (1,2,3)
print(tuple1)
print(type(tuple1))

# 소괄호 없이 선언해도 튜플 생성 가능
tuple2 = 1,2,3
print(tuple2)
print(type(tuple2))
# 그러나 소괄호로 튜플을 생성해 주는 것이 더 명확하게 표현해주는 장점이 있음

list1 = [1,2,3]
tuple3 = tuple(list1)
print(tuple3)
print(type(tuple3))
# list를 넣어서 튜플을 생성해도 대괄호가 아닌 소괄호로 생성됨

# 리스트처럼 인덱스를 통해서 값을 얻어올 수 있음
print(tuple3[0]) #1
print(tuple3[1]) #2

# 그러면 리스트처럼 값을 바꾸기도 가능? -> 불가능 
# 튜플은 한 번 만들고 나면 변경할 수 없는 '순서가 정해진 값의 연속'임
# 그래서 pop도 사용 불가능 