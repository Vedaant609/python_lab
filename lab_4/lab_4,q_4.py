def is_prime(a):
    t = 0
    for i in range(2,a):
        if a%i == 0:
            t+=1
    if t >0:
        print("the number is not prime")
    else:
        print("the number is prime")

def is_perfect(a):
    t = []
    for i in range(1,a):
        if a%i == 0:
            t.append(i)
    if sum(t)==a:
        print("the number is perfect")
    else:
        print("the number is not perfect")
def is_pelindrome(a):
    t = str(a)
    if t == t[::-1]:
        print("palindrome")
    else:
        print("not pelindrome")
def is_armstrong(a):
    new_a = a
    t = []
    counter = 0
    while a%10 !=0:
        u = int(a%10)
        a = (a-u)/10
        t.append(u)
    for i in t:
        counter+= i**len(t)
    if counter == new_a:
        print("armstron")
    else:
        print("not armstrong")

def is_automorphic(a):
    y = str(a)
    t = a**2
    t = str(t)
    
    if t.endswith(y) == True:
        print("automorphic")
    else:
        print("not automorphic")
print('''

1.prime
2.perfect
3.pelindrome
4.armstrong
5.automorphic''')
num = int(input("enter"))
r = int(input("enter the value"))
if num == 1:
    is_prime(r)
elif num == 2:
    is_perfect(r)
elif num == 3:
    is_pelindrome(r)
elif num == 4:
    is_armstrong(r)
elif num == 5:
    is_automorphic(r)
    
            
    
    
















    
