"""Main game file. Run from here.
"""
from Environment import coord_setup, Room, Map
from Inputs import Command
from Character import Player

def process_command(word1_2):
    """ Given a command, process (that is: execute) the command.
    Parameters
    ----------
    command: Command
        The command to be processed
    
    Returns true If the command ends the game, false otherwise.
    """
    want_to_quit = False

    if word1_2[0] == "help":
        Command().user_help()
    elif word1_2[0] == "go":
        go_room(word1_2)
    elif word1_2[0] == "quit":
        return user_quit(word1_2)
    elif word1_2[0] == "back":
        back_command(word1_2)
    elif word1_2[0] == "take":
        take_item(word1_2)
    elif word1_2[0] == "open":
        open_command(word1_2)
    elif word1_2[0] == "drop":
        drop_item(word1_2)

    return want_to_quit

def go_room(word1_2):
    """ Try to in to one direction. If there is an exit, enter the new
        room, otherwise print an error message.

        Parameters
        ----------
        word1_2: tuple of two integers 
    """
    #validate action
    if word1_2[1] in n.return_exit_string(player1.position):
        player1.update_player_pos(word1_2[1])
    else:
        print("You can't go that way!")

def back_command(word1_2):
    """ Determines if correct input has been made to activated command

        Parameters
        ----------
        word1_2: tuple of two integers 
    """
    if word1_2[1] is not None:
        print("Back where?")
        return False
    else:
        if len(player1.history) == 0:
            print("You can not go back!")
        else:
            player1.position = player1.history.pop()

def take_item(word1_2):
    """ Adds inputed item to user inventory, then removes it from the room
    
        Parameters
        ----------
        word1_2: tuple of two integers  
    """
    if len(player1.inventory) < weight_limit: #checks players weight limit
        if word1_2[1] in n.return_item_string(player1.position): #validate if the user input exsists
            player1.inventory.append(word1_2[1])
            n.rooms[player1.position].items.remove(word1_2[1]) #deletes item from room
        else:
            print("That item isn't here")
    else:
        print("You cannot carry this! Inventory is full")

def drop_item(word1_2):
    """ Determines if correct input has been made to activated command
    
        Parameters
        ----------
        word1_2: tuple of two integers  
    """
    if word1_2[1] in player1.inventory:
        player1.inventory.remove(word1_2[1])
        n.rooms[player1.position].items.append(word1_2[1]) #drops item into the current room
    else:
        print("You can't drop that!") 

def open_command(word1_2):
    """ Opens users things (maps,inventory,items)
        checks the second word of the input and then executes relevant command

        Parameters
        ----------
        word1_2: tuple of two integers  
    """
    if word1_2[1] is None:
        print("Open what?")
        return False
    elif word1_2[1] == "inventory":
        print("Inventory:")
        for item in player1.inventory:
            print("  " + str(player1.inventory.index(item)+1) + ". " + item) #Nicely formats inventory
    elif word1_2[1] == "map":
        if 'map' in player1.inventory:
            print("The map is to faded to read.") #Needed more time to add print_map function
        else:
            print("You do not have a map currently")
    else:
        print("You can't open that!")
        
        
def user_quit(word1_2):
    """ "Quit" was entered. Check the rest of the command to see whether we really quit the game.
        Parameters
        ----------
        word1_2: tuple of two charcters 
    
        Returns true, if this command quits the game, false otherwise.
    """
    if word1_2[1] is not None:
        print("Quit what?")
        return False
    else:
        return True  # signal that we want to quit

def game_complete():
        """ Checks player position if they have fufilled a win condition
        """
        if player1.position == (0,5):
            print("\n\tCONGLATURATION !!@!1\n\tA WINNER IS YOU!!1")
            return True # signal that we want to end the game
        else:
            return False 

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Game starts here 
# Print out the opening message for the player
print(" _    _                   _____ ")
print("| |  | |                 /  ___|")
print("| |  | |       ___       \\ `--. ")
print("| |/\\| |      / _ \\       `--. \\")
print("\\  /\\  /  _  | (_) |  _  /\\__/ /")
print(" \\/  \\/  (_)  \\___/  (_) \\____/ ")

print("\nWelcome to the WORLD OF SURVIVE!")
print("W.o.S is a new, incredibly boring adventure game.")
print("Type 'help' if you need help.")

#Set up of Map/Room + Player 
n=Map(coord_setup())
player1 = Player((2,0)) #Set players initial co-ordinates
weight_limit = 3

#Game Loop
finished = False
while finished == False:
    print("-----------------------------------------------------------------------")
    print("\n" + str(n.rooms[player1.position].description)[2:-2] + "\n" + n.return_item_string(player1.position) + "\n" + n.return_exit_string(player1.position))
    command = Command().user_input()
    state1 = process_command(command)
    state2 = game_complete()
    if  state1 or state2 == True: #checks if a win/quit state has been reached
        finished = True
print("\nThank you for playing. Good bye.")