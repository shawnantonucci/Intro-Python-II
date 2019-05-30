
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"{self.name} picked up")

    def on_drop(self):
        print(f"{self.name} dropped")
        return True

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
