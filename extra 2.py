arr = [1,2,3,4,5,6,7,8,9,10]

def f3(arr):
    return list(map(lambda x: x*x, arr))


print ("with map",f3(arr),"\n")


res = [x*x for x in range(11)]

print ("with list comp.",res)