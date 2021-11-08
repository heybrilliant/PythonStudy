#2021.11.08 Progrmmers Python Basic <딕셔너리와 리스트 비교>

# 값을 호출할 때
list = [1,2,3,4,5]
dict = {'one':1, 'two':2}
# 리스트는 인덱스를 넣고, 딕셔너리는 키를 입력해서 값을 받아옴
print(list[0])
print(dict['one'])


# 값을 지울 때
del(list[0])
print(list)
del(dict['one'])
print(dict)

# 총 길이를 구할 때
print(len(list))
print(len(dict))

# 내부에 어떤 값이 들어있는지 확인할 때
print(2 in list) #True 출력
print(7 in list) #False 출력
print('two' in dict.keys()) #True 출력
print('to' in dict.keys()) #False 출력
# 딕셔너리는 keys 외에도 values에서도 확인 가능 
print(2 in dict.values()) #True 출력
print(32 in dict.values()) #False 출력

# 내용물을 모두 지우는 방법 
list.clear()
dict.clear()

# 리스트는 인덱스로 값을 가져오기 때문에 값이 추가되거나 빠진 경우 최종적으로 가져오는 값이 달라질 수 있음
# 그러나 딕셔너리는 key값으로 value를 가져오기 때문에 추가 혹은 삭제가 진행되어도 값이 달라지는 일이 없음
