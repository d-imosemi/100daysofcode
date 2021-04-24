from art_calc import logo_calc
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operetions = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calc():
    print(logo_calc)
    num1 = float(input('What"s the first number?: '))
    for symbol in operetions:
        print(symbol)
    should_continue = True

    while should_continue:
        operetion_symbol = input('pick an operation: ')
        num2 = float(input("what's the next number?: "))
        calculation_function = operetions[operetion_symbol]
        answer = calculation_function(num1, num2)
        print(f'{num1} {operetion_symbol} {num2} = {answer}')
        if input(f'type "y" to continue with {answer}, or type "n" to start a new calculation: ') == 'y':
            num1 = answer
        else:
            should_continue = False
            calc()
calc()