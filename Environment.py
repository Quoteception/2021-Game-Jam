class Room():
    """Room class handles the name and descriptions
    """
    def __init__(self, pos, description=None, inventory=None, entities=None):
        self.pos=pos
        self.description=description
        self.inventory=inventory
        self.entities=entities
        self.exits={"N":False, "S":False, "E":False, "W":False}
    
    def set_desctription(self, pos):
        """Input description for each room here, if cell key matches update description
        """
        des_dict = { 
            (0,5):['[TBA]'],
            (0,4):['[TBA]'], 
            (2,5):['[TBA]'], 
            (2,4):['[TBA]'], 
            (0,3):['[TBA]'], 
            (1,4):['[TBA]'], 
            (1,3):['[TBA]'], 
            (2,3):['[TBA]'], 
            (1,2):['in a long, dimly lit path.'],
            (1,1):['to your south there is a room with a faint glow.'], 
            (2,2):['seems to be a dead-end'], 
            (2,1):['confronted by a 3-way split in the cave, there is a left, centre, and right path. Centre path is blocked but strange noise can be heard beyond...'],
            (3,1):['in the right path of the cave.'], 
            (3,2):['seems to be a dead-end'], 
            (1,0):['in a room with glowing key. It looks like you can take it'], 
            (2,0):['infront of the entrance to a cave. The entrance is big and round and is dark inside.']} 
        
        if pos in des_dict.keys():
            self.description = des_dict[pos]

        
    def set_exits(self, exits):
        """ Allow exit setup during map generation
        exits = list e.g. [N/S/E/W]
        """
        while True:
            try:
                if exits[0] is not None:
                    for e in exits:
                        if e[0] in self.exits.keys():
                            self.exits[e[0]] = True
                break
            except IndexError:
                break

class Map():
    """ Map class set up a grid of co-ordinates. #Takes the keys (postions)
        and assigns each one a room class, then passes it to Room class

        Parameter
        ---------
        cells: dictionary of each co-ordinate and what exits it has
    """
    def __init__(self, cells):
        self.rooms={} #initialise dictionary of rooms
        for pos in cells.keys(): 
            room=Room(pos)
            room.set_exits(cells[pos])
            room.set_desctription(pos)
            self.rooms[pos]=room
            
    def return_exit_string(self, pos):
        """ Returns to the user what the possible exits are

            Parameters
            ----------
            pos: current room positiion 
        """
        print
        return_string = "Exits:"
        direction = {'N':'north','S':'south','E':'east','W':'west'} #Formatting 
        for path in self.rooms[(pos)].exits.items():
            if path[1]: #checks if the value is true, if so add to string
                return_string += " " + direction[path[0]]
        return(return_string)

def coord_setup():
    """ One a hard set grid size, add rooms via path dictionary, function adds paths to reduce human error

        Returns a dictionary of all rooms

        Parameters
        ----------
        
    """
    # Grid size
    HEIGHT=6
    WIDTH=4
    # Enter room co-ordinates 
    path_dict={
    (0,4):['N','E'],   
    (2,4):['N'],
    (0,3):['N','E'],   
    (1,3):['N','E'],
    (2,3):['N'],
    (1,2):['N'],
    (1,1):['N','E'],
    (2,1):['N','E'],
    (3,1):['N'],
    (1,0):['N'],
    (2,0):['N']}
    # Mask paths to co-ordinates in a 4x6 grid
    coord_dict = {}
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x,y) in path_dict.keys():
                coord_dict[(x,y)] = path_dict[(x,y)]
            else:
                coord_dict[(x,y)] = []
    # Adds a opposite exit to added rooms (saves having to do this manually)
    for item in coord_dict.items(): # dict.items = [coord,paths]
        if len(item[1]) > 0:
            if 'N' in item[1]:
                # append S to the cell North of the 'N' flagged cell 
                coord_dict[item[0][0],(item[0][1]+1)].append('S')
            if 'E' in item[1]:
                # append W to the cell East of the 'E' flagged cell
                coord_dict[(item[0][0]+1),(item[0][1])].append('W')
    return coord_dict