class Character:
        
    def __init__(self, name: str, hp: int, inventory: list, damage: int):
        self.name = name
        self.hp = hp
        self.inventory = inventory
        self.damage = damage

    def is_alive(self) -> bool:
        return self.hp > 0
    
    def show_inventory(self) -> None:
        for i in self.inventory:
            print(i)
    
    def show_hp(self) -> str:
        return f"{self.name}'s HP: {self.hp}"

    def take_damage(self, amount) -> None:
        self.hp -= amount
        print(self.show_hp(), "Alive" if self.is_alive() else "Dead")

    def attack(self, target: "Player | Enemy") -> None:
        target.take_damage(self.damage) 
    
    def heal(self, amount) -> None:
        self.hp += amount    

    def add_item(self, item : str) -> None:
        self.inventory.append(item)
        for i in self.inventory:
            print(i)
    def __init__(self, name: str, hp: int, inventory: list, damage: int):
        self.name = name
        self.hp = hp
        self.inventory = inventory
        self.damage = damage
        
class Player(Character):
    pass



class Enemy(Character):
    pass



#player = Player('Knight', 10, ['Espada', 'Escudo', 'poção'])
player = Player("Knight", 100, [], 20)
goblin = Enemy("Goblin", 30,[], 15)
