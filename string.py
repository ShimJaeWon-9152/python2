"""
title = "Blue PC Room"

# 대문자 변환
print(title.upper())

# 소문자 변환
print(title.lower())

# 문자열 갯수
print(len(title))

# 찾을 문자열이 몇개 있는지
print(title.count('o'))

# 찾을 문자열로 시작하는지
print(title.startswith('B'))

# 찾을 문자열로 끝나는지
print(title.endswith('m'))

print(1,2,3)
print("a"+ " " + "b" + " " + "c" )
print("%d %d %d" %(1,2,3))
print("{} {} {}".format("a","b","c"))

#format

print("%s %s" %("SIM","JAEWON"))
print("%d %d" %(1,3))

#format2

print("I eat %d apples" %(3))
print("I eat %s apples" %("five"))

#format3

number = 3
day = "three"

print("I ate %d apples. I was sick for %s day" %(number, day))

#format4

print("I'm {0} years old".format(20))

#format5
age = 26
name = "SIM JAE WON"
print("I'm {0} years old".format(age))
print("My name is {0}".format(name))
print("Product: {0}, Price per unit: {1:.2f}".format("apple",5.32))

#padding

print("%10d" %12)
print("%-10d" %12)

#padding2

print("%10.3f" %5.32412)
print("%10.2f" %5.32412)
print("%-10.3f" %5.32412)

#format, padding

print("{0:>10s}".format("Apple"))
print("{0:<10s}".format("Apple"))

#format, padding 2

print("{0},{1:10.5f}".format("apple",5.234))
"""