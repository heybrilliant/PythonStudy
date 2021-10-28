#2021.10.28 Progrmmers Python Basic <따옴표(quote)>

# 파이썬에서 따옴표의 역할 : 문자열(String)을 만드는 것

string1 = 'Some text'
string2 = "어떤 텍스트"
string3 = '{}도 {}도 지금 이것도 문자열'.format(string1, string2)

print(string1, string2, string3)

quote = '문법 검사기 : "직접 인용은 큰 따옴표 사용!!!"'
emphasize = "'작은 따옴표'는 인용"
# error = "큰(작은) 따옴표 안에 "큰(작은) 따옴표" 사용하면 에러나요!"

"""
long_string = '여러줄이 들어가는 긴 문자열은 
파이썬에서는 문법 오류가 됩니다 
파이썬의 문자열은 첫째줄에서 끝나길 원합니다'

긴 문자열은
"""
long_string = '''이렇게 작은 따옴표 3개를 
이어쓰면 됩니다 긴 문자열 표현'''

print(long_string)

quote1 = "가끔은 '와 "+ '"를 모두 쓰기도 해'
quote2 = """가끔은 '와 "를 모두 쓰기도 해"""

print(quote1)
print(quote2)

# error = "'"이런건 안돼요'"'