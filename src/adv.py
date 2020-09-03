import textwrap
from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", 
                     [Item("torch", "unused, almost like someone is expecting you"), 
                     Item("rock", "a pretty standard rock")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("key", "rusted and old")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("helmet", "it looks like it would sit on your head comfortably")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("sword", "the hilt has some valuable looking jewels, but the blade itself looks dull")]),
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

wrapper = textwrap.TextWrapper(width=50)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("What is your name? ")
command = ""
item = None
new_player = Player(name, room["outside"], [])
is_playing = True
not_valid = "Invalid key. Please try again."
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

# 

while is_playing:
    print(new_player)
    print("---------------")
    command = input("Select the first letter of the direction you would like to move.\nTo pick up an item, type the word 'get' and the name of the item.\nTo drop an item, type the word 'drop' and the name of the item in your inventory.\nPress 'q' to quit.\nPress 'i' to check your inventory.")
    print("---------------")
    key = command.split()
 
    if len(key) == 1:
        if key[0] == "q":
            print("Thanks for playing.")
            is_playing = False
            break
        if key[0] == "i":
            new_player.check_inventory()
            continue
        if new_player.room == room['outside']:
            if key[0] == "n":
                new_player.room = new_player.room.n_to  
            elif key[0] != "i" or key[0] != "n" or key[0] !="q":
                print(not_valid)
        elif new_player.room == room['foyer']:
            if key[0] == "s":
                new_player.room = new_player.room.s_to
            elif key[0] == "n":
                new_player.room = new_player.room.n_to
            elif key[0] == "e":
                new_player.room = new_player.room.e_to
            elif key[0] != "i" or key[0] != "n" or key[0] != "s" or key[0] != "e" or key[0] !="q":
                print(not_valid)
        elif new_player.room == room['overlook']:
            if key[0] == "s":
                new_player.room = new_player.room.s_to
            elif key[0] != "i" or  key != "s" or key !="q":
                print(not_valid)
        elif new_player.room == room["narrow"]:
            if key[0] == "w":
                new_player.room = new_player.room.w_to
            elif key[0] == "n":
                new_player.room = new_player.room.n_to
            elif key[0] != "i" or key[0] != "n" or key[0] != "w" or key[0] !="q":
                print(not_valid)
        elif new_player.room == room['treasure']:
            if key[0] == "s":
                new_player.room = new_player.room.s_to
            elif key[0] != "i" or key[0] != "n" or key[0] != "w" or key[0] != "e" or key[0] !="q":
                print(not_valid)
    elif len(key) == 2:       
        if key[0] == "get":
            new_player.get_item(key[1])
        elif key[0] == "drop":
            new_player.drop_item(key[1])
        else:
            print("Invalid key. Please make another selection to continue your adventure.")
    