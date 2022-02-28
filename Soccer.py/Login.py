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
    def  __init__ (self):
         #your username
        self.check_address() # we call method check_address from class EmailAddress
        self.name = self.Emailaddress[0] #first part of EmailAddress to @
        self.balance = 1000 # your currently 
        print("Username:",self.name) 
        print("Balance:",self.balance) #currently balance
        self.amount = int(input("Amount: "))
        
    def amounts (self): # method of class Card
        if self.amount <= self.balance:
           self.new_balance_after_ticket_pay = self.balance - self.amount
           print(f"New balance after paid ticket: {self.new_balance_after_ticket_pay}  Kn")
        else:
            print("You do not have enough money!")
            exit()
    
    

    
        

                