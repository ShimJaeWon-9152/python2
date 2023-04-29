#문제 12번
alist = ['a','b','c']
blist = ['1','2','3']
abcd = []

for a,b in enumerate(zip(alist,blist)):
   print(a,b)
   try:
      abcd.append(b[a])
   except IndexError:
      abcd.append("ERROR")
print(abcd)

#문제 13번
alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a,b in zip(alist,blist):
   print(a,b)

#문제 14번
alphabet = ['a','b','c','d','e','f','g','h']
nums = [i for i in range(20)]
answer = [alpha + str(num) for alpha in alphabet for num in nums if num%2 ==0]

print(answer)
print(len(answer))

#문제 15번 틀림 - 물어볼것
url = 'cs50.gachon.ac.kr'
university_name = 'Gachon University'
gachon_info = [(i +" "+j) for i,j in zip(university_name.split(" "),url.split("."))
blank = -2;
print(gachon_info[blank])

#람다 함수 
f = lambda x,y : x + y
print(f(1,4))

f = lambda x : x **2
print(f(3))

f = lambda x: x/2
print(f(3))

#map() 함수
ex = [1,2,3,4,5]
f = lambda x : x **2
print(list(map(f,ex)))