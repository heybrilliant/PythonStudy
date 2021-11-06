#2021.11.06 Progrmmers Python Basic <딕셔너리 Dictionary>

# 딕셔너리 : 여러 값을 저장해두고 필요한 값을 꺼내쓰는 기능

wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
    }
print(wintable['가위']) # -> 보 라고 출력 
# wintable은 각 가위 바위 보 게임에서 승리 조건을 담은 테이블 = 즉 딕셔너리임
# 이름표를 이용하여 값을 꺼내 사용 => '이름표':'값'
# 리스트에서 값을 가져오는 문법과 비슷하다


def rsp(mine,yours):
    if mine == yours :
        return 'draw'
    elif wintable[mine] == yours : 
        return 'win'
    else :
        return 'lose'
result = rsp('가위','바위')

messages = {
    'win':'이겼다!!',
    'draw':'비겼다',
    'lose':'졌어...'
}

print(messages[result])

# -------------------


# 딕셔너리의 이름표에는 문자열과 숫자형, 튜플을 사용할 수 있으며, 값으로는 어떤 자료형이 오던 상관 없습니다. 
#↓ 이름표는 문자열 또는 숫자를 주로 사용하지만
dict = {     "이름표"    :    [1,2,3] }
#                           ↑ 값은 리스트를 포함해서 무엇이든 올 수 있습니다.

print( dict["이름표"] )