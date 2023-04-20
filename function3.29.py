#예제 문제
"""
def f(x):
    return 2*x+7
def g(x):
    return x**2
x=2

print(f(x)+g(x)+f(g(x))+g(f(x)))

def print_something_2(my_name, your_name = "TEAM LAB"):
    print("Hello {0}, My name is {1}".format(my_name,your_name))

print_something_2("JaeWon","TEAM LAB")
print_something_2("JeeWon")

def asterisk_test(a,b,*arg):
    return a + b +sum(arg)

print(asterisk_test(1,2,3,4,5))


def asterisk_test_2(*args):
    x,y,*z = args
    return x,y,z

print(asterisk_test_2(3,4,5,10,20))


def kwargs_test(**kwargs):
    print(kwargs)
    print("First Value is {first}".format(**kwargs))
    print("Second Value is {second}".format(**kwargs))
    print("Third Value is {third}".format(**kwargs))

kwargs_test(first=3,second=2,third=3)


#연습문제

def test(t):
    t = 20
    print("In Function:",t)

x= 10 
print("Before:",x)
test(x)
print("After:",x)


def sotring_function(list_value):
    return list_value.soft()

print(sotring_function([5,4,3,2,1]))


number = "100"

def midtern(number):
    result = ""
    if number.isdigit() is True:
        if number == 100:
            if number / 10 == 1:
                result = True
    else:
        result = False
    
    return result


def is_yes(your_answer):
    if your_answer.upper() == "Yes" or your_answer.upper() == "Y":
        result = your_answer.lower()

print(is_yes("Yes"))

def add_and_mul(a,b,c):
    return b + a * c + b
print(add_and_mul(3,4,5)==63)


def args_test_3(one,two,*args, three):
    print(one+two+sum(args))
    print(args)

args_test_3(3,4,5,6,7)


def rain(colors):
    colors.append("purple")
    colors=["green","blue"]
    return colors

rainbow = ["red","orange"]
print(rain(rainbow))

def function(value):
    print(value ** 3)

print(function(2))

def ger_apple(fruit):
    fruit = list(fruit)
    
    fruit.append("e")
    
    fruit = ["apple"]
    
    return fruit

fruit = "appl"
ger_apple(fruit)
print(fruit)


def return_sectence(sectence,n):
    sectence += str(n)
    n -= 1 
    if n < 0:
        return sectence
    else:
        return return_sectence(sectence,n)
    
sectence = "I LOVE YOU"
print(return_sectence(sectence,5))


def test(x,y):
    tmp = x
    x = y
    y = tmp
    return y.append(x)

x = ["y"]
y = ["x"]
test(x,y)
print(y)


def countdown(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("0dd")
        countdown(n-1)
countdown(3)


def factorial_calculator(n):
    if n in (0,1):
        return 1
    else:
        return n * factorial_calculator(n-1)
print(factorial_calculator(5))

# 물어보기
def calculrate_rectangle_area(rectangle_x,rectangle_y):
    rectangle_x = 3
    rectangle_y = 5
    result = rectangle_x * rectangle_y
    return result


calculrate_rectangle_area(rectangle_x=3,rectangle_y=4)
print(calculrate_rectangle_area)


def exam_func():
    x = 10
    print("Value:",x)

x = 20
exam_func()
print("Value:",x)
"""

#물어보기
country =["Korea","Japan","China"]
country.append("Remove")

print(country.remove("Remove"))
