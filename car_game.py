car_action = ""
car_state = "stop"
print('Enter "help" for list of commands')
while True:
    car_action = input('> ').upper()
    if car_action == "HELP":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif car_action == 'QUIT':
        print('DONE')
        break
    elif car_action == "START" and not car_state.upper() == "START":
        print('Car started...Ready to go!')
        car_state = car_action
    elif car_action == "STOP"and not car_state.upper() == "STOP":
        print('Car stopped.')
        car_state = car_action
    elif car_action == "START" and car_state.upper() == "START":
        print('Car is already started!')
    elif car_action == "STOP"and car_state.upper() == "STOP":
        print('Car is already stopped!')
    else:
        print("I don't understand that...")