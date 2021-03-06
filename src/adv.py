from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Items in rooms

room['foyer'].add_item(Item("Torch", "an unlit torch"))
room['overlook'].add_item(Item("Matches", "a box of matches"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
playerOne = Player("Shawn", room["outside"])
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
directions = ["n", "s", "w", "e"]

while True:
    print(f"\nCurrent room: {playerOne.current_room.name}")
    print(f"Room description: {playerOne.current_room.description}")
    print(f"Items around the room: \n", end = "")
    print([item.name for item in playerOne.current_room.items])

    cmd = str(input("\nChoose a direction or Q to quit: \n\n"))
    print("\n\n\n------------------------------\n")

    # if (cmd == "p"):
    #    item_select = str(input("please select an item: "))
    #    if (playerOne.current_room.items):
    #        playerOne.add_item(item_select)

    # if (cmd == "i"):
    #     print(f"Inventory: {playerOne.items}")

    if (cmd == "" or not str):

        print("Please enter a direction or Q to exit the game. \n")
    if (cmd == "q"):
        print("Thanks for playing!")

        break
    elif (cmd in directions):
        try:
            playerOne.current_room = getattr(playerOne.current_room, f"{cmd}_to")
        except:
            print("That direction doesn't exist..Try another direction..")

    elif (cmd == "i"):
        print("Inventory: ", end = "")
        print([item.name for item in playerOne.items])
    else:
        cmds = cmd.split(" ")
        if (len(cmds) != 2):
            print("Bad command")
        else:
            verb,obj = cmds
            if (verb == "take"):
                try:
                    item = [x for x in playerOne.current_room.items if x.name == obj][0]
                    playerOne.current_room.remove_item(item)
                    playerOne.add_item(item)
                    item.on_take()
                except IndexError:
                    print("Item not found")

            elif (verb == "drop"):
                try:
                    item = [x for x in playerOne.items if x.name == obj][0]
                    playerOne.remove_item(item)
                    playerOne.current_room.add_item(item)
                    item.on_drop()
                except IndexError:
                    print("Player not holding that item")

            else:
                print("Bad command")

