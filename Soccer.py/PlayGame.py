from BettingInfo import NameBettingHouse
from BettingInfo import Offer
from Login       import Card
from BeforeMatch import Team
from YourBettingChoice import  YourBettingChoice
from Results     import FinallyBetting
from Game        import Game
# START GAME 
betttt = NameBettingHouse()
betttt.nbh()
card = Card()
card.amounts()
offr = Offer()
offr.offering()
team_1 = Team("Barcelona")
team_2 = Team("Real Madrid")
ybt = YourBettingChoice()
match = FinallyBetting(team_1,team_2)
match.my_choice()
match.start_match()
match.finallybetting()






