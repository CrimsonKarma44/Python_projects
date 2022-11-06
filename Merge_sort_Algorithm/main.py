'''Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
Examples

[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''
def find_it(seq):
    cat = {}
    for v, i in enumerate(seq):
        if i in seq[0:v+1]:
            cat[i] = seq.count(i)
    value = [i for i in cat.values() if i%2 != 0]
    valu = [i for i in cat if cat[i]==max(value)]
    return int(valu[0])


lov = find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])
print(lov)
love =find_it([1,1,2])
print(love)
love =find_it([0,1,0,1,0])
print(love)
love =find_it([0])
print(love)
