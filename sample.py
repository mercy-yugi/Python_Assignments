
from datetime import datetime
class Account:
    def __init__(self,accname,accountno):
        self.accname = accname
        self.accountno = accountno
        self.balance = 0
        self.transaction_fee = 100
        self.loan=0
        self.deposits=[]
        self.withdrawals = []
        self.statement = []
        
        
    def  deposit(self,amount):
        if amount <=0:
             print(f"Deposit must be positive amount")
        else:
            self.balance+=amount   
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"You have deposited"
            }
            self.deposits.append(amount)
            self.statement.append(transaction) 
            print(f"Hello {self.accname}, your new balance is {self.balance} and your deposits are {self.deposits}and your statement is {self.statement}" )
    def withdrawal(self,amount):
        
        if amount+self.transaction_fee > self.balance:
            print(f"Hello {self.accname}, your balance is {self.balance} you can't withdraw {amount}")    
        elif amount <=0:
            print(f"Withdrawal amount must be greater than 0")
        else:    
            self.balance-=amount+self.transaction_fee
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"You have withdrawn "
            }
            self.withdrawals.append(amount)
            self.statement.append(transaction)
            print(f"Hello {self.accname}, your new balance is {self.balance} and the withdrawals are {self.statement}")
    def deposit_statements(self):
         for deposit in self.statement:
             print(deposit)
             
    def withdrawals_statement(self):
        for withdrawal in self.statement:
            print(withdrawal)

    def current_balance(self):
        print(f"{self.balance}")     

    
    def full_Statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%x/%X")
            print(f"{date}:   {Narration}   {amount}")
              
    def loaning(self,amount):    
        item = len(self.deposits)
        item_s = sum(self.deposits)
        limit = item_s*(1/3)
        amount+=(amount)*0.03 
       
        if amount<=100:
            return "Sorry we can't give you this loan, your loan must be more than 100 "
        elif self.loan>0:
            return f"Dear customer you still have a loan of {self.loan}"
        elif item<10:
            return f"Your deposits must be atleast 10"

        elif amount>=limit:
            return f"Dear customer you can't borrow {amount}is higher than a limit of {self.balance}"

        else:
            self.loan+=amount
            return f"Dear customer {self.accname} your loan of ksh{amount} has been granted successfully"

    def loan_repay(self,amount): 
        if amount<self.loan:
            paying = self.loan-amount
            return f"Dear customer you have paid {amount} and your loan balance is {paying}"
        else:
            over_pay = amount-self.loan
            self.balance+=over_pay
            return f"You succesfully completed paying your loan and the over pay is {over_pay} and your new balance is {self.balance}"    

    def transfer(self,amount,account):
        fee= amount*0.05
        Total=fee+amount
        if amount<0:
            return f"Dear customer {self.accname} your amount is too low"
        elif Total>self.balance:
            return f"Dear customer {self.accname} you balance is {self.balance} and you need atleast {Total}"
        else:
            self.balance-=Total
            return f"Dear customer you  have sent {amount} to {account} and your new balance is {self.balance}"