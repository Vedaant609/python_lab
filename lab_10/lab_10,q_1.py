import csv
w = open("vedaant.csv","a")
l = [["vedaant",98],["manthan",98],["vakil",96],["utsav",95],["nirmal",96]]
r = csv.writer(w)
r.writerows(l)
w.close()


