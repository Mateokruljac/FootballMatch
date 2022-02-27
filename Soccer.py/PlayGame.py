from BettingInfo import NameBettingHouse
from BettingInfo import Offer
from Login       import Bet
from BeforeMatch import Team
from YourBettingChoice import  YourBettingChoice
from Results     import FinallyBetting
# START GAME 
betttt = NameBettingHouse()
betttt.nbh()
bet = Bet("Mateo",1000)
bet.amount()
offr = Offer()
offr.offering()
team_1 = Team("Barcelona")
team_2 = Team("Real Madrid")
ybt = YourBettingChoice()
match = FinallyBetting(team_1,team_2)
match.my_choice()
match.start_match()
match.finallybetting()





