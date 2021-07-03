user_input = ""
is_started = False

while True:
    user_input = input("> ").lower()
    if user_input == "help":
        print("""
start - to start the car 
stop - to stop the car 
quit - to quit
        """)
    elif user_input == "start" and is_started == False:
        print("Car started...Ready to go! \n")
        is_started = True
    elif user_input == "stop" and is_started == True:
        print("Car  Stopped.\n")
        is_started = False
    elif user_input == "start" and is_started == True:
        print("The car is already started!\n")
    elif user_input == "stop" and is_started == False:
        print("Car is already stopped!\n")
    elif user_input == "quit":
        break
    else:
        print("I don't understand that...\n")

# ## Another Way is ##

# # veration one
# if user_input == "start":
#     if is_started:
#         print("Car already started!")
#     else:
#     is_started = True
#     print("Car started...")

# # veration two
# if user_input == "start" and is_started == False:
#     print("Car started...Ready to go! \n")
#     is_started = True
# elif user_input == "start" and is_started == True:
#     print("The car is already started!\n")
