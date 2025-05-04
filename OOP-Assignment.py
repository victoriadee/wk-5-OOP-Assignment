# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Origin: {self.origin}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass: Polymorphism and Inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, speed):
        super().__init__(name, power, origin)
        self.speed = speed

    def use_power(self):
        print(f"{self.name} soars through the sky with {self.power} at {self.speed} km/h!")

# Subclass: Another variation
class StrengthHero(Superhero):
    def __init__(self, name, power, origin, strength_level):
        super().__init__(name, power, origin)
        self.strength_level = strength_level

    def use_power(self):
        print(f"{self.name} lifts a car using {self.power} with strength level {self.strength_level}!")