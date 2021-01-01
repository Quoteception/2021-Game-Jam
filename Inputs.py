valid_commands = {
            "go", "quit", "help", "back"
        }

def user_input():
    # Initialise word1 and word2 to <None>
    word1 = None        # None is a special Python value that says the variable contains nothing
    word2 = None

    input_line = input( "> " ).lower()

    # Find up to two words on the line and set word1 and word2 appropriately
    tokens = input_line.strip().split( " " )
    if len( tokens ) > 0:
        word1 = tokens[0]
        if len( tokens ) > 1:
            word2 = tokens[1]
    if word1 not in valid_commands:
        print("I don't know what you mean...")
        return (None, word2)
    else:
        return (word1, word2)

def user_help():
    """ Print out some help information. """
    print("You are lost. You are alone. You wander....\n")
    print("Your command words are:")
    for command in valid_commands:
            print( command + " ", end="" )  
            # 'end' is a keyword argument that determines the character printed at the end of the string
            # This defaults to the newline character but here we are setting it to the blank string
            # This means each command follows the previous one on the same line
    print()



