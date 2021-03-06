#2021.10.31 Progrmmers Python Basic <리스트 List>

# List : (자료형) 여러 값을 순서대로 담아두고 꺼내 쓸 때 사용할 수 있는 자료형
# 여러 값이 한 번에 입력되어 있기 때문에 출력할 때도 여러 값이 한꺼번에 나옴

list1 = ['가위', '바위', '보']
list2 = [37, 23, 10, 33, 29]

print(list1)
print(list2)

# 값을 꺼내 쓸 때에는 대괄호[]를 사용하여 숫자를 넣으면 해당하는 값을 불러올 수 있음
# 리스트를 사용할때는 0번째가 첫번째
print(list1[1])
print(list2[2])
print(list1[0])

# 리스트 안에 든 값은 변수처럼 다룰 수 있음

list1[0] = '바위' # 변수처럼 선언하여 list안의 값을 변경
print(list1[0])
print(list1)

# 뒤에서 첫번째 값 list1[-1]
# 뒤에서 두번째 값 list1[-2]
# 리스트에 들어있는 값 보다 큰 값을 읽어오려고 하면 에러