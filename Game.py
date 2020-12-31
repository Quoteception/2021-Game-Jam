class Room():
    def __init__(self, pos, description, inventory=None, entities=None):
        self.pos=pos
        self.description=description
        self.inventory=inventory
        self.entities=entities
        self.exits={"north":False, "south":False, "east":False, "west":False}

    def set_exits(self, exits):
        """ init exits """
        if exits isinstance(list):
            for e in exits:
                if e in self.exits.keys():
                    self.exits[e[0]]=True

    def get_look(self):
        """ out descrpiton 
        """
        pass 
