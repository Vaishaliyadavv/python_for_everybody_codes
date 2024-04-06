import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1945987.txt"
handle = open(name)
data = handle.read()
numbers = re.findall('[0-9]+', data)
# print(numbers)
total = 0
for i in numbers:
    total = total + int(i)
print(total)

