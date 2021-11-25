#2021.11.24 Progrmmers Python Basic <자료형 다루기>

s = "Hello world"
print(type(s)) # <class 'str'> 출력
# type(변수)를 입력하면 어떤 자료형인지 출력됨
f = 3.14
print(type(f)) # <class 'float'> 출력
# float = 부동소수점
i = 42
print(type(i)) # <class 'int'> 출력
# int = 정수
print(42.0) # <class 'float'>
print(42 == 42.0) #True 출력


# isinstance(값, 자료형) = 자료형 검사
isinstance(42, int) # True 출력
isinstance(42, float) # False 출력
isinstance(42.0, float) # True 출력 
isinstance(42.0, int) # False 출력