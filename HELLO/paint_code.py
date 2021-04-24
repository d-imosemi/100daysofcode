import math
def paint_calc(height, width, cover):
    area = height * width
    num = math.ceil(area / cover)
    print(f'you\'ll need {num} cans of paint')


test_h = int(input('Height of wall: '))
test_w = int(input('width of wall: '))
coverage = 5


paint_calc(height=test_h, width=test_w, cover=coverage)

