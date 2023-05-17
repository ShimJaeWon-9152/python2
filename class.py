# 선수 등번호 표시 및 변경
"""
class SoccerPlayer:
    def __init__(self,name,position,back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    
    def Change_Numer(self,new_number):
        print("안득수 선수의 등번호가",int(new_number),"로 변경되었습니다.")
        self.back_number = new_number



a1 = SoccerPlayer("안득수","Strike",69)
print(a1.name)
a1.Change_Numer(49)
print(a1.back_number)
"""

#예시 
"""
names = ["안득수","김범권","정수용","차승원","백해성"]
positions = ["MF","DF","CF","WF","GK"]
numbers = [10,4,5,6,12]

players = [[name,positions,number] for name,positions,number in zip(names,positions,numbers)]
print(players)

class SoccerPlayer():
    def __init__(self,name,position,back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
        
    def __str__(self):
        return "안녕하세요 나의 이름은 %s 입니다. 나는 %s 포지션에서 뛰고 있다." %(self.name,self.position)

players_objects = [SoccerPlayer(name,position,number) for name,position,number in zip(names,positions,numbers)]
print(players_objects[0])
"""

"""
# Note 클래스

class Note():
    def __init__(self,contents = None):
        self.contents = contents

# 다형성 예시
class animal:
   def __init__(self,name):
      self.name = name
   def talk(self):
      raise NotImplementedError("Subclass must implement abstract method")
      
class cat(animal):
   def talk(self):
      return 'Meow!'
      
class dog(animal):
   def talk(self):
      return "Woof!"
      
animals = [cat('Missy'), cat('Mr.Mis'),dog('lassie')]
for animal in animals:
   print(animal.name + ':' +animal.talk())

#예제 1번
class Person(object):
   def __init__(self,name):
      self.name = name
      
   def language(self):
      pass
   
class Earthling(Person):
   def language(self, language):
      return language
      
class Groot(Person):
   def language(self, language):
      return "I'm Groot"
      
#예제 1번
name = ['Gachon','Dr.strange','Groot']
country = ['Korea','USA','Galaxy']
language = ['Korean','English','Groot']

for idx,name in enumerate(name):
   if country[idx].upper() != 'GALAXY':
      person = Earthling(name)
      print(person.language(language[idx]))
      
   else:
      groot = Groot(name)
      print(groot.language(language[idx]))

#예제 2번
class SoccerPlayer(object):
   def __init__(self,name,position,back_number):
      self.name = name
      self.position = position
      self.back_number = back_number
      
   def change_back_number(self,back_number):
      self.back_number = back_number
      

jaewon = SoccerPlayer("jaewon","MF",10)
print("현재 선수의 등번호는:",jaewon.back_number)
jaewon.change_back_number(5)
print("현재 선수의 등번호는:",jaewon.back_number)

#예제 3번

class Marvel(object):
   def __init__(self,name,character):
      self.name = name
      self.character = character
   def __str__(self):
      return "My name is {0} and my weapon is {1}.".format(self.name,self.character)
      
class Villain(Marvel):
   pass

first_villain = Villain("Thanos","infinity gauntlet")
print(first_villain)

#예제 4번- 상속 사용
class Class(object):
   def __init__(self,name,score):
      self.name = name
      self.score = score
      

class Math(Class):
   def say():
      print("힘내")

class TV(object):
   def __init__(self,size,year,company):
      self.size = size
      self.year = year
      self.company = company
   def describe(self):
      print(self.company + "에서 만든" + self.year + "년형" + self.size + "인치TV")
      
class Laptop(TV):
   def describe(self):
      print(self.company + "에서 만든" + self.year + "년형" + self.size + "인치노트북")
      
LG_TV = TV(32,2019,"LG")
LG_TV.describe()

samsung_microwave = Laptop(15,2022,"Samsung")
samsung_microwave.describe()
"""
"""
class Person:
    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position
    def show_info(self):
        print('이름:{}'.format(self.name))
        print('나이:{}'.format(self.age))
        print('직위:{}'.format(self.position))
        print('저는 가천대학교 연구소 {0} {1} 입니다 나이는 {2}입니다.'.format(self.position,self.name,self.age))

class Resarcher(Person):
    def __init__(self,name,age,position,degree):
        Person.__init__(self,name,age,position)
        self.degree = degree
    def show_info(self):
        Person.show_info(self)
        print("저는 {} 입니다.".format(self.degree))

if __name__ == '__main__':
    resarcher_john = Resarcher("John","22","연구원","학사")
    resarcher_ted = Resarcher("Ted","40","소장","박사")
    resarcher_john.show_info()
    print('='*50)
    resarcher_ted.show_info()
"""
"""
class Score:
    def __init__(self,student):
        tmp = student.split(",")
        self.name = tmp[0]
        self.midterm = int(tmp[1])
        self.final = int(tmp[2])
        self.assignmet = int(tmp[3])
        self.score = None
        self.grade = None

    def total_score(self):
        test_score = ((self.midterm + self.final)/2)*0.8
        
        if self.assignmet >= 3:
            assign_score = 20
        elif self.assignmet >= 2:
            assign_score = 10
        elif self.assignmet >= 1:
            assign_score = 5
        else:
            assign_score = 0
         
        self.score = test_score + assign_score

    def total_grade(self):
        if self.assignmet == 0:
            grade = 'F'
        elif self.score >= 90:
            grade = 'A'
        elif self.score >= 70:
            grade = 'B'
        elif self.score >= 60:
            grade = 'C'

        else:
            grade = 'F'

        self.grade = grade
        return grade

student_john = Score("John,90,90,0")
aa = student_john.total_score()
bb = student_john.total_grade()
print(aa,bb,student_john.score,student_john.grade)
"""
"""
class IceCream(object):
    def __init__(self,flavor):
        self.flavor = flavor
    def change_flavor(self,new_flavor):
        print('아이스크림을 %s 에서 %s로 변경해주세요'%(self.flavor,new_flavor))
        self.flavor = new_flavor
        print('아이스크림을 %s로 변경했습니다.'%(self.flavor))

ice_cream = IceCream('레인보우샤베트')
ice_cream.change_flavor('엄마는 외계인')
"""
"""
class Terran(object):
    def __init__(self,mineral):
        self.scv = 4
        self.marine = 0
        self.medic = 0
        self.mineral = mineral
    def command(self,SCV = False):
        self.mineral += 8*self.scv
        if SCV:
            self.scv += 1
            self.mineral -= 10

    def barrack(self, Marine = False, Medic = False):
        self.mineral += 8*self.scv
        if Marine:
            self.marine += 1
            self.mineral -= 15
        if Medic:
            self.medic += 1
            self.mineral -= 25
    def check_source(self):
        print("Mineral:"+str(self.mineral)) 

User = Terran(50)
User.command(True)
User.barrack(True,True)
User.check_source()
"""

