#2021.11.05 Progrmmers Python Basic <module 만들기>

def random_rsp() :
    # 무작위로 가위바위보를 낸다
    import random
    return random.choice(['가위', '바위', '보'])

# 이렇게 선언하면 random_rsp가 담긴 모듈이 된다

# 변수 추가 또는 저장은 똑같이 해주면 된다 
PAPER = '보'
SCISSOR = '가위'
ROCK = '바위'