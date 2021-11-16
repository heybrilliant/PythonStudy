#2021.11.16 Progrmmers Python Basic <List의 다양한 기능>

list1= [135,462,27,2753,234]
print(list1.index(27))
# list.index(특정값) = 특정값이 어느 위치에 있는지 알 수 있음 

# print(list1.index(50))
# 만약 .index()문법에서 없는 값을 입력하면 ValueError가 뜨는 것을 알 수 있음
# if 50 in list1:
    # list1.index(50)
    # 미리 검사하기 때문에 에러가 나지 않음
    
list2 = [1,2,3] + [4,5,6]
print(list2)
# 이와 비슷한 list.extend 문법을 이용해서 합칠 수도 있음

list1.extend([9,10,11])
print(list1)
# 더하기 연산자보다 list.extend 문법이 더 명확하게 볼 수 있고 성능이 좀 더 좋음

list1.insert(2,999)
print(list1)
# list.insert(인덱스, 입력할 입력값) 문법은 설정한 인덱스 자리에 입력할 입력값을 주고 원래 인덱스에 있던 값들이 한 칸씩 뒤로 밀린다
list1.insert(-1,9999)
# 인덱스에서 -1은 맨 뒤에서 첫번째를 의미하기 때문에 가장 마지막에 있던 자리에 9999를 입력하고 원래 맨 마지막에 있던 값을 한칸 뒤로 밀기 때문에 맨 뒤에서 두번째값으로 출력되게 된다
print(list1) #[135, 462, 999, 27, 2753, 234, 9, 10, 9999, 11]으로 출력