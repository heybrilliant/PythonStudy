#2021.10.21 Progrmmers Python Basic <조건문>

people = 3
apple = 20

# (1)if 조건문의 시작 : if
# (2)실행 여부를 결정하는 조건 
# (3)조건식 끝에 콜론 기호 
# (4)들여쓰기(tab키 or 4칸 들여쓰기)
# (5)조건(2)이 참이면 실행할 코드

if people < apple / 5 :
    print('신나는 사과 파티! 배터지게 먹자!')

if apple % people > 0 :
    print('사과 수가 맞지 않아! 몇 개는 쪼개먹자!')

if people > apple :
    print('사람이 너무 많아! 몇 명은...')
#  조건식 : people > apple 

# 실행흐름 : 조건식이 참일 때 코드1 실행 / 조건식이 참이 아니면 실행하지 않음 or 코드2 실행 


#2021.10.22 Progrmmers Python Basic <조건식>
# 비교 : > , < , >= , =< , ==(같다), !=(다르다)
# 비교 결과 : True, False (조건식에 사용 가능)
# boolean 조건 : and(두 조건 모두 참이어야 참), or(두 조건 중 하나라도 참이면 참), not(조건 뒤집기 위해 사용, True -> False, False -> True)