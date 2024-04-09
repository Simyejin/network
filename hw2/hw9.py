d = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]

for user in d:
    if user['phone'].endswith('8'):
        print(user['name'])

print(' ')

for user in d:
    if not user['email']:
        print(user['name'])

print('')

name = input()
found = False
for user in d:
    if user['name'] == name:
        print(f"전화번호: {user['phone']}")
        print(f"이메일: {user['email'] if user['email'] else '이메일 없음'}")
        found = True
        break
if not found:
    print("이름이 없습니다.")