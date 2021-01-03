class Player():
    """ The player class is tbe base class for all entinties in the game. Including NPCs as well as monsters each class/subclass
        is able to have thier own position and inventory

        Parameter(s)
        ------------
        position: players current co-ordinate position (tuple)
        history: a list of previously visited rooms (list)
        inventory: a list of items currently on the player (list)
    """
    def __init__(self, position, history=[], inventory=[]):
        #Sets starting parameters
        self.position = position
        self.history = history
        self.inventory = inventory

    def update_player_pos(self, direction):
        """ Turns the player position tuple into a list then updates the
            values depending on the given direction.
            Also stores a list of previously visited rooms

            Included in seperate file for clarity

            Parameter(s)
            ------------
            direction: string
        """
        update=[]
        self.history.append(self.position)
        update = list(self.position) #unlocks the tuple briefly so it can be edited
        if direction == 'north':
            update[1]=update[1]+1
        elif direction == 'south':
            update[1]=update[1]-1
        elif direction == 'east':
            update[0]=update[0]+1 
        elif direction == 'west':
            update[0]=update[0]-1
        self.position = tuple(update)
        return False