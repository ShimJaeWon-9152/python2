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



