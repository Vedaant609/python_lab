def counter(l):
    counter_b = 0
    counter_g = 0
    for i in l:
        if isinstance(i,tuple):
            for j in i:
                counter_b+=1
        else:
            counter_g+=1
    print(counter_b,"boys")
    print(counter_g,"girls")
l = ["dhyani",("vedaant",),"nirmal","akruti",("manthan","vakil","utsav")]
counter(l)
