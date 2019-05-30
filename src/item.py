
class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"{self.name} picked up")

    def on_drop(self):
        print(f"{self.name} dropped")
        return True

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class LightSource(Item):

    def on_drop(self):
        print("You may need this later! Might want to pick it back up...")
        cmd = input("Are you sure? y/n \n")
        if (cmd == "y"):
            print(f"{self.name} dropped")
            return True
        elif (cmd == "n"):
           print("Good call")
           return False

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)
