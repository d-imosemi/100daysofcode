print('''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 ''')

print('welcome to the treasure island\n', 'your mission is to find the treasure.')
start = input('Were do you wish to start from? Left or Right: ').lower()
if start == 'left':
    river = input('This is a big river, a boat might arrive soon, what do you wanna do? swim or wait: ').lower()
    if river == 'wait':
        door = input('You are almost close "PICK WISELY!!!" Which colour do you pick? red, blue, yellow: ').lower()
        if door == 'yellow':
             print('You found the teasure, YOU WON!!!')
        elif door == 'red':
             print('There is fire in the room, GAME OVER!!!')
        elif door == 'blue':
             print('You have been frozen to death, GAME OVER!!!')
        else:
            print('There is fire in the room, GAME OVER!!!')
    else:
        print('you have been eaten by a beast, GAME OVER!!!')
else:
    print('Wrong choice, GAME OVER!!!')

