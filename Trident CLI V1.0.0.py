# TRIDENT CLI V1.0

# Setup.
VALID_COMMANDS = ["help", "quit"]
command_no = 0
running = True
print("TRIDENT CLI V1.0")

# Main loop
while running:
    # Set things up for the next line.
    command_no += 1
    
    # Get user input.
    command = input("Enter command > ")

    # Check if it's an excecutable command or not
    if command in VALID_COMMANDS:
        # Valid command

        if command == "help":
            # help - returns a list of all valid commands
            print("""Valid commands:
"help"
"quit" """)
        elif command == "quit":
            # quit - quits the program
            running = False
            print("Interface stopped.")
    else:
        # Invalid command. Return an error
        print("Invalid command. (Use \"help\" for a list of valis commands.")
