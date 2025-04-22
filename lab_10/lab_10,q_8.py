r = open("record8.txt","r")
t = open("newrecord8.txt","w")
s = r.readlines()
for i in s:
    i = i.split()
    for j in i:
        if j  not in "a,an,the":
            t.write(j)
t.close()
r.close()
