def check():
    z = int(input("Enter amount of numbers "))
    i = 0
    sum = 0
    while i < z:
        k = int(input("Enter integer "))
        if k % 3 == 0:
            sum += k
        i += 1
    print(sum)


check()