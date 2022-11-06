'''Description:

Some numbers have funny properties. For example:

    89 --> 8¹ + 9² = 89 * 1

    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

    we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.

In other words:

    Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.'''


def dig_pow(n, p):
    count = 0
    n_string = str(n)
    sol = 0
    while count < len(n_string):
        sol += int(n_string[count])**(p+count)
        count+=1 
    if sol>=n:
        if sol/n > sol//n:
            return -1       
        return int(sol/n)
    return -1

love = dig_pow(89, 1)
print(love)
love = dig_pow(92, 1)
print(love)
love = dig_pow(695, 2)
print(love)
love = dig_pow(46288, 3)
print(love)
love = dig_pow(3263, 3)
print(love)