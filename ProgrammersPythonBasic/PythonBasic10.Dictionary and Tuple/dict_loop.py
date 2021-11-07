#2021.11.07 Progrmmers Python Basic <딕셔너리와 반복문>

# 일반 반복문
seasons =['봄','여름','가을','겨울']

for season in seasons : 
    print(season)

ages = {'Tod':35,'Jane':23,'Paul':62}
print(ages)

# 딕셔너리에서 반복문을 사용할 때에는 경우에 따라서 키를 가져올 수도 값을 가져올 수도 있음
# Tod, Jane, Paul : Key
# 35, 23, 62 : 값

for key in ages.keys():
    print(key)
# Tod, Jane, Paul의 key값이 불러와짐

for value in ages.values():
    print(value)
# 35, 23, 62의 값이 불러와짐

for key in ages.keys():
    print('{}의 나이는 {}살 입니다.'.format(key,ages[key]))
# ages.keys()에서 keys()는 생략 가능하다

# key와 value 값을 동시에 읽어오려면 .items()를 사용 
for key,value in ages.items():
    print('{}의 나이는 {}살 입니다.'.format(key,value))

# 딕셔너리에서는 리스트처럼 값의 순서를 지켜주지 않는다
# 모두 한 번 씩만 호출되는 건 보장되지만 순서를 지켜주지 않는다
# 그래서 혹시 순서가 중요한 경우라면 list를 쓰는 것을 추천한다