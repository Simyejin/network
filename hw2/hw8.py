days = {'January':31, 'February':28, 'March':31, 'April':30, 
'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30, 
'December':31}

user = input()

if user in days:
    print(days[user])

print('---')

print(sorted(days))

print('---')

for i, j in days.items():
    if j == 31:
        print(i)

print('---')

for i, j in sorted(days.items(), key = lambda x : x[1]):
    print(i, ":", j)

print('---')

user = input()
for i, j in days.items():
    if i.startswith(user):
        print(j)
        break