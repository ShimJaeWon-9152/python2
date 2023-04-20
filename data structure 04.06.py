#dictionary - 사전
#defaultdict - dictionary에 변수를 생성할때 기본값으로 지정

#예제 1번
"""
from collections import defaultdict

d = defaultdict(lambda: 0)
print(d["first"])
"""

#예제 2번 
"""
from collections import defaultdict

s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
d = defaultdict(list)

for k, v in s:
    d[k].append(v)
    print(k)
    print(v)
print(d.items())

"""
#예제 3번 
"""
from collections import Counter

text = list("gallahad")
print(text)
c = Counter(text)
print(c)
print(c['a'])



#textmining.py
text = A press is the quickest and easiest way to get free publicity. if well written, a press release can result
in multiple published articles about your firm and its product.lower().split()


from collections import defaultdict

word_count = defaultdict(lambda:0)
for word in text:
    word_count[word] += 1

print(word_count)
"""


# 04월 10일

#문제 1번
"""
i = 3 ** 5
print(i)

j = 15 % 4
print(j)

k = 4
k -= 3
print(k)

a = {'prof.choi': 'The Best'}
print(type(a))
"""

#문제 2번
"""
list_1 = [0,3,1,7,5,0,5,8,0,4]
def quiz_2(list_data):
    a = set(list_data)
    print(a)
    return (list(a)[1:5])

print(quiz_2(list_1))
"""

#문제 3번
"""
country_code = {"America":1, "Korea":84, "China":86,"Japan":44}
print(country_code.values())
print(country_code)
print(country_code.keys())
print(85 in country_code.values())
print("Korea" in country_code.values())
"""

#문제 4번
"""
a = ""
midterm_set = set[(1,5,7,4,3,2,1,1,2,3)]
for i in midterm_set:
    
print(a)
"""


#문제 5번
"""
def delete_a_list_element(list_data, element_value):
    if element_value in list_data:
        list_data.remove(element_value)
        return list_data
    else:
        return "False"

list_data=['a',1,'gachon','2016.0']
element = float(2016)
result = delete_a_list_element(list_data,element)
print(result)
"""

#문제 6번
"""
def add_number(original_list):
    original_list += [1]
    print(original_list)
mylist = [1,2,3,4]
add_number(mylist)
print(set(mylist))
"""

#문제 7번
"""
a =[3,"apple",2016,4]
b = a.pop(0)
c = a.pop(1)
print(b+c) 
"""

#문제 8번
"""
def week_seven(sentence1):
    cells = set(sentence1.replace('','').lower())
    print(cells)
    return cells

setence_a = "The quick brown fox jump over the lazy dog"
setence_b = "I love you"
print(len(week_seven(setence_a)-week_seven(setence_b)))
"""
#문제 9번
"""
tuple_1=(1,2,3)
tuple_2=(4,5,6)

def quiz_1(data_1,data_2):
    result = []

    for i in (tuple_1 + tuple_2):
        result.append(i)
    return(result)

print(quiz_1(tuple_1,tuple_2))
"""

#문제 10번
"""
dict_1 = {2:1,4:2,6:3,8:4,10:5}

dict_key=list(dict_1.keys())
dict_values=list(dict_1.values())

dict_2 = dict()

for i in range(len(dict_key)):
    dict_2[dict_values[i]]=dict_key[i]

print(dict_2[2])
"""

#문제 11번
"""
animal = ['cat','snake','monkey','ant','spider',]
legs = [4,0,2,4,8]
animal_legs_dict = {}

for i in range(len(animal)):
    animal_legs_dict[legs[i]]=animal[i]
animal_legs_dict['ant'] = 6
print(animal_legs_dict)
"""

#문제 12번
"""
t = (1,2,3)

print(t + t)
print(t * 2)
print(t,t)
"""

#문제 13번
"""
Mydict = {'1':1,'2':2}
Copy = Mydict
Mydict['1'] = 5
print(Mydict)
print(Copy)
result = Mydict['1']+Copy['1']
print(result)
"""

#문제 14번
"""
sentence = list("You Love Me?")


sentence = list("You Love Me?")
result = ''
for i in range(len(sentence)):
    if i % 3 == 0:
        result += sentence.pop()
    else:
        result += sentence.pop(0)
print(result)
"""

#문제 15번
"""
number = [5,6,7,8,9,1,2,3,4]
result = []
result.append(number.pop(0))
result.append(number.pop())
result.append(number.pop(1))
result.append(number.pop())
result.append(number.pop(0))
print(number[0]+result[-1])
print(result[-1])
print(number)
"""

#문제 16번
"""
a = list(range(10))
a.append(a[3])
print(a)
a.pop(a[3])
print(a)
a.insert(3,a[-1]) # 3번째 자리에 a[-1]
print(a)
a.pop()

print(a)
"""

#문제 17번
"""
box = [1,'red',3,(),None]
print(len(box))
"""

#문제 18번
"""
data_1 = {'one' : (1,2,3,4,5,6), 'two':[1,2,3,4,5,6],'three':{'four':4,'five':5}}
for k in ['one','two','three']:
    
    try:
        print(data_1[k][:1])

    except TypeError:
        print("error")

for k in ['one','two','three']:
    
    try:
        data_1[k][-1] = "a"
        print(data_1[k][-1])
    except TypeError :
        print("error")
"""

#문제 20번
class_category = ["A","B","C","D"]
student_category = ["Sam","Sarah","Jane","John"]

class_student_cate = {}
for i in range(len(class_category)):
    class_student_cate[class_category[i]] = student_category[i]
print(class_student_cate)