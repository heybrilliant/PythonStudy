#2021.10.25 Progrmmers Python Basic <함수의 값2>
# return의 기능 : return을 이용해 값을 돌려줄 수 있다

def root(a, b, c) : 
    r1 = ( -b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = ( -b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2

# return값이 여러개라면 쉼표로 구분

x = 2
y = -6
z = -8

r1, r2 = root(x, y, z)
print('근은 {}, {}'.format(r1, r2))

