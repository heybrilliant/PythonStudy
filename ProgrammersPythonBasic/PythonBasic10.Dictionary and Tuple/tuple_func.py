#2021.11.08 Progrmmers Python Basic <튜플을 이용한 함수의 리턴값>

list = [1,2,3,4,5]
for i, v in enumerate(list) :
    print('{}번째 값 : {}'.format(i,v))

# 튜플을 이용한 반복문 출력 
print('-----튜플 이용-----')
for a in enumerate(list) :
    print('{}번째 값 : {}'.format(a[0], a[1]))

# 튜플 앞에 *를 사용해주면 '쪼개라'라는 의미가 됨
print('-----*tuple 이용-----')
for a in enumerate(list) :
    print('{}번째 값 : {}'.format(*a))

print('-----딕셔너리 이용-----')
ages = {'Tod':35,'Jane':23,'Paul':62}
for key,val in ages.items():
    print('{}의 나이는 {}살 입니다'.format(key,val))

for a in ages.items():
    print('{}의 나이는 {}살 입니다'.format(*a))