import csv
w = open("record(lab_10,q_2).csv","r")#pre existing data
a = csv.reader(w)
x = {}
for i in a:
    x[i[0]] = i[1::]
print(x)
x.pop("rollno")
for i in x:
    print(int(x[i][-1])+int(x[i][-2])+int(x[i][-3]))

    

