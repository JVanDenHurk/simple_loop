user_input = ""

while user_input.lower() != "quit":
    user_input = input("> ")
    if user_input.lower() == "help":
        print(f"start - to start the car \nstop - to stop the car \nquit - to exit \n")
    elif user_input.lower() == "start":
        print(f"Car started...Ready to go! \n")
    elif user_input.lower() == "stop":
        print(f"Car  Stopped.\n")
    elif user_input == "quit":
        print("")
    else:
        print("I don't understand that...\n")
