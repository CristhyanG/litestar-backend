class BankAccount :

    def __init__(self, user : str, balance : int):
        self.user = user
        self.balance = balance
        
    def deposit(self, amount : int) :
        self.balance += amount
        return f"{amount} Deposited, now you have {self.balance}"
    
    def withdraw(self, amount : int) :
        self.balance -= amount
        return f"{amount} withdrown, now you have {self.balance}"
    def show_balance(self):
        return f"Your balance is {self.balance}"
    
user = BankAccount('Roberto', 1000)

question : int = int(input("Fucked Bank, what do you want to do? \n 1 - Deposit \n 2 - Withdraw \n 3 - exit \n 4 - Fuck u"))
if question == 1 :
    amount = int(input("How much?: "))
    print(user.deposit(amount))
    