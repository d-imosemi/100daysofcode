print('Welcome to my calculator')
bill = float(input('What was the total bill? #'))
tip = int(input('What percentage tip woulld be given to waiter? 10, 15, 20: '))
share = int(input('How many people will share the bill: '))
new_pay = tip / 100 * bill + bill
total = round(new_pay / share)
print('Each person should pay: #',total)