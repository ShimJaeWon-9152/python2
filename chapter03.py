#input
"""print("이름을 넣어주세요")
name=input()
print("Hi",name)"""

#한칸 띄우기
"""print("Hi 심재원", "Hi 심만섭")"""

"""print("온도를 입력하세요!")
temperature = float(input())"""

#input문을 사용하면 자료형은 문자형이 됨
"""temperature=float(input("온도를입력하세요: "))
print(temperature)"""

#화씨온도 변환기
"""print("본 프로그램은 섭씨 온도를 화씨온도로 변환하는 프로그램입니다.") 
print("변환하고 싶은 섭씨온도를 입력하세요!")
celsius=float(input())
fahrenheit=(float(celsius)*1.8)+32
print("섭씨온도:", celsius)
print("화씨온도:", fahrenheit)"""


"""color=['red','blue','green']
print(color[2])
print(color[1])
print(len(color))
#       0      1      2     3      4
city=['부산','서울','광주','대구','대전']
print(city[0:5])
print(city[3:])
print(city[-4:])
# 변수명[시작인덱스:마지막 인덱스:증가값] - ★ 자꾸 헷갈림
print(city[0:5:2])

color1=['red','blue','yellow']

print(len(color1))
print(color1*2)
print('blue' in color1) # in 하나의 값이 해당 리스트에 들어 있는지 확인하는거

color1.append('orange') # append - 맨뒤 인덱스 추가 하는거
print(color1)

color1.extend(['green','dark']) # extend - 새로운 배열 추가!
print(color1)

color1.insert(0,'gray') # insert - 배열에 삽입!
print(color1)

color1.remove('gray')
print(color1)"""

"""x=[1,2,3]
a,b,c=x
print(x,a,b,c)

kor_score=[49,79,20,100,80]
math_score=[43,59,45,11,18]
eng_score=[79,63,44,12,19]

select_score=[kor_score,math_score,eng_score]
print(select_score)
print(select_score[1][4])

a=100
b=100
print(a is b)
print(a==b)"""

"""
a=['color',1,0.2]
color=['black','white','gray']
a[0]=color
print(a)

a=[5,4,3,2,1]
b=[1,2,3,4,5]
b=a
print(b)
a.sort()
print(b)

a=[0,1,2,3,4,]
print(a[:3],a[:-3])

a=[0,1,2,3,4]
print(a[::-1])

first=["egg","salad","bread","soup","canafe"]
second=["fish","lamb","pork","beef","chicken"]
third=["apple","banana","orange","grape","mango"]

order=[first,second,third]
john=[order[0][:-2],second[1::3],third[0]]
del john[2]
john.extend([order[2][0:1]])
print(john)
"""

list_a=[3, 2, 1, 4]
list_a.sort()
list_b=list_a
print(list_a,list_b)

a=[5,7,3]
b=[3,9,1]
c=a+b
print(c) # 배열끼리 더하면 합쳐진다. 실수 하지말자
c.sort()
print(c)

fruits=['apple','banana','cherry','grape','orange','strawberry','mellon']
print(fruits[-3:],fruits[1::3]) 

a=[1,2,3,5]
b=['a','b','c','d','e']

a.append('g')
b.append(6)
print('g'in b, len(b))
