q = open("q_5record1.txt","w")
w = "Vedaant is a good boi"
q.write(w)
q.close()
e = open("q_5record2.txt","w")
q = open("q_5record1.txt","r")
c = q.read()
c = c.upper()
e.write(c)
q.close()
e.close()

