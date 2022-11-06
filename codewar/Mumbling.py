'''Description:

This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

def accum(text):
    dump = ''
    for v, i in enumerate(text):
        count = 0
        dump+=i.upper()
        while count < v:
            dump+=i.lower()
            count+=1
        if count != len(text)-1:
            dump+='-'
    return dump
print(accum("device"))