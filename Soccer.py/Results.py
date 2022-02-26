from Match import Match
from YourBettingChoice import YourBettingChoice


class FinallyBetting (Match,YourBettingChoice) :
    def start_match(self):
        return super().start_match()
    
    def my_choice(self):
        return super().my_choice()    
    def finallybetting (self):
    
        if self.x == 1: # if your choice is that first team win
            if self.score.home > self.score.away:
                self.coeficcient = 0.180  
                print("1 You win")

            else:
                print("1 You lose")
        if self.x == 2:# look at BettingInfo.py
           if self.score.home < self.score.away:
               self.coeficcient = 0.190
               print("2 You win")
           else:
               print("2 You lose")
        
        if self.x == 3:
           if self.corner.home > self.corner.away:
               self.coeficcient = 0.140
               print("3 You win")
           else:
               print("3You lose")
        
        if self.x == 4:
            if self.corner.home < self.corner.away:
                self.coeficcient = 0.170
                print("4 You win")
            else:
               print("4 You lose") 
        
        if self.x == 5:
            if self.home.yellow > self.away.yellow:
                self.coeficcient = 0.170
                print("5 You Win")
            else:
                print("5 You lose")
        
        if self.x == 6:
            if self.home.yellow < self.away.yellow:
                self.coeficcient = 0.190
                print("6 You win")
            else:
                print("6 You lose")
        if self.x == 7:
            if self.home.red == True:
                self.coeficcient = 0.360
                print("7 You win")
            else:
                print("7 You lose")
        if self.x == 8:
            if self.home.red == True:
                self.coeficcient = 0.420
                print("8 You win")
            else:
                print("8 You lose") 
      
    
