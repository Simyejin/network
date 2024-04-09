from random import randint
money = 50

while (money > 0 and money < 100):
    coin = randint(1, 2)
    guess = randint(1, 2)
    if (coin == guess):
        money += 9
    else:
        money -= 10

print("my money = ", money)