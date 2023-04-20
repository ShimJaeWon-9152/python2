"""
# 1번
a = 11
b = 9

print('a'+'b')

#2번
fact = "Python is funny"

print(str(fact.count('n')+fact.find('n')+fact.rfind('n')))

#3번
text = 'Gachon CS50 - programing with python'
text2 = " Human cs50 knowledge belongs to the world "

text.lower()

print(text[:5] + text[-1] + text[6] + text2.split()[0])
print(text[-1])
print(text2.split()[1])

#4번
class_name = 'introduction programming with python'

for i in class_name:
    if i == 'python':
        i = i.upper()
print(class_name)

#5번
a = '10'
b = '5-2'.split('-')[1]

print(a * 3 + b)

#6번
name = "hanbit"
a = name.find('h')
b = name.count('h') * 4
c = len(name) * 2 + 4
print("REMEMBER",str(a)+str(b)+str(c))

#7번
a='abcd e f g'
b=a.split()
c=(a[:3][0])
d=(b[:3][0][0])

print(c+d)


#8번
number = 10
day = 'three'

print("I eat {0} orange every {1} days".format(number,day))

#9번
result = "CODE2018"
print("{0},{1}".format(result[-1],result[-2]))

#10번

str_a = "this is"
str_b = "Python"
print(str_a.title()+" "+str_b.upper())
"""


