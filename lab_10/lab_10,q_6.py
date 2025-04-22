w = open("q_5record1.txt","r")
q = open("q_5record2.txt","r")
p = open("q_6record1.txt","w")
while True:
    l = w.readline()
    b = q.readline()
    if not l and not b:
        break
    if l:
        p.write(l)
    if b:
        p.write(b)
    
w.close()
q.close()
p.close()
