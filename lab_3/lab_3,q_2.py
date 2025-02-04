def lower(a):
    for i in a:
        if i>='A' and i<='Z':
            t= ord(i)+32
            print(chr(t),end = '')
def upper(a):
    for i in a:
        if i>='a' and i<='z':
            t= ord(i)-32
            print(chr(t),end = '')
        
def toggle(a):
    for i in a:
        if i>='A' and i<='Z':
            t= ord(i)+32
            print(chr(t),end = '')
        elif i>='a' and i<='z':
            t= ord(i)-32
            print(chr(t),end = '')
st = input('enter the string')
y = int(input('''enter choice
        1. lower
        2. upper
        3. toggle'''))
if y==1:
    lower(st)
elif y==2:
    upper(st)
else:
    toggle(st)
