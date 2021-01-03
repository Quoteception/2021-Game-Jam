LAB session 3
GAME: World of Survive
Description:
	In this game we take control of a character stranded in the depths of the mountains. 
 	They find a cave to rest in for the time being but all is not as it seems

To complete the game you just have to reach the other side of the cave.

Important implementation features:
	For this project I converted the room system given to a much easier to edit co-ordinate system. Where each "cell" has it own  changable varibles for its exits, description, as   well as any items contained in said cell.

Classes:
  class Map():
    """ Map class set up a grid of co-ordinates. Takes the keys (postions)
        and assigns each one a room class, then passes it to Room class

        Parameter
        ---------
        cells: dictionary of each co-ordinate and what exits it has
    """
    
    class Room():
    """ Room class handles the name and descriptions

        Parameter(s)
        ---------
        pos: co-ordinate position (tuple)
        description: flavour text for the room (list of strings)
        items: a list of strings for items in a room (list of strings)
    """
    
    class Player():
    """ The player class is tbe base class for all entinties in the game. Including NPCs as well as monsters each class/subclass
        is able to have thier own position and inventory

        Parameter(s)
        -----------
        position: players current co-ordinate position (tuple)
        history: a list of previously visited rooms (list)
        inventory: a list of items currently on the player (list)
    """
    
   class Command():
    """ This class handles requests to do with the usable commands

        Parameter(s)
        ------------
        [N/A]
    """
    
Special features:
	Unfortunately, due to unforseen time constraints (having to restart the project due to my group leaving) I haven't been able to add something particualy noteworthy for 	the player to do . 
	However, I hope the way that I've constructed the layout of the game which allows for very easy room creation as well as editing is a unique way of tackling the task.
	
