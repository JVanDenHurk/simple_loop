user_input = input("> ")

while True:
    if user_input.lower() == "help":
        print(f"start - to start the car \nstop - to stop the car \nquit - to exit \n")
        user_input = input("> ")
    elif user_input.lower() == "start":
        print(f"Car started...Ready to go! \n")
        user_input = input("> ")
    elif user_input.lower() == "stop":
        print(f"Car  Stopped.\n")
        user_input = input("> ")
    elif user_input.lower() == "quit":
        break
    else:
        print("I don't understand that...\n")
        user_input = input("> ")
