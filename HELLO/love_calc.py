print('welcome to the love calculator')
name1 = input('What is your name? \n')
name2 = input('what is their name? \n')
total = name1 + name2
total.count('truelove')
total1 = total.lower()

t = total1.count('t')
r = total1.count('r')
u = total1.count('u')
e = total1.count('e')

true = t + r + u + e

l = total1.count('l')
o = total1.count('o')
v = total1.count('v')
e = total1.count('e')

love = l + o + v + e
love_score = int(str(true) + str(love))
print(love_score, '%')
if love_score < 10 or love_score > 90:
    print(f'your score is , {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <= 50:
    print(f'your score is {love_score} you are alright together.')
else:
    print(f'your score is {love_score}')