my_name = '은경' 
# 문자열 : 사람을 위한 텍스트를 프로그래머가 부르는 방법, 항상 따옴표를 붙여 구분

my_age = 30
# 숫자 : 사람과 컴퓨터가 모두 이해 가능, 따옴표 붙이지 않음

print(my_name, '이는 이제 ', my_age, '살')

# 파이썬은 텍스트보다는 숫자를 더 유용하게 다룸

my_next_age = my_age + 1
print('내년에는 ',my_next_age,'살!' )
# my_age가 텍스트였다면 오류가 생겼을 것

# 파이썬에서 쓰이는 사칙연산 기호 
add = 1 + 2 + 3             # 더하기
subtraction = 2021 - 1992   # 빼기 
multiply = 2 * 3            # 곱하기
devide = 30 / 5             # 나누기
power = 2 ** 10             # 제곱 (2의 10승 = 1024)
reminder = 15 % 4           # 나머지 (15 % 4 = 3)

print(multiply, devide, power, reminder)

# 문자열 더하기와 숫자 더하기 
text = '2021'+'1020'
number = 2021 + 1020

print(text) # 20211020 출력 = 문자열을 붙여서 새 문자열 출력 
print(number) # 3041 출력