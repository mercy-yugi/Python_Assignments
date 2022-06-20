import datetime
class Account:
    def __init__(self,full_name, number):
        self.full_name =full_name
        self.number =number
        self.account_balance=0
        self.deposits=[] #Add a new attribute to the class Account called deposits which by default is an empty list.
        self.withdraws=[] #Add another attribute to the class Account called withdrawals which by default is an empty list.
        self.transaction=100
        self.new_dict1={}
        self.new_dict2={}
        self.now=datetime.datetime.now()
        self.date=self.now.strftime("%d:%m:%y")
        self.new_merged={}
        # Update the withdrawal method to store each withdrawal transaction as a dictionary like like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }
    def deposit(self,amount):
        if amount<=0:
            return f"must be greater than 0"
        else:
            self.account_balance+=amount
            self.deposits.append({amount})
            self.new_dict2["date"]=self.date
            self.new_dict2["amount"]=amount
            self.new_dict2["narration"]="Confirmed, you have deposited",amount, "Your new balance is", self.account_balance
        return self.new_dict2
          
# Update the withdrawal method to store each withdrawal transaction as a dictionary like like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }
    def withdraw(self,amount) :
        if amount>=self.account_balance:
            return f"Insuffiecient funds"
        elif amount<=0:
            return f"must be greater than 0"
        else:
             self.account_balance -= amount + self.transaction
             self.withdraws.append({amount})
             self.new_dict1["date"]=self.date
             self.new_dict1["amount"]=amount
             self.new_dict1["narration"]="You've withdrawn", amount ,"your new balance is",self.account_balance
             return self.new_dict1
    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for statements in self.withdraws:
            print(statements)  
    def current_balance(self):
        return self.account_balance
    def full_statement(self):
        for x in self.new_merged:
            return x
