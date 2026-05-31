class Player:


    def __init__(self, name: str, hp: int, inventory: list):
        self.name = name
        self.hp = hp
        self.inventory = inventory


    def show_inventory(self) -> None:
        for i in self.inventory:
            print(i)
    
    def show_hp(self) -> str:
        return f"{self.name}'s HP: {self.hp}"

    def take_damage(self, amount) -> None:
        self.hp -= amount
        print(self.show_hp())


    def heal(self, amount) -> None:
        self.hp += amount
    

    def add_item(self, item : str) -> None:
        self.inventory.append(item)
        for i in self.inventory:
            print(i)
    

player = Player('Knight', 10, ['Espada', 'Escudo', 'poção'])

player.show_inventory()
player.take_damage(1)
player.heal(1)
player.add_item('flecha')
