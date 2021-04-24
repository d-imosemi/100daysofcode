print('welcome to python pizza delieveries!')
size = input('What size of pizza do you want? S, M, or L: ')
add_pepperoni = input('do you want to add pepperoni? Y or N: ')
etra_cheese = input('do you want extra etra_cheese? Y or N: ')
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
if etra_cheese == 'Y':
    bill += 1
print(f'Your final bill is: #{bill}')

