#2021.10.26 Progrmmers Python Basic <format>

# 인사로봇
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

# 지금까지는 print함수를 이용해서 출력할 변수를 하나씩 넣는 방법으로 출력했음

# old way
print(number, '번 손님', greeting, '.', place, '에 오신 것을 ', welcome, '!')

# new way
base ='{}번 손님, {}. {}에 오신 것을 {}!'
new_way = base.format(number, greeting, place, welcome)
# 대괄호를 열어 쌍을 만들어 변수가 순서대로 입력, 출력됨

print(base)
print(new_way)
# .format = base에 속해있는 값, 역할은 base의 {}를 다른 값으로 바꿔주는 역할

# 다른 코드도 작성해보자!

mine = '가위'
yours = '바위'
result = '졌다ㅠㅠ'

print('나는 {}, 너는 {}, 그래서 {}'.format(mine, yours, result))
# 주의할 점! 대괄호의 개수가 맞지 않을때
# 괄호 > 변수 -> 에러발생
# 괄호 < 변수 -> 정상작동