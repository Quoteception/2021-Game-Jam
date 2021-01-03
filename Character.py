class Player():
    """ The player class is tbe base class for all entinties in the game. Including NPCs as well as monsters each class/subclass
        is able to have thier own position and inventory 
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

            Parameters
            ----------
            direction: string
        """
        if direction == 'north':
            self.history.append(self.position)
            update=[]
            update = list(self.position)
            update[1]=update[1]+1
            self.position = tuple(update)
            return False
        elif direction == 'south':
            self.history.append(self.position)
            update=[]
            update = list(self.position)
            update[1]=update[1]-1
            self.position = tuple(update)
            return False
        elif direction == 'east':
            self.history.append(self.position)
            update=[]
            update = list(self.position)
            update[0]=update[0]+1
            self.position = tuple(update)
            return False
        elif direction == 'west':
            self.history.append(self.position)
            update=[]
            update = list(self.position)
            update[0]=update[0]-1
            self.position = tuple(update)
            return False