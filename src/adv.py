from room import Room
from player import Player
from item import Item
from item import LightSource
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False),

    'narrow':   Room("Narrow Passage", """A dark quite passage. There is a door to the east
and a door to the north""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),

    'closet': Room("Closet", """Just a normal closet with cleaning supplies in it. there is a
    toolbox in the corner of the closet. The only exit is to the west""", False),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].e_to = room['closet']
room['closet'].w_to = room['narrow']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Items in rooms

room['foyer'].add_item(LightSource("torch", "an unlit torch", 0))
room['foyer'].add_item(Item("book", "a book on lockpicking", 0))
room['overlook'].add_item(Item("book", "a book on lockpicking", 0))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Shawn", room['outside'])

if (player.currentRoom.is_light == True or [item.name == "torch" for item in player.items]):
        print(player.currentRoom)
elif (player.currentRoom.is_light == False):
        print("Its pitch black in here. Need a light source")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    cmd = input("-> ")
    if cmd in ["n", "s", "e", "w"]:
        player.travel(cmd)
    elif cmd == "q":
        break
    # else:
    #     print("I did not understand that command\n")

    if (cmd == "i"):
        print("Inventory: ", end="")
        print(player.currentRoom)
        print([item.name for item in player.items])
    else:
        cmds = cmd.split(" ")
        if (len(cmds) != 2):
             if cmd in ["n", "s", "e", "w"]:
                 continue
             else:
                 print("Bad command")
        else:
            verb, obj = cmds
            if (verb == "take"):
                try:
                    item = [
                        x for x in player.currentRoom.items if x.name == obj][0]
                    player.currentRoom.remove_item(item)
                    player.add_item(item)
                    item.on_take()
                    print(player.currentRoom)
                except IndexError:
                    print("Item not found")

            elif (verb == "drop"):
                # if (playerOne.items != "torch"):
                item = [x for x in player.items if x.name == obj][0]
                if item.on_drop():
                    player.remove_item(item)
                    player.currentRoom.add_item(item)
                    print(player.currentRoom)
                else:
                    print(player.currentRoom)
