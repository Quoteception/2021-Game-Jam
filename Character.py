class Player():
    """ The player class is tbe base class for all entinties in the game. Including NPCs as well as monsters each class/subclass
        is able to have thier own position and inventory 
    """
    def __init__(self, position=(2,0)):
        self.position = position
    def update_player_pos(self, direction):
        """ Turns the player position tuple into a list then updates the
            values depending on the given direction 

            Parameters
            ----------
            direction: string
        """
        if direction == 'north':
            update=[]
            update = list(self.position)
            update[1]=update[1]+1
            self.position = tuple(update)
            return False
        elif direction == 'south':
            update=[]
            update = list(self.position)
            update[1]=update[1]-1
            self.position = tuple(update)
            return False
        elif direction == 'east':
            update=[]
            update = list(self.position)
            update[0]=update[0]+1
            self.position = tuple(update)
            return False
        elif direction == 'west':
            update=[]
            update = list(self.position)
            update[0]=update[0]-1
            self.position = tuple(update)
            return False