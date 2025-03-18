def peli(x):
    if x == x[::-1]:
        return True
    else:
        return False

a = input("enter the string")
b = peli(a)
print(b)
