# List 생성
odd = [1, 3, 5, 7, 9]
print(odd)

print(odd[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][0])

# 리스트의 슬라이싱 -> 문자열 슬라이싱과 완전하게 동일하다.
print(odd[0:2])

# 리스트 연산하기
# 리스트 더하기
b = [1, 2, 3]
c = [4, 5, 6]
print(b + c)

# 리스트 반복하기
print(b * 3)

# 리스트 길이 구하기
print(len(b))

# 리스트에서 값 수정하기
d = [1, 2, 3]
d[2] = 4
print(d)

# 리스트에서 값 삭제하기
del d[2]
print(d)

del d[0:2]
print(d)

# 리스트 관련 함수들
# 리스트에 요소 추가(append)
e = [1, 2, 3]
e.append(4)
print(e)

e.append([5, 6])
print(e)

# 리스트 정렬
f = [3, 1, 6, 8, 2]
f.sort()
print(f)

# 리스트 뒤집기
f.reverse()
print(f)

# 위치 반환
print(f.index(1))
# print(f.index(9)) 9는 없으므로 오류 발생

# 리스트에 요소 삽입(insert)
g = [1, 2, 3]
g.insert(0, 0)
print(g)

# 리스트 요소 제거(remove)
g.remove(1)
print(g)

# 리스트 요소 끄집어내기(pop)
h = [1, 2, 3, 1]
h.pop(1)
print(h)

# 리스트에 포함된 요소 x의 개수 세기(count)
print(h.count(1))

# 리스트 확장(extend)
i = [1, 2, 3]
i.extend([4, 5])
print(i)