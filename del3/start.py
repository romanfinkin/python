z = int(input("Enter amount of numbers "))
i = 0
sum = 0
k = int(input('Enter %d numbers' % z))
while i < z:
    if k % 3 == 0:
        sum += k
    i += 1
print(sum)
