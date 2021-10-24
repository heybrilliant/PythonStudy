#2021.10.24 Progrmmers Python Basic <function1>

a = 1
b = 2
c = -8

# a * x^2 + b * x + c = 0, a != 0 인 x에 관한 2차방정식에 대해, 
# 근의 공식은 

r1 = ( -b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = ( -b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print('해는 {} 또는 {}'.format(r1, r2))

# 한 번 더 구하려면 

a = 2
b = -6
c = -8

r1 = ( -b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = ( -b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print('해는 {} 또는 {}'.format(r1, r2))

# 이렇게 한 번 더 써줘야함
# 편리성에서 떨어지기 때문에 [함수]라는 기능을 사용함 

# 함수
# 반복되는 기능들을 블럭으로 만들고 간단하게 반복적으로 사용 가능한 기능

def print_sqrt() :
    r1 = ( -b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = ( -b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1, r2))

# 이후 사용법

print_sqrt()

a = 2
b = -6
c = -8