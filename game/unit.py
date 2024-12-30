class Unit:
    def __init__(self, unit_type, position, health, attack, speed):
        self.unit_type = unit_type
        self.position = position
        self.health = health
        self.attack = attack
        self.speed = speed

    def move(self, target_position):
        # Implement movement logic here
        pass

    def attack_unit(self, target_unit):
        # Implement attack logic here
        pass

    def gather_resource(self, resource):
        # Implement resource gathering logic here
        pass
