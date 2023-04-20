"""for a in [1,2,3,4,5]:
    print(a)

for b in [1,2,3,4,5]:
    print("SIM JAE WON")

for c in range(100): # 반복문을 많이 할때
    print(c)

for i in 'SIMJAEWON': # 문자열
    print(i)

for x in ['SIMJAEWON','LEEMIYEON','SIMMANSEOP']:
    print(x)

for y in range(1,10,2): # 증가
    print(y)

for z in range(10,1,-1): # 감소
    print(z)

i = 1
while i < 10:
    print(i)
    i=i+1

for i in range(10):
    if i == 5: break
    print(i)
print("끝")

for j in range(10):
    if j == 5: continue
    print(j)
    print("End")

for i in range(10):
    print(i)
else:
    print("END")

print("구구단 계산기") # 구구단 계산기
print("몇단을 볼것입니까?")
x=int(input())
print(x,"단을 보여주겠습니다")
for i in range(1,10):
    result= x * i
    print(result) 


sentence = "SIM JAE WON"
reverse_sentence = ''
for char in sentence:
    reverse_sentence = reverse_sentence + char 
    print(char)
    print(reverse_sentence)
print(reverse_sentence)

# 시발... 
import random
x=random.randrange(1,100)
print("숫자를 맞혀보세요. (1~100)")
y = int(input())

while (x != y):
    if (x > y):
        print("숫자가 작습니다")
        y = int(input())
    else :
        print("숫자가 큽니다.")
        y = int(input())
else :
    print("정답입니다.")


print("구구단 몇단을 검색할까요?")
x=1
while(x != 0):
    x= int(input())
    if x == 0: break
    else:
        for y in range(1,10):
            print((x),"*",(y),"=",(x*y)) 
        print("몇단을 입력할까요?")
print("구구단을 종료합니다")


korean = [49,80,20,100,80]
math = [43,60,85,30,90]
eng = [49,80,48,50,100]
hap_score=[korean,math,eng]
stu_score=[0,0,0,0,0]
i=0
for x in hap_score:
    for y in x:
        stu_score[i]+=y
        i+=1
    i=0
a,b,c,d,e = stu_score
stu_hap_score=[int(a/3),int(b/3),int(c/3),int(d/3),int(e/3)\]
print(stu_hap_score)


def calculator(N):
    if N % 2 == 0:
        result = 1
        for i in range(1, N):
            result = result * 1
    else:
        result = 0
        for i in range(1,N):
            result = result + i
    return result




fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)

num = ['12','34','56']
for i in num:
    i = int(i)
print(num)
"""
"""
number = ["1",2,3,float(4),str(5)]
if number[4] == 5:
    print(type(number[0]))
elif number[3] == 4:
    print(number[2:-1])


num = 0
i = 1

while i < 8:
    if i % 3 == 0: break
    i=i+1
    num = num+1
print(num)



result = 0
for i in range(5,-5,-2):
    if i < -3:
        result += 1
    else:
        result -= 1

print(result)




fir_value = 0
sec_value = 0
for i in range(1,10):
    if i == 5:
        continue
        fir_value = i
    if i == 10:
        break
        sec_value = i

print(fir_value + sec_value)


def work_status(task,worker,day):
    rest_task = task 
    for k in range(day):
        if rest_task > 0:
            rest_task = rest_task - worker
        elif rest_task <= 0:
            print("Task End")
    if rest_task > 0:
        print("Hire More Worker")

work_status(100,11,11)
work_status(100,1,10)
work_status(100,9,10)
work_status(100,10,10)


score_list = [5,10,15,20,25,30]

sum_of_score = 0
i = 0
while i < len(score_list):
    if i % 2 == 0:
        sum_of_score += score_list[i]
    i += 1

print(sum_of_score)

coupon = 0
money = 200000
coffee = 3500
while money > coffee:
    if coupon < 4:
        money = money - coffee
        coupon += 1
    else:
        money += 2800
        coupon = 0
print(money)
"""


#157P 13번
a = "369"
b = "639"


strike = 0
ball = 0


for number in a:
    if b.count(number) == a.count(number):
        if b.find(number) == a.find(number):
            strike += 1
        else:
            ball += 1
            

print("Strike:",strike,"ball:",ball)



"""
#157P 14번
list_data_a=[1,2]
list_data_b=[3,4]

for i in list_data_a:
    for j in list_data_b:
        result = i + j
print(result)

list_1 = [[1,2],[3],[4,5,6]]
a,b,c = list_1
list_2 = a + b + c

print(list_2)



"""