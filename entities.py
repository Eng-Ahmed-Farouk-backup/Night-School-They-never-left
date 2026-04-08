import random
class Entity:
    def __init__(self, base_hp, base_attack, base_defense, base_armor, base_agility):
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.base_armor = base_armor
        self.base_agility = base_agility
    def is_alive(self):
        return self.base_hp > 0

class Player(Entity):
    def __init__(self, name, base_hp, base_attack, base_defense, base_armor, base_agility):
        super().__init__(base_hp, base_attack, base_defense, base_armor, base_agility)
        self.max_hp = base_hp
        self.name = name
    
    def get_hp(self):
        return self.base_hp
    
    def get_attack(self):
        return self.base_attack
    
    def get_defense(self):
        return self.base_defense
    
    def get_armor(self):
        return self.base_armor
    
    def get_agility(self):
        return self.base_agility
    
    def take_damage(self, damage):
        self.base_hp -= damage
        if self.base_hp < 0:
            self.base_hp = 0
    
    def increase_health(self, amount):
        self.base_hp = min(self.base_hp+amount, self.max_hp)
    
    

    
class Enemy(Entity):
    def __init__(self, name, base_hp, base_attack, base_defense, base_armor, base_agility, drops, lost_honor, honor_drop, gold_drop):
        super().__init__(base_hp, base_attack, base_defense, base_armor, base_agility)
        self.name = name
    def get_hp(self):
        return self.base_hp
