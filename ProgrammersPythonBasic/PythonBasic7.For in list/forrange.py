#2021.11.03 Progrmmers Python Basic <for in range>

# 0,1,2,3,4를 순서대로 출력하려면?
for i in [0,1,2,3,4] : 
    print(i)

# 그렇다면 1부터 1000까지 출력하려면..?
# 1부터 1000까지 하나씩 입력한 큰 리스트를 출력하거나
# list 부분을 range라는 함수를 써서 바꿔줄 수 있음

for i2 in range(5): # ~= [0,1,2,3,4]
    print(i2)

names = ['철수', '영희', '바둑이', '흰둥이']

for i3 in range(4) : 
    name = names[i3]
    print('{}번 : {}'.format(i3+1, name))

    # i라고 쓰면 0번부터 출력이 되고, i+1이라고 쓰면 1부터 출력

# 만약 한 명이 더 들어온다면????

for i3 in range(len(names)) : 
    name = names[i3]
    print('{}번 : {}'.format(i3+1, name))
# 위 코드와 같이 len(names) 함수로 names의 길이를 측정하는 함수를 사용하면 리스트에 요소가 추가 혹은 제거되어도 숫자를 일일이 바꾸지 않아도 됨


# enumerate 함수 : 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
for i3, name in enumerate(names) :
    print('{}번 : {}'.format(i3 + 1, name))



# 가 출력 
print(chr(44032))

for i4 in range(11172) : 
    print(chr(44032 + i4), end='')
# 이러면 가 ~ 힣까지 총 11172개의 숫자가 연속 나열된다


# for in list : 순회할 리스트가 정해져 있을 때 
# for in range() : 순회할 횟수가 정해져 있을 때 
