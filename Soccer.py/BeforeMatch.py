import pygame 
import random
class Team:
    def __init__(self,name):
        # the variable that user could describe (write)...team name
        self.name = name    # home and away name 
     
class Score:
    home = 0 #started score
    away = 0 # strated score


class Shoot:
    home = 0 #started shoot 
    away = 0 #started shoot

class Corner:
    home = 0 # starting number of corner TEAM 1 
    away = 0 # starting number of corner TEAM 2

class YellowRedCard:
    home = 0 
    away = 0
    # if computer`s number is equal 4, it returns yellow card for home.team 
    def get_yellow_card(self):
      return random.randint(1,60) == 4 
    # if computer`s number is equal 4, it returns yellow card for away.team   
    def get_yellow_card2(self):                
        return random.randint(1,60) ==4   
    def get_red_card(self):           
        return random.randint(1,100) == 9
    
    def get_red_card_away(self):      
        return random.randint(1,100) == 4
    
    
    