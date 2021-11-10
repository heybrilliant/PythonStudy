#2021.11.11 Progrmmers Python Basic <예외처리 - raise:예외를 직접 일으키는 법>

def rap(mine, yours):
    #가위바위보 승패를 판단하는 코드
    allowed =['가위','바위','보']
    if mine not in allowed : 
        raise ValueError # allowed에 속하지 않는 값이 나왔을 때 valueerror를 발생시킴
    if yours not in allowed :
        raise ValueError

try : 
    rap('가위','바') #ValueError 발생 
except ValueError: 
    print('잘못된 입력값입니다.')


school = {'1반' : [172,185,198,177,165,199], '2반':[165,177,167,180,191]}
# school은 반의 학생 키를 가진 리스트이고 만약 190이 넘는 학생이 있는 반이 있다면 반이름을 출력하는 코드를 작성한다면 
for class_number, students in school.items():
    for student in students:
        if student>190:
            print(class_number,'반에 190을 넘는 학생이 있습니다.')
            break

# 이때 만약 한 반만 출력시키고 바로 종료하고 싶다면

try: 
    for class_number, students in school.items():
        for student in students:
            if student>190:
                print(class_number,'반에 190을 넘는 학생이 있습니다.')
                raise StopIteration # 예외 발생
except StopIteration :
    print('출력 후 정상종료')

# 대신 예외 발생을 많이 사용하면 코드를 읽기 어려워지기 때문에 꼭 필요한 경우에만 사용하는 것이 좋다