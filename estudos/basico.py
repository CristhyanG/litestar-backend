class user :
  name : str 
  age : int
  status : bool
  def __init__(self, name, age, status) :
    self.name = name 
    self.age = age
    self.status = status
  def __str__(self) :
    return f"{self.name} is {self.age} years old and has status {self.status}"

users = [user("John", 30, True),
         user("Jane", 25, False),
         user("Doe", 40, True)]
for u in users :
  print(u)