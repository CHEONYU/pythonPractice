# list built-in function practice

# append : 리스트 끝에 원소를 추가
x = [1, 2, 3, 4]
print(x)
x.append([2, 3])
print('append result :', x)
print('----------------------------------')
x.clear()

# extend : 리스트 끝에 모든 원소를 추가
x = [1, 2, 3, 4]
print(x)
x.extend([2, 3])
print('extend result :', x)
print('----------------------------------')
x.clear()

# copy : 원본에 영향을 주지 않기 위해서 사용
x = [1, 2, 3, 4]
y = x
y.extend([2, 3])
print('x = y 후 y에 extend x:', x)
print('x = y 후 y에 extend y:', y)
print('----------------------------------')
x.clear()
x = [1, 2, 3, 4]
y = x.copy()
y.extend([2, 3])
print('x.copy 후 y에 extend x:', x)
print('x.copy 후 y에 extend x:', y)
print('----------------------------------')

# count : 리스트 안에 원소 a의 개수 반환
print('x에서 3원소의 개수 반환 :', x.count(3))
print('y에서 3원소의 개수 반환 :', y.count(3))
print('----------------------------------')

