

def lost():
    s1 = input("Enter prime number ")
    i = 0
    z = s1[i]
    x = s1[i]
    while i != len(s1)-1:
        if z < s1[i+1]:
            z = s1[i+1]
        if x > s1[i+1]:
            x = s1[i+1]
        i += 1

    print("big number",z)
    print("small number ", x)





 #   s = s1[0]
 #   x = s1[1]
 #   print("s=", s)
 #   if x>s :
 #       s=x
 #   print("s=", s)


lost()