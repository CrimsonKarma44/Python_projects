'''Description:

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
'''

DNA1 = "ATTGC"
DNA2 = "GTAT"

def main(value):
    reverse = ''
    for i in value:
        if i == 'A':
            reverse += 'T'
        elif i == 'T':
            reverse += 'A'
        elif i == 'C':
            reverse += ' G'
        elif i == 'G':
            reverse += 'C'
    return reverse

change = main(DNA1)
print(change)
change = main(DNA2)
print(change)