#2021.11.21 Progrmmers Python Basic <Slice로 List 수정하기>

numbers = list(range(10))
print(numbers)

del numbers[0] # numbers에서 0 값을 삭제함
print(numbers)

print(numbers[:5])
del numbers[:5] # 슬라이스를 이용해서 범위를 삭제할 수 있음
print(numbers) #[6, 7, 8, 9]

print(numbers[1:3]) # [7, 8]
numbers[1:3] = [77, 88]
print(numbers) # [6, 77, 88, 9] 출력 -> 7과 8이 77, 88로 변경된 걸 볼 수 있음
numbers[1:3] = [77, 88, 99] # 더 많은 개수로 변환 
print(numbers) # [6, 77, 88, 99, 9] 출력
numbers[1:4] = [ 8 ] # 더 적은 개수로 변환

# numbers[1:4] = 8 -> 타입에러 : 값을 변환해 줄 때도 list 형태로 입력하기