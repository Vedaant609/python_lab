def sanitiser(x,c =0):
    if len(x) == c:
        return []
    return ([0] if x[c]<0 else [x[c]])+(sanitiser(x,c+1))
print(sanitiser([1,2,3,4,-6,-4,-1]))
