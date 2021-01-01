
class Room():
    def __init__(self, pos, description=None, inventory=None, entities=None):
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
        self.rooms={}
        for pos in cells.keys():
            room=Room(pos)
            room.set_exits(cells[pos])
            self.rooms[pos]=room

def coord_setup():
    HEIGHT=6
    WIDTH=4
    # Enter room co-ordinates 
    path_dict={(0,5):[], 
    (0,4):['N','E'],
    (2,5):[], # No new S/W exits
    (2,4):['N'],
    (0,3):['N','E'],
    (1,4):[], # No new S/W exits
    (1,3):['N','E'],
    (2,3):['N'],
    (1,2):['N'],
    (1,1):['N','E'],
    (2,2):[], # No new S/W exits
    (2,1):['N','E'],
    (3,1):['N'],
    (3,2):[], # No new S/W exits
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


n=Map(coord_setup())
for room in n.rooms:
    print((str(room.pos))+' with exits '+(room.exits))