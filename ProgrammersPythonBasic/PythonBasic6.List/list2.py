#2021.11.01 Progrmmers Python Basic <리스트 수정>

list2 = [37, 23, 10, 33, 29, 40]
print(list2)

# 리스트에 새로운 값을 추가하는 방법 
# 1) .append()를 이용한다 
list2.append(16)
print(list2)

# 2) 새로운 list에 list를 더하는 방법
list3 = list2 + [14]
print(list3)

# in 연산 : 리스트에 특정 값이 들어있는지 아닌지 확인하는 방법
n = 12
ownership = n in list3
print(ownership)
# 답은 False

# 결과가 boolean값이므로 if문을 이용해서 다양하게 사용 가능 
n = 10 
if n in list3 :
    print('{}은 있어!'.format(n))

# del을 이용해서 특정 위치의 값을 지우기
print(list3)
del list3[3]
# 3번째 값을 지워라
print(list3)

# 내장함수 remove를 이용하여 특정 값 지우기
# 여러개의 값이 있는 경우 가장 앞에 있는 하나만 지워짐
list3.remove(40)
print(list3)