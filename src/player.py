# Write a class to hold player information, e.g. what room they are in
# currently.
# class Player:
#     def __init__(self, name, current_room):
#         self.name = name
#         self.current_room = current_room
import item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.currentRoom = current_room
        self.items = []
        self.hp = 100
        self.victory = False
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(self.currentRoom)
        else:
            print("You cannot move in that direction.")

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def is_alive(self):
        return self.hp == 0

    def print_inventory(self):
        for item in self.inventory:
            print(f"Inventory: {item}, '\n'")
