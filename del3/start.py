z = int(input("Enter amount of numbers "))
i = 0
sum = 0
print('Enter %d number' % z)
while i < z:
    k = int(input())
    if k % 3 == 0:
        sum += k
    i += 1
print(sum)
