class Command():
    """ This class handles requests to do with the usable commands

        Parameter(s)
        ------------
        
    """
    def __init__ (self):
        #Valid commands
        self.actions = {
            "go", "quit", "help", "back", "take", "open", "drop"
        }

    def user_input(self):
        """ Returns The next command from the user as a tuple

            splits the imput string and runs a small test to see if it word1
            is a vlaid command.
        """
        # Initialise word1 and word2 to <None>
        word1 = None        # None is a special Python value that says the variable contains nothing
        word2 = None

        input_line = input("> ").lower()
        print()
        # Find up to two words on the line and set word1 and word2 appropriately
        tokens = input_line.strip().split( " " )
        if len( tokens ) > 0:
            word1 = tokens[0]
            if len( tokens ) > 1:
                word2 = tokens[1]
        if word1 not in self.actions:
            print("I don't know what you mean...")
            return (None, word2)
        else:
            return (word1, word2)

    def user_help(self):
        """ Print out some help information. """
        print("You are lost. You are alone. You wander....")
        print("Your command words are:")
        for command in self.actions:
                print( command + " ", end="" )  
                # 'end' is a keyword argument that determines the character printed at the end of the string
                # This defaults to the newline character but here we are setting it to the blank string
                # This means each command follows the previous one on the same line
        print()