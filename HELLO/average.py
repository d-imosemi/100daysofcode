stu_hei = input('enter a list of student heights: ').split()
for n in range(0, len(stu_hei)):
    stu_hei[n] = int(stu_hei[n])
print(stu_hei)
total_height = 0
for height in stu_hei:
    total_height += height
print(total_height)

number_of_students = 0
for student in stu_hei:
    number_of_students += 1
print(number_of_students)

ans = round(total_height / number_of_students)
print(ans)