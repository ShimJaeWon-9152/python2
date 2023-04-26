#enumerate()
"""
for i, v in enumerate(['tic','tac','toe']):
    print(i,v)
"""

#zip() 함수
"""
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
week  = ['mon','tue','wed','thu','fri','sat','sun']
rainbow = ['red','orange','yellow','green','blue','navy','purple']
list_data = [week, rainbow]

print(list_data[1][2])