a = [1,2,3,4,5,0,6]
b = [2,4,6]

def arrayDiff(first, second):
    arr = []
    for i in first:
        if i not in second:
            arr.append(i)
    return arr

b = arrayDiff(a,b)
print(b)