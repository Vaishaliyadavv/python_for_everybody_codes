f_name = input('Enter file:')
try:
    if len(f_name) < 1:
        f_name = "mbox-short.txt"
    f_hand = open(f_name)
except FileNotFoundError:
    print('File not found')
    quit()

senders = dict()
for line in f_hand:
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            sender = words[1]
            senders[sender] = senders.get(sender, 0) + 1

max_sender = None
max_count = None
for sender, count in senders.items():
    if max_count is None or count > max_count:
        max_sender = sender
        max_count = count
print(max_sender, max_count)
