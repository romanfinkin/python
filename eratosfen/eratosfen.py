def check():
    n = int(input("endter "))
    s = list(range(n + 1))
    s[1] = 0 
    for i in s:
        if i > 1:
            for j in range(i + i, len(s), i):
                s[j] = 0
    print(s)


check()