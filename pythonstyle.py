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
cat_song = "my cat has blue eyes, my cat is cute"
print(cat_song.split())
print({i:j for j,i in enumerate(cat_song.split())})