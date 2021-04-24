#float because the value will be in decimal in decimal
height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))
#bmi is weight divided by height to power of 2
#round to print a whole number
bmi = round(weight / height ** 2)
print(f'Your BMI is: {bmi}')
if bmi <= 18.5:
    print('you\'re underweight')
elif bmi >=18.5 and bmi <=25:
    print('normal weight')
elif bmi >=25 and bmi <30:
    print('overweight')
elif bmi >30 and bmi <35:
    print('obese')
else:
    print('clinically obese')