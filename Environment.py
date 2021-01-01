
class Room():
    def __init__(self, pos, description, inventory=None, entities=None):
        self.pos=pos
        self.description=description
        self.inventory=inventory
        self.entities=entities
        self.exits={"N":False, "S":False, "E":False, "W":False}
    
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
    """ Map class set up a grid of co-ordinates 
    """
    def __init__(self, cells):
        self.rooms=set()
        for cell in cells.keys():
            room=Room(cell,None,)
            room.set_exits(cells[cell])
            self.rooms.add(room)

def coord_setup():
    HEIGHT=7
    WIDTH=5
    # Enter room co-ordinates 
    path_dict={(0,5):['N'],
                (0,4):['N','E'],                              (3,4):['N'],
                (0,3):['N','E'], (1,3):['N','E'],(2,3):['E'], (3,3):['N'],
                                 (1,2):['N'],
                (0,1):['E'],     (1,1):['N','E'], (2,1):['E'],(3,1):['N','E'], (4,1):['N'],
                (0,0):['N'],                                  (3,0):['N']}
    coord_dict = {} 
    # Mask paths to co-ordinates in a 5x7 grid 
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


"""
TEST CODE:
n = Map(coord_setup())
for room in n.rooms:
    print((str(room.pos))+' with exits '+str(room.exits))
"""