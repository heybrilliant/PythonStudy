#2021.10.29 Progrmmers Python Basic <정수와 실수>

five1 = 5
five2 = 5.0
five3 = 5.00000

print(five1)
print(five2)
print(five3)

five4 = 5 * 1
five5 = 5 * 1.0

print(five4)
print(five5)

# 나눗셈은 항상 값이 정수가 아닐 가능성이 크다 
# -> 정수 나누기 정수여도 소수점 자리를 표기
print(6/5) # 1.2
print(10/5) # 2.0

# 나머지 연산 
print(6%5)
print(10%5)

# 정수끼리 나누면 실수가 나올 수 있으나, 나눗셈의 몫만을 구하려면 //연산자를 이용

a = 6
b = 5
print(a == b * (a // b) +  (a % b))

# 파이썬에서는 [부동소수점]이라는 표현법을 이용해 소숫점을 표현
# 어느정도의 계산 정확도는 가지지만, 계산에 있어서 완벽한 정확성은 가지지 않는다.
print(0.1 + 0.1 == 0.2) #True
print(0.1 + 0.1 + 0.1 == 0.3) #True ?? -> False가 나올 때도 있음

print(int(5.0)) # 정수로
print(float(5)) # 부동소수점으로
print(5 * 1.0) # 부동소수점으로