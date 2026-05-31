class Bank_Account :

    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount : int):
        self.balance += amount
        return f"{amount} deposited, now you have {self.balance} in your account"


    def withdraw(self, amount: int) :
         self.balance -= amount
         return f"{amount} withdrowed, now you have {self.balance} in your account"

user1 = Bank_Account('William', 2000)
print(user1.withdraw(500))

        
