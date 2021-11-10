#2021.11.10 Progrmmers Python Basic <while문과 반복제어, break, continue>

# break
# : 반복문 내부에서 쓰면 반복문이 종료됨

list = [1,2,3,5,7,2,5,237,55]

for val in list :
    if val % 3 == 0:
        print(val)

# 이 때 값을 하나만 출력하고 싶은 조건을 걸게 된다면 조건문 아래에 break를 입력해준다 
# -> 조건문 혹은 반복문에서 break를 만나면 break가 속한 상위 블럭의 값을 한 번만 출력시키고 종료함

for val in list :
    if val % 3 == 0:
        print(val)
        break

# continue

# 1 ~ 10까지 숫자 중에 홀수를 4줄씩 출력하는 조건문을 생성해보자 
for i in range(10) : 
    if i % 2 != 0 : 
        print(i)
        print(i)
        print(i)
        print(i)

# 이 조건문을 continue를 이용한 코드로 수정해보자
for i in range(10) : 
    if i % 2 == 0 :
        continue
    # 짝수이면 반복문의 나머지 부분을 보지않고 반복문의 처음으로 돌아감
    print(i)
    print(i)
    print(i)
    print(i)

# continue를 쓰는 장점
# continue : 반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능
# 제외하는 기능을 첫 번째에 처리해줌 -> 핵심이 되는 블럭이 너무 깊이 들어가지 않도록 방지해줌