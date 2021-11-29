#2021.11.29 Progrmmers Python Basic <클래스 만들기>

# 클래스 선언
class Human():
    '''사람에 대한 클래스'''

# 인스턴스 생성 
person1 = Human()
person2 = Human()

a = list()
print(a)

print(isinstance(a, list)) #True 출력

person1.language = '한국어'
person2.language = 'English'

print(person1.language) # 한국어 출력
print(person2.language) # English 출력

person1.name = '서울시민'
person2.name = '인도인'

# 클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 이해하기 쉽게 포장할 수 있다. = 보기가 좋다 
# 클래스를 정의하면 값 뿐만 아니라 행동 등도 클래스에 넣어 사용할 수 있음 

def speak(person) : 
    print("{}이 {}로 말을 합니다. ".format(person.name, person.language))

speak(person1) #서울시민이 한국어로 말을 합니다.
speak(person2) #인도인이 English로 말을 합니다.

Human.speak = speak # Human class는 말할 수 있는 능력이 생긴것임 

person1.speak()
person2.speak()