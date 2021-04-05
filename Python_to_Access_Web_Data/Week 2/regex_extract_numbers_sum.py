import re

numlist = []
hand = open('regex_sum_1195433.txt')
for line in hand:
    # remove trailing spaces
    line = line.rstrip()
    # match and return digits from each line
    num = re.findall('([0-9]+)', line)
    # append all numbers in num into numlist
    x = 0
    while x < len(num):
        numlist.append(int(num[x]))
        x += 1
print(sum(numlist))
