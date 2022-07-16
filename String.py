# 여러 줄의 문자열을 변수에 대입하기
multiline = '''Hello, I'm YuJung
Nice to meet you!
How are you?'''
print(multiline)
print()

multiline = "Hello, I'm YuJung\nNice to meet you!\nHow are you?"
print(multiline)

# 문자열 더하기 / 곱하기 / 길이
a = 'Python'
b = 'Practice'
print(a + b)
print(a * 2)
print(len(a), len(b))

# 인덱싱
c = 'my cat is too cute'
print(c[0], c[1], c[-1])

# 슬라이싱 기법 : a[시작 번호:끝 번호]를 지정할 때 끝 번호에 해당하는 것은 포함하지 않음
print(c[0:3], c[3:6])
print(c[0:], '/', c[:2], '/', c[:])

# 문자열 포맷팅
number = 3
d = '현재 온도는 %d 입니다.' % number
print(d)

food = '사과'
e = '나는 오늘 %s를 먹었다.' % food
print(e)

f = '나는 %d일전에 %s를 먹었다' % (3, '사과')
print(f)

g = 'I have %s apples' % 3
print(g)  # %s는 자동으로 %뒤에 있는 값을 문자열로 변환해준다.

h = '다운로드 %d%% 완료되었습니다.' % 99
print(h)

# 포맷코드와 숫자 함께 사용하기
i = '%10s 앞에 공백이 생긴다.' % '반가워'
print(i)

j = '%-10s 앞에 공백이 생긴다.' % '반가워'
print(j)

# 소수점 표현하기
k = '%0.4f' % 3.14134234
print(k)
k = '{0:10.4f}'.format(3.14134234)
print(k)

# format 함수를 사용한 포매팅
l = '나는 사과를 {0}개 먹었다'.format(3)
print(l)

m = '나는 {0}일전에 {1}를 먹었다'.format(3, '사과')
print(m)

n = '나는 {day}일전에 {food}를 먹었다'.format(day=3, food='사과')
print(n)

# 정렬
o = '{0:<10}'.format('hi') # 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있음
print(o)

p = '{0:>10}'.format('hi') # 치환되는 문자열을 오른쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있음
print(p)

q = '{0:^10}'.format('hi') # 치환되는 문자열을 가운데 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있음
print(q)

# 공백 채우기
r = '{0:=^10}'.format('hi')
print(r)

# 문자열 포매팅
name = "천유정"
age = 29
s = f'안녕하세요 저의 이름은 {name}입니다. 저의 나이는 {age}살 입니다. 저는 내년이면 {age+1}살이 됩니다.'
print(s)

# 문자열 관련 함수
#  문자 개수 세기(count)
t = 'hobby'
print(t.count('b'))

#  위치 알려주기1 [처음으로 나온 위치 반환, 없으면 -1 반환]
print(t.find('y'), t.find('d'))
#  위치 알려주기2 [처음으로 나온 위치 반환, 없으면 오류]
print(t.index('y'))

# 문자열 삽입
u = ','.join(['a', 'b', 'c', 'd'])
print(u)

# 대문자 or 소문자로 변환
v = 'hello'
print(v.upper())
v = 'HELLO'
print(v.lower())

# 공백 지우기
w = '     python     '
print(w.lstrip()) # 왼쪽 공백 지우기
print(w.rstrip()) # 오른쪽 공백 지우기
print(w.strip())  # 양쪽 공백 지우기

# 문자열 바꾸기
x = 'I want to take a rest'
print(x.replace('want', 'don\'t want'))

# 문자열 나누기
y = x.split()
print(y)
