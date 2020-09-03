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
key = None
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

while is_playing:
    print(new_player)
    key = input("Select the first letter of the direction you would like to move.\nTo pick up an item, type the word 'get'.\nTo drop an item, type the word 'drop'.\nPress 'q' to quit. ")
    print("-------------------------")
    if key == "q":
        print("Thanks for playing.")
        is_playing = False
        break;
    if new_player.room == room['outside']:
        if key != "n" or key !="q":
            print(not_valid)
        elif key == "n":
            new_player.room = new_player.room.n_to    
    elif new_player.room == room['foyer']:
        if key == "s":
            new_player.room = new_player.room.s_to
        elif key == "n":
             new_player.room = new_player.room.n_to
        elif key == "e":
            new_player.room = new_player.room.e_to
        elif key != "n" or key != "s" or key != "e" or key !="q":
            print(not_valid)
    elif new_player.room == room['overlook']:
        if key == "s":
            new_player.room = new_player.room.s_to
        elif key != "s" or key !="q":
            print(not_valid)
    elif new_player.room == room["narrow"]:
        if key == "w":
             new_player.room = new_player.room.w_to
        elif key == "n":
             new_player.room = new_player.room.n_to
        elif key != "n" or key != "w" or key !="q":
            print(not_valid)
    elif new_player.room == room['treasure']:
        if key == "s":
            new_player.room = new_player.room.s_to
        elif key != "n" or key != "w" or key != "e" or key !="q":
            print(not_valid)

    