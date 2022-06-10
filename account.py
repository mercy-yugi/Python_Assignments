class Account():
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
    def __init__(self,name,number):
        self.name=name
        self.number=number
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
# Modify the deposit method to append each successful deposit to self.deposits

    def deposit(self, amount):
        if amount<=0:
            return f"The deposit amount must be greater than zero"
        else:
            self.balance+=amount
            self.deposits.append(amount)
            print(self.deposits)
            return f"Hello,{self.name} you have deposited {amount} and your balance is {self.balance}"
    # the requested amount must be greater than current balance
    # requested amount must b greater than zero.
    # create a withdraw instance of a class.
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals


    def withdraw(self,amount):
        if amount>self.balance:
            return f"insufficient funds"
        elif amount<=0:
            return "Amount must be greater than zero"
        else:
             self.balance-=amount
             self.withdrawals.append(amount)
             print(self.withdrawals)
             return f"Hello {self.name} you have withdrawn {amount} and your balance is {self.balance}"
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
    def deposits_statement(self):
        for deposit in self.deposits:
            print(f"Amount deposited is {deposit}")  
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
    def withdrawals_statement(self):
        for withdrawal in self.withdrawals:
            print(f"Amount withdrawn is {withdrawal}")
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
    def withdraws(self,amount):
        if amount > 0:
            self.balance-=amount
            return f"Hello {self.name}, you have deposited {amount} and your new balance is {self.balance-100}"
        else:    
            return f"Deposit amount must be greater than zero"
# Add a method to show the current balance.
    def current_balance(self):
        return f"The current balance is Ksh {self.balance}"