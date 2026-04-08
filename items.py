class Item:
    def __init__(self, name, description, buy_price = 0, sell_price = 0):
        self.name = name
        self.description = description
        self.buy_price = buy_price
        self.sell_price = sell_price
    def __repr__(self):
        return self.name

class HealthPotion(Item):
    def __init__(self, level):
        self.level = level
        super().__init__(f"Health Potion {self.level}", f"Restore {5*(2**(self.level-1))} HP", 10*(2**(self.level-1)), 5*(2**(self.level-1)))
    def use(self, player):
        player.increase_health(5*(2**(self.level-1)))
        player.inventory.remove(self)

class HealthPotion1(HealthPotion):
    def __init__(self):
        super().__init__(1)

class HealthPotion2(HealthPotion):
    def __init__(self):
        super().__init__(2)

class HealthPotion3(HealthPotion):
    def __init__(self):
        super().__init__(3)
