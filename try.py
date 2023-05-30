#예외 처리 
"""
for i in range(10):
  try:
    print(10/i)
  except ZeroDivisionError:
    print("0으로는 나눌 수 없다.")
"""

#예외 에러 메세지
"""
for i in range(10):
  try:
    print(10/i)
  except ZeroDivisionError as e:
    print(e)
    print("0으로는 나눌 수 없다.")
"""

#try - except - finally 문
"""
try:
  for i in range(1,10):
    result = 10 // i
    print(result)
except ZeroDivisionError:
  print("0으로는 나눌 수 없다.")
finally:
  print("끝!")
"""

#raise 문
"""
while True:
  value = input("숫자를 입력하시오!")
  for digit in value:
    if digit not in "0123456789":
      raise ValueError("숫자값을 입력하지 않았다.")
  print("정수값으로 변환된 숫자 -", int(value))
"""

#assert 문