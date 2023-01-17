import math
data = open('input_day25.txt', 'r')
snafus = data.read().strip().split('\n')

numbers = []
for snafu in snafus:
    number = 0
    elements = len(snafu)
    positions = [pow(5,j) for j in range(elements)]
    for index, i in enumerate(snafu):
        if i == '2':
            i = 2
        elif i == '1':
            i = 1
        elif i == '0':
            i == 0
        elif i == '-':
            i = -1
        elif i == '=':
            i = -2
        number = number + i*positions[len(snafu)-index]
        numbers.append(number)
snafu_total = sum(numbers)
print(snafu_total)


new_snafu_total = str(snafu_total)
len_snafu = len(new_snafu_total)
new_numbers = ''
for index, i in enumerate(new_snafu_total):
    pass