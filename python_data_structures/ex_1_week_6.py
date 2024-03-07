name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hours_dict = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            time = words[5].split(':')
            hours = time[0]
            hours_dict[hours] = hours_dict.get(hours, 0) + 1
# print(hours_dict)
for hour, count in sorted(hours_dict.items()):
    print(hour, count)
