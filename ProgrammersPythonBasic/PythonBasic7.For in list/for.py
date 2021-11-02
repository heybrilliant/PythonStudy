#2021.11.02 Progrmmers Python Basic <for 반복문>

# for in 반복문
# 코드를 필요한만큼 반복해서 실행
# 1.리스트 patterns의 값을 하나씩 꺼내 pattern으로 전달
# 2.리스트의 길이만큼 print (pattern) 실행

patterns = ['가위', '바위', '보', '가위', '바위', '보', '가위', '바위', '보']
# patterns에 든 값이 모두 한 번씩 출력됨
for pattern in patterns :
    print(pattern)

# pattern이라는 변수는 어디서 온걸까?
"""
Python에는 대입하지 않고도 생겨나는 변수이름이 가끔 있음
지금에서의 pattern은 for문이 만들어낸 새로운 변수이고 
그 값은 for문에 딸린 블럭을 실행하기 전에
매번 patterns에서 값을 하나씩 꺼내서 순서대로 대입하고 실행하는 것과 같음
"""

# for in 의 이점??
# 가장 큰 장점은 in list의 크기에 관계없이 항상 모든 list에 대해서 실행할 수 있다는 것