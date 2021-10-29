#2021.10.30 Progrmmers Python Basic <사용자 입력 받기>

# 프로그래밍의 3단계
# 사용자 입력 -> 자료 처리 -> 결과 출력

print('가위, 바위, 보 중 하나를 입력하세요 > ', end = ' ')
mine = input()
print('mine : ', mine)

# input : 사용자의 키보드 입력을 return
# round : 수의 반올림 값을 return

# end = ' ' 를 사용하면 같은 줄에서 입력받기 가능

# 또는 이렇게 입력받기가 가능

mine = input('가위, 바위, 보 중 하나를 입력하세요 > ')
print('mine : ', mine)

# ctrl + c : 프로그램 즉시 종료