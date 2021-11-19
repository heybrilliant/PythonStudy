#2021.11.19 Progrmmers Python Basic <Slice>

list = [1,2,3,4,5]
print(list[1]) # 2 출력 

text = "hello world"
print(text[1]) # e 출력

# 여러값을 한 번에 가져올 수 있는 방법이 있음
# slice = list의 일부분을 썰어서 가져온다해서 slice

# 만약 text의 ello를 가져오고 싶다면?
print(text[1:5]) # text의 인덱스1부터 인덱스5 >전< 까지의 값을 가져와라

list = ['영','일','이','삼','사','오']
print(list[1:3]) #list의 인덱스 1부터 인덱스 3 전의 값을 가져와라 = ['일','이'] 출력

# 리스트와 스트링은 slice 하는 방법이 같음 
# slice하고 나면 slice된 새로운 리스트나 스트링이 만들어짐

print(list[0:2])
print(list[2:len(list)]) # 리스트의 인덱스 2번째 값부터 리스트의 끝 값까지 가져오려 할때 len(list) 사용

print(list[:2]) #['영', '일']
print(list[2:]) #['이', '삼', '사', '오']
print(list[:]) #['영', '일', '이', '삼', '사', '오']