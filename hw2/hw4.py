num1 = int(input("num1 = "))
num2 = int(input("num2 = "))

if (num1 > num2):
    max = num1
    min = num2
else:
    max = num2
    min = num1

while (min != 0):
    #print(max % min)
    num = min
    min = max % num
    max = num

print(max)