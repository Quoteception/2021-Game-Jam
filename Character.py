class Player():
    """ The player class is tbe base class for all entinties in the game. Including NPCs as well as monsters each class/subclass
        is able to have thier own position and inventory 
    """
    def __init__(self, position=(2,0), history=[(2,0)], inventory=[]):
        self.position = position
        self.history = history
        self.inventory = inventory
        
    def update_player_pos(self, direction):
        """ Turns the player position tuple into a list then updates the
            values depending on the given direction.
            Also stores a list of previously visited rooms

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
    
    def back_update(self):
        """ Removes the last visted room and returns player to the previous room
        """
        if len(self.history) == 1:
            print("You can not go back!")
        elif len(self.history) == 2:
            self.history.pop()
            self.position = self.history[0]
        elif len(self.history) >= 3 :
            self.history.pop()
            self.position = self.history[-1]
            