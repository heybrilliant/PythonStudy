#2021.11.08 Progrmmers Python Basic <튜플 만들기>
# packing : 튜플을 이용해서 하나의 변수에 여러 개의 변수를 대입할 수 있는 것
# unpacking : packing된 변수에서 여러 개의 값을 꺼내오는 것 

a, b = 1, 2
print(a) # 1 출력 
print(b) # 2 출력

# a,b를 선언 => 튜플 생성 & 1, 2를 선언 => 튜플 생성
# 튜플 하나에 하나가 대응되는 것

c = (3,4)
print(c)
d, e = c 
print(d) # 3 출력  
print(e) # 4 출력
# c의 값을 unpacking해서 d와 e에 대입 

f = d, e
# 변수 d와 e를 변수f에 packing 함
print(f) # (3, 4) 출력

# 튜플을 이용하면 두 변수 간의 값을 바꾸는 걸 쉽게 할 수 있다(임시변수가 필요 없다)
x = 5 , y = 10
x, y = y, x
print(x)
print(y)

# 튜플을 활용하면 함수의 리턴 값으로 여러 값을 전달할 수 있다
def tuple_func():
    return 1, 2

q, w = tuple_func()
print(q)
print(w)