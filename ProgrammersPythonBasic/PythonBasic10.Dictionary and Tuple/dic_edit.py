#2021.11.06 Progrmmers Python Basic <딕셔너리 수정하기>
# 딕셔너리에 새 값을 넣거나 있던 값을 지우는 법

# 먼저 리스트에서 값을 수정하는 법을 생각해보자
list = [1,2,3,4,5]
print(list)

list[2] = 33    # list[2] 재정의
print(list)     # 수정된 값 출력

# list[5] = 6     # 맨마지막에 6을 추가하고 싶을 때
# print(list)     # 인덱스에러 
list.append(6)
print(list)

# 리스트 삭제법 
del(list[0])
print(list)


# 딕셔너리 정의
dict = {
    'one':1,
    'two':2,
    'three':3
}
# 딕셔너리 수정 = 리스트 수정법 같음
dict['one'] = 11
print(dict)
# 딕셔너리 새 값 추가 -> 딕셔너리는 append함수가 없음 따라서 그냥 값을 변경할 때 처럼 추가해주는 방법 사용 
dict['four'] = 4
print(dict)
# 딕셔너리 값 삭제 = 리스트 삭제법과 같음
del(dict['one'])
print(dict)


# 삭제의 또다른 방법으로는 pop함수를 사용할 수 있음 
print(list.pop(0))     # 0번째에 있는 값을 지우라는 함수
#pop의 특징은 값을 지우면서 지운 값을 return해준다
print(list)

print(dict)
print(dict.pop('two'))
print(dict)