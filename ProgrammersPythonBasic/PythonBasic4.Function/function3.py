#2021.10.25 Progrmmers Python Basic <매개변수>
# 매개변수 parameter: 함수를 정의할 때 사용하는 이름

def print_root(a, b, c) : 
    r1 = ( -b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = ( -b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1, r2))

# 한 번 더 구하려면 

x = 2
y = -6
z = -8

def print_sqrt(a, b, c) :
    r1 = ( -b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = ( -b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1, r2))

print_sqrt(x, y, z)

x = 2
y = -6
z = -8

# 이 때 ()안에 넣어준 x,y,z를 실행인자라고 함
# 실행인자 argument : 함수를 실행할 때 넘기는 변수, 값
# 매개변수와 실행인자의 개수는 일치해야하며 여러 개일 때는 쉼표로 구분한다


# round : 숫자를 반올림할 때 사용하는 함수 
def print_round(number) : 
    rounded = round(number)
    print(rounded)

print_round(4.6)
print_round(2.2)
print_round(3.8)
# 실행인자로 꼭 변수를 넣어줄 필요는 없음
