# import random

# dice = random.randint(0, 1)
# if dice == 1:
#     print('Head')
# else:
#     print('Tail')
import random
people_name = input('Enter the names of people with comma: ').split()
#use the .split to arrange the imput in a specific

#use the .choice to get a random element fromt he list
person_who_will_pay = random.choice(people_name)
print(person_who_will_pay , 'is going to buy the meal today')