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