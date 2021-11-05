#2021.11.05 Progrmmers Python Basic <module 만들기-사용하기>

import mymodule # 모듈을 만들 py이름을 import해줌

selected = mymodule.random_rsp()
print(selected)
print('가위?', mymodule.SCISSOR == selected)
# 가위일 때는 True가 나오고 아닐 때는 False가 나온다

"""
!!! 주의점 !!!
이미 내장되어있는 모듈이 아닌 
내가 생성한 모듈을 사용하려면 
만든 모듈 파일과 그 모듈을 사용하는 파일이 
>> 같은 폴더 안에 들어있어야 함 <<
"""