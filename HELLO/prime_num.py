
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == n:
            is_prime = False
    if is_prime:
        print('it\'s a prime number')
    else:
        print('it\'s not a prime number')


n =int(input('check this number: '))
prime_checker(number=n)