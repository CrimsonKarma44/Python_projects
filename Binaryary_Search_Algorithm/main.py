
def slicer(arr, target, count = 0):
    arr = list(arr)
    arr.sort()
    # print(arr)
    mid = int(len(arr)/2)
    if len(arr) == 1:
        if arr[0] == target:
            print("'{}' Found in {} steps".format(target, count))
        else:
            print("'{}' not found".format(target))

    else:
        if target > arr[mid-1]:
            arr = arr[mid:]
        else:
            arr = arr[0:mid]
        
        count+=1
        slicer(arr, target, count)


slicer([10,4,3,8,9,5,2,4,3], 4)
print()
slicer(range(0, 1000000), 99)
