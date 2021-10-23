#2021.10.23 Progrmmers Python Basic <if else>
# if else문을 이용한 가위바위보 게임 만들기 

# if-else 문 : if의 조건이 맞지 않는 경우 항상 실행
"""
 if True : 
     pass -> 조건이 참일 때 실행 
 else : 
     pass -> 조건이 거짓일 때 실행
"""
# else는 반드시 if 뒤에 나와야함, 혼자서 쓸 수 없는 문법

scissor = '가위'
rock = '바위'
paper = '보'

win = '이겼다!'
draw = '비겼다..'
lose = '졌다ㅠㅠ'

mine = '가위'
yours = '바위'

if mine == yours :
    result = draw
else : 
    if mine == scissor :
        if yours == rock :
            result = lose
        else :
            result = win
    else :
        if mine == rock :
            if yours == paper :
                result = lose
            else :
                result = win
        else :
            if mine == paper :
                if yours == scissor : 
                    result = lose 
                else :
                    result = win
            else : 
                print ('값이 이상해요')
print(result)

# 코드에 개선점이 있음 == 코드가 작성자의 의도를 더 잘 반영하게 개선할 수 있음

# else와 if가 각각 하나의 블럭으로 처리되어 들여쓰기가 다르게 들어감 

# elif 문법 
"""
 if True : 
     pass -> 조건이 참일 때 실행 
 else : 
     pass -> 조건이 거짓일 때 실행

일때 elif문으로 치환시키면 

 if :
     <다른 코드>
 elif ... : 
     <코드>

로 변환 가능함
"""
if mine == yours :
    result = draw
else : 
    if mine == scissor :
        if yours == rock :
            result = lose
        else :
            result = win
    elif mine == rock :
        if yours == paper :
            result = lose
        else :
            result = win
    elif mine == paper :
        if yours == scissor : 
            result = lose 
        else :
            result = win
    else : 
        print ('값이 이상해요')
print(result)

"""
<else와 elif>
if True :
    pass #조건이 참일 때 실행
elif False :
    pass #다른 조건이 참일 때 실행
else : 
    pass #조건이 거짓일 때 실행
"""