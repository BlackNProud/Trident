# TRIDENT CLI V2.0

# Setup.
VALID_COMMANDS = ["help", "quit", "var"]
command_no = 0
running = True
variables = {}
print("TRIDENT CLI V1.0")
print("Use \"help\" for a list of valid commands")

# Main loop
while running:
    # Set things up for the next line.
    command_no += 1
    
    # Get user input.
    raw_command = input("Enter command > ")

    # Separate the input into a list of strings, where each space is a separate word
    args = raw_command.split()
    command = args[0]

    # Check if it's an excecutable command or not
    if command in VALID_COMMANDS:
        # Valid command

        if command == "help":
            # help - returns a list of all valid commands
            print("""Valid commands:
"help"
"quit"
"var add <name>"
"var set <name> <value>"
"var remove <name>"
"var viewall" """)
        elif command == "quit":
            # quit - quits the program
            running = False
            print("Interface stopped.")
        elif command == "var":
            if args[1] == "add":
                try:
                    varname = str(args[2])
                    variables.update({varname: 0})
                    print("Variable %s added with value of 0" % (varname))
                except:
                    print("Could not create variable, try again")
            elif args[1] == "viewall":
                if len(variables) == 0:
                    print("No variables have been created yet")
                else:
                    print("Created variables:")
                    print(variables)
            elif args[1] == "set":
                try:
                    if args[2] in variables.keys():
                        variables.update({args[2]: args[3]})
                        print("Variable %s updated with value of %s" % (args[2],args[3]))
                    else:
                        print("Variable " + args[2] + " does not exist")
                except:
                    print("Could not update variable.")
            elif args[1] == "remove":
                try:
                    if args[2] in variables.keys():
                        temp = variables.pop(args[2])
                        print("Variable %s deleted" % (args[2]))
                    else:
                        print("Variable " + args[2] + " does not exist")
                except:
                    print("Could not delete variable.")
            else:
                print("Invalid variable command.")
    else:
        # Invalid command. Return an error
        print("Invalid command. (Use \"help\" for a list of valid commands")
