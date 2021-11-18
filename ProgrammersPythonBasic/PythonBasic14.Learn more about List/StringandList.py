#2021.11.18 Progrmmers Python Basic <List와 문자열>

my_list = [1,2,3,4,5,6]
print(my_list[0]) # 1 출력 
print(my_list[1]) # 2 출력

str = "Hello World"
print(str[0]) # 첫 번째 글자 H 출력
print(str[1]) # 두 번째 글자 e 출력

print(3 in my_list) # True 출력 
print(9 in my_list) # False 출력

print("H" in str) # True 출력
print("z" in str) # False 출력

print(my_list.index(5)) # 5라는 숫자가 몇 번 인덱스에 있는지 알려줌 -> 4 출력 
print(str.index("r")) # r라는 문자가 몇 번 인덱스에 있는지 알려줌 -> 8 출력

# 이와 같이 String과 List는 유사점이 많고 왔다갔다 할 수 있음
# String을 List로 만들어보기 

characters = list("abcdef")
print(characters) # a,b,c,d,e,f가 들어있는 리스트를 생성해줌

words = "Hello world는 프로그래밍을 배우기에 아주 좋은 사이트 입니다."
words_list = words.split()
print(words_list)
# words_list에는 각 단어가 들어있는 리스트가 생성됨
# .split() : 괄호 안을 비워두면 공백을 기준으로 잘라서 리스트를 생성해줌

time_str = "10:35:27"
time_list = time_str.split(":")
print(time_list)

# 이 때 이렇게 string으로 이루어진 list를 다시 string으로 재변경할 수 있음 
":".join(time_list)
print(time_list)
" ".join(words_list)
