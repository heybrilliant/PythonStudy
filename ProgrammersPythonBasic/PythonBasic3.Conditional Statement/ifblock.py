#2021.10.23 Progrmmers Python Basic <블럭>

if True : 
        print('블럭에 속한 코드')
        
        if False :
            print('한 줄 더')
        
        if True :   
            print('또 한 줄 더')

            if True :
                print('블럭 하나 더')
        
        print('블럭의 끝 코드')

print('블럭 끝')

# 블럭 : 조건문에서 조건식 콜론 뒤에 나오는 코드 덩어리 
# 1. 블럭은 항상 콜론 뒤에서 들여쓰기와 함께 나타남
# 2. 여러 줄의 블럭일 때는 항상 모든 블럭에 들여쓰기를 해줘야한다 
#   -> 들여쓰기가 어긋나면 문법 오류 발생
# 3. 블럭을 마칠 땐 내어쓰기를 해줌 = 블럭이 끝남 
# 3-1. 한 번 끝난 블럭은 다시 열 수 없다
# 4. 블럭 내부에 또 다른 블럭이 위치할 수 있다
# 5. 내부 블럭은 외부 블럭에 종속적이다(포함되어 있다)
# 종속적의 예시 
# 첫 블럭이 False 이므로 내부 코드는 하나도 실행되지 않고 맨 끝블럭인 '2블럭 끝'만 print된다
# 파이썬 코드 전체를 하나의 블럭으로 볼 수 있다

if False : 
        print('2블럭에 속한 코드')
        
        if False :
            print('한 줄 더')
        
        if True :   
            print('또 한 줄 더')
        
        print('2블럭의 끝 코드')

print('2블럭 끝')

# 종속성 예시2
if False : 
    print('조건이 안 맞는 코드')

    if True :
        print('조건이 맞는 코드')
    
    print('어쨌든 실행되지 않는 코드')

print('다시 바깥에 있는 코드')