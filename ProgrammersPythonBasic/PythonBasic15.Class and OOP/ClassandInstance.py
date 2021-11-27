#2021.11.27 Progrmmers Python Basic <인스턴스 이해>

numbers1 = []
print(type(numbers1))

numbers2 = list(range(10))
print(numbers2)
print(type(numbers2))

characters = list("hello")
print(characters)
print(type(characters))

# 모두 class 'list'라고 나옴 

print(isinstance(numbers1, list)) # True 출력
print(numbers1 == list) # False 출력

# 클래스 : 함수나 변수를 모아놓은 집합체
# 인스턴스 : 클래스에 의해 생성된 객체, 인스턴스는 각자 자신의 값을 가지고 있다