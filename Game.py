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
        pass

    return want_to_quit

def go_room(word1_2):
    """ Try to in to one direction. If there is an exit, enter the new
        room, otherwise print an error message.
        Parameters
        ----------
        word1_2: tuple of two charcters 
        """
    if word1_2[1] in n.return_exit_string(player_pos): #validate action
        #update_player_pos
        pass

        


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
        """ Checks game state to see if the game is complete
        """
        if player_pos == (0,5):
            print("\n\tCONGLATURATION !!@!1\n\tA WINNER IS YOU!!1")
            return True # signal that we want to end the game
        else:
            return False 



#Print out the opening message for the player
print()
print("Welcome to the WORLD OF SURVIVE!")
print("W.o.S is a new, incredibly boring adventure game.")
print("Type 'help' if you need help.")

n=Map(coord_setup())
player_pos = (0,5)
print(n.return_exit_string(player_pos))

#Game Loop
finished = False
while finished == False:
    command = Command().user_input()
    state1 = process_command(command)
    state2 = game_complete()
    if  state1 or state2 == True: #checks if a win/quit state has been reached
        finished = True
print("\nThank you for playing. Good bye.")