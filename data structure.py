"""
#예제 1번
word = input("Input a word")
world_list = list(word)
print(world_list)

result = []
for _ in range(len(world_list)):
    result.append(world_list.pop())

print(result)
print(word[::-1])

a = [1,2,3,4,5]
a.append(10)
a.append(20)
print(a)
print(a.pop(0))
print(a.pop(1))


s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])

#합집합
print(s1.union(s2))
print(s1|s2)

#교집합
print(s1.intersection(s2))
print(s1&s2)

#차집합
print(s1.difference(s2))
print(s1-s2)

#dictionary

student_info = {}
student_info = {20140012:'Janhyeok',20140059:'Jiyong',20150234:'JaeHong',20140058:'Wonchul'}
print(student_info)
print(student_info[20140012])
student_info[20140049] = 'Wonchol'
print(student_info)

country_code = {}
country_code = {"America":1,"Korea":82,"China":30,"Japan":40}
print(country_code.keys())

country_code["Russia"] = 89
print(country_code)
print(country_code.values())
print(country_code.items())

for k, v in country_code.items():
    print(k)
    print(v)

print("Korea" in country_code.keys())
print(79 in country_code.values())


#collection - 파이썬의 내장 자료구조
from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)

print(deque_list)
deque_list.pop()
print(deque_list)
deque_list.pop()
print(deque_list)
print(deque_list)


from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.appendleft(i)

print(deque_list)
deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)
deque_list.reverse()
print(deque_list)
deque_list.extend([5,6,7])
print(deque_list)
deque_list.extendleft([5,6,7])
print(deque_list)
deque_list.extendleft([1,2,3])
print(deque_list)
"""

#orderedDict

def sort_by_key(t):
    return t[0]

from collections import OrderedDict

d = dict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in OrderedDict(sorted(d.items(), key = sort_by_key)).items():
    print(k,v)

