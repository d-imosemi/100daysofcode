#used an integer
age = int(input('What is your current age? '))
#minus life expectancy with any inputes age
new_age = 90 - age
#multiply new_age with days, weeks and months
days = new_age * 365
weeks = new_age * 52
months = new_age * 12
print('You have', days, 'days', weeks, 'weeks', 'and', months, 'months', 'left.')