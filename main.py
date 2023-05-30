"""
import fah_converter

print("Enter a celsius value:")
celsius = float(input())
fahrenheit = fah_converter.covert_c_to_f(celsius)
print("That's", fahrenheit,"degress Fahrenheit")
"""

#예제2 - 네임스페이스 as 사용
"""
import fah_converter as fah
print(fah.covert_c_to_f(41.6))
"""

#예제3 - 네임스페이스 From 모듈명 import 함수명
"""
from fah_converter import covert_c_to_f
print(covert_c_to_f(41.6))
"""

#예제4 - *로 호출
"""
from fah_converter import *
print(covert_c_to_f(41.6))
"""

#예제5 - random 모듈
"""
import random
print(random.randint(0,100))
print(random.random())
"""

#예제6 - time 모듈
"""
import time
print(time.localtime())
"""

#예제6 - urllib 모듈
"""
import urllib.request
response = urllib.request.urlopen("https://www.youtube.com/watch?v=250rS-RvwlU&list=UULPXcnRAydzstW5HehZYxtzzA&index=3&ab_channel=%E3%81%B5%E3%81%83%E3%81%8F%E3%81%97%E3%81%AE%E3%82%93%2Fphyxinon")
print(response.read())
"""

#연습문제 1번
"""
import sample as gc
gc.test()
"""

#연습문제 2번
"""
from calculator import sum_func, minus_func, devide_func, multiply_func 
user_input = input("사칙연산 프로그램:").split(" ")
first_val , second_val = int(user_input[0]),int(user_input[2])
fourcal = user_input[1]

if fourcal == "+":
  result = sum_func(first_val, second_val)

elif fourcal == "-":
  result = minus_func(first_val, second_val)

elif fourcal == "/":
  result = devide_func(first_val, second_val)

else:
  result = multiply_func(first_val, second_val)

print("실행 결과는", result)
"""

#연습문제 3번
"""
import quiz as q
q.quiz()
"""