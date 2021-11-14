#2021.11.13 Progrmmers Python Basic <논리연산 더 알아보기>

a = 10
if a<0 and 2**a >1000 and a%5==2 and round(a)==a:
    print("복잡한 식")
    # and가 모두 만족하는 식을 포함하기 때문에 a<0 부터 False가 되기때문에 만족하는 값이 없음
    # -> 논리식이 틀렸기 때문에 print 행이 출력되지 않음
    
def return_false():
    print("함수 return_false")
    return False

def return_true():
    print("함수 return_true")
    return True

print("테스트1")
a = return_false()
b = return_true()
if a and b:
    print(True)
else:
    print(False)
# False 출력

print("테스트2")
if return_false() and return_true():
    print("True")
else:
    print("False")
# 파이썬에서는 첫 번째 값을 실행하고 그 이후로 실행할 필요가 없으면 두 번째 값은 실행하지 않기 때문 = 단락 평가

dic = {"Key2":"Value1"}

if "Key1" in dic and dic["Key1"] == "Value1":
    print("Key1도 있고, 그 값은 Value1이네")
else:
    print("아니네")
# -> 이 코드는 단락 평가를 하지 않는다면 에러가 발생할 수 있는 코드
