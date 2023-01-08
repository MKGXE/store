# 입력과 출력   print
# 변수와 자료형

# 출력
print('반갑다 파이썬')

# 변수 : 저장공간
# = 대입연산자를 이용
변수1 = '파이썬'
print('반갑다',변수1)

# 입력  input
변수2 = input('입력할 값을 적으세요>>')
# 사용자가 입력한 값이 변수2 공간에 저장이 되었음
print('내가 입력한 값',변수2)

# 자료형  (type)
# str : 문자열  (글자)
# int : 정수  (소수점없는숫자)
# float : 실수  (소수점있는숫자)

# 자료 형태를 변환
int('123')      # 문자열 -> 정수
int(3.14)       # 실수 -> 정수

str(123)        # 정수 -> 문자열
str(3.14)       # 실수 -> 문자열

float('3.14')   # 문자열 -> 실수
float(314)      # 정수 -> 실수

# 연산자
# +, -, *, /, %
# =
# ==, !=, >, <, >=, <=
# and, or, not
# +=, -=, *=, /=, %=

# 대입연산자 =
숫자1 = '314'       # 314 값을 숫자1이라는 공간에 담는다
숫자1 = 숫자1 + 3    # 317
숫자1 += 3          # 320    누적 연산
숫자1 + 3           # 얘는 숫자1에 저장 안됨