def sorter(l):
    o = [i[1] for i in l]
    c = 0
    o.sort()
    for n in o:
        for i in range(len(l)):
            if l[i][1] == n:
                print(l[i])
s = [('asd',123),('rgrbrb',2456),('rty',567),('mikjh',1348)]
sorter(s)
