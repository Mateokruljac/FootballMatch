import time
import random
from gtts   import gTTS
from BeforeMatch import Score
from BeforeMatch import Shoot
from BeforeMatch import Corner
from BeforeMatch import YellowRedCard
from Playsound   import playsound
class Match  (YellowRedCard):
    def __init__(self,home,away):
        self.home = home
        self.away = away
        self.score = Score() # self.score get value of class Score()
        self.minute = 0
        self.shoot = Shoot() # self.shoot get value of class Shoot()
        self.corner = Corner() # self.corner get value of class Corner()
        self.home.yellow = 0
        self.away.yellow = 0
        self.home.red = 0
        self.away.red = 0
    
    def corner_team1(self):
        return random.randint(1,24) == 17
    
    def get_yellow_card1(self):
         # return value from YellowRedCard
         return super().get_yellow_card()
    
    def get_yellow_card2(self):
        return super().get_yellow_card2()
    
    def get_red_card1(self):
        return super().get_red_card()    
    
    def get_red_card_away2(self):
        return super().get_red_card_away()       
    
    def corner_team2(self):
        return random.randint (1,21) == 17
    
    def get_goal_return(self):
        return  random.randint(1,35)== 2
    
    def get_goal_return_2(self):
        return random.randint(1,30)  ==  2
        
    def shoots_on_goal_team1(self):
         return random.randint(1,20) == 5
    
    def shoots_on_goal_team2(self):
        return random.randint (1,18) == 4
    def start_match (self):
        self.minute = 0
        while self.minute < 91: # 91, because football match during 90 minutes 
            print(f"{self.home.name}   vs     {self.away.name}     Minutes")
            if self.minute < 1:
                self.convert_toaudio(f"""Welcome to San Siro,Hello ladies and gentleman, Welcome to the UEFA 
                        Championship football match between {self.home.name} and {self.away.name}
                        Today beer is 2 Euro, hot-dog too. So, Match start!!""")
        
            firstteam_goal = self.get_goal_return()  # get method from class Match
            secondteam_goal = self.get_goal_return_2() # 
            self.home_yellow = self.get_yellow_card1() #
            self.away_yellow = self.get_yellow_card2() #
            self.home_red = self.get_red_card1()       #
            self.away_red = self.get_red_card_away2()  #
            if self.home_yellow: # TRUE
                self.home.yellow += 1
                pass
            
            if self.away_yellow: # TRUE
                self.away.yellow += 1
                pass
            
            if self.home_red:  # TRUE
                self.home.red += 1
                pass
            
            if self.away_red: # TRUE
                self.away.red += 1
                pass
            
            if firstteam_goal: # TRUE
                self.score.home += 1
                print((f"{self.home.name} scores goal!"))
                time.sleep(0.2)
                pass
            else:
                self.score.home += 0
                pass
                
            if secondteam_goal: #TRUE
                self.score.away += 1
                print((f"{self.away.name} scores goal"))
                time.sleep(0.2)
                pass
            else:
                self.score.away += 0
                pass
            
            self.first_team_shoot = self.shoots_on_goal_team1()#
            if self.first_team_shoot:
                self.shoot.home += 1
                pass
            else:
                self.shoot.home += 0
            self.second_team_shoot = self.shoots_on_goal_team2()#
            
            corner_firstteam = self.corner_team1()#
            corner_secondteam = self.corner_team2()#
            if corner_firstteam:
                self.corner.home += 1
                pass
            else:
                self.corner.home += 0
            
            if corner_secondteam:
                self.corner.away += 1
                pass
            else:
                self.corner.away += 0
            
            if self.second_team_shoot:
                self.shoot.away += 1
                pass
            else:
                self.shoot.away += 0
            
            self.shoots_on_goal_team2()#
            self.shoots_on_goal_team1()#
            self.get_yellow_card()#
            self.get_yellow_card2()#
            self.get_red_card()#
            self.get_red_card_away()#
            self.print_goal()#
            self.minute += 1
            time.sleep(0.1)
            #if means that if 46 == 46, that number won`t execute, but function will execute and than worth that self.minute ==46
            if self.minute == 46: #46, because HT is on 45 minutes....if write self.minute == 45
                print ("Half-time      HT") # it will stop on 44 minutes
                time.sleep(1.1)
            
            if self.minute > 90:
                print("End game!")
                if self.score.home > self.score.away:
                    print(f"{self.home.name} WIN!!!")
                elif self.score.home < self.score.away:
                    print(f"{self.away.name} WIN!!!")
                else:
                    print("DRAW!!!")
                self.statistic()
                
                 
            
            
    def statistic (self):
                print()
                print()
                print("_____________________________________________")
                print(f"{self.home.name}                             {self.away.name}")
                print("_____________________________________________")   
                print("                    RESULT                   ")
                print(f"{self.score.home}                                   {self.score.away}")
                print("_____________________________________________")
                print("                 SHOOTS ON GOAL         ")
                print(f"{self.shoot.home + self.score.home}                                  {self.shoot.away + self.score.away}")
                print("_____________________________________________")
                print("                   CORNER               ")
                print(f"{self.corner.home}                                   {self.corner.away}")
                print("_____________________________________________") 
                print("                YELLOW/RED CARD        ")   
                print(f"{self.home.yellow}/{self.home.red}                               {self.away.yellow}/{self.away.red}")           
    def  print_goal (self):
        print(f"    {self.score.home}      :       {self.score.away}            {self.minute} ")         
    
    def song (self,audio):
        time.sleep(0.2)
        playsound(audio)
    
    def convert_toaudio(self,text):
        self.my_audio = gTTS(text)
        self.my_audio.save("hello.mp3")
        self.song("hello.mp3")