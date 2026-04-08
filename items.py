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

class StengthPotion(Item):
    def __init__(self, level):
        self.level = level
        super().__init__(f"Strength Potion {self.level}", f"Increase attack by {2*(2**(self.level-1))}", 15*(2**(self.level-1)), 7*(2**(self.level-1)))
    def use(self, player):
        player.base_attack += 2*(2**(self.level-1))
        player.inventory.remove(self)

class StrengthPotion1(Item):
    def __init__(self):
        super().__init__(1)

class StrengthPotion2(Item):
    def __init__(self):
        super().__init__(2)

class StrengthPotion3(Item):
    def __init__(self):
        super().__init__(3)


class Boots(Item):
    def __init__(self, level):
        self.level = level
        super().__init__(f"Boots {self.level}", f"Increase agility by {1*(2**(self.level-1))}", 20*(2**(self.level-1)), 10*(2**(self.level-1)))
    def use(self, player):
        player.base_agility += 0.25 * self.level

class Boots1(Boots):
    def __init__(self):
        super().__init__(1)

class Boots2(Boots):
    def __init__(self):
        super().__init__(2)

class Botts3(Boots):
    def __init__(self):
        super().__init__(3)


    
    
