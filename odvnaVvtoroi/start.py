def banana():
    x = input("enter str 1 ")
    y = input("enter str 2 ")

    if x.find(y, 0, len(x)) != -1:
        print("str 2 belongs str 1")
    else:
        print("sorry try again")

banana()