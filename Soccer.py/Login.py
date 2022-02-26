class EmailAddress():
    def check_address(self):
        self.address = input("Enter your Email: ") # login...check your Email Address
        self.characteristicSign = "@"
        self.Emailaddress = self.address.split("@")
        if self.characteristicSign == "@":
            pass
            if self.address.endswith(".com") or self.address.endswith(".hr"):
                pass
                if self.characteristicSign in self.address:
                   pass
                   if self.Emailaddress[1].islower():
                    print(f"Welcome, {self.Emailaddress[0]}")
                   else:
                       print("""Invalid Email address.
                          Try with another account or check your Address!
                          Your BHS \N{winking face}""")
                       exit()
                else:
                    print("""Invalid Email address.
                          Try with another account or check your Address!
                          Your BHS \N{winking face}""")
                    exit()        
            else: 
                print(""" Invalid Email address.
                          Try with another account or check your Address!
                          Your BHS \N{winking face}""")
                exit()
class Card(EmailAddress): # class EmailAdress is in class Card
    def __init__(self,name,balance):
        self.name = name #your username
        self.check_address() # we call method check_address from class EmailAddress
        name = self.Emailaddress[0] #first part of EmailAddress to @
        self.balance = balance # your currently 
        print("Username:",name) 
        print("Balance:",balance) #currently balance
        
    def amount (self): # method of class Card
        #self.amount_ = amounts #amount for betting 
        self.amount_ = int(input("Amount: "))
        if self.amount_ <= self.balance:
           self.new_balance_after_ticket_pay = self.balance - self.amount_
           print(f"New balance after paid ticket: {self.new_balance_after_ticket_pay}  Kn")
        else:
            print("You do not have enough money!")
            exit()
    
    
class Bet (Card): # class Card in class Bet
    def __init__(self,name,balance):
        super().__init__(name,balance)
        # class Bet gets __init__ from class Card
    def amount (self):
        super().amount()

    
        

                