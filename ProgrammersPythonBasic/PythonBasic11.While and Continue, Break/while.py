#2021.11.08 Progrmmers Python Basic <While 반복문>

selected = None
# None = 아무값도 들어있지 않다
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요 > ')

print('선택된 값은: ', selected)
# 가위, 바위, 보 중에 입력하면 입력된 문구와 선택한 값이 출력되면서 종료, 그 외의 값을 입력하면 다시 input에 입력된 문구가 계속해서 반복 출력