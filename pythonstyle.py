"""
#enumerate()

for i, v in enumerate(['tic','tac','toe']):
    print(i,v)


#zip() 함수

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a,b in zip(alist,blist):
    print(a,b)
"""

#zip() 예제 2번
"""
a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)
k = [sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
print(k)
"""

#예제 3번
"""
alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for i, (a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)
"""

#연습문제 1번
"""
mylist = ['apple', 'banana','grape']
result = list(enumerate(mylist))
print(result)
"""

#연습문제 2번
"""
cat_song = "my cat has blue eyes, my cat is cute"
print(cat_song.split())
print({i:j for j,i in enumerate(cat_song.split())})
for j,i in enumerate(cat_song.split()):
    print(j)
    print(i)
"""

#연습문제 3번
"""
colors = ['orange','pink','brown','black','white']
result = '&'.join(colors)
print(result)
"""

#연습문제 4번
"""
user_dict = {}
user_list = ["student","superuser","professor","employee"]
for value_1,value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)
"""

#문제 5번
"""
result1 = [i for i in range(10) if i%2 == 0]
print(result1)

items = 'zero one two three'.split("two")
result1 = [i for i in range(10)]
print(result1)

items = 'zero one two three'.split()
print(items)

example = 'cs50.gachon.edu'
subdomain,domain,tld = example.split('.')
print(subdomain)
"""

#문제 6번
"""
animal = ['fox','dog','cat','monkey','hores','panda','owl']
print([ani for ani in animal if 'o' not in ani])
"""

#문제 7번
"""
name = "Hanbit University"
student = ["Hong","Gil","Dong"]
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:]+split_name[1])
"""

#문제 8번

"""
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
mid_score = [kor_score,math_score,eng_score]
print(mid_score[0][2])
"""

#문제 9번 
"""
a = [1,2,3]
b = [4,5, ]
c = [7,8,9]
print([[sum(k),len(k)]for k in zip(a,b,c)])
for k in zip(a,b,c):
    print(k)
"""

#문제 10번
"""
week  = ['mon','tue','wed','thu','fri','sat','sun']
rainbow = ['red','orange','yellow','green','blue','navy','purple']
list_data = [week, rainbow]

print(list_data[1][2])
"""

# 제네레이터의 사용
"""
ex = [1,2,3,4,5]
f = lambda x : x + 5
for value in list(map(f,ex)):
    print(value)
"""

# 리스트 컴프리헨션
"""
ex = [1,2,3,4,5]
i = [x ** 2 for x in ex]
print(i)
"""

# 한개 이상의 시퀸스 자료형 데이터의 처리
"""
ex = [1,2,3,4,5]
f = lambda x,y:x+y
print(list(map(f,ex,ex)))
"""

# 필터링 기능
# - MAP() 함수는 리스트 컴프리헨션처럼 필터링 기능을 사용가능 리스트 컴프리헨션과 달리 else문을 반드시 작성
"""
ex = [1,2,3,4,5]
i = list(map(lambda x:x **2 if x % 2 == 0 else x, ex))
print(i)
"""

#reduce 함수
"""
from functools import reduce
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))
"""

#별표의 사용
"""
def asterisk_test(a,*args):
    print(a,args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)
"""

#키워드 가변 인수
"""
def asterisk_test(a,*kargs):
    print(a,kargs)
    print(type(kargs))

asterisk_test(1,f=1,b=2,c=3,d=4,e=5)
"""

# 별표의 언패킹 기능
"""
def asterisk_test(a,kargs):
    print(a,*kargs)
    print(type(kargs))

asterisk_test(1,(1,2,3,4,5))
"""

# 별표의 언패킹 기능2

"""
def asterisk_test(a,*kargs):
    print(a,kargs)
    print(type(kargs))
asterisk_test(1,(1,2,3,4,5))
"""

# zip 함수를 함께 사용한 가변인수
"""
for data in zip(*[[1,2],[3,4],[5,6]]):
   print(data)
   print(type(data))


# zip 함수를 함께 사용한 가변인수

for data in zip(*[[1,2],[3,4],[5,6]]):
   print(data)
   print(type(data))
   
def asterisk_data(a,**args):
   print(a,args)
   
data = {"b":1,"c":2,"d":3}
asterisk_data(10,data)

#예제 1번문제
f = lambda x : x **2

#예제 2번문제
ex = [1,2,3,4,5]
value = lambda x : x **2
print(list(map(value,ex)))

#예제 3번 문제 몰?루
"""
"""
from functools import reduce

input_str = input("Enter a number: ")
digits = [int(d) for d in input_str]  # convert string to list of integers
product = reduce(lambda x, y: x * y, digits)
print(product)


#예제 4번 
def transpose_list (two_dimensional_list):
   return [row for row in zip(*two_dimensional_list)]
   
   
print(transpose_list([[1,4,6],[2,5,6],[3,6,8]]))

#예제 5번
date_info = {year : 2019, month : 9, day : 6}
result = year-month-day.format(**date_info)
print(result)
"""