class person :
    def __init__(self, name : str, age : int) :
        self.name = name 
        self.age = age 
    def introduce(self) :
        return f"Hello my is {self.name} and im {self.age} years old"
    
user1 = person('Alice', 22)
print(user1.introduce())